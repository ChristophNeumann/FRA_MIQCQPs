from pyomo.environ import *
m = ConcreteModel()
m.y1 = Var(within=Integers, bounds=(0, 5))
m.y2 = Var(within=Integers, bounds=(0, 5))
m.c1 = Constraint(expr = 2*m.y1**2 + 2*m.y2**2 - 4*m.y1*m.y2 <= 10.3 )



