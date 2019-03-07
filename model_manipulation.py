from model_information import *
from pyomo.core.base.expr import clone_expression
from milp_formulation import *
from pyomo.repn import generate_canonical_repn
import globals
import logging

def add_objective_bound(m):
    m.obj_con = Constraint(expr = m.obj.expr >= -globals.ABS_BOUND)

def enlarged_IPS(m):
    ''' Computes the enlarged inner parallel set of a MIQCQP m.
    There are three enlargement steps
    1. Compute the EIPS of nonlinear constraints
    2. Compute the EIPS of polyhedral constraints that are NO box constraints
    3. Compute the EIPS of box constraints
    '''

    time_ips = 0
    eips = m.clone()
    linear_constrs = get_linear_constraints(eips)
    nonlinear_constrs = get_nonlinear_constrs(eips)
    is_int = bool_vec_is_int(eips)
    model_vars = get_model_vars(eips)

    ## Step 1: nonlinear constrs.
    for constr in nonlinear_constrs:
        if not constr.equality:
            L_infty, runtime_i = compute_lipschitz(constr,eips)
            if L_infty == np.inf:
                return None, runtime_i # EIPS cannot be computed
            omega = get_enlargement_nonlinear(constr)
            time_ips += runtime_i
            if is_leq_constr(constr):
                constr.set_value(constr.body <= constr.upper() - 1 / 2 * L_infty + globals.delta_enlargement * omega)
            else:
                constr.set_value(-constr.body <= -constr.lower() - 1/2*L_infty + globals.delta_enlargement * omega)


    ## Step 2: EIPS of linear constrs
    for constr in linear_constrs:
        coeff = get_coeff(constr, model_vars)
        beta = np.linalg.norm(coeff[is_int],ord=1)
        g = enlargement_param(coeff,is_int)
        if not constr.equality:
            if is_leq_constr(constr):
                constr.set_value(constr.body <= floor_g(constr.upper(),g) - 1 / 2 * beta + globals.delta_enlargement * g)
            else:
                constr.set_value(-constr.body <= floor_g(-constr.lower(),g) - 1 / 2 * beta + globals.delta_enlargement * g)

    ## Step 3: Enlarge box constraints
    EIPS_box_constrs(model_vars)
    cont_relax_model(model_vars) # Integral variables become continuous
    return eips, time_ips

def fill_with_zeros(nablaG,index_inactive):
    for idx in index_inactive:
        nablaG.insert(idx,0.0)
    return nablaG

def compute_lipschitz(constr, model):
    y = get_int_vars(model)
    y_active, index_inactive = get_active_int_vars_from_constr(constr, y)
    nablaG = gradient_symb(constr, y_active)
    nablaG = fill_with_zeros(nablaG,index_inactive)
    D = get_linear_constraints(model)

    if is_zero_vector(nablaG):
        L_infty = 0
        runtime = 0

    elif contains_only_numbers(nablaG):
        L_infty = np.linalg.norm(np.array(nablaG))
        runtime = 0
        logging.debug("Constraint " + constr.name + " is linear in y")

    else:
        x = get_cont_vars(model)
        L_infty, runtime = milp_for_L(nablaG, D, x, y) # Main work is done here!
    return L_infty, runtime

def box_constrs_to_expr(m, in_vars):
    for var in in_vars:
        if var.bounds[0] is not None:
            m.add_component(var.name + "_lb", Constraint(expr = var >= var.bounds[0]))
        if var.bounds[1] is not None:
            m.add_component(var.name + "_ub", Constraint(expr = var <= var.bounds[1]))


def enlarge_box_constraint(var):
    if (var.bounds is not None) and (var.bounds[0] is not None):
        var.setlb(math.ceil(var.bounds[0]) + 1/2 - globals.delta_enlargement)
    if (var.bounds is not None) and (var.bounds[1] is not None):
        var.setub(math.floor(var.bounds[1]) - 1/2 + globals.delta_enlargement)


def cont_relax_model(model_vars):
    for var in model_vars:
        if str(var.domain) in int_type:
            var.domain = Reals

def EIPS_box_constrs(model_vars):
    for var in model_vars:
        if str(var.domain) in int_type:
            enlarge_box_constraint(var)



def deactivate_nonlinear_constrs(m):
    """Deactivates all nonlinear constraints of a pyomo model m"""
    for constr in m.component_objects(Constraint, active=True):
        if not (constr.body.polynomial_degree() in [0, 1]):
            constr.deactivate()

def activate_nonlinear_constrs(m):
    """Activates all constraints of a pyomo model m"""
    for constr in m.component_objects(Constraint):
        if not (constr.body.polynomial_degree() in [0, 1]):
             constr.activate()


def add_box_constraints(m):
    for var in get_model_vars(m):
        if (var.bounds is None) or ((var.bounds[0] == None) and (var.bounds[1] == None)):
            var.setlb(-globals.ABS_BOUND)
            var.setub(globals.ABS_BOUND)
        elif var.bounds[0] is None:
            var.setlb(-globals.ABS_BOUND)
        elif var.bounds[1] is None:
            var.setub(globals.ABS_BOUND)

def set_var_vals(var_list,value_list,is_int):
    for idx,var in enumerate(var_list):
        if(is_int[idx]):
            var.set_value(int(value_list[idx]))
        else:
            var.set_value(value_list[idx])

def invert_sense(model):
    model.obj.sense = model.obj.sense * (-1)
    model.obj.expr = model.obj.expr * (-1)

def epgraph_reformulation(model):

    #get lower bound for alpha
    model_lb_epi = model.clone()
    model_vars = get_model_vars(model_lb_epi)
    cont_relax_model(model_vars)
    opt = SolverFactory('gurobi')
    try:
        solver_message = opt.solve(model_lb_epi)
        lb = value(model_lb_epi.obj)
        print('runtime for lower bound epi: ' + str(solver_message.solver.time))
        print('lower bound is: ' + str(lb))
    except:
        print('cannot compute lower bound with gurobi')
        lb = -globals.ABS_BOUND
    epi_model = model.clone()
    epi_model.alpha_epi = Var(within = Reals, bounds =(lb,globals.ABS_BOUND) )
    epi_model.con_epi = Constraint(expr = epi_model.obj.expr <= epi_model.alpha_epi )
    epi_model.obj = Objective(expr = epi_model.alpha_epi, sense = minimize)
    return epi_model

def preprocess_model(model):
    is_epi = False
    if (not objective_is_linear(model)):
        model = epgraph_reformulation(model)
        is_epi = True
        print('Performing FCPA on epigraph reformulation')
    return model, is_epi

def rounding(x, isInt):
    """Returns the componentwise rounding x_check of some point x (list or numpy array),
       where x_check[i] = x[i], if isInt is false, and x_check[i] = round(x[i]), otherwise """
    x = np.array(x)
    x_check = np.array(x)
    x_check[isInt] = np.round(x[isInt])
    return x_check
