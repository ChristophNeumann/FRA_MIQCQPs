import numpy as np
'''
Variables that are declared global need to be changed
during runtime from other modules'''
overall_time_limit_SOR = 1800.0 #includes computation of Lipschitz constant
time_limit_Bonmin = 1800.0
global benchmark_algorithm
benchmark_algorithm = 'B-BB'
nonlinear_solver = 'ipopt'
write_log = False
feas_tol_SOR = 1e-4
enlargement_parameter_general = 1 - 1e-4 #Used for linear and nonlinear constraints
global enlargement_parameter_box_constrs  #We want to change this parameter during runtime from other modules
enlargement_parameter_box_constrs = 1 - 1e-4
opt_gap_bonmin = 1e-4

