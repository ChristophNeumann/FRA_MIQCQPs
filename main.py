from pyomo.environ import *
import numpy as np

'''
Input data which defines a function of shape
G(y) = y'*Q*y + beta'*y
Q is assumed to be square, symmetric but possibly indefinite
'''
Q = np.array([[3, 0], [-1, 2]])
beta = np.zeros((2, 1))

# Model declaration
model = ConcreteModel()
# Dimension of y
model.m = Q.shape[1]
# Index set
model.J = RangeSet(1, model.m)
# Decision variables
model.y = Var(model.J, domain=Reals)
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
