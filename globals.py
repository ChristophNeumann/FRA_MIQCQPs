import numpy as np
time_limit_SOR = 1800.0 # joint time limit for SOR and Lipschitz-computation
nonlinear_solver = 'ipopt'
write_log = False
feas_tol_SOR = 1e-4

ABS_BOUND = 1E12 #Lower bound for objective value/ variables in case of unboundedness
global delta_enlargement # We want to change this parameter
delta_enlargement = 1-1e-4 # Enlargement parameter

testset_bonmin = ['autocorr_bern20_03', 'autocorr_bern25_03', 'cvxnonsep_normcon20r',
       'cvxnonsep_normcon30r', 'ex1223a', 'ex4', 'genpooling_lee1',
       'genpooling_lee2', 'genpooling_meyer10', 'genpooling_meyer15', 'ndcc12',
       'ndcc13', 'ndcc14', 'ndcc15', 'ndcc16', 'nous1', 'nous2',
       'ringpack_10_1', 'ringpack_10_2', 'ringpack_20_1', 'ringpack_20_2',
       'ringpack_30_1', 'smallinvDAXr1b150-165', 'smallinvDAXr1b200-220',
       'smallinvDAXr2b150-165', 'smallinvDAXr2b200-220',
       'smallinvDAXr3b150-165', 'smallinvDAXr3b200-220',
       'smallinvDAXr4b150-165', 'smallinvDAXr4b200-220',
       'smallinvDAXr5b150-165', 'smallinvDAXr5b200-220']
obj_vals = np.array([-3.98880458e+00, -2.99832064e+01, -1.46549272e+01, -1.48031228e+01,
        6.06978728e+00, -6.70152493e+00, -4.30983051e+03, -3.84925401e+03,
        5.12965913e+06,  6.55802971e+06,  1.08113885e+02,  1.07568617e+02,
        1.43307101e+02,  1.02422768e+02,  1.45888986e+02,  1.56707202e+00,
        1.38431745e+00, -4.17164353e+00,  0.00000000e+00, -4.17164353e+00,
        0.00000000e+00, -6.25746530e+00,  2.24691303e+02,  3.13317443e+02,
        2.22737793e+02,  3.11286782e+02,  2.20659693e+02,  3.09154124e+02,
        2.18434169e+02,  3.06442287e+02,  2.15850557e+02,  3.03063561e+02])

opt_gap_bonmin = 1e-4

