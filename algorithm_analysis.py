import sys
import importlib.util
from model_information import *
sys.path.append('testbed')  # For loading models as modules
import os
import pandas as pd
import pickle
from FRA_SOR import *
import logging
import globals

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
    model_data = {'var': str((n_of_vars,n_of_int_vars,n_of_bin_vars)), 'constrs': str(p_quadrupel) }
    return model_data

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
    print("\n \nTesting SOR with delta =", globals.enlargement_parameter_box_constrs, "\n\n")
    for idx, name in enumerate(test_problems):
        print("#################################################")
        print('Testing problem ', name, "(", idx + 1, "/", len(test_problems),")")
        model = load_pyomo_model(name)
        model_data = get_model_data_for_print(model)
        result = SOR(model)
        print_results(result)
        result_matrix.append([model_data['var'] ,model_data['constrs'], result['time_ips'],
                              result['time_SOR'], result['obj'], result['g']])
        result_dataframe = pd.DataFrame(np.array(result_matrix), columns=['vars','constrs','time L', 'time SOR',
                                                                          'obj', 'constr_value'])
        result_dataframe[['time L', 'time SOR', 'obj', 'constr_value']] = \
            result_dataframe[['time L', 'time SOR', 'obj', 'constr_value']].apply(pd.to_numeric)
        result_dataframe.index = test_problems[:idx+1]
        save_obj(result_dataframe,'intermediate_results_' + str(globals.enlargement_parameter_box_constrs))
        del model
        del result
    return result_dataframe

def print_results(result):
    print("Value obtained by SOR is: ", result['obj'])
    print("Overall time for the computation of Lipschitz constants is: ", result['time_ips'])
    print("Time for SOR is: ", result['time_SOR'])

def run_bonmin(test_problems,cutoff_values):

    result_matrix = []
    algorithm = globals.benchmark_algorithm
    for idx, name in enumerate(test_problems):
        print('Testing problem ', name)
        current_model = load_pyomo_model(name)
        result_bonmin = solve_with_bonmin(current_model, cutoff_value=cutoff_values[idx])
        result_matrix.append([result_bonmin['time'],result_bonmin['obj']])

        result_dataframe = pd.DataFrame(np.array(result_matrix), columns=['time_'+algorithm,'obj_'+algorithm])
        result_dataframe.index = test_problems[:idx+1]
        save_obj(result_dataframe,'intermediate_results_bonmin')
        del current_model
    return result_dataframe


def save_obj(obj, name ):
    with open('results/'+ name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

def solve_with_bonmin(model, cutoff_value = float('-inf'), name = 'default_problem', save_to_file = False):

    if globals.benchmark_algorithm == 'gurobi':
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
            logging.info('cutoff is set to: ' + str(cutoff_value))
            opt.options['bonmin.cutoff'] = cutoff_value
        opt.options['bonmin.algorithm'] = globals.benchmark_algorithm
        logging.info('using ' + str(globals.benchmark_algorithm))
        # Set Options for solver.
        opt.options['bonmin.solution_limit'] = '1'
        opt.options['bonmin.time_limit'] = globals.time_limit_Bonmin
        if save_to_file:
            opt.options['bonmin.fp_log_level'] = '2'
            opt.options['bonmin.milp_log_level'] = '1'
            orig_stdout = sys.stdout
            f = open('solver_log/'+ name + globals.benchmark_algorithm + '.txt', 'w')
            sys.stdout = f
            solver_message = opt.solve(model,tee = True)
            sys.stdout = orig_stdout
            f.close()
            time = solver_message.solver.time
        else:
            try:
                solver_message = opt.solve(model, tee=False)
                if not(model_status(solver_message) == 'infeasible'):
                    time = solver_message.solver.time
                else:
                    logging.warning('Not obtaining a feasible point with bonmin for this problem')
                    time = np.inf
            except:
                logging.warning('Could not solve this problem using bonmin')
                time = np.inf
                solver_message = None

    # Solver time and objective
        if time >= opt.options['bonmin.time_limit'] :
            time = np.inf
            obj = np.inf
        else:
            model.solutions.store_to(solver_message)
            obj = solver_message.solution.objective.get('obj').get('Value')
        print('time', globals.benchmark_algorithm, time)
        print('objective', globals.benchmark_algorithm, obj)

    return {'time': time,
            'obj': obj,
             'solver_message': solver_message}

def update_objective_value_epi_problems(result):
    epi_subset = result['constr_value'] != float('-inf')
    print('Updating objecitve values. Old vales are:')
    print(result.loc[epi_subset, 'obj'])
    print("new values are: ")
    result.loc[epi_subset,'obj'] = np.array(result[epi_subset]['obj']+result[epi_subset]['constr_value'])
    print(result.loc[epi_subset, 'obj'])
    result = result.drop('constr_value',axis=1)
    return result