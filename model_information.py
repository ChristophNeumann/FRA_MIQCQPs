from pyomo.repn import generate_canonical_repn
from pyomo.core.base.expr import identify_variables
from math_functions import *
from pyomo.core.base.symbolic import differentiate
from pyomo.opt import SolverStatus, TerminationCondition
from pyomo.environ import *
import numbers

int_type = ['Integers', 'PositiveIntegers', 'NonPositiveIntegers',
            'NegativeIntegers', 'NonNegativeIntegers', 'Boolean', 'Binary']


def bool_vec_is_int(m):
    """Returns an numpy-array isInt with isInt[i] = True iff variable i is some Integral variable"""
    variables = get_model_vars(m)
    isInt = np.array([str(v.domain) in int_type for v in variables])
    return isInt


def get_bounds(var_list):
    lb = []
    ub = []
    for var in var_list:
        lb.append(var.bounds[0])
        ub.append(var.bounds[1])
    return lb, ub


def check_sense_on_minimize(m):
    return m.obj.sense == 1


def enlargement_param(coeff, is_int):
    if any(coeff[np.logical_not(is_int)]) | any(coeff[is_int] - np.floor(coeff[is_int])):
        g = 0
    else:
        g = gcd_vec(coeff[is_int])
    return g


def get_coeff(expression, model_vars):
    """Returns the vector of coefficients coeff of a linear pyomo constraint constr.
    Note that coeff[i] = 0 holds, if the variable does not appear in the constraint"""

    # assert(constr.body.polynomial_degree()==1)
    names_model_vars = [v.name for v in model_vars]  # all variablenames from the model
    coeff = np.zeros(len(model_vars))
    if type(expression) == pyomo.core.base.constraint.SimpleConstraint:
        expression = expression.body
    repn = generate_canonical_repn(expression)
    for i, coefficient in enumerate(repn.linear or []):
        coeff[names_model_vars.index(repn.variables[i].name)] = coefficient
    return coeff


def is_leq_constr(constr):
    """Returns true, if and only if a pyomo constraint constr is of the form body <= upper"""
    if constr.lower is None:
        return True
    else:
        return False


def constr_value(constr):
    """Rearranges a constraint at some point x to g_i(x) <= 0 and computes g_i(x"""
    if is_leq_constr(constr):
        g_val = constr.body() - constr.upper()
    else:
        g_val = constr.lower() - constr.body()
    return g_val


def get_vars_from_constr(constr):
    """Returns all variables appearing in a constraint constr"""
    return list(identify_variables(constr.body))

def get_active_int_vars_from_constr(constr, y):
    xy_active = get_vars_from_constr(constr)
    xy_active_name_list = [var.name for var in xy_active]
    y_active = []
    index_inactive = []
    for idx, var in enumerate(y):
        if var.name in xy_active_name_list:
            y_active.append(var)
        else:
            index_inactive.append(idx)
    return y_active, np.array(index_inactive)

def get_vars_from_grad_el(el):
    """Returns all variables appearing in a constraint constr"""
    return list(identify_variables(el))


def contains_eq_constrs_on_int_vars(m):
    """Checks if a model m contains some equality constraint ax+by=c with y Integer"""
    result = False
    for c in m.component_objects(Constraint, active=True):
        if c.equality:
            my_vars = get_vars_from_constr(c)
            for v in my_vars:
                if str(v.domain) in int_type:
                    result = True
                    break
    return result


def model_status(result_solver):
    if (result_solver.solver.status == SolverStatus.ok) and \
            (result_solver.solver.termination_condition == TerminationCondition.optimal):
        result = 'optimal'
    elif result_solver.solver.termination_condition == TerminationCondition.infeasible:
        result = 'infeasible'
    elif result_solver.solver.termination_condition == TerminationCondition.unbounded:
        result = 'unbounded'
    else:
        result = result_solver.solver.termination_message

    return result


def get_linear_constraints(m):
    linear_constrs = []
    for constr in m.component_objects(Constraint):
        if constr.body.polynomial_degree() in [0, 1]:
            linear_constrs.append(constr)
    return linear_constrs


def g_max(m):
    """Returns the maximum value of all constraint functions of a pyomo model m for a given point x,
    implicitly rearranging all constraints to g_i(x) <= 0 and computing max(g_i(x))"""
    nonlinear_constrs = []
    for constr in m.component_objects(Constraint):
        if not (constr.body.polynomial_degree() in [0, 1]):
            nonlinear_constrs.append(constr)
    # Note that equality constraints are always fulfilled, as they are assumed
    # to be linear and to only contain continuous variables and are not changed when rounding.
    if len(nonlinear_constrs) >= 2:
        g_vals = np.zeros(len(nonlinear_constrs))
        for idx, constr in enumerate(nonlinear_constrs):
            g_vals[idx] = constr_value(constr)
        idx_max = np.argmax(g_vals)
        return nonlinear_constrs[idx_max]
    else:
        return nonlinear_constrs[0]


def gradient(constr, variables):
    grad_num = np.array([value(partial) for partial in differentiate(constr.body, wrt_list=variables)])
    if not is_leq_constr(constr):
        grad_num = -grad_num
    return grad_num


def gradient_symb(constr, variables):
    grad_num = np.array([partial for partial in differentiate(constr.body, wrt_list=variables)])
    if not is_leq_constr(constr):
        grad_num = -grad_num
    return grad_num


