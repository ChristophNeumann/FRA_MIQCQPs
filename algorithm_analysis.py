import sys
import importlib.util
from model_information import *
sys.path.append('testbed')  # For loading models as modules
import os
import pandas as pd

def load_pyomo_model(problem_name):
    testinstance = importlib.import_module(problem_name)
    return testinstance.m

def read_test_instances(filename):
    '''Read test instance Data '''
    dir = os.path.dirname(__file__)
    problem_data = os.path.join(dir, 'problem_information', filename + '.txt')
    f = open(problem_data, 'r')
    test_problems = f.read().splitlines()
    f.close()
    return test_problems

def get_model_data_for_print(m):
    p = len(list(m.component_objects(Constraint)))
    p_nl = number_nonlinear_constrs(m)
    is_int = bool_vec_is_int(m)
    m = np.sum(is_int)
    return [str(len(is_int)) + '(' + str(m)  + ')',str(p) + '(' + str(p_nl) + ')']

def get_data_matrix(test_problems):
    '''Creates a pandas data matrix for test problems, containing
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


def run_FCPA(test_problems, mode = 'INNER', epsilon = 10 ** -6, max_iter = 1000, only_epi = False):

    """
       Parameter for the algorithm
       :param epsilon Feasibility tolerance of the FCPA
       :param Iteration Limit for FCPA
       :param: only_epi. Userspecific knowledge that a problem is an epigraph reformulation where
                the only source of nonlinearity stems from the reformulation
       """
    result_matrix = []

    for idx, name in enumerate(test_problems):

        print('Testing problem ', name)
        original_model = load_pyomo_model(name)
        current_model = original_model.clone()
        current_model, red_successful, is_epi = preprocess_model(current_model)

        if is_epi and (number_nonlinear_constrs(current_model) <=1):
            only_epi = True

        if only_epi:
            print('Only Epi')

        if red_successful:
            result = FCPA(current_model, mode, epsilon, max_iter, only_epi)
            save_obj(result, name + '_raw') # we write each result in a pickle file
            # postprocessing in case of epigraph reformulation. Already internally taken care of in the case of only epi.
            if is_epi and not only_epi:
                print('reducing objective value')
                result['obj'] += constr_value(result['model'].con_epi)
                print('minimum objective of iterates value would be: ' + str(min(result['obj_vals'])))
            print('Objective value: ', result['obj'])
            print('Iterations: ', result['iterations'])
            print('Run time: ', result['runtime'])
            result_matrix.append([result['iterations'],result['runtime'],result['obj']])

            del original_model
            del current_model
            del result

    result_matrix = pd.DataFrame(np.array(result_matrix), columns = ['iter','time','obj'])
    result_matrix.index = test_problems
    result_matrix['iter'] = result_matrix['iter'].astype('int')
    return result_matrix