import numpy as np
from pyomo.environ import *

import milp_formulation
import nonlinear_formulation

'''
Input data which defines a function of shape
G(y) = y'*Q*y + beta'*y
Q is assumed to be square, symmetric but possibly indefinite
'''
Q = np.array([[3, 0], [-1, 2]])
beta = np.zeros((2, 1))
B = np.array([[-1,0],[0,-1],[1,0],[0,1]])
b = np.array([1,1,2,2])
# Needed for the MILP formulation
BigM = 100

#result_nlp = nonlinear_formulation.solve_nonlinear(Q, beta)
result_milp = milp_formulation.solve_milp(Q, beta, B, b, BigM)
print(result_milp)
