import numpy as np

from FRA_SOR import *
from algorithm_analysis import *

m = load_pyomo_model('smallinvDAXr1b150-165')
result_SOR = SOR(m)
print(result_SOR)
