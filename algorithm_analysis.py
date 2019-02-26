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

def read_all_test_instances():
    files = os.listdir('./testbed')
    suffix = ".py"
    pyfiles = [file for file in files if file.endswith(suffix)]
    testset = [file[:-3] for file in pyfiles]
    return testset

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

def run_SOR(test_problems, time_limit = 600.0):

    result_matrix = []
    for idx, name in enumerate(test_problems):
        print('Testing problem ', name)
        original_model = load_pyomo_model(name)
        current_model = original_model.clone()
        datalist = get_model_data_for_print(current_model)
        result = SOR(current_model, time_limit=time_limit)
        result_matrix.append([datalist[0],datalist[1],result['time_ips'],result['time'],result['obj'],result['g']])
        result_dataframe = pd.DataFrame(np.array(result_matrix), columns=['vars','constrs','time L', 'time SOR', 'obj', 'constr_value'])
        result_dataframe[['time L', 'time SOR', 'obj', 'constr_value']] = result_dataframe[['time L', 'time SOR', 'obj', 'constr_value']].apply(pd.to_numeric)
        result_dataframe.index = test_problems[:idx+1]
        save_obj(result_dataframe,'intermediate_results')
        print("#################################################")
        print(str(idx+1) + "/" + str(len(test_problems)) + "done.")
        print("Value obtained by SOR is: " + str(result['obj']))
        print("#################################################")
        del original_model
        del current_model
        del result
    return result_dataframe

def run_bonmin(test_problems,cutoff_values, time_limit = 600.0):

    result_matrix = []
    for idx, name in enumerate(test_problems):
        print('Testing problem ', name)
        current_model = load_pyomo_model(name)
        result_bonmin = solve_with_bonmin(current_model, 'b-hyb', \
                                          cutoff_value=cutoff_values[idx], time_limit = time_limit)
        result_matrix.append([result_bonmin['time'],result_bonmin['obj']])
        result_dataframe = pd.DataFrame(np.array(result_matrix), columns=['time_bonmin','obj_bonmin'])
        result_dataframe.index = test_problems[:idx+1]
        save_obj(result_dataframe,'intermediate_results_bonmin')
        del current_model
    return result_dataframe


def save_obj(obj, name ):
    with open('results/'+ name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def solve_with_bonmin(model,algorithm = 'b-ifp', time_limit = 600.0, cutoff_value = float('-inf'), name = 'default_problem', save_to_file = False):

    if algorithm == 'gurobi':
        opt = SolverFactory('gurobi',solver_io="python")
        opt.options["Cutoff"] = cutoff_value
        opt.options["SolutionLimit"] = 1
        opt.options["TimeLimit"] = 300
        opt.options["MIPFocus"] = 1
        solver_message = opt.solve(model, tee=False)
        time = solver_message['solver'][0]['Wallclock time']
        obj = solver_message['Problem'][0]['Upper bound']
        print('time gurobi:' + str(time))
        print('objective gurobi: ' + str(obj))
    else:
        opt = SolverFactory('bonmin')
        if cutoff_value > float('-inf'):
            print('cutoff is set to: ' + str(cutoff_value))
            opt.options['bonmin.cutoff'] = cutoff_value
        if algorithm == 'b-hyb':
            opt.options['bonmin.algorithm'] = 'b-hyb'
            print('using b-hyb')
        else:
            opt.options['bonmin.algorithm'] = 'b-ifp'
            print('using b-ifp')
        # Set Options for solver.
        opt.options['bonmin.solution_limit'] = '1'
        opt.options['bonmin.time_limit'] = time_limit
        if save_to_file:
            opt.options['bonmin.fp_log_level'] = '2'
            opt.options['bonmin.milp_log_level'] = '1'
            orig_stdout = sys.stdout
            f = open('solver_log/'+ name + algorithm + '.txt', 'w')
            sys.stdout = f
            solver_message = opt.solve(model,tee = True)
            sys.stdout = orig_stdout
            f.close()
            time = solver_message.solver.time
        else:
            try:
                solver_message = opt.solve(model, tee=False)
                time = solver_message.solver.time
            except:
                print('Could not solve this problem due to a value error')
                time = np.inf
                solver_message = None

    # Solver time and objective
        if time >= opt.options['bonmin.time_limit'] :
            time = np.inf
            obj = np.inf
        else:
            model.solutions.store_to(solver_message)
            obj = solver_message.solution.objective.get('obj').get('Value')
            print('time B-Hyb:' + str(time))
            print('objective B-Hyb: ' + str(obj))

    return {'time': time,
            'obj': obj,
             'solver_message': solver_message}