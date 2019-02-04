import numpy as np

from FRA_SOR import *
from algorithm_analysis import *

testbed = 'small_testset'
test_instances = read_test_instances(testbed)
run_SOR(test_instances)
