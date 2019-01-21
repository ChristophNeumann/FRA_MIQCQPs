from model_information import *
from pyomo.core.base.expr import clone_expression
from milp_formulation import *
from pyomo.repn import generate_canonical_repn
ABS_BOUND = 1E12 #Lower bound for objective value/ variables in case of unboundedness
delta = 1-10**-4 # Enlargement parameter

def add_objective_bound(m):
    m.obj_con = Constraint(expr = m.obj.expr >= -ABS_BOUND)


def enlarged_IPS(m):
    eips = m.clone()
    linear_constrs = get_linear_constraints(eips)
    nonlinear_constrs = get_nonlinear_constrs(eips)
    model_vars = get_model_vars(eips)
    is_int = bool_vec_is_int(eips)

    #Initially, we enlarge the box constraints. These are then used for the computation of the Lipschitz constants.
    enlarge_box_constrs(model_vars)

    ## Compute inner approximation wrt. nonlinear constraints. Needs to be done BEFORE the linear constraints,
    ## due to the reason that extract D_y from EIPS! Note that we can't use m, because constr is taken from eips.
    for constr in nonlinear_constrs:
        if not constr.equality:
            print(constr)
            L_infty = compute_lipschitz(constr,eips) #Todo: Enlargmenet
            if is_leq_constr(constr):
                constr.set_value(constr.body <= constr.upper() - 1/2*L_infty)
            else:
                constr.set_value(-constr.body <= -constr.lower() - 1/2*L_infty)


    ## Compute EIPS of linear constraints first
    for constr in linear_constrs:
        coeff = get_coeff(constr, model_vars)
        beta = np.linalg.norm(coeff[is_int],ord=1)
        g = enlargement_param(coeff,is_int)
        if not constr.equality:
            if is_leq_constr(constr):
                constr.set_value(constr.body <= floor_g(constr.upper(),g)-1/2*beta + delta*g)
            else:
                constr.set_value(-constr.body <= floor_g(-constr.lower(),g) - 1/2*beta + delta*g)

    cont_relax_model(model_vars) # Integral variables become continuous
    return eips

def compute_lipschitz(constr, model):
    y = get_int_vars(model)
    D = get_linear_constraints(model)
    D_y = filter_only_integer_constrains(D)
    nablaG = gradient_symb(constr, y)
    if is_zero_vector(nablaG):
        L_infty = 0
        print("Constraint " + constr.name + " has no integral variables")
    else:
        L_infty = milp_for_L(nablaG, D_y, y) # Main work is done here!
    return L_infty

def box_constrs_to_expr(m, in_vars):
    for var in in_vars:
        if var.bounds[0] is not None:
            m.add_component(var.name + "_lb", Constraint(expr = var >= var.bounds[0]))
        if var.bounds[1] is not None:
            m.add_component(var.name + "_ub", Constraint(expr = var <= var.bounds[1]))


def enlarge_box_constraint(var):
    if (var.bounds is not None) and (var.bounds[0] is not None):
        var.setlb(math.ceil(var.bounds[0]) - delta / 2)
    if (var.bounds is not None) and (var.bounds[1] is not None):
        var.setub(math.floor(var.bounds[1]) + delta / 2)


def cont_relax_model(model_vars):
    for var in model_vars:
        if str(var.domain) in int_type:
            var.domain = Reals

def enlarge_box_constrs(model_vars):
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
            var.setlb(-ABS_BOUND)
            var.setub(ABS_BOUND)
        elif var.bounds[0] is None:
            var.setlb(-ABS_BOUND)
        elif var.bounds[1] is None:
            var.setub(ABS_BOUND)

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
        lb = -ABS_BOUND
    epi_model = model.clone()
    epi_model.alpha_epi = Var(within = Reals, bounds =(lb,ABS_BOUND) )
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
