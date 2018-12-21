import numpy as np

import milp_formulation
import nonlinear_formulation

'''
Input data which defines a function of shape
G(y) = y'*Q*y + beta'*y
Q is assumed to be square, symmetric but possibly indefinite
'''
Q = np.array([[3, 0], [-1, 2]])
beta = np.zeros((2, 1))
lb = np.array([1, 1])
ub = np.array([2, 2])
# Needed for the MILP formulation
BigM = max(ub)

#result_nlp = nonlinear_formulation.solve_nonlinear(Q, beta)
result_milp = milp_formulation.solve_milp(Q, beta, lb, ub, BigM)
print(result_milp)
