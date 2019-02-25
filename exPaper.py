#  MINLP written by GAMS Convert at 01/04/19 10:37:13
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         13        1        0       12        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#          9        1        2        6        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         33       25        8        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *
from model_manipulation import *
from model_information import *

model = m = ConcreteModel()


m.i1 = Var(within=Integers,bounds=(-1,2))
m.i2 = Var(within=Integers,bounds=(-1,2))
m.x = Var(within = Reals)

m.obj = Objective(expr=  -m.i1 - m.i2, sense=minimize)
m.c1 = Constraint(expr = m.i1 - m.i2 <=0)
m.c2 = Constraint(expr = 3*m.i1**2 - m.i1*m.i2 + 2*m.i2**2 + 2.5*m.i2 + m.x**2 <= 10 )
m.c3 = Constraint(expr = m.i1 + m.x <= 1000)
m.c4 = Constraint(expr = 4*m.i1**2 + 2*m.i1 + 8*m.i1*m.i2 <= 3)

eips, time_IPS = enlarged_IPS(m)
print(eips)