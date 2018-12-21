from pyomo.environ import *


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
        return (lb[i-1], ub[i-1])

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
    opt = SolverFactory('glpk')
    # Solve statement
    result_obj = opt.solve(model, tee=True)

    #Return the optimal objective value which serves as a Lipschitz constant
    # TODO: 'value' is not known, other command?
    #L_const = value(model.obj)
    #print(str(L_const))

    model.pprint()

    return result_obj
