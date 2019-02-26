import numpy as np
import pandas as pd

from FRA_SOR import *
from algorithm_analysis import *
sys.setrecursionlimit(5000)

testbed = 'small_testset'
test_instances = read_test_instances(testbed)

testbed_instances = read_all_test_instances()
result_SOR = run_SOR(test_instances)
save_obj(result_SOR,'res_SOR_overview_' + testbed)
cutoff_values_for_bonmin= np.array(result_SOR['obj'],dtype = float)
result_BHyb = run_bonmin(test_instances,cutoff_values_for_bonmin)
result_overview = pd.concat([result_SOR,result_BHyb],axis=1)
save_obj(result_overview,'res_overview_' + testbed)