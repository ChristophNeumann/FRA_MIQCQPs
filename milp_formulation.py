from pyomo.environ import *
import numpy as np
from pyomo.repn import generate_canonical_repn
from model_information import *
import numbers
#from model_manipulation import *
import globals
import logging

def milp_for_L(nablaG, eips_before_polyhedral_enlargement, x, y):

    D = get_linear_constraints(eips_before_polyhedral_enlargement)
    is_int = bool_vec_is_int(eips_before_polyhedral_enlargement)
    M_u, M_v = bigMNabla(nablaG, y) #Compute bigM values

    model = ConcreteModel()
    model.m = len(y) #We differentiate wrt all integer variables
    model.n = len(x)
    model.J = Set(initialize = range(model.m))
    model.K = Set(initialize = range(model.n))
    model.I = Set(initialize = range(len(D)))

    def bounds_y(model,j):
        lb,ub = get_bounds(y)
        lb_adapted = math.ceil(lb[j]) + 1/2 - globals.enlargement_parameter_box_constrs
        ub_adapted = math.floor(ub[j]) - 1/2 + globals.enlargement_parameter_box_constrs
        return  lb_adapted , ub_adapted # Compute Lipschitz constant on slightly larger set

    def bounds_x(model,j):
        lb,ub = get_bounds(x)
        return lb[j],ub[j]

    def bounds_u(model,j):
        return 0, M_u[j]

    def bounds_v(model,j):
        return 0, M_v[j]

    model.y = Var(model.J, domain= Reals, initialize = 0, bounds = bounds_y)
    model.x = Var(model.K, domain= Reals, initialize=0, bounds = bounds_x)

    model.u = Var(model.J, domain=Reals, initialize = 0, bounds = bounds_u)
    model.v = Var(model.J, domain=Reals, initialize = 0, bounds = bounds_v)
    model.b = Var(model.J, initialize = 0, domain=Binary)

    model.obj = Objective(
        expr=sum(model.u[j] + model.v[j] for j in model.J),
        sense=maximize
    )


    def migrate_linear_constrs(model, i):
        constr = D[i]
        xy = x+y
        coeff = np.array(get_coeff(constr,xy))
        coeff_x = coeff[:len(x)]
        coeff_y = coeff[len(x):]
        if is_leq_constr(constr):
            constr_add = sum( [coeff_y[i]*model.y[i] for i in range(len(coeff_y))] ) + \
                         sum([coeff_x[i] * model.x[i] for i in range(len(coeff_x))]) <= constr.upper()
        else:
            constr_add = sum( [coeff_y[i]*model.y[i] for i in range(len(coeff_y))] ) +\
                         sum([coeff_x[i] * model.x[i] for i in range(len(coeff_x))]) >= constr.lower()
        return constr_add


    def lgs_constr(model, j):

        # nablaG is written with old variables and can potentially be a number.
        if isinstance(nablaG[j],numbers.Number):
            constr = float(nablaG[j]) == model.u[j] - model.v[j]
        else:
            coeff = get_coeff(nablaG[j], y)
            constr = sum( [coeff[i]*model.y[i] for i in range(model.m)]) == model.u[j] - model.v[j] #Has to be done componentwise, returns numeric value otherwise
        return constr

    def compl_constr_bigm1(model, j):
        return model.u[j] <= M_u[j]*model.b[j]

    def compl_constr_bigm2(model, j):
        return model.v[j] <= M_v[j]*(1-model.b[j])

    model.lgs = Constraint(model.J, rule=lgs_constr)
    model.compl_1 = Constraint(model.J, rule=compl_constr_bigm1)
    model.compl_2 = Constraint(model.J, rule=compl_constr_bigm2)
    model.D = Constraint(model.I, rule = migrate_linear_constrs)
    # Write the LP file for debugging purposes
#    model.write('model.lp')
    # possible choices: 'ipopt' (NLP), 'glpk' (MIP), 'gurobi'
    opt = SolverFactory('gurobi')
    opt.options["OptimalityTol"] = 1e-2
    opt.options["TimeLimit"] = globals.overall_time_limit_SOR
    # Solve statement
    result_obj = opt.solve(model, tee=False)
    runtime = result_obj.solver.time
    if runtime < globals.overall_time_limit_SOR:
        L_const = value(model.obj)
        logging.debug('Upper bound is:' + str(result_obj['Problem'][0]['Upper bound']))
        logging.info('Lipschitz constant is: ' + str(L_const))
        logging.debug(var_value(get_model_vars(model)))
        ub = result_obj['Problem'][0]['Upper bound']
        L_const = max(L_const,ub)
    else:
        L_const = np.inf

    return L_const, runtime



def bigMNabla(nablaG, y):

    p = len(nablaG)
    M_u = np.zeros(p)
    M_v = np.zeros(p)
    lb, ub = get_bounds(y)
    lb = np.ceil(np.array(lb)) + (1 / 2 - globals.enlargement_parameter_box_constrs) * np.ones(len(lb))
    ub = np.floor(np.array(ub)) + (-1 / 2 + globals.enlargement_parameter_box_constrs) * np.ones(len(ub))

    for i in range(0,p):
        if isinstance(nablaG[i],numbers.Number):
            M_u[i] = nablaG[i]
            M_v[i] = nablaG[i]
        else:
            nablaG_i = get_coeff(nablaG[i],y)
            for j, coefficient in enumerate(nablaG_i):
                if coefficient >0:
                    M_u[i] += coefficient*ub[j]
                    M_v[i] += coefficient*lb[j]
                if coefficient< 0:
                    M_u[i] += coefficient*lb[j]
                    M_v[i] += coefficient*ub[j]
        M_u[i] = max(M_u[i], 0)
        M_v[i] = max(-M_v[i], 0)

    return M_u, M_v


def bigM(Q,beta,lb,ub):

    """Compute the big M of the above MILP problem.
    This version is for given lower and upper bounds and computes an individual bigM for each u_i, v_i.

    Obviously, if we want a single bigM for the model, we can just use the maximum of all values.
    Currently, it is computed with an explicit formula, iterating through two for-loops only making use of lower- and
    upper bounds. If we additionally have a potentially tighter polyhedral set P available, we may replace it by
    the linear optimization problem

    u[i] = max{ max_{y in P} q_i^T y + beta,0}
    v[i] = max{-min_{y in P} q_i^T y + beta, 0}.

    The idea of the computation is that it follows from the LPCC formulation that u is bounded by the maximum of

    Qy + beta

    and that v is bounded by the minimum of

    Qy + beta

    multiplied with (-1).

    """

    p = Q.shape[0]
    M_u = np.zeros(p)
    M_v = np.zeros(p)

    for i in range(0,p):
        for j in range(0,Q.shape[1]):
            if Q[i,j]>0:
                M_u[i] += Q[i,j]*ub[j]
                M_v[i] += Q[i,j]*lb[j]
            if Q[i,j]< 0:
                M_u[i] += Q[i,j]*lb[j]
                M_v[i] += Q[i,j]*ub[j]
        M_u[i] = max(M_u[i] + beta[i], 0)
        M_v[i] = max(-M_v[i] + beta[i], 0)


    return M_u, M_v