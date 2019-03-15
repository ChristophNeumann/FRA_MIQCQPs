import numpy as np
import pandas as pd
import logging
from FRA_SOR import *
import globals
from algorithm_analysis import *
sys.setrecursionlimit(5000)
logging.basicConfig(level=logging.DEBUG)
testproblems = ['genpooling_meyer10']
run_SOR(testproblems)
