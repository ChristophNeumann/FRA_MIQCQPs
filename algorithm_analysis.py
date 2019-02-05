import sys
import importlib.util
from model_information import *
sys.path.append('testbed')  # For loading models as modules
import os
import pandas as pd
import pickle
from FRA_SOR import *

def load_pyomo_model(problem_name):
    testinstance = importlib.import_module(problem_name)
    return testinstance.m

def read_test_instances(filename):
    '''Read test instance Data '''
    dir = os.path.dirname(__file__)
    problem_data = os.path.join(dir, 'testbed', filename + '.txt')
    f = open(problem_data, 'r')
    test_problems = f.read().splitlines()
    f.close()
    return np.array(test_problems)

def get_model_data_for_print(m):
    p_quadrupel = numbers_constrs(m)
    is_int = bool_vec_is_int(m)
    n_of_vars = len(is_int)
    n_of_int_vars = np.sum(is_int)
    n_of_bin_vars = get_number_of_binary_vars(m)

    return [str((n_of_vars,n_of_int_vars,n_of_bin_vars)),str(p_quadrupel)]

def get_data_matrix(test_problems):
    '''Creates a pandas data matrix for test problems, containing
        - #variables (int variables)
        - #constraints (nonlinear constraints)
        :param test_problems: list of strings that correspond to python files containing pyomo models
    '''
    data_matrix = []
    names = []
    for idx, name in enumerate(test_problems):
        current_model = load_pyomo_model(name)
        names.append(name)
        datalist = get_model_data_for_print(current_model)
        data_matrix.append(datalist)
    pd_data_matrix = pd.DataFrame(data_matrix, columns = ['vars','constrs'])
    pd_data_matrix.index = names
    return pd_data_matrix

def run_SOR(test_problems):

    result_matrix = []

    for idx, name in enumerate(test_problems):

        print('Testing problem ', name)
        original_model = load_pyomo_model(name)
        current_model = original_model.clone()
        result = SOR(current_model)
        datalist = get_model_data_for_print(current_model)
        result_matrix.append([datalist[0],datalist[1],result['time_ips'],result['time'],result['obj'],result['g']])
        intermediate_dataframe = pd.DataFrame(np.array(result_matrix), columns=['vars','constrs','time L', 'time SOR', 'obj', 'constr_value'])
        intermediate_dataframe.index = np.array(test_problems)[:idx+1]
        save_obj(intermediate_dataframe,'intermediate_results')
        del original_model
        del current_model
        del result

def save_obj(obj, name ):
    with open('results/'+ name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)