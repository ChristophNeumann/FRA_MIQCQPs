import numpy as np
import pandas as pd
import logging
from FRA_SOR import *
import globals
from algorithm_analysis import *
sys.setrecursionlimit(5000)

#logging.basicConfig(level=logging.DEBUG)
RUN_SOR = False
RUN_BONMIN = True
if RUN_SOR:
    testbed = 'all_instances'
    test_instances = read_all_test_instances()
    for enlargement_parameter_box_constrs in [0.5, 0.75, 1 - 1e-4]:
        globals.enlargement_parameter_box_constrs = enlargement_parameter_box_constrs
        result_SOR = run_SOR(test_instances)
        save_obj(result_SOR,'SOR_' + testbed + "_" + str(enlargement_parameter_box_constrs))
if RUN_BONMIN:
    testbed = 'SOR_succ'
    cutoff_values =np.load(r'results/vals_SOR.npy')
    test_instances = read_test_instances(testbed)
    res_bonmin = run_bonmin(test_instances, cutoff_values)
    save_obj(res_bonmin,'res_bonmin')