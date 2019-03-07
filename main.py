import numpy as np
import pandas as pd
import logging
from FRA_SOR import *
import globals
from algorithm_analysis import *
sys.setrecursionlimit(5000)

logging.basicConfig(level=logging.WARNING)

testbed = 'all_instances'
test_instances = read_all_test_instances()

for delta_enlargement in [0.5,0.75,1-1e-4]:
    globals.delta_enlargement = delta_enlargement
    result_SOR = run_SOR(test_instances)
    save_obj(result_SOR,'SOR_' + testbed + "_" + str(delta_enlargement))