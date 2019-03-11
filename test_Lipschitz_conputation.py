import unittest
from testmodels.testmodel1_Lipschitz import *
import sys
import importlib.util
from model_information import *
from model_manipulation import*
import globals
sys.path.append('testmodels')  # For loading models as modules
import logging

class MyTestCase(unittest.TestCase):
    def test_Lipschitz_constrant_from_test_model(self):
        testinstance1 = importlib.import_module('testmodel1_Lipschitz')
        testinstance2 = importlib.import_module('exPaper')
        for delta_enlargement in np.linspace(0.5,0.9,10):
            globals.enlargement_parameter_box_constrs = delta_enlargement

            L1, runtime = compute_lipschitz(testinstance1.m.c1, testinstance1.m)
            self.assertFalse(L1>=30.99) # This should only hold for 1-1e-4 (tested below)

            L2, runtime = compute_lipschitz(testinstance2.m.c1, testinstance2.m)
            self.assertGreaterEqual(L2, 12 + 8 * (delta_enlargement - .01))
            self.assertLessEqual(L2, 12 + 8 * (delta_enlargement + .01))

        globals.enlargement_parameter_box_constrs = 1 - 1e-4
        L1, runtime = compute_lipschitz(testinstance1.m.c1, testinstance1.m)
        self.assertGreaterEqual(L1, 30.99)
        self.assertLessEqual(L1, 31)

    def test_enlargement_for_nonlinear_constr(self):
        testinstance = importlib.import_module('testmodel_enlargement')
        omega = get_enlargement_nonlinear(testinstance.m.c1)
        self.assertEqual(omega,2)
        self.assertEqual(floor_g(testinstance.m.c1.upper(),omega),10)

    def test_if_enlarged_inner_parallel_set_is_as_expected(self):
        testinstance = importlib.import_module('testmodel2_enlargement')
        globals.enlargement_parameter_box_constrs = 0.5
        eips = enlarged_IPS(testinstance.m)[0]
        self.assertEqual(eips.c2.upper(),-1+2*globals.enlargement_parameter_general)
        self.assertEqual(eips.c1.upper(), 6+2*globals.enlargement_parameter_general)

if __name__ == '__main__':
    unittest.main()
