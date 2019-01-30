import os
import algorithm_analysis as aa
from model_information import *


def check_existence_xy(nonlinear_constraints, vars):
    for constr in nonlinear_constraints:
        grad = gradient_symb(constr, vars)
        for el in grad:
            if not contains_only_integer_vars_grad_el(el):
                return True
    return False

models_with_xy_expr = []
all_models = [file.split('.')[0] for file in os.listdir("testbed/y_nonlinear") if '.py' in file]

it = 1
F = open('Models_With_xy.txt', 'w')
F.close()

for model_name in all_models:
    print(model_name)
    print('Model %d out of %d' % (it, len(all_models)))
    model = aa.load_pyomo_model(model_name)
    vars = get_int_vars(model)
    nonlinear_constraints = get_nonlinear_constrs(model)
    nonlinear_constraints_with_integer_vars = [constr for constr in nonlinear_constraints
                                               if contains_some_integer_vars(constr)]
    model_contains_xy = check_existence_xy(nonlinear_constraints_with_integer_vars, vars)
    if model_contains_xy:
        models_with_xy_expr.append(model_name)
        F = open('Models_With_xy.txt', 'a')
        F.write(model_name + '\n')
        F.close()
    print('Up to now, %d out of %d models contain xy expressions.' % (len(models_with_xy_expr), it))
    it += 1
