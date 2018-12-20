from pyomo.environ import *


def solve_milp(Q, beta, B, b, BigM):
    # Model declaration
    # Y := \{ y| By <= b\}. Maybe only box constraints? / additional modelling capacity for box constraints?
    model = ConcreteModel()
    # Dimension of y
    model.m = Q.shape[1]
    # Index set
    model.J = RangeSet(1, model.m)
    # Decision variables
    model.y = Var(model.J, domain=Reals)
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
        return model.v[j] <= BigM*model.b[j]

    #Todo: Add linear constraints Y := \{ y| By <= b\}

    model.lgs = Constraint(model.J, rule=lgs_constr)
    model.compl_1 = Constraint(model.J, rule=compl_constr_bigm1)
    model.compl_2 = Constraint(model.J, rule=compl_constr_bigm2)
    # Solver
    # possible choices: 'ipopt' (NLP), 'glpk' (MIP)
    opt = SolverFactory('gurobi')
    # Solve statement
    result_obj = opt.solve(model, tee=True)

    #Return the optimal objective value which serves as a Lipschitz constant
    L_const = value(model.obj)
    print(str(L_const))

    model.pprint()

    return result_obj
