import algorithm_analysis as aa
import os
from model_information import *


def check_ynonlinearity(nonlinear_constraints, vars):
    for constr in nonlinear_constraints:
        grad = gradient_symb(constr, vars)
        for el in grad:
            if type(el) is pyomo.core.kernel.expr_coopr3._SumExpression:
                for arg in el._args:
                    if arg._domain.name in int_type:
                        return True
    return False


models_with_Qy_not_zero = []
all_models = [file.split('.')[0] for file in os.listdir("testbed") if '.py' in file]
it = 1
for model_name in all_models:
    print(model_name)
    print('Model %d out of %d' % (it, len(all_models)))
    model = aa.load_pyomo_model(model_name)
    vars = get_int_vars(model)
    nonlinear_constraints = get_nonlinear_constrs(model)
    num_nonlinear_constraints = len(nonlinear_constraints)
    model_is_ynonlinear = check_ynonlinearity(nonlinear_constraints, vars)
    if model_is_ynonlinear:
        models_with_Qy_not_zero.append(model_name)
    print(models_with_Qy_not_zero)
    print('Up to now, %d out of %d models contain nonlinear constraints in y.' % (len(models_with_Qy_not_zero), it))
    it += 1
F = open('Models_With_Nonlinear_Y.txt', 'w')
for model in models_with_Qy_not_zero:
    F.write(model+'\n')
F.close()
