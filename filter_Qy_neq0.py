import algorithm_analysis as aa
import os
import numbers
from model_information import *


def check_ynonlinearity(nonlinear_constraints, vars):
    for constr in nonlinear_constraints:
        grad = gradient_symb(constr, vars)
        for el in grad:
            if not isinstance(el, numbers.Number):
                    return True
    return False


models_with_Qy_not_zero = []
all_models = [file.split('.')[0] for file in os.listdir("testbed") if '.py' in file]
it = 1
F = open('Models_With_Nonlinear_Y.txt', 'w')
F.close()

for model_name in all_models:
    print(model_name)
    print('Model %d out of %d' % (it, len(all_models)))
    model = aa.load_pyomo_model(model_name)
    vars = get_int_vars(model)
    nonlinear_constraints = get_nonlinear_constrs(model)
    nonlinear_constraints_with_integer_vars = [constr for constr in nonlinear_constraints
                                               if contains_some_integer_vars(constr)]
    model_is_ynonlinear = check_ynonlinearity(nonlinear_constraints_with_integer_vars, vars)
    if model_is_ynonlinear:
        models_with_Qy_not_zero.append(model_name)
        F = open('Models_With_Nonlinear_Y.txt', 'a')
        F.write(model_name + '\n')
        F.close()
    print('Up to now, %d out of %d models contain nonlinear constraints in y.' % (len(models_with_Qy_not_zero), it))
    it += 1
