from model_information import *
from os import listdir
import shutil
from os.path import isfile, join
import sys
sys.setrecursionlimit(10000) # For larger Problems

def load_pyomo_model(problem_name):
    testinstance = importlib.import_module(problem_name)
    return testinstance.m

def read_all_test_instances(path):
    '''Read test instance Data '''
    files = listdir(path)
    suffix = ".py"
    pyfiles = [file for file in files if file.endswith(suffix)]
    testset = [file[:-3] for file in pyfiles]
    return testset

def copy_files(instance_list ,from_path, to_path):
    for f in instance_list:
        f = from_path + "\\"+ f + ".py"
        shutil.copy(f, to_path)

def copy_models_without_eq_constrs(path_from, path_to):
    sys.path.append(path_from)
    instances = read_all_test_instances(path_from)
    print(len(instances))
    testset = []
    for instance in instances:
       m = load_pyomo_model(instance)
       print('testing ' + instance )
       if not contains_eq_constrs_on_int_vars(m):
           print('add ' + instance + " to testset" )
           testset.append(instance)
    copy_files(testset, path_from, path_to)

#path_from = r"Z:\hg2412\Research\minlplib_quad_pyomo"
#path_to = r"Z:\hg2412\Research\01_FeasibleRoundingApproaches\04_numeric_granularity\testbed"
#copy_models_without_eq_constrs(path_from,path_to)




