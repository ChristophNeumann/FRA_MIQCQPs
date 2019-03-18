import numpy as np
import pandas as pd
import logging
from FRA_SOR import *
import globals
from algorithm_analysis import *
sys.setrecursionlimit(5000)
testbed = 'SOR_succ'
test_instances = read_test_instances(testbed)
result_SOR = run_SOR(test_instances)
result_SOR = update_objective_value_epi_problems(result_SOR)
save_obj(result_SOR, 'SOR_' + testbed + "_" + str(enlargement_parameter_box_constrs))
cutoff_values = np.array(result_SOR['obj'])
print(cutoff_values)
results_overall =  result_SOR
for solver in ['B-BB', 'B-Hyb', 'B-iFP']:
    globals.benchmark_algorithm = solver
    res_bonmin = run_bonmin(test_instances, cutoff_values)
    save_obj(res_bonmin, solver)
    results_overall = pd.concat([results_overall,res_bonmin['time_'+solver]],axis=1)
save_obj(results_overall,'Comparison' + testbed)
