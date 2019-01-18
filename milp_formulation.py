from pyomo.environ import *
import numpy as np
from pyomo.repn import generate_canonical_repn
from model_information import *
import numbers
#from model_manipulation import *

def milp_for_L(nablaG, D_y, y):

#    print("Computing bigM values")
    M_u, M_v = bigMNabla(nablaG, y) #Compute bigM values

#    print("Computation of bigM done. Maximum value is:  " + str(max(max(M_u),max(M_v))))
    model = ConcreteModel()
    model.m = len(nablaG) #We differentiate wrt all integer variables
    model.J = Set(initialize = range(model.m))
    model.I = Set(initialize = range(len(D_y)))

    def bounds_y(model,j):
        lb,ub = get_bounds(y)
        return lb[j],ub[j]

    def bounds_u(model,j):
        return 0, M_u[j]

    def bounds_v(model,j):
        return 0, M_v[j]

    model.y = Var(model.J, domain= Reals, bounds = bounds_y)

    model.u = Var(model.J, domain=Reals, bounds = bounds_u)
    model.v = Var(model.J, domain=Reals, bounds = bounds_v)
    model.b = Var(model.J, domain=Binary)

    model.obj = Objective(
        expr=sum(model.u[j] + model.v[j] for j in model.J),
        sense=maximize
    )


    def migrate_linear_constrs(model, i):
        constr = D_y[i]
        coeff = get_coeff(constr,y)
        if is_leq_constr(constr):
            constr_add = sum( [coeff[i]*model.y[i] for i in range(len(coeff))] ) <= constr.upper()
        else:
            constr_add = sum( [coeff[i]*model.y[i] for i in range(len(coeff))] ) >= constr.lower()
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
    model.D_y = Constraint(model.I, rule = migrate_linear_constrs)
    # Write the LP file for debugging purposes
#    model.write('model.lp')
    # Solver
    # possible choices: 'ipopt' (NLP), 'glpk' (MIP), 'gurobi'
    opt = SolverFactory('gurobi')
    # Solve statement
    result_obj = opt.solve(model, tee=False)

    L_const = value(model.obj)
    print(str(L_const))
    print(str(var_value(model.y)))
#    print("Found Lipschitz constant is:   " + str(L_const))

#    model.pprint()

    return L_const



def solve_milp(Q, beta, lb, ub):

    # TODO: Implement additional polyhedral constraints of the form B*y=b
    # Model declaration
    model = ConcreteModel()
    # Dimension of y
    model.m = Q.shape[1]
    # Index set
    model.J = RangeSet(1, model.m)
    # Decision variables

    def fb(model, i):
        # lower bound, upper bound pair is declared for each index element
        return lb[i-1], ub[i-1]

    model.y = Var(model.J, domain=Reals, bounds=fb)
    model.u = Var(model.J, domain=NonNegativeReals)
    model.v = Var(model.J, domain=NonNegativeReals)
    model.b = Var(model.J, domain=Binary)
    # objective function
    model.obj = Objective(
        expr=sum(model.u[j] + model.v[j] for j in model.J),
        sense=maximize
    )

    # constraints

    def lgs_constr(model, j):
        # numpy starts to count at 0 and we want to start at 1
        return sum(Q[j - 1][k - 1] * model.y[k] for k in model.J) + beta[j - 1] == model.u[j] - model.v[j]

    #Computes upper bounds for u and v individually
    M_u, M_v = bigM(Q,beta,lb,ub)

    def compl_constr_bigm1(model, j):
        return model.u[j] <= M_u[j-1]*model.b[j]

    def compl_constr_bigm2(model, j):
        return model.v[j] <= M_v[j-1]*(1-model.b[j])

    model.lgs = Constraint(model.J, rule=lgs_constr)
    model.compl_1 = Constraint(model.J, rule=compl_constr_bigm1)
    model.compl_2 = Constraint(model.J, rule=compl_constr_bigm2)
    # Write the LP file for debugging purposes
    model.write('model.lp')
    # Solver
    # possible choices: 'ipopt' (NLP), 'glpk' (MIP), 'gurobi'
    opt = SolverFactory('gurobi')
    # Solve statement
    result_obj = opt.solve(model, tee=True)

    #Return the optimal objective value which serves as a Lipschitz constant
    # TODO: 'value' is not known, other command?
    #L_const = value(model.obj)
    #print(str(L_const))

    model.pprint()

    return result_obj

def bigMNabla(nablaG, y):

    p = len(nablaG)
    M_u = np.zeros(p)
    M_v = np.zeros(p)
    lb, ub = get_bounds(y)

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
        print(M_u)
        print(M_v)

    return M_u, M_v