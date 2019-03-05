from pyomo.environ import *
from model_manipulation import *

m = ConcreteModel()
m.y1 = Var(within=Integers, bounds=(0, 5))
m.y2 = Var(within=Integers, bounds=(0, 5))
m.x = Var(within = Reals, bounds = (2,None))

m.obj = Objective(expr= -m.y1 - m.y2, sense=minimize)
m.c1 = Constraint(expr = 2*m.y1**2 + m.y2**2 - 3*m.y1*m.y2 <= 10 )
m.c2 = Constraint(expr = m.y1 + m.x <= 3)
m.c3 = Constraint(expr = m.y1 + m.y2 <= 5)
