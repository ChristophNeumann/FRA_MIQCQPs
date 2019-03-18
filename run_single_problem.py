import numpy as np
import pandas as pd
import logging
from FRA_SOR import *
import globals
from algorithm_analysis import *
sys.setrecursionlimit(5000)
logging.basicConfig(level=logging.WARNING)
testproblems = ['ex1223a', 'ex4', 'genpooling_lee1', 'genpooling_lee2',
       'genpooling_meyer10', 'genpooling_meyer15', 'ndcc12', 'ndcc13',
       'ndcc14', 'ndcc15', 'ndcc16', 'nous1', 'nous2', 'ringpack_10_1',
       'ringpack_10_2', 'ringpack_20_1', 'ringpack_20_2', 'ringpack_30_1']
run_SOR(testproblems)
