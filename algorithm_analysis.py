import sys
import importlib.util
sys.path.append('testbed\y_nonlinear')  # For loading models as modules

def load_pyomo_model(problem_name):
    testinstance = importlib.import_module(problem_name)
    return testinstance.m
