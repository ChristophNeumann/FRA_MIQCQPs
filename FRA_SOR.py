from model_information import *
from model_manipulation import *
from milp_formulation import *
import numpy as np
from globals import time_limit_SOR
from globals import nonlinear_solver

def SOR(m):

    vars_original = get_model_vars(m)
    is_int = bool_vec_is_int(m)
    eips, time_IPS = enlarged_IPS(m)
    if eips:
        opt = SolverFactory(nonlinear_solver)
        opt.options["max_cpu_time"] = time_limit_SOR
        solver_message = opt.solve(eips, tee=False)
        runtime = solver_message.solver.time
        if model_status(solver_message) == 'optimal':
            x = rounding(var_value(get_model_vars(eips)), is_int)
            set_var_vals(vars_original, x, is_int)
            obj_val = value(m.obj)
        else:
            print(solver_message)
            x = np.full(len(vars_original), np.inf)
            obj_val = np.inf
    else:
        x = np.full(len(vars_original),np.inf)
        obj_val = np.inf
        runtime = np.inf

    if number_nonlinear_constrs(m) == 1:
        g_value = constr_value(get_nonlinear_constrs(m)[0])
    else: g_value = -np.inf
    return {'x' : x, 'obj' : obj_val, 'time' : runtime, 'time_ips':time_IPS, 'g':g_value}

