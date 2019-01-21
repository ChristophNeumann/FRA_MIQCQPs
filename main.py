import numpy as np

from FRA_SOR import *
from algorithm_analysis import *

m = load_pyomo_model('ringpack_10_1')
result_SOR = SOR(m)
print(result_SOR)
