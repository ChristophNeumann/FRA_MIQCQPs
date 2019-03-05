import numpy as np
import pandas as pd

from FRA_SOR import *
from algorithm_analysis import *
sys.setrecursionlimit(5000)

testbed = 'current'
test_instances = read_test_instances(testbed)
#test_instances = testset_bonmin

#testbed = 'all_instances'
#test_instances = read_all_test_instances()
result_SOR = run_SOR(test_instances)
save_obj(result_SOR,'res_SOR_overview_' + testbed)
#cutoff_values_for_bonmin= np.array(result_SOR['obj'],dtype = float)
#result_BHyb = run_bonmin(testset_bonmin,obj_vals)
#result_overview = pd.concat([result_SOR,result_BHyb],axis=1)
# save_obj(result_BHyb,'res_BHyb')