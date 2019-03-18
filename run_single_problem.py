import numpy as np
import pandas as pd
import logging
from FRA_SOR import *
import globals
from algorithm_analysis import *
sys.setrecursionlimit(5000)
logging.basicConfig(level=logging.INFO)
testproblems = ['sonet17v4','sonet18v6', 'sonet19v5', 'sonet24v2' ]
run_SOR(testproblems)
