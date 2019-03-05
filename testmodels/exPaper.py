from pyomo.environ import *
from model_manipulation import *
from model_information import *

model = m = ConcreteModel()


m.i1 = Var(within =Integers, bounds = (1,2))
m.i2 = Var(within=Integers,bounds=(1,2))

m.obj = Objective(expr=  -m.i1 - m.i2, sense=minimize)
m.c1 = Constraint(expr = 3*m.i1**2 - m.i1*m.i2 + 2*m.i2**2 <= 9 )
