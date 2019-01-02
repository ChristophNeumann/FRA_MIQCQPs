from pyomo.environ import *
import numpy as np

def solve_milp(Q, beta, lb, ub, BigM):
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

    def compl_constr_bigm1(model, j):
        return model.u[j] <= BigM*model.b[j]

    def compl_constr_bigm2(model, j):
        return model.v[j] <= BigM*(1-model.b[j])

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
                M_u[i] += Q[i,j]*ub[i]
                M_v[i] += Q[i,j]*lb[i]
            if Q[i,j]< 0:
                M_u[i] += Q[i,j]*lb[i]
                M_v[i] += Q[i,j]*ub[i]
        M_u[i] = max(M_u[i] + beta[i], 0)
        M_v[i] = max(-M_v[i] + beta[i], 0)
        print(M_u)
        print(M_v)

    return M_u, M_v