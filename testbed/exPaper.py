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

model = m = ConcreteModel()


m.i1 = Var(within=Integers,bounds=(-1,2))
m.i2 = Var(within=Integers,bounds=(-1,2))


m.obj = Objective(expr=  -m.i1 - m.i2, sense=minimize)

m.c1 = Constraint(expr = 3*m.i1**2 - m.i1*m.i2 + 2*m.i2**2 <= 10 )
