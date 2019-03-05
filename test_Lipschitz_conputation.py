import unittest
from testmodels.model_t import *
import sys
import importlib.util
from model_information import *
from globals import delta_enlargement
sys.path.append('testmodels')  # For loading models as modules

class MyTestCase(unittest.TestCase):
    def test_Lipschitz_constrant_from_test_model(self):
        testinstance1 = importlib.import_module('model_t')
        testinstance2 = importlib.import_module('exPaper')

        L1, runtime = compute_lipschitz(testinstance1.m.c1, testinstance1.m)
        L2, runtime = compute_lipschitz(testinstance2.m.c1, testinstance2.m)
        self.assertGreaterEqual(L1, 30.99)
        self.assertLessEqual(L1,31)
        self.assertGreaterEqual(L2, 12+8*(delta_enlargement-.01))
        self.assertLessEqual(L2,12+8*(delta_enlargement+.01))

if __name__ == '__main__':
    unittest.main()
