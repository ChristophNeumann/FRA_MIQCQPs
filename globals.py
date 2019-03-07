import numpy as np
overall_time_limit_SOR = 1800.0 #joint time limit for SOR and Lipschitz-computation
time_limit_Bonmin = 1800.0
nonlinear_solver = 'ipopt'
write_log = False
feas_tol_SOR = 1e-4

global delta_enlargement # We want to change this parameter from other modules
delta_enlargement = 1-1e-4
opt_gap_bonmin = 1e-4

