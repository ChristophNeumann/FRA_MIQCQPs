from pyomo.environ import *


def solve_nonlinear(Q, beta, lb, ub):
    # Model declaration
    model = ConcreteModel()
    # Dimension of y
    model.m = Q.shape[1]
    # Index set
    model.J = RangeSet(1, model.m)
    # Decision variables

    def fb(model, i):
        # lower bound, upper bound pair is declared for each index element
        return (lb[i-1], ub[i-1])

    model.y = Var(model.J, domain=Reals, bounds=fb)
    model.u = Var(model.J, domain=NonNegativeReals)
    model.v = Var(model.J, domain=NonNegativeReals)
    # objective function
    model.obj = Objective(
        expr=sum(model.u[j]+model.v[j] for j in model.J),
        sense=maximize
    )
    # constraints


    def lgs_constr(model, j):
        # numpy starts to count at 0 and we want to start at 1
        return sum(Q[j-1][k-1]*model.y[k] for k in model.J)+beta[j-1] == model.u[j]-model.v[j]


    def compl_constr(model, j):
        return model.u[j]*model.v[j] == 0


    model.lgs = Constraint(model.J, rule=lgs_constr)
    model.compl = Constraint(model.J, rule=compl_constr)
    # Solver
    # possible choices: 'ipopt' (NLP), 'glpk' (MIP)
    opt = SolverFactory('ipopt')
    # Solve statement
    result_obj = opt.solve(model, tee=True)

    model.pprint()
    return result_obj