def var_value(model_vars):
    result = []
    if type(model_vars) == pyomo.core.base.var.IndexedVar:
        for i in list(model_vars.keys()):
            result.append(value(model_vars[i]))
        result = np.array(result)
    else:
        result = np.array([value(v) for v in model_vars])
    return result


def get_model_vars(m):
    """Returns a list of all variables in a model. Distinguishes between
    indexed and non-indexed variables"""
    variable_list = []
    for v in m.component_objects(Var, active=True):
        if type(v) == pyomo.core.base.var.IndexedVar:
            for i in list(v.keys()):
                variable_list.append(v[i])
        else:
            variable_list.append(v)
    return variable_list


def get_int_vars(m):
    """Returns a list of all integer variables from the model"""
    model_vars = get_model_vars(m)
    int_vars = [v for v in model_vars if (str(v.domain) in int_type)]
    return int_vars

def get_cont_vars(m):
    """Returns a list of all continuous variables from the model"""
    model_vars = get_model_vars(m)
    cont_vars = [v for v in model_vars if (str(v.domain) not in int_type)]
    return cont_vars


def get_linear_constrs(m):
    linear_constrs = []
    for constr in m.component_objects(Constraint, active=True):
        if constr.body.polynomial_degree() in [0, 1]:
            linear_constrs.append(constr)
    return linear_constrs


def get_nonlinear_constrs(m):
    nonlinear_constrs = []
    for constr in m.component_objects(Constraint, active=True):
        if not constr.body.polynomial_degree() in [0, 1]:
            nonlinear_constrs.append(constr)
    return nonlinear_constrs

def contains_only_numbers(nablaG):
    result = True
    for i in range(len(nablaG)):
        if not(isinstance(nablaG[i],numbers.Number)):
            result = False
            return result
    return result



def is_zero_vector(nablaG):
    """
    With this function, we check if nablaG contains only zeros. Note that we can't just query
    any(nablaG), because we might have an expression exrp=x as entry
    with variable x=0 which will then return True
    """

    result = True
    for i in range(len(nablaG)):
        if not((isinstance(nablaG[i], numbers.Number)) and (nablaG[i] == 0)):
            result = False
            return result
    return result


def objective_is_linear(model):
    if model.obj.expr.polynomial_degree() in [0, 1]:
        result = True
    else:
        result = False
    return result


def filter_only_integer_constrains(linear_constr_list):
    result = []
    for constr in linear_constr_list:
        if contains_only_integer_vars(constr):
            result.append(constr)
    return result


def contains_only_integer_vars(constr):
    result = True
    my_vars = get_vars_from_constr(constr)
    for v in my_vars:
        if str(v.domain) not in int_type:
            result = False
            break
    return result


def contains_some_integer_vars(constr):
    my_vars = get_vars_from_constr(constr)
    for v in my_vars:
        if str(v.domain) in int_type:
            return True
    return False


def contains_only_integer_vars_grad_el(el):
    my_vars = get_vars_from_grad_el(el)
    for v in my_vars:
        if str(v.domain) not in int_type:
            return False
    return True

def number_nonlinear_constrs(m):
    result = 0
    for constr in m.component_objects(Constraint, active=True):
        if not (constr.body.polynomial_degree() in [0, 1]):
            result = result + 1
    return result

def numbers_constrs(m):
    y = get_int_vars(m)
    n_constrs = 0
    n_nl_constrs = 0
    n_nl_lin_in_y_constrs = 0
    n_nl_nl_in_y_constrs = 0
    for constr in m.component_objects(Constraint, active=True):
        n_constrs+=1
        if not (constr.body.polynomial_degree() in [0, 1]):
            n_nl_constrs +=1
            nablaG = gradient_symb(constr,y)
            if not is_zero_vector(nablaG):
                n_nl_lin_in_y_constrs += 1
                if not contains_only_numbers(nablaG):
                    n_nl_nl_in_y_constrs += 1
    result = (n_constrs, n_nl_constrs,n_nl_lin_in_y_constrs,n_nl_nl_in_y_constrs)
    return result

def get_number_of_binary_vars(m):

    variables = get_model_vars(m)
    isBinary = np.zeros(len(variables))
    for i,v in enumerate(variables):
        if (str(v.domain) == 'Binary') or (v.domain in int_type and v.bounds[0] == 0 and v.bounds[1] == 1):
            isBinary[i] = 1
    return int(sum(isBinary))


def contains_cont_vars(constr):

    vars = get_vars_from_constr(constr)
    for v in vars:
        if str(v.domain) not in int_type:
            return True
    return False



def get_enlargement_nonlinear(constr):

    omega = 0
    if contains_cont_vars(constr):
        return omega
    else:
        active_vars = get_vars_from_constr(constr)
        nabla_G = gradient_symb(constr,active_vars)
        for i, grad in enumerate(nabla_G):
            coeff = get_coeff(grad,active_vars)
            try:
                const = grad._const
            except:
                const = 0
            if const!=0:
                coeff = np.append(coeff,grad._const) # coefficient of linear part. Gets appended so that coeff contains m+1 entries
            coeff[i] = coeff[i]/2 # If we have y_1**2, we get coeff 2, but want 1.
            if any(coeff - np.floor(coeff) > 0): # If any value is no integer, we cannot enlarge the constraint
                return 0
            else:
                coeff = coeff.astype(int)
            if i==0:
                omega = gcd_vec(coeff)
            else:
                omega = min(omega,gcd_vec(coeff))
    return  omega

def get_coeff_nonlinear_constr(c):
    result = 0
    return result


