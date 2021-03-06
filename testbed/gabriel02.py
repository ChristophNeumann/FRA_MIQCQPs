#  MINLP written by GAMS Convert at 01/04/19 10:30:22
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        598      120       56      422        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        262      191       71        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       2609     1585     1024        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x2 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x10 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x13 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x14 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x15 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x16 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x17 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x18 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x19 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x20 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x21 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x22 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x23 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x24 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x25 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x26 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x27 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x28 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x29 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x30 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x31 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x32 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x33 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x34 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x35 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x36 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x37 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x38 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x39 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x40 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x41 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x42 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x43 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x44 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x45 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x46 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x47 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x48 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x49 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x50 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x51 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x52 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x53 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x54 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x55 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x56 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x57 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x58 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x59 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x60 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x61 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x62 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x63 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x64 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x65 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x66 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x67 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x68 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x69 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x70 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x71 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x72 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x73 = Var(within=Reals,bounds=(0.7,1),initialize=0.7)
m.x74 = Var(within=Reals,bounds=(0.7,1),initialize=0.7)
m.x75 = Var(within=Reals,bounds=(0.7,1),initialize=0.7)
m.x76 = Var(within=Reals,bounds=(0.7,1),initialize=0.7)
m.x77 = Var(within=Reals,bounds=(0,0.9),initialize=0)
m.x78 = Var(within=Reals,bounds=(0,0.9),initialize=0)
m.x79 = Var(within=Reals,bounds=(0,0.9),initialize=0)
m.x80 = Var(within=Reals,bounds=(0,0.9),initialize=0)
m.x81 = Var(within=Reals,bounds=(0.66,1),initialize=0.66)
m.x82 = Var(within=Reals,bounds=(0.66,1),initialize=0.66)
m.x83 = Var(within=Reals,bounds=(0.66,1),initialize=0.66)
m.x84 = Var(within=Reals,bounds=(0.66,1),initialize=0.66)
m.x85 = Var(within=Reals,bounds=(0,0.92),initialize=0)
m.x86 = Var(within=Reals,bounds=(0,0.92),initialize=0)
m.x87 = Var(within=Reals,bounds=(0,0.92),initialize=0)
m.x88 = Var(within=Reals,bounds=(0,0.92),initialize=0)
m.x89 = Var(within=Reals,bounds=(0.67,0.99),initialize=0.67)
m.x90 = Var(within=Reals,bounds=(0.67,0.99),initialize=0.67)
m.x91 = Var(within=Reals,bounds=(0.67,0.99),initialize=0.67)
m.x92 = Var(within=Reals,bounds=(0.67,0.99),initialize=0.67)
m.x93 = Var(within=Reals,bounds=(0,0.96),initialize=0)
m.x94 = Var(within=Reals,bounds=(0,0.96),initialize=0)
m.x95 = Var(within=Reals,bounds=(0,0.96),initialize=0)
m.x96 = Var(within=Reals,bounds=(0,0.96),initialize=0)
m.x97 = Var(within=Reals,bounds=(0.66,1),initialize=0.66)
m.x98 = Var(within=Reals,bounds=(0.66,1),initialize=0.66)
m.x99 = Var(within=Reals,bounds=(0.66,1),initialize=0.66)
m.x100 = Var(within=Reals,bounds=(0.66,1),initialize=0.66)
m.x101 = Var(within=Reals,bounds=(0,0.91),initialize=0)
m.x102 = Var(within=Reals,bounds=(0,0.91),initialize=0)
m.x103 = Var(within=Reals,bounds=(0,0.91),initialize=0)
m.x104 = Var(within=Reals,bounds=(0,0.91),initialize=0)
m.b105 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b106 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b107 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b108 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b109 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b110 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b111 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b112 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b113 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b114 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b115 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b116 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b117 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b118 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b119 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b120 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b121 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b122 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b123 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b124 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b125 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b126 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b127 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b128 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b129 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b130 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b131 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b132 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b133 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b134 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b135 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b136 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b137 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b138 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b139 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b140 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b141 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b142 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b143 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b144 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b145 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b146 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b147 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b148 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b149 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b150 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b151 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b152 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b153 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b154 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b155 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b156 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b157 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b158 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b159 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b160 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b161 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b162 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b163 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b164 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b165 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b166 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b167 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b168 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b169 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b170 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b171 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b172 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b173 = Var(within=Binary,bounds=(0,1),initialize=0)
m.x174 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x175 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x176 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x177 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x178 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x179 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x180 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x181 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x182 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x183 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x184 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x185 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x186 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x187 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x188 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x189 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x190 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x191 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x192 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x193 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x194 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x195 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x196 = Var(within=Reals,bounds=(0,2),initialize=0)
m.b197 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b198 = Var(within=Binary,bounds=(0,1),initialize=0)
m.x199 = Var(within=Reals,bounds=(0.7,1),initialize=0.7)
m.x200 = Var(within=Reals,bounds=(0.7,1),initialize=0.7)
m.x201 = Var(within=Reals,bounds=(0.7,1),initialize=0.7)
m.x202 = Var(within=Reals,bounds=(0.7,1),initialize=0.7)
m.x203 = Var(within=Reals,bounds=(0.7,1),initialize=0.7)
m.x204 = Var(within=Reals,bounds=(0.7,1),initialize=0.7)
m.x205 = Var(within=Reals,bounds=(0.7,1),initialize=0.7)
m.x206 = Var(within=Reals,bounds=(0.7,1),initialize=0.7)
m.x207 = Var(within=Reals,bounds=(0,0.9),initialize=0)
m.x208 = Var(within=Reals,bounds=(0,0.9),initialize=0)
m.x209 = Var(within=Reals,bounds=(0,0.9),initialize=0)
m.x210 = Var(within=Reals,bounds=(0,0.9),initialize=0)
m.x211 = Var(within=Reals,bounds=(0,0.9),initialize=0)
m.x212 = Var(within=Reals,bounds=(0,0.9),initialize=0)
m.x213 = Var(within=Reals,bounds=(0,0.9),initialize=0)
m.x214 = Var(within=Reals,bounds=(0,0.9),initialize=0)
m.x215 = Var(within=Reals,bounds=(0.66,1),initialize=0.66)
m.x216 = Var(within=Reals,bounds=(0.66,1),initialize=0.66)
m.x217 = Var(within=Reals,bounds=(0.66,1),initialize=0.66)
m.x218 = Var(within=Reals,bounds=(0.66,1),initialize=0.66)
m.x219 = Var(within=Reals,bounds=(0.66,1),initialize=0.66)
m.x220 = Var(within=Reals,bounds=(0.66,1),initialize=0.66)
m.x221 = Var(within=Reals,bounds=(0.66,1),initialize=0.66)
m.x222 = Var(within=Reals,bounds=(0.66,1),initialize=0.66)
m.x223 = Var(within=Reals,bounds=(0,0.92),initialize=0)
m.x224 = Var(within=Reals,bounds=(0,0.92),initialize=0)
m.x225 = Var(within=Reals,bounds=(0,0.92),initialize=0)
m.x226 = Var(within=Reals,bounds=(0,0.92),initialize=0)
m.x227 = Var(within=Reals,bounds=(0,0.92),initialize=0)
m.x228 = Var(within=Reals,bounds=(0,0.92),initialize=0)
m.x229 = Var(within=Reals,bounds=(0,0.92),initialize=0)
m.x230 = Var(within=Reals,bounds=(0,0.92),initialize=0)
m.x231 = Var(within=Reals,bounds=(0.67,0.99),initialize=0.67)
m.x232 = Var(within=Reals,bounds=(0.67,0.99),initialize=0.67)
m.x233 = Var(within=Reals,bounds=(0.67,0.99),initialize=0.67)
m.x234 = Var(within=Reals,bounds=(0.67,0.99),initialize=0.67)
m.x235 = Var(within=Reals,bounds=(0.67,0.99),initialize=0.67)
m.x236 = Var(within=Reals,bounds=(0.67,0.99),initialize=0.67)
m.x237 = Var(within=Reals,bounds=(0.67,0.99),initialize=0.67)
m.x238 = Var(within=Reals,bounds=(0.67,0.99),initialize=0.67)
m.x239 = Var(within=Reals,bounds=(0,0.96),initialize=0)
m.x240 = Var(within=Reals,bounds=(0,0.96),initialize=0)
m.x241 = Var(within=Reals,bounds=(0,0.96),initialize=0)
m.x242 = Var(within=Reals,bounds=(0,0.96),initialize=0)
m.x243 = Var(within=Reals,bounds=(0,0.96),initialize=0)
m.x244 = Var(within=Reals,bounds=(0,0.96),initialize=0)
m.x245 = Var(within=Reals,bounds=(0,0.96),initialize=0)
m.x246 = Var(within=Reals,bounds=(0,0.96),initialize=0)
m.x247 = Var(within=Reals,bounds=(0.66,1),initialize=0.66)
m.x248 = Var(within=Reals,bounds=(0.66,1),initialize=0.66)
m.x249 = Var(within=Reals,bounds=(0.66,1),initialize=0.66)
m.x250 = Var(within=Reals,bounds=(0.66,1),initialize=0.66)
m.x251 = Var(within=Reals,bounds=(0.66,1),initialize=0.66)
m.x252 = Var(within=Reals,bounds=(0.66,1),initialize=0.66)
m.x253 = Var(within=Reals,bounds=(0.66,1),initialize=0.66)
m.x254 = Var(within=Reals,bounds=(0.66,1),initialize=0.66)
m.x255 = Var(within=Reals,bounds=(0,0.91),initialize=0)
m.x256 = Var(within=Reals,bounds=(0,0.91),initialize=0)
m.x257 = Var(within=Reals,bounds=(0,0.91),initialize=0)
m.x258 = Var(within=Reals,bounds=(0,0.91),initialize=0)
m.x259 = Var(within=Reals,bounds=(0,0.91),initialize=0)
m.x260 = Var(within=Reals,bounds=(0,0.91),initialize=0)
m.x261 = Var(within=Reals,bounds=(0,0.91),initialize=0)
m.x262 = Var(within=Reals,bounds=(0,0.91),initialize=0)

m.obj = Objective(expr= - 0.45*m.x2 - 0.45*m.x3 - 0.45*m.x4 - 0.67*m.x5 - 0.67*m.x6 - 0.67*m.x7 - 1.03*m.x8 - 1.03*m.x9
                        - 1.03*m.x10 - 1.75*m.x11 - 1.75*m.x12 - 1.75*m.x13 - 1.57*m.x14 - 1.57*m.x15 - 1.57*m.x16
                        - 1.05*m.x17 - 1.05*m.x18 - 1.05*m.x19 - 0.13*m.x20 - 0.13*m.x21 - 0.13*m.x22 - 0.47*m.x23
                        - 0.47*m.x24 - 0.47*m.x25 - 0.34*m.x26 - 0.34*m.x27 - 0.34*m.x28 + 8.81*m.x29 + 8.81*m.x30
                        + 9.07*m.x31 + 9.07*m.x32 - 0.6*m.x33 - 0.6*m.x34 - 0.6*m.x35 - 0.65*m.x36 - 0.65*m.x37
                        - 0.65*m.x38 - 0.75*m.x39 - 0.75*m.x40 - 0.75*m.x41 + 9.52*m.x42 + 9.52*m.x43 + 9.52*m.x44
                        + 8.69*m.x45 + 8.69*m.x46 - 0.83*m.x47 - 0.83*m.x48 - 0.83*m.x49 - m.x50 - m.x51 - m.x52
                        - 0.44*m.x53 - 0.44*m.x54 - 0.44*m.x55 + 8.64*m.x56 + 8.64*m.x57 + 8.83*m.x58 + 8.83*m.x59
                        - 0.87*m.x60 - 0.87*m.x61 - 0.87*m.x62 - 0.4*m.x63 - 0.4*m.x64 - 0.4*m.x65 - 0.8*m.x66
                        - 0.8*m.x67 - 0.8*m.x68 + 8.69*m.x69 + 8.69*m.x70 + 9.34*m.x71 + 9.34*m.x72 - 0.2*m.b105
                        - 0.2*m.b106 - 0.2*m.b107 - 0.62*m.b108 - 0.62*m.b109 - 0.62*m.b110 - 0.35*m.b111 - 0.35*m.b112
                        - 0.35*m.b113 - 0.76*m.b114 - 0.76*m.b115 - 0.76*m.b116 - 0.38*m.b117 - 0.38*m.b118
                        - 0.38*m.b119 - 0.08*m.b120 - 0.08*m.b121 - 0.08*m.b122 - 0.93*m.b123 - 0.93*m.b124
                        - 0.93*m.b125 - 0.57*m.b126 - 0.57*m.b127 - 0.57*m.b128 - 0.01*m.b129 - 0.01*m.b130
                        - 0.01*m.b131 - 0.16*m.b132 - 0.16*m.b133 - 0.31*m.b134 - 0.31*m.b135 - 0.17*m.b136
                        - 0.17*m.b137 - 0.17*m.b138 - 0.26*m.b139 - 0.26*m.b140 - 0.26*m.b141 - 0.69*m.b142
                        - 0.69*m.b143 - 0.69*m.b144 - 0.45*m.b145 - 0.45*m.b146 - 0.45*m.b147 - 0.23*m.b148
                        - 0.23*m.b149 - 0.15*m.b150 - 0.15*m.b151 - 0.15*m.b152 - 0.54*m.b153 - 0.54*m.b154
                        - 0.54*m.b155 - 0.08*m.b156 - 0.08*m.b157 - 0.08*m.b158 - 0.11*m.b159 - 0.11*m.b160
                        - 0.82*m.b161 - 0.82*m.b162 - 0.82*m.b163 - 0.08*m.b164 - 0.08*m.b165 - 0.08*m.b166
                        - 0.26*m.b167 - 0.26*m.b168 - 0.26*m.b169 - 0.43*m.b170 - 0.43*m.b171 - 0.18*m.b172
                        - 0.18*m.b173, sense=maximize)

m.c2 = Constraint(expr=   m.x2 + m.x5 + m.x8 + m.x174 == 1.9)

m.c3 = Constraint(expr=   m.x11 + m.x14 + m.x17 + m.x175 == 1.8)

m.c4 = Constraint(expr= - m.x11 + m.x20 + m.x23 + m.x26 - m.x33 - m.x47 - m.x60 + m.x176 == 0.3)

m.c5 = Constraint(expr= - m.x2 - m.x14 - m.x20 + m.x33 + m.x36 + m.x39 + m.x42 - m.x50 - m.x63 + m.x177 == 1.8)

m.c6 = Constraint(expr= - m.x5 - m.x17 - m.x23 - m.x36 + m.x47 + m.x50 + m.x53 - m.x66 + m.x178 == 1.3)

m.c7 = Constraint(expr= - m.x8 - m.x26 - m.x39 - m.x53 + m.x60 + m.x63 + m.x66 + m.x179 == 0.2)

m.c8 = Constraint(expr= - m.x42 + m.x180 == -0.35)

m.c9 = Constraint(expr=   m.x3 + m.x6 + m.x9 - m.x174 + m.x181 == 0.1)

m.c10 = Constraint(expr=   m.x4 + m.x7 + m.x10 - m.x181 + m.x182 == 0.7)

m.c11 = Constraint(expr=   m.x12 + m.x15 + m.x18 - m.x175 + m.x183 == 0.8)

m.c12 = Constraint(expr=   m.x13 + m.x16 + m.x19 - m.x183 + m.x184 == 0.3)

m.c13 = Constraint(expr= - m.x12 + m.x21 + m.x24 + m.x27 + m.x29 + m.x31 - m.x34 - m.x48 - m.x61 - m.x176 + m.x185 == 0)

m.c14 = Constraint(expr= - m.x13 + m.x22 + m.x25 + m.x28 + m.x30 + m.x32 - m.x35 - m.x49 - m.x62 - m.x185 + m.x186 == 0)

m.c15 = Constraint(expr= - m.x3 - m.x15 - m.x21 + m.x34 + m.x37 + m.x40 + m.x43 + m.x45 - m.x51 - m.x64 - m.x177
                         + m.x187 == 0)

m.c16 = Constraint(expr= - m.x4 - m.x16 - m.x22 + m.x35 + m.x38 + m.x41 + m.x44 + m.x46 - m.x52 - m.x65 - m.x187
                         + m.x188 == 0)

m.c17 = Constraint(expr= - m.x6 - m.x18 - m.x24 - m.x37 + m.x48 + m.x51 + m.x54 + m.x56 + m.x58 - m.x67 - m.x178
                         + m.x189 == 0)

m.c18 = Constraint(expr= - m.x7 - m.x19 - m.x25 - m.x38 + m.x49 + m.x52 + m.x55 + m.x57 + m.x59 - m.x68 - m.x189
                         + m.x190 == 0)

m.c19 = Constraint(expr= - m.x9 - m.x27 - m.x40 - m.x54 + m.x61 + m.x64 + m.x67 + m.x69 + m.x71 - m.x179 + m.x191 == 0)

m.c20 = Constraint(expr= - m.x10 - m.x28 - m.x41 - m.x55 + m.x62 + m.x65 + m.x68 + m.x70 + m.x72 - m.x191 + m.x192 == 0)

m.c21 = Constraint(expr= - m.x29 - m.x43 - m.x56 - m.x69 - m.x180 + m.x193 == -0.44)

m.c22 = Constraint(expr= - m.x30 - m.x44 - m.x57 - m.x70 - m.x193 + m.x194 == -0.77)

m.c23 = Constraint(expr= - m.x31 - m.x45 - m.x58 - m.x71 + m.x195 == 0.69)

m.c24 = Constraint(expr= - m.x32 - m.x46 - m.x59 - m.x72 - m.x195 + m.x196 == -0.8)

m.c25 = Constraint(expr=   m.x2 - m.b105 <= 0)

m.c26 = Constraint(expr=   m.x3 - m.b106 <= 0)

m.c27 = Constraint(expr=   m.x4 - m.b107 <= 0)

m.c28 = Constraint(expr=   m.x5 - m.b108 <= 0)

m.c29 = Constraint(expr=   m.x6 - m.b109 <= 0)

m.c30 = Constraint(expr=   m.x7 - m.b110 <= 0)

m.c31 = Constraint(expr=   m.x8 - m.b111 <= 0)

m.c32 = Constraint(expr=   m.x9 - m.b112 <= 0)

m.c33 = Constraint(expr=   m.x10 - m.b113 <= 0)

m.c34 = Constraint(expr=   m.x11 - m.b114 <= 0)

m.c35 = Constraint(expr=   m.x12 - m.b115 <= 0)

m.c36 = Constraint(expr=   m.x13 - m.b116 <= 0)

m.c37 = Constraint(expr=   m.x14 - m.b117 <= 0)

m.c38 = Constraint(expr=   m.x15 - m.b118 <= 0)

m.c39 = Constraint(expr=   m.x16 - m.b119 <= 0)

m.c40 = Constraint(expr=   m.x17 - m.b120 <= 0)

m.c41 = Constraint(expr=   m.x18 - m.b121 <= 0)

m.c42 = Constraint(expr=   m.x19 - m.b122 <= 0)

m.c43 = Constraint(expr=   m.x20 - m.b123 <= 0)

m.c44 = Constraint(expr=   m.x21 - m.b124 <= 0)

m.c45 = Constraint(expr=   m.x22 - m.b125 <= 0)

m.c46 = Constraint(expr=   m.x23 - m.b126 <= 0)

m.c47 = Constraint(expr=   m.x24 - m.b127 <= 0)

m.c48 = Constraint(expr=   m.x25 - m.b128 <= 0)

m.c49 = Constraint(expr=   m.x26 - m.b129 <= 0)

m.c50 = Constraint(expr=   m.x27 - m.b130 <= 0)

m.c51 = Constraint(expr=   m.x28 - m.b131 <= 0)

m.c52 = Constraint(expr=   m.x29 - m.b132 <= 0)

m.c53 = Constraint(expr=   m.x30 - m.b133 <= 0)

m.c54 = Constraint(expr=   m.x31 - m.b134 <= 0)

m.c55 = Constraint(expr=   m.x32 - m.b135 <= 0)

m.c56 = Constraint(expr=   m.x33 - m.b136 <= 0)

m.c57 = Constraint(expr=   m.x34 - m.b137 <= 0)

m.c58 = Constraint(expr=   m.x35 - m.b138 <= 0)

m.c59 = Constraint(expr=   m.x36 - m.b139 <= 0)

m.c60 = Constraint(expr=   m.x37 - m.b140 <= 0)

m.c61 = Constraint(expr=   m.x38 - m.b141 <= 0)

m.c62 = Constraint(expr=   m.x39 - m.b142 <= 0)

m.c63 = Constraint(expr=   m.x40 - m.b143 <= 0)

m.c64 = Constraint(expr=   m.x41 - m.b144 <= 0)

m.c65 = Constraint(expr=   m.x42 - m.b145 <= 0)

m.c66 = Constraint(expr=   m.x43 - m.b146 <= 0)

m.c67 = Constraint(expr=   m.x44 - m.b147 <= 0)

m.c68 = Constraint(expr=   m.x45 - m.b148 <= 0)

m.c69 = Constraint(expr=   m.x46 - m.b149 <= 0)

m.c70 = Constraint(expr=   m.x47 - m.b150 <= 0)

m.c71 = Constraint(expr=   m.x48 - m.b151 <= 0)

m.c72 = Constraint(expr=   m.x49 - m.b152 <= 0)

m.c73 = Constraint(expr=   m.x50 - m.b153 <= 0)

m.c74 = Constraint(expr=   m.x51 - m.b154 <= 0)

m.c75 = Constraint(expr=   m.x52 - m.b155 <= 0)

m.c76 = Constraint(expr=   m.x53 - m.b156 <= 0)

m.c77 = Constraint(expr=   m.x54 - m.b157 <= 0)

m.c78 = Constraint(expr=   m.x55 - m.b158 <= 0)

m.c79 = Constraint(expr=   m.x56 - m.b159 <= 0)

m.c80 = Constraint(expr=   m.x57 - m.b160 <= 0)

m.c81 = Constraint(expr=   m.x58 - m.b197 <= 0)

m.c82 = Constraint(expr=   m.x59 - m.b198 <= 0)

m.c83 = Constraint(expr=   m.x60 - m.b161 <= 0)

m.c84 = Constraint(expr=   m.x61 - m.b162 <= 0)

m.c85 = Constraint(expr=   m.x62 - m.b163 <= 0)

m.c86 = Constraint(expr=   m.x63 - m.b164 <= 0)

m.c87 = Constraint(expr=   m.x64 - m.b165 <= 0)

m.c88 = Constraint(expr=   m.x65 - m.b166 <= 0)

m.c89 = Constraint(expr=   m.x66 - m.b167 <= 0)

m.c90 = Constraint(expr=   m.x67 - m.b168 <= 0)

m.c91 = Constraint(expr=   m.x68 - m.b169 <= 0)

m.c92 = Constraint(expr=   m.x69 - m.b170 <= 0)

m.c93 = Constraint(expr=   m.x70 - m.b171 <= 0)

m.c94 = Constraint(expr=   m.x71 - m.b172 <= 0)

m.c95 = Constraint(expr=   m.x72 - m.b173 <= 0)

m.c96 = Constraint(expr=   0.1*m.b134 - m.x199 <= -0.7)

m.c97 = Constraint(expr=   0.1*m.b135 - m.x200 <= -0.7)

m.c98 = Constraint(expr=   0.1*m.b148 - m.x201 <= -0.7)

m.c99 = Constraint(expr=   0.1*m.b149 - m.x202 <= -0.7)

m.c100 = Constraint(expr=   0.1*m.b197 - m.x203 <= -0.7)

m.c101 = Constraint(expr=   0.1*m.b198 - m.x204 <= -0.7)

m.c102 = Constraint(expr=   0.1*m.b172 - m.x205 <= -0.7)

m.c103 = Constraint(expr=   0.1*m.b173 - m.x206 <= -0.7)

m.c104 = Constraint(expr=   0.5*m.b132 - m.x207 <= 0)

m.c105 = Constraint(expr=   0.5*m.b133 - m.x208 <= 0)

m.c106 = Constraint(expr=   0.1*m.b134 - m.x207 <= 0)

m.c107 = Constraint(expr=   0.1*m.b135 - m.x208 <= 0)

m.c108 = Constraint(expr=   0.5*m.b146 - m.x209 <= 0)

m.c109 = Constraint(expr=   0.5*m.b147 - m.x210 <= 0)

m.c110 = Constraint(expr=   0.1*m.b148 - m.x209 <= 0)

m.c111 = Constraint(expr=   0.1*m.b149 - m.x210 <= 0)

m.c112 = Constraint(expr=   0.5*m.b159 - m.x211 <= 0)

m.c113 = Constraint(expr=   0.5*m.b160 - m.x212 <= 0)

m.c114 = Constraint(expr=   0.1*m.b197 - m.x211 <= 0)

m.c115 = Constraint(expr=   0.1*m.b198 - m.x212 <= 0)

m.c116 = Constraint(expr=   0.5*m.b170 - m.x213 <= 0)

m.c117 = Constraint(expr=   0.5*m.b171 - m.x214 <= 0)

m.c118 = Constraint(expr=   0.1*m.b172 - m.x213 <= 0)

m.c119 = Constraint(expr=   0.1*m.b173 - m.x214 <= 0)

m.c120 = Constraint(expr=   0.05*m.b132 - m.x215 <= -0.66)

m.c121 = Constraint(expr=   0.05*m.b133 - m.x216 <= -0.66)

m.c122 = Constraint(expr=   0.13*m.b134 - m.x215 <= -0.66)

m.c123 = Constraint(expr=   0.13*m.b135 - m.x216 <= -0.66)

m.c124 = Constraint(expr=   0.05*m.b146 - m.x217 <= -0.66)

m.c125 = Constraint(expr=   0.05*m.b147 - m.x218 <= -0.66)

m.c126 = Constraint(expr=   0.13*m.b148 - m.x217 <= -0.66)

m.c127 = Constraint(expr=   0.13*m.b149 - m.x218 <= -0.66)

m.c128 = Constraint(expr=   0.05*m.b159 - m.x219 <= -0.66)

m.c129 = Constraint(expr=   0.05*m.b160 - m.x220 <= -0.66)

m.c130 = Constraint(expr=   0.13*m.b197 - m.x219 <= -0.66)

m.c131 = Constraint(expr=   0.13*m.b198 - m.x220 <= -0.66)

m.c132 = Constraint(expr=   0.05*m.b170 - m.x221 <= -0.66)

m.c133 = Constraint(expr=   0.05*m.b171 - m.x222 <= -0.66)

m.c134 = Constraint(expr=   0.13*m.b172 - m.x221 <= -0.66)

m.c135 = Constraint(expr=   0.13*m.b173 - m.x222 <= -0.66)

m.c136 = Constraint(expr=   0.48*m.b132 - m.x223 <= 0)

m.c137 = Constraint(expr=   0.48*m.b133 - m.x224 <= 0)

m.c138 = Constraint(expr=   0.09*m.b134 - m.x223 <= 0)

m.c139 = Constraint(expr=   0.09*m.b135 - m.x224 <= 0)

m.c140 = Constraint(expr=   0.48*m.b146 - m.x225 <= 0)

m.c141 = Constraint(expr=   0.48*m.b147 - m.x226 <= 0)

m.c142 = Constraint(expr=   0.09*m.b148 - m.x225 <= 0)

m.c143 = Constraint(expr=   0.09*m.b149 - m.x226 <= 0)

m.c144 = Constraint(expr=   0.48*m.b159 - m.x227 <= 0)

m.c145 = Constraint(expr=   0.48*m.b160 - m.x228 <= 0)

m.c146 = Constraint(expr=   0.09*m.b197 - m.x227 <= 0)

m.c147 = Constraint(expr=   0.09*m.b198 - m.x228 <= 0)

m.c148 = Constraint(expr=   0.48*m.b170 - m.x229 <= 0)

m.c149 = Constraint(expr=   0.48*m.b171 - m.x230 <= 0)

m.c150 = Constraint(expr=   0.09*m.b172 - m.x229 <= 0)

m.c151 = Constraint(expr=   0.09*m.b173 - m.x230 <= 0)

m.c152 = Constraint(expr=   0.16*m.b134 - m.x231 <= -0.67)

m.c153 = Constraint(expr=   0.16*m.b135 - m.x232 <= -0.67)

m.c154 = Constraint(expr=   0.16*m.b148 - m.x233 <= -0.67)

m.c155 = Constraint(expr=   0.16*m.b149 - m.x234 <= -0.67)

m.c156 = Constraint(expr=   0.16*m.b197 - m.x235 <= -0.67)

m.c157 = Constraint(expr=   0.16*m.b198 - m.x236 <= -0.67)

m.c158 = Constraint(expr=   0.16*m.b172 - m.x237 <= -0.67)

m.c159 = Constraint(expr=   0.16*m.b173 - m.x238 <= -0.67)

m.c160 = Constraint(expr=   0.51*m.b132 - m.x239 <= 0)

m.c161 = Constraint(expr=   0.51*m.b133 - m.x240 <= 0)

m.c162 = Constraint(expr=   0.07*m.b134 - m.x239 <= 0)

m.c163 = Constraint(expr=   0.07*m.b135 - m.x240 <= 0)

m.c164 = Constraint(expr=   0.51*m.b146 - m.x241 <= 0)

m.c165 = Constraint(expr=   0.51*m.b147 - m.x242 <= 0)

m.c166 = Constraint(expr=   0.07*m.b148 - m.x241 <= 0)

m.c167 = Constraint(expr=   0.07*m.b149 - m.x242 <= 0)

m.c168 = Constraint(expr=   0.51*m.b159 - m.x243 <= 0)

m.c169 = Constraint(expr=   0.51*m.b160 - m.x244 <= 0)

m.c170 = Constraint(expr=   0.07*m.b197 - m.x243 <= 0)

m.c171 = Constraint(expr=   0.07*m.b198 - m.x244 <= 0)

m.c172 = Constraint(expr=   0.51*m.b170 - m.x245 <= 0)

m.c173 = Constraint(expr=   0.51*m.b171 - m.x246 <= 0)

m.c174 = Constraint(expr=   0.07*m.b172 - m.x245 <= 0)

m.c175 = Constraint(expr=   0.07*m.b173 - m.x246 <= 0)

m.c176 = Constraint(expr=   0.06*m.b132 - m.x247 <= -0.66)

m.c177 = Constraint(expr=   0.06*m.b133 - m.x248 <= -0.66)

m.c178 = Constraint(expr=   0.17*m.b134 - m.x247 <= -0.66)

m.c179 = Constraint(expr=   0.17*m.b135 - m.x248 <= -0.66)

m.c180 = Constraint(expr=   0.06*m.b146 - m.x249 <= -0.66)

m.c181 = Constraint(expr=   0.06*m.b147 - m.x250 <= -0.66)

m.c182 = Constraint(expr=   0.17*m.b148 - m.x249 <= -0.66)

m.c183 = Constraint(expr=   0.17*m.b149 - m.x250 <= -0.66)

m.c184 = Constraint(expr=   0.06*m.b159 - m.x251 <= -0.66)

m.c185 = Constraint(expr=   0.06*m.b160 - m.x252 <= -0.66)

m.c186 = Constraint(expr=   0.17*m.b197 - m.x251 <= -0.66)

m.c187 = Constraint(expr=   0.17*m.b198 - m.x252 <= -0.66)

m.c188 = Constraint(expr=   0.06*m.b170 - m.x253 <= -0.66)

m.c189 = Constraint(expr=   0.06*m.b171 - m.x254 <= -0.66)

m.c190 = Constraint(expr=   0.17*m.b172 - m.x253 <= -0.66)

m.c191 = Constraint(expr=   0.17*m.b173 - m.x254 <= -0.66)

m.c192 = Constraint(expr=   0.47*m.b132 - m.x255 <= 0)

m.c193 = Constraint(expr=   0.47*m.b133 - m.x256 <= 0)

m.c194 = Constraint(expr=   0.11*m.b134 - m.x255 <= 0)

m.c195 = Constraint(expr=   0.11*m.b135 - m.x256 <= 0)

m.c196 = Constraint(expr=   0.47*m.b146 - m.x257 <= 0)

m.c197 = Constraint(expr=   0.47*m.b147 - m.x258 <= 0)

m.c198 = Constraint(expr=   0.11*m.b148 - m.x257 <= 0)

m.c199 = Constraint(expr=   0.11*m.b149 - m.x258 <= 0)

m.c200 = Constraint(expr=   0.47*m.b159 - m.x259 <= 0)

m.c201 = Constraint(expr=   0.47*m.b160 - m.x260 <= 0)

m.c202 = Constraint(expr=   0.11*m.b197 - m.x259 <= 0)

m.c203 = Constraint(expr=   0.11*m.b198 - m.x260 <= 0)

m.c204 = Constraint(expr=   0.47*m.b170 - m.x261 <= 0)

m.c205 = Constraint(expr=   0.47*m.b171 - m.x262 <= 0)

m.c206 = Constraint(expr=   0.11*m.b172 - m.x261 <= 0)

m.c207 = Constraint(expr=   0.11*m.b173 - m.x262 <= 0)

m.c208 = Constraint(expr= - 0.2*m.b134 - m.x207 >= -0.9)

m.c209 = Constraint(expr= - 0.2*m.b135 - m.x208 >= -0.9)

m.c210 = Constraint(expr= - 0.2*m.b148 - m.x209 >= -0.9)

m.c211 = Constraint(expr= - 0.2*m.b149 - m.x210 >= -0.9)

m.c212 = Constraint(expr= - 0.2*m.b197 - m.x211 >= -0.9)

m.c213 = Constraint(expr= - 0.2*m.b198 - m.x212 >= -0.9)

m.c214 = Constraint(expr= - 0.2*m.b172 - m.x213 >= -0.9)

m.c215 = Constraint(expr= - 0.2*m.b173 - m.x214 >= -0.9)

m.c216 = Constraint(expr= - 0.05*m.b132 - m.x215 >= -1)

m.c217 = Constraint(expr= - 0.05*m.b133 - m.x216 >= -1)

m.c218 = Constraint(expr= - 0.05*m.b146 - m.x217 >= -1)

m.c219 = Constraint(expr= - 0.05*m.b147 - m.x218 >= -1)

m.c220 = Constraint(expr= - 0.05*m.b159 - m.x219 >= -1)

m.c221 = Constraint(expr= - 0.05*m.b160 - m.x220 >= -1)

m.c222 = Constraint(expr= - 0.05*m.b170 - m.x221 >= -1)

m.c223 = Constraint(expr= - 0.05*m.b171 - m.x222 >= -1)

m.c224 = Constraint(expr= - 0.12*m.b134 - m.x223 >= -0.92)

m.c225 = Constraint(expr= - 0.12*m.b135 - m.x224 >= -0.92)

m.c226 = Constraint(expr= - 0.12*m.b148 - m.x225 >= -0.92)

m.c227 = Constraint(expr= - 0.12*m.b149 - m.x226 >= -0.92)

m.c228 = Constraint(expr= - 0.12*m.b197 - m.x227 >= -0.92)

m.c229 = Constraint(expr= - 0.12*m.b198 - m.x228 >= -0.92)

m.c230 = Constraint(expr= - 0.12*m.b172 - m.x229 >= -0.92)

m.c231 = Constraint(expr= - 0.12*m.b173 - m.x230 >= -0.92)

m.c232 = Constraint(expr= - 0.1*m.b132 - m.x231 >= -0.99)

m.c233 = Constraint(expr= - 0.1*m.b133 - m.x232 >= -0.99)

m.c234 = Constraint(expr= - 0.1*m.b146 - m.x233 >= -0.99)

m.c235 = Constraint(expr= - 0.1*m.b147 - m.x234 >= -0.99)

m.c236 = Constraint(expr= - 0.1*m.b159 - m.x235 >= -0.99)

m.c237 = Constraint(expr= - 0.1*m.b160 - m.x236 >= -0.99)

m.c238 = Constraint(expr= - 0.1*m.b170 - m.x237 >= -0.99)

m.c239 = Constraint(expr= - 0.1*m.b171 - m.x238 >= -0.99)

m.c240 = Constraint(expr= - 0.23*m.b134 - m.x239 >= -0.96)

m.c241 = Constraint(expr= - 0.23*m.b135 - m.x240 >= -0.96)

m.c242 = Constraint(expr= - 0.23*m.b148 - m.x241 >= -0.96)

m.c243 = Constraint(expr= - 0.23*m.b149 - m.x242 >= -0.96)

m.c244 = Constraint(expr= - 0.23*m.b197 - m.x243 >= -0.96)

m.c245 = Constraint(expr= - 0.23*m.b198 - m.x244 >= -0.96)

m.c246 = Constraint(expr= - 0.23*m.b172 - m.x245 >= -0.96)

m.c247 = Constraint(expr= - 0.23*m.b173 - m.x246 >= -0.96)

m.c248 = Constraint(expr= - 0.12*m.b134 - m.x247 >= -1)

m.c249 = Constraint(expr= - 0.12*m.b135 - m.x248 >= -1)

m.c250 = Constraint(expr= - 0.12*m.b148 - m.x249 >= -1)

m.c251 = Constraint(expr= - 0.12*m.b149 - m.x250 >= -1)

m.c252 = Constraint(expr= - 0.12*m.b197 - m.x251 >= -1)

m.c253 = Constraint(expr= - 0.12*m.b198 - m.x252 >= -1)

m.c254 = Constraint(expr= - 0.12*m.b172 - m.x253 >= -1)

m.c255 = Constraint(expr= - 0.12*m.b173 - m.x254 >= -1)

m.c256 = Constraint(expr= - 0.1*m.b134 - m.x255 >= -0.91)

m.c257 = Constraint(expr= - 0.1*m.b135 - m.x256 >= -0.91)

m.c258 = Constraint(expr= - 0.1*m.b148 - m.x257 >= -0.91)

m.c259 = Constraint(expr= - 0.1*m.b149 - m.x258 >= -0.91)

m.c260 = Constraint(expr= - 0.1*m.b197 - m.x259 >= -0.91)

m.c261 = Constraint(expr= - 0.1*m.b198 - m.x260 >= -0.91)

m.c262 = Constraint(expr= - 0.1*m.b172 - m.x261 >= -0.91)

m.c263 = Constraint(expr= - 0.1*m.b173 - m.x262 >= -0.91)

m.c264 = Constraint(expr=   m.b114 + m.b123 <= 1)

m.c265 = Constraint(expr=   m.b115 + m.b124 <= 1)

m.c266 = Constraint(expr=   m.b116 + m.b125 <= 1)

m.c267 = Constraint(expr=   m.b114 + m.b126 <= 1)

m.c268 = Constraint(expr=   m.b115 + m.b127 <= 1)

m.c269 = Constraint(expr=   m.b116 + m.b128 <= 1)

m.c270 = Constraint(expr=   m.b114 + m.b129 <= 1)

m.c271 = Constraint(expr=   m.b115 + m.b130 <= 1)

m.c272 = Constraint(expr=   m.b116 + m.b131 <= 1)

m.c273 = Constraint(expr=   m.b115 + m.b132 <= 1)

m.c274 = Constraint(expr=   m.b116 + m.b133 <= 1)

m.c275 = Constraint(expr=   m.b115 + m.b134 <= 1)

m.c276 = Constraint(expr=   m.b116 + m.b135 <= 1)

m.c277 = Constraint(expr=   m.b123 + m.b136 <= 1)

m.c278 = Constraint(expr=   m.b124 + m.b137 <= 1)

m.c279 = Constraint(expr=   m.b125 + m.b138 <= 1)

m.c280 = Constraint(expr=   m.b126 + m.b136 <= 1)

m.c281 = Constraint(expr=   m.b127 + m.b137 <= 1)

m.c282 = Constraint(expr=   m.b128 + m.b138 <= 1)

m.c283 = Constraint(expr=   m.b129 + m.b136 <= 1)

m.c284 = Constraint(expr=   m.b130 + m.b137 <= 1)

m.c285 = Constraint(expr=   m.b131 + m.b138 <= 1)

m.c286 = Constraint(expr=   m.b132 + m.b137 <= 1)

m.c287 = Constraint(expr=   m.b133 + m.b138 <= 1)

m.c288 = Constraint(expr=   m.b134 + m.b137 <= 1)

m.c289 = Constraint(expr=   m.b135 + m.b138 <= 1)

m.c290 = Constraint(expr=   m.b123 + m.b150 <= 1)

m.c291 = Constraint(expr=   m.b124 + m.b151 <= 1)

m.c292 = Constraint(expr=   m.b125 + m.b152 <= 1)

m.c293 = Constraint(expr=   m.b126 + m.b150 <= 1)

m.c294 = Constraint(expr=   m.b127 + m.b151 <= 1)

m.c295 = Constraint(expr=   m.b128 + m.b152 <= 1)

m.c296 = Constraint(expr=   m.b129 + m.b150 <= 1)

m.c297 = Constraint(expr=   m.b130 + m.b151 <= 1)

m.c298 = Constraint(expr=   m.b131 + m.b152 <= 1)

m.c299 = Constraint(expr=   m.b132 + m.b151 <= 1)

m.c300 = Constraint(expr=   m.b133 + m.b152 <= 1)

m.c301 = Constraint(expr=   m.b134 + m.b151 <= 1)

m.c302 = Constraint(expr=   m.b135 + m.b152 <= 1)

m.c303 = Constraint(expr=   m.b123 + m.b161 <= 1)

m.c304 = Constraint(expr=   m.b124 + m.b162 <= 1)

m.c305 = Constraint(expr=   m.b125 + m.b163 <= 1)

m.c306 = Constraint(expr=   m.b126 + m.b161 <= 1)

m.c307 = Constraint(expr=   m.b127 + m.b162 <= 1)

m.c308 = Constraint(expr=   m.b128 + m.b163 <= 1)

m.c309 = Constraint(expr=   m.b129 + m.b161 <= 1)

m.c310 = Constraint(expr=   m.b130 + m.b162 <= 1)

m.c311 = Constraint(expr=   m.b131 + m.b163 <= 1)

m.c312 = Constraint(expr=   m.b132 + m.b162 <= 1)

m.c313 = Constraint(expr=   m.b133 + m.b163 <= 1)

m.c314 = Constraint(expr=   m.b134 + m.b162 <= 1)

m.c315 = Constraint(expr=   m.b135 + m.b163 <= 1)

m.c316 = Constraint(expr=   m.b105 + m.b136 <= 1)

m.c317 = Constraint(expr=   m.b106 + m.b137 <= 1)

m.c318 = Constraint(expr=   m.b107 + m.b138 <= 1)

m.c319 = Constraint(expr=   m.b105 + m.b139 <= 1)

m.c320 = Constraint(expr=   m.b106 + m.b140 <= 1)

m.c321 = Constraint(expr=   m.b107 + m.b141 <= 1)

m.c322 = Constraint(expr=   m.b105 + m.b142 <= 1)

m.c323 = Constraint(expr=   m.b106 + m.b143 <= 1)

m.c324 = Constraint(expr=   m.b107 + m.b144 <= 1)

m.c325 = Constraint(expr=   m.b105 + m.b145 <= 1)

m.c326 = Constraint(expr=   m.b106 + m.b146 <= 1)

m.c327 = Constraint(expr=   m.b107 + m.b147 <= 1)

m.c328 = Constraint(expr=   m.b106 + m.b148 <= 1)

m.c329 = Constraint(expr=   m.b107 + m.b149 <= 1)

m.c330 = Constraint(expr=   m.b117 + m.b136 <= 1)

m.c331 = Constraint(expr=   m.b118 + m.b137 <= 1)

m.c332 = Constraint(expr=   m.b119 + m.b138 <= 1)

m.c333 = Constraint(expr=   m.b117 + m.b139 <= 1)

m.c334 = Constraint(expr=   m.b118 + m.b140 <= 1)

m.c335 = Constraint(expr=   m.b119 + m.b141 <= 1)

m.c336 = Constraint(expr=   m.b117 + m.b142 <= 1)

m.c337 = Constraint(expr=   m.b118 + m.b143 <= 1)

m.c338 = Constraint(expr=   m.b119 + m.b144 <= 1)

m.c339 = Constraint(expr=   m.b117 + m.b145 <= 1)

m.c340 = Constraint(expr=   m.b118 + m.b146 <= 1)

m.c341 = Constraint(expr=   m.b119 + m.b147 <= 1)

m.c342 = Constraint(expr=   m.b118 + m.b148 <= 1)

m.c343 = Constraint(expr=   m.b119 + m.b149 <= 1)

m.c344 = Constraint(expr=   m.b123 + m.b136 <= 1)

m.c345 = Constraint(expr=   m.b124 + m.b137 <= 1)

m.c346 = Constraint(expr=   m.b125 + m.b138 <= 1)

m.c347 = Constraint(expr=   m.b123 + m.b139 <= 1)

m.c348 = Constraint(expr=   m.b124 + m.b140 <= 1)

m.c349 = Constraint(expr=   m.b125 + m.b141 <= 1)

m.c350 = Constraint(expr=   m.b123 + m.b142 <= 1)

m.c351 = Constraint(expr=   m.b124 + m.b143 <= 1)

m.c352 = Constraint(expr=   m.b125 + m.b144 <= 1)

m.c353 = Constraint(expr=   m.b123 + m.b145 <= 1)

m.c354 = Constraint(expr=   m.b124 + m.b146 <= 1)

m.c355 = Constraint(expr=   m.b125 + m.b147 <= 1)

m.c356 = Constraint(expr=   m.b124 + m.b148 <= 1)

m.c357 = Constraint(expr=   m.b125 + m.b149 <= 1)

m.c358 = Constraint(expr=   m.b136 + m.b153 <= 1)

m.c359 = Constraint(expr=   m.b137 + m.b154 <= 1)

m.c360 = Constraint(expr=   m.b138 + m.b155 <= 1)

m.c361 = Constraint(expr=   m.b139 + m.b153 <= 1)

m.c362 = Constraint(expr=   m.b140 + m.b154 <= 1)

m.c363 = Constraint(expr=   m.b141 + m.b155 <= 1)

m.c364 = Constraint(expr=   m.b142 + m.b153 <= 1)

m.c365 = Constraint(expr=   m.b143 + m.b154 <= 1)

m.c366 = Constraint(expr=   m.b144 + m.b155 <= 1)

m.c367 = Constraint(expr=   m.b145 + m.b153 <= 1)

m.c368 = Constraint(expr=   m.b146 + m.b154 <= 1)

m.c369 = Constraint(expr=   m.b147 + m.b155 <= 1)

m.c370 = Constraint(expr=   m.b148 + m.b154 <= 1)

m.c371 = Constraint(expr=   m.b149 + m.b155 <= 1)

m.c372 = Constraint(expr=   m.b136 + m.b164 <= 1)

m.c373 = Constraint(expr=   m.b137 + m.b165 <= 1)

m.c374 = Constraint(expr=   m.b138 + m.b166 <= 1)

m.c375 = Constraint(expr=   m.b139 + m.b164 <= 1)

m.c376 = Constraint(expr=   m.b140 + m.b165 <= 1)

m.c377 = Constraint(expr=   m.b141 + m.b166 <= 1)

m.c378 = Constraint(expr=   m.b142 + m.b164 <= 1)

m.c379 = Constraint(expr=   m.b143 + m.b165 <= 1)

m.c380 = Constraint(expr=   m.b144 + m.b166 <= 1)

m.c381 = Constraint(expr=   m.b145 + m.b164 <= 1)

m.c382 = Constraint(expr=   m.b146 + m.b165 <= 1)

m.c383 = Constraint(expr=   m.b147 + m.b166 <= 1)

m.c384 = Constraint(expr=   m.b148 + m.b165 <= 1)

m.c385 = Constraint(expr=   m.b149 + m.b166 <= 1)

m.c386 = Constraint(expr=   m.b108 + m.b150 <= 1)

m.c387 = Constraint(expr=   m.b109 + m.b151 <= 1)

m.c388 = Constraint(expr=   m.b110 + m.b152 <= 1)

m.c389 = Constraint(expr=   m.b108 + m.b153 <= 1)

m.c390 = Constraint(expr=   m.b109 + m.b154 <= 1)

m.c391 = Constraint(expr=   m.b110 + m.b155 <= 1)

m.c392 = Constraint(expr=   m.b108 + m.b156 <= 1)

m.c393 = Constraint(expr=   m.b109 + m.b157 <= 1)

m.c394 = Constraint(expr=   m.b110 + m.b158 <= 1)

m.c395 = Constraint(expr=   m.b109 + m.b159 <= 1)

m.c396 = Constraint(expr=   m.b110 + m.b160 <= 1)

m.c397 = Constraint(expr=   m.b109 + m.b197 <= 1)

m.c398 = Constraint(expr=   m.b110 + m.b198 <= 1)

m.c399 = Constraint(expr=   m.b120 + m.b150 <= 1)

m.c400 = Constraint(expr=   m.b121 + m.b151 <= 1)

m.c401 = Constraint(expr=   m.b122 + m.b152 <= 1)

m.c402 = Constraint(expr=   m.b120 + m.b153 <= 1)

m.c403 = Constraint(expr=   m.b121 + m.b154 <= 1)

m.c404 = Constraint(expr=   m.b122 + m.b155 <= 1)

m.c405 = Constraint(expr=   m.b120 + m.b156 <= 1)

m.c406 = Constraint(expr=   m.b121 + m.b157 <= 1)

m.c407 = Constraint(expr=   m.b122 + m.b158 <= 1)

m.c408 = Constraint(expr=   m.b121 + m.b159 <= 1)

m.c409 = Constraint(expr=   m.b122 + m.b160 <= 1)

m.c410 = Constraint(expr=   m.b121 + m.b197 <= 1)

m.c411 = Constraint(expr=   m.b122 + m.b198 <= 1)

m.c412 = Constraint(expr=   m.b126 + m.b150 <= 1)

m.c413 = Constraint(expr=   m.b127 + m.b151 <= 1)

m.c414 = Constraint(expr=   m.b128 + m.b152 <= 1)

m.c415 = Constraint(expr=   m.b126 + m.b153 <= 1)

m.c416 = Constraint(expr=   m.b127 + m.b154 <= 1)

m.c417 = Constraint(expr=   m.b128 + m.b155 <= 1)

m.c418 = Constraint(expr=   m.b126 + m.b156 <= 1)

m.c419 = Constraint(expr=   m.b127 + m.b157 <= 1)

m.c420 = Constraint(expr=   m.b128 + m.b158 <= 1)

m.c421 = Constraint(expr=   m.b127 + m.b159 <= 1)

m.c422 = Constraint(expr=   m.b128 + m.b160 <= 1)

m.c423 = Constraint(expr=   m.b127 + m.b197 <= 1)

m.c424 = Constraint(expr=   m.b128 + m.b198 <= 1)

m.c425 = Constraint(expr=   m.b139 + m.b150 <= 1)

m.c426 = Constraint(expr=   m.b140 + m.b151 <= 1)

m.c427 = Constraint(expr=   m.b141 + m.b152 <= 1)

m.c428 = Constraint(expr=   m.b139 + m.b153 <= 1)

m.c429 = Constraint(expr=   m.b140 + m.b154 <= 1)

m.c430 = Constraint(expr=   m.b141 + m.b155 <= 1)

m.c431 = Constraint(expr=   m.b139 + m.b156 <= 1)

m.c432 = Constraint(expr=   m.b140 + m.b157 <= 1)

m.c433 = Constraint(expr=   m.b141 + m.b158 <= 1)

m.c434 = Constraint(expr=   m.b140 + m.b159 <= 1)

m.c435 = Constraint(expr=   m.b141 + m.b160 <= 1)

m.c436 = Constraint(expr=   m.b140 + m.b197 <= 1)

m.c437 = Constraint(expr=   m.b141 + m.b198 <= 1)

m.c438 = Constraint(expr=   m.b150 + m.b167 <= 1)

m.c439 = Constraint(expr=   m.b151 + m.b168 <= 1)

m.c440 = Constraint(expr=   m.b152 + m.b169 <= 1)

m.c441 = Constraint(expr=   m.b153 + m.b167 <= 1)

m.c442 = Constraint(expr=   m.b154 + m.b168 <= 1)

m.c443 = Constraint(expr=   m.b155 + m.b169 <= 1)

m.c444 = Constraint(expr=   m.b156 + m.b167 <= 1)

m.c445 = Constraint(expr=   m.b157 + m.b168 <= 1)

m.c446 = Constraint(expr=   m.b158 + m.b169 <= 1)

m.c447 = Constraint(expr=   m.b159 + m.b168 <= 1)

m.c448 = Constraint(expr=   m.b160 + m.b169 <= 1)

m.c449 = Constraint(expr=   m.b168 + m.b197 <= 1)

m.c450 = Constraint(expr=   m.b169 + m.b198 <= 1)

m.c451 = Constraint(expr=   m.b111 + m.b161 <= 1)

m.c452 = Constraint(expr=   m.b112 + m.b162 <= 1)

m.c453 = Constraint(expr=   m.b113 + m.b163 <= 1)

m.c454 = Constraint(expr=   m.b111 + m.b164 <= 1)

m.c455 = Constraint(expr=   m.b112 + m.b165 <= 1)

m.c456 = Constraint(expr=   m.b113 + m.b166 <= 1)

m.c457 = Constraint(expr=   m.b111 + m.b167 <= 1)

m.c458 = Constraint(expr=   m.b112 + m.b168 <= 1)

m.c459 = Constraint(expr=   m.b113 + m.b169 <= 1)

m.c460 = Constraint(expr=   m.b112 + m.b170 <= 1)

m.c461 = Constraint(expr=   m.b113 + m.b171 <= 1)

m.c462 = Constraint(expr=   m.b112 + m.b172 <= 1)

m.c463 = Constraint(expr=   m.b113 + m.b173 <= 1)

m.c464 = Constraint(expr=   m.b129 + m.b161 <= 1)

m.c465 = Constraint(expr=   m.b130 + m.b162 <= 1)

m.c466 = Constraint(expr=   m.b131 + m.b163 <= 1)

m.c467 = Constraint(expr=   m.b129 + m.b164 <= 1)

m.c468 = Constraint(expr=   m.b130 + m.b165 <= 1)

m.c469 = Constraint(expr=   m.b131 + m.b166 <= 1)

m.c470 = Constraint(expr=   m.b129 + m.b167 <= 1)

m.c471 = Constraint(expr=   m.b130 + m.b168 <= 1)

m.c472 = Constraint(expr=   m.b131 + m.b169 <= 1)

m.c473 = Constraint(expr=   m.b130 + m.b170 <= 1)

m.c474 = Constraint(expr=   m.b131 + m.b171 <= 1)

m.c475 = Constraint(expr=   m.b130 + m.b172 <= 1)

m.c476 = Constraint(expr=   m.b131 + m.b173 <= 1)

m.c477 = Constraint(expr=   m.b142 + m.b161 <= 1)

m.c478 = Constraint(expr=   m.b143 + m.b162 <= 1)

m.c479 = Constraint(expr=   m.b144 + m.b163 <= 1)

m.c480 = Constraint(expr=   m.b142 + m.b164 <= 1)

m.c481 = Constraint(expr=   m.b143 + m.b165 <= 1)

m.c482 = Constraint(expr=   m.b144 + m.b166 <= 1)

m.c483 = Constraint(expr=   m.b142 + m.b167 <= 1)

m.c484 = Constraint(expr=   m.b143 + m.b168 <= 1)

m.c485 = Constraint(expr=   m.b144 + m.b169 <= 1)

m.c486 = Constraint(expr=   m.b143 + m.b170 <= 1)

m.c487 = Constraint(expr=   m.b144 + m.b171 <= 1)

m.c488 = Constraint(expr=   m.b143 + m.b172 <= 1)

m.c489 = Constraint(expr=   m.b144 + m.b173 <= 1)

m.c490 = Constraint(expr=   m.b156 + m.b161 <= 1)

m.c491 = Constraint(expr=   m.b157 + m.b162 <= 1)

m.c492 = Constraint(expr=   m.b158 + m.b163 <= 1)

m.c493 = Constraint(expr=   m.b156 + m.b164 <= 1)

m.c494 = Constraint(expr=   m.b157 + m.b165 <= 1)

m.c495 = Constraint(expr=   m.b158 + m.b166 <= 1)

m.c496 = Constraint(expr=   m.b156 + m.b167 <= 1)

m.c497 = Constraint(expr=   m.b157 + m.b168 <= 1)

m.c498 = Constraint(expr=   m.b158 + m.b169 <= 1)

m.c499 = Constraint(expr=   m.b157 + m.b170 <= 1)

m.c500 = Constraint(expr=   m.b158 + m.b171 <= 1)

m.c501 = Constraint(expr=   m.b157 + m.b172 <= 1)

m.c502 = Constraint(expr=   m.b158 + m.b173 <= 1)

m.c503 = Constraint(expr=m.x199*m.x176 - 0.9*m.x11 + 0.7*m.x20 + 0.7*m.x23 + 0.7*m.x26 - 0.8*m.x33 - 0.7*m.x47
                          - 0.7*m.x60 == 0.21)

m.c504 = Constraint(expr=m.x201*m.x177 - 0.7*m.x2 - 0.9*m.x14 - 0.7*m.x20 + 0.8*m.x33 + 0.8*m.x36 + 0.8*m.x39
                          + 0.8*m.x42 - 0.7*m.x50 - 0.7*m.x63 == 1.44)

m.c505 = Constraint(expr=m.x203*m.x178 - 0.7*m.x5 - 0.9*m.x17 - 0.7*m.x23 - 0.8*m.x36 + 0.7*m.x47 + 0.7*m.x50
                          + 0.7*m.x53 - 0.7*m.x66 == 0.91)

m.c506 = Constraint(expr=m.x205*m.x179 - 0.7*m.x8 - 0.7*m.x26 - 0.8*m.x39 - 0.7*m.x53 + 0.7*m.x60 + 0.7*m.x63
                          + 0.7*m.x66 == 0.14)

m.c507 = Constraint(expr=m.x207*m.x176 - 0.01*m.x11 - 0.9*m.x33 - 0.8*m.x47 - 0.3*m.x60 == 0)

m.c508 = Constraint(expr=m.x209*m.x177 - 0.2*m.x2 - 0.01*m.x14 + 0.9*m.x33 + 0.9*m.x36 + 0.9*m.x39 + 0.9*m.x42
                          - 0.8*m.x50 - 0.3*m.x63 == 1.62)

m.c509 = Constraint(expr=m.x211*m.x178 - 0.2*m.x5 - 0.01*m.x17 - 0.9*m.x36 + 0.8*m.x47 + 0.8*m.x50 + 0.8*m.x53
                          - 0.3*m.x66 == 1.04)

m.c510 = Constraint(expr=m.x213*m.x179 - 0.2*m.x8 - 0.9*m.x39 - 0.8*m.x53 + 0.3*m.x60 + 0.3*m.x63 + 0.3*m.x66 == 0.06)

m.c511 = Constraint(expr=m.x215*m.x176 - 0.88*m.x11 + 0.68*m.x20 + 0.68*m.x23 + 0.68*m.x26 - 0.81*m.x33 - 0.71*m.x47
                          - 0.66*m.x60 == 0.204)

m.c512 = Constraint(expr=m.x217*m.x177 - 0.69*m.x2 - 0.88*m.x14 - 0.68*m.x20 + 0.81*m.x33 + 0.81*m.x36 + 0.81*m.x39
                          + 0.81*m.x42 - 0.71*m.x50 - 0.66*m.x63 == 1.458)

m.c513 = Constraint(expr=m.x219*m.x178 - 0.69*m.x5 - 0.88*m.x17 - 0.68*m.x23 - 0.81*m.x36 + 0.71*m.x47 + 0.71*m.x50
                          + 0.71*m.x53 - 0.66*m.x66 == 0.923)

m.c514 = Constraint(expr=m.x221*m.x179 - 0.69*m.x8 - 0.68*m.x26 - 0.81*m.x39 - 0.71*m.x53 + 0.66*m.x60 + 0.66*m.x63
                          + 0.66*m.x66 == 0.132)

m.c515 = Constraint(expr=m.x223*m.x176 + 0.01*m.x20 + 0.01*m.x23 + 0.01*m.x26 - 0.9*m.x33 - 0.8*m.x47 - 0.4*m.x60
                          == 0.003)

m.c516 = Constraint(expr=m.x225*m.x177 - 0.18*m.x2 - 0.01*m.x20 + 0.9*m.x33 + 0.9*m.x36 + 0.9*m.x39 + 0.9*m.x42
                          - 0.8*m.x50 - 0.4*m.x63 == 1.62)

m.c517 = Constraint(expr=m.x227*m.x178 - 0.18*m.x5 - 0.01*m.x23 - 0.9*m.x36 + 0.8*m.x47 + 0.8*m.x50 + 0.8*m.x53
                          - 0.4*m.x66 == 1.04)

m.c518 = Constraint(expr=m.x229*m.x179 - 0.18*m.x8 - 0.01*m.x26 - 0.9*m.x39 - 0.8*m.x53 + 0.4*m.x60 + 0.4*m.x63
                          + 0.4*m.x66 == 0.08)

m.c519 = Constraint(expr=m.x231*m.x176 - 0.92*m.x11 + 0.72*m.x20 + 0.72*m.x23 + 0.72*m.x26 - 0.79*m.x33 - 0.73*m.x47
                          - 0.8*m.x60 == 0.216)

m.c520 = Constraint(expr=m.x233*m.x177 - 0.72*m.x2 - 0.92*m.x14 - 0.72*m.x20 + 0.79*m.x33 + 0.79*m.x36 + 0.79*m.x39
                          + 0.79*m.x42 - 0.73*m.x50 - 0.8*m.x63 == 1.422)

m.c521 = Constraint(expr=m.x235*m.x178 - 0.72*m.x5 - 0.92*m.x17 - 0.72*m.x23 - 0.79*m.x36 + 0.73*m.x47 + 0.73*m.x50
                          + 0.73*m.x53 - 0.8*m.x66 == 0.949)

m.c522 = Constraint(expr=m.x237*m.x179 - 0.72*m.x8 - 0.72*m.x26 - 0.79*m.x39 - 0.73*m.x53 + 0.8*m.x60 + 0.8*m.x63
                          + 0.8*m.x66 == 0.16)

m.c523 = Constraint(expr=m.x239*m.x176 - 0.05*m.x11 - 0.92*m.x33 - 0.21*m.x47 - 0.29*m.x60 == 0)

m.c524 = Constraint(expr=m.x241*m.x177 - 0.22*m.x2 - 0.05*m.x14 + 0.92*m.x33 + 0.92*m.x36 + 0.92*m.x39 + 0.92*m.x42
                          - 0.21*m.x50 - 0.29*m.x63 == 1.656)

m.c525 = Constraint(expr=m.x243*m.x178 - 0.22*m.x5 - 0.05*m.x17 - 0.92*m.x36 + 0.21*m.x47 + 0.21*m.x50 + 0.21*m.x53
                          - 0.29*m.x66 == 0.273)

m.c526 = Constraint(expr=m.x245*m.x179 - 0.22*m.x8 - 0.92*m.x39 - 0.21*m.x53 + 0.29*m.x60 + 0.29*m.x63 + 0.29*m.x66
                          == 0.058)

m.c527 = Constraint(expr=m.x247*m.x176 - 0.87*m.x11 + 0.66*m.x20 + 0.66*m.x23 + 0.66*m.x26 - 0.78*m.x33 - 0.75*m.x47
                          - 0.7*m.x60 == 0.198)

m.c528 = Constraint(expr=m.x249*m.x177 - 0.68*m.x2 - 0.87*m.x14 - 0.66*m.x20 + 0.78*m.x33 + 0.78*m.x36 + 0.78*m.x39
                          + 0.78*m.x42 - 0.75*m.x50 - 0.7*m.x63 == 1.404)

m.c529 = Constraint(expr=m.x251*m.x178 - 0.68*m.x5 - 0.87*m.x17 - 0.66*m.x23 - 0.78*m.x36 + 0.75*m.x47 + 0.75*m.x50
                          + 0.75*m.x53 - 0.7*m.x66 == 0.975)

m.c530 = Constraint(expr=m.x253*m.x179 - 0.68*m.x8 - 0.66*m.x26 - 0.78*m.x39 - 0.75*m.x53 + 0.7*m.x60 + 0.7*m.x63
                          + 0.7*m.x66 == 0.14)

m.c531 = Constraint(expr=m.x255*m.x176 - 0.91*m.x33 - 0.89*m.x47 - 0.43*m.x60 == 0)

m.c532 = Constraint(expr=m.x257*m.x177 - 0.21*m.x2 + 0.91*m.x33 + 0.91*m.x36 + 0.91*m.x39 + 0.91*m.x42 - 0.89*m.x50
                          - 0.43*m.x63 == 1.638)

m.c533 = Constraint(expr=m.x259*m.x178 - 0.21*m.x5 - 0.91*m.x36 + 0.89*m.x47 + 0.89*m.x50 + 0.89*m.x53 - 0.43*m.x66
                          == 1.157)

m.c534 = Constraint(expr=m.x261*m.x179 - 0.21*m.x8 - 0.91*m.x39 - 0.89*m.x53 + 0.43*m.x60 + 0.43*m.x63 + 0.43*m.x66
                          == 0.086)

m.c535 = Constraint(expr=m.x199*m.x21 + m.x199*m.x24 + m.x199*m.x27 + m.x199*m.x29 + m.x199*m.x31 - m.x201*m.x34 - 
                         m.x203*m.x48 - m.x205*m.x61 - m.x199*m.x176 + m.x200*m.x185 - 0.9*m.x12 == 0)

m.c536 = Constraint(expr=m.x200*m.x22 + m.x200*m.x25 + m.x200*m.x28 + m.x200*m.x30 + m.x200*m.x32 - m.x202*m.x35 - 
                         m.x204*m.x49 - m.x206*m.x62 + m.x186*m.x73 - m.x200*m.x185 - 0.9*m.x13 == 0)

m.c537 = Constraint(expr=m.x201*m.x34 - m.x199*m.x21 + m.x201*m.x37 + m.x201*m.x40 + m.x201*m.x43 + m.x201*m.x45 - 
                         m.x203*m.x51 - m.x205*m.x64 - m.x201*m.x177 + m.x202*m.x187 - 0.7*m.x3 - 0.9*m.x15 == 0)

m.c538 = Constraint(expr=m.x202*m.x35 - m.x200*m.x22 + m.x202*m.x38 + m.x202*m.x41 + m.x202*m.x44 + m.x202*m.x46 - 
                         m.x204*m.x52 - m.x206*m.x65 + m.x188*m.x74 - m.x202*m.x187 - 0.7*m.x4 - 0.9*m.x16 == 0)

m.c539 = Constraint(expr=(-m.x199*m.x24) - m.x201*m.x37 + m.x203*m.x48 + m.x203*m.x51 + m.x203*m.x54 + m.x203*m.x56 + 
                         m.x203*m.x58 - m.x205*m.x67 - m.x203*m.x178 + m.x204*m.x189 - 0.7*m.x6 - 0.9*m.x18 == 0)

m.c540 = Constraint(expr=(-m.x200*m.x25) - m.x202*m.x38 + m.x204*m.x49 + m.x204*m.x52 + m.x204*m.x55 + m.x204*m.x57 + 
                         m.x204*m.x59 - m.x206*m.x68 + m.x190*m.x75 - m.x204*m.x189 - 0.7*m.x7 - 0.9*m.x19 == 0)

m.c541 = Constraint(expr=(-m.x199*m.x27) - m.x201*m.x40 - m.x203*m.x54 + m.x205*m.x61 + m.x205*m.x64 + m.x205*m.x67 + 
                         m.x205*m.x69 + m.x205*m.x71 - m.x205*m.x179 + m.x206*m.x191 - 0.7*m.x9 == 0)

m.c542 = Constraint(expr=(-m.x200*m.x28) - m.x202*m.x41 - m.x204*m.x55 + m.x206*m.x62 + m.x206*m.x65 + m.x206*m.x68 + 
                         m.x206*m.x70 + m.x206*m.x72 + m.x192*m.x76 - m.x206*m.x191 - 0.7*m.x10 == 0)

m.c543 = Constraint(expr=m.x207*m.x21 + m.x207*m.x24 + m.x207*m.x27 + m.x207*m.x29 + m.x207*m.x31 - m.x209*m.x34 - 
                         m.x211*m.x48 - m.x213*m.x61 - m.x207*m.x176 + m.x208*m.x185 - 0.01*m.x12 == 0)

m.c544 = Constraint(expr=m.x208*m.x22 + m.x208*m.x25 + m.x208*m.x28 + m.x208*m.x30 + m.x208*m.x32 - m.x210*m.x35 - 
                         m.x212*m.x49 - m.x214*m.x62 + m.x186*m.x77 - m.x208*m.x185 - 0.01*m.x13 == 0)

m.c545 = Constraint(expr=m.x209*m.x34 - m.x207*m.x21 + m.x209*m.x37 + m.x209*m.x40 + m.x209*m.x43 + m.x209*m.x45 - 
                         m.x211*m.x51 - m.x213*m.x64 - m.x209*m.x177 + m.x210*m.x187 - 0.2*m.x3 - 0.01*m.x15 == 0)

m.c546 = Constraint(expr=m.x210*m.x35 - m.x208*m.x22 + m.x210*m.x38 + m.x210*m.x41 + m.x210*m.x44 + m.x210*m.x46 - 
                         m.x212*m.x52 - m.x214*m.x65 + m.x188*m.x78 - m.x210*m.x187 - 0.2*m.x4 - 0.01*m.x16 == 0)

m.c547 = Constraint(expr=(-m.x207*m.x24) - m.x209*m.x37 + m.x211*m.x48 + m.x211*m.x51 + m.x211*m.x54 + m.x211*m.x56 + 
                         m.x211*m.x58 - m.x213*m.x67 - m.x211*m.x178 + m.x212*m.x189 - 0.2*m.x6 - 0.01*m.x18 == 0)

m.c548 = Constraint(expr=(-m.x208*m.x25) - m.x210*m.x38 + m.x212*m.x49 + m.x212*m.x52 + m.x212*m.x55 + m.x212*m.x57 + 
                         m.x212*m.x59 - m.x214*m.x68 + m.x190*m.x79 - m.x212*m.x189 - 0.2*m.x7 - 0.01*m.x19 == 0)

m.c549 = Constraint(expr=(-m.x207*m.x27) - m.x209*m.x40 - m.x211*m.x54 + m.x213*m.x61 + m.x213*m.x64 + m.x213*m.x67 + 
                         m.x213*m.x69 + m.x213*m.x71 - m.x213*m.x179 + m.x214*m.x191 - 0.2*m.x9 == 0)

m.c550 = Constraint(expr=(-m.x208*m.x28) - m.x210*m.x41 - m.x212*m.x55 + m.x214*m.x62 + m.x214*m.x65 + m.x214*m.x68 + 
                         m.x214*m.x70 + m.x214*m.x72 + m.x192*m.x80 - m.x214*m.x191 - 0.2*m.x10 == 0)

m.c551 = Constraint(expr=m.x215*m.x21 + m.x215*m.x24 + m.x215*m.x27 + m.x215*m.x29 + m.x215*m.x31 - m.x217*m.x34 - 
                         m.x219*m.x48 - m.x221*m.x61 - m.x215*m.x176 + m.x216*m.x185 - 0.88*m.x12 == 0)

m.c552 = Constraint(expr=m.x216*m.x22 + m.x216*m.x25 + m.x216*m.x28 + m.x216*m.x30 + m.x216*m.x32 - m.x218*m.x35 - 
                         m.x220*m.x49 - m.x222*m.x62 + m.x186*m.x81 - m.x216*m.x185 - 0.88*m.x13 == 0)

m.c553 = Constraint(expr=m.x217*m.x34 - m.x215*m.x21 + m.x217*m.x37 + m.x217*m.x40 + m.x217*m.x43 + m.x217*m.x45 - 
                         m.x219*m.x51 - m.x221*m.x64 - m.x217*m.x177 + m.x218*m.x187 - 0.69*m.x3 - 0.88*m.x15 == 0)

m.c554 = Constraint(expr=m.x218*m.x35 - m.x216*m.x22 + m.x218*m.x38 + m.x218*m.x41 + m.x218*m.x44 + m.x218*m.x46 - 
                         m.x220*m.x52 - m.x222*m.x65 + m.x188*m.x82 - m.x218*m.x187 - 0.69*m.x4 - 0.88*m.x16 == 0)

m.c555 = Constraint(expr=(-m.x215*m.x24) - m.x217*m.x37 + m.x219*m.x48 + m.x219*m.x51 + m.x219*m.x54 + m.x219*m.x56 + 
                         m.x219*m.x58 - m.x221*m.x67 - m.x219*m.x178 + m.x220*m.x189 - 0.69*m.x6 - 0.88*m.x18 == 0)

m.c556 = Constraint(expr=(-m.x216*m.x25) - m.x218*m.x38 + m.x220*m.x49 + m.x220*m.x52 + m.x220*m.x55 + m.x220*m.x57 + 
                         m.x220*m.x59 - m.x222*m.x68 + m.x190*m.x83 - m.x220*m.x189 - 0.69*m.x7 - 0.88*m.x19 == 0)

m.c557 = Constraint(expr=(-m.x215*m.x27) - m.x217*m.x40 - m.x219*m.x54 + m.x221*m.x61 + m.x221*m.x64 + m.x221*m.x67 + 
                         m.x221*m.x69 + m.x221*m.x71 - m.x221*m.x179 + m.x222*m.x191 - 0.69*m.x9 == 0)

m.c558 = Constraint(expr=(-m.x216*m.x28) - m.x218*m.x41 - m.x220*m.x55 + m.x222*m.x62 + m.x222*m.x65 + m.x222*m.x68 + 
                         m.x222*m.x70 + m.x222*m.x72 + m.x192*m.x84 - m.x222*m.x191 - 0.69*m.x10 == 0)

m.c559 = Constraint(expr=m.x225*m.x34 - m.x223*m.x21 + m.x225*m.x37 + m.x225*m.x40 + m.x225*m.x43 + m.x225*m.x45 - 
                         m.x227*m.x51 - m.x229*m.x64 - m.x225*m.x177 + m.x226*m.x187 - 0.18*m.x3 == 0)

m.c560 = Constraint(expr=m.x226*m.x35 - m.x224*m.x22 + m.x226*m.x38 + m.x226*m.x41 + m.x226*m.x44 + m.x226*m.x46 - 
                         m.x228*m.x52 - m.x230*m.x65 + m.x188*m.x86 - m.x226*m.x187 - 0.18*m.x4 == 0)

m.c561 = Constraint(expr=(-m.x223*m.x24) - m.x225*m.x37 + m.x227*m.x48 + m.x227*m.x51 + m.x227*m.x54 + m.x227*m.x56 + 
                         m.x227*m.x58 - m.x229*m.x67 - m.x227*m.x178 + m.x228*m.x189 - 0.18*m.x6 == 0)

m.c562 = Constraint(expr=(-m.x224*m.x25) - m.x226*m.x38 + m.x228*m.x49 + m.x228*m.x52 + m.x228*m.x55 + m.x228*m.x57 + 
                         m.x228*m.x59 - m.x230*m.x68 + m.x190*m.x87 - m.x228*m.x189 - 0.18*m.x7 == 0)

m.c563 = Constraint(expr=(-m.x223*m.x27) - m.x225*m.x40 - m.x227*m.x54 + m.x229*m.x61 + m.x229*m.x64 + m.x229*m.x67 + 
                         m.x229*m.x69 + m.x229*m.x71 - m.x229*m.x179 + m.x230*m.x191 - 0.18*m.x9 == 0)

m.c564 = Constraint(expr=(-m.x224*m.x28) - m.x226*m.x41 - m.x228*m.x55 + m.x230*m.x62 + m.x230*m.x65 + m.x230*m.x68 + 
                         m.x230*m.x70 + m.x230*m.x72 + m.x192*m.x88 - m.x230*m.x191 - 0.18*m.x10 == 0)

m.c565 = Constraint(expr=m.x231*m.x21 + m.x231*m.x24 + m.x231*m.x27 + m.x231*m.x29 + m.x231*m.x31 - m.x233*m.x34 - 
                         m.x235*m.x48 - m.x237*m.x61 - m.x231*m.x176 + m.x232*m.x185 - 0.92*m.x12 == 0)

m.c566 = Constraint(expr=m.x232*m.x22 + m.x232*m.x25 + m.x232*m.x28 + m.x232*m.x30 + m.x232*m.x32 - m.x234*m.x35 - 
                         m.x236*m.x49 - m.x238*m.x62 + m.x186*m.x89 - m.x232*m.x185 - 0.92*m.x13 == 0)

m.c567 = Constraint(expr=m.x233*m.x34 - m.x231*m.x21 + m.x233*m.x37 + m.x233*m.x40 + m.x233*m.x43 + m.x233*m.x45 - 
                         m.x235*m.x51 - m.x237*m.x64 - m.x233*m.x177 + m.x234*m.x187 - 0.72*m.x3 - 0.92*m.x15 == 0)

m.c568 = Constraint(expr=m.x234*m.x35 - m.x232*m.x22 + m.x234*m.x38 + m.x234*m.x41 + m.x234*m.x44 + m.x234*m.x46 - 
                         m.x236*m.x52 - m.x238*m.x65 + m.x188*m.x90 - m.x234*m.x187 - 0.72*m.x4 - 0.92*m.x16 == 0)

m.c569 = Constraint(expr=(-m.x231*m.x24) - m.x233*m.x37 + m.x235*m.x48 + m.x235*m.x51 + m.x235*m.x54 + m.x235*m.x56 + 
                         m.x235*m.x58 - m.x237*m.x67 - m.x235*m.x178 + m.x236*m.x189 - 0.72*m.x6 - 0.92*m.x18 == 0)

m.c570 = Constraint(expr=(-m.x232*m.x25) - m.x234*m.x38 + m.x236*m.x49 + m.x236*m.x52 + m.x236*m.x55 + m.x236*m.x57 + 
                         m.x236*m.x59 - m.x238*m.x68 + m.x190*m.x91 - m.x236*m.x189 - 0.72*m.x7 - 0.92*m.x19 == 0)

m.c571 = Constraint(expr=(-m.x231*m.x27) - m.x233*m.x40 - m.x235*m.x54 + m.x237*m.x61 + m.x237*m.x64 + m.x237*m.x67 + 
                         m.x237*m.x69 + m.x237*m.x71 - m.x237*m.x179 + m.x238*m.x191 - 0.72*m.x9 == 0)

m.c572 = Constraint(expr=(-m.x232*m.x28) - m.x234*m.x41 - m.x236*m.x55 + m.x238*m.x62 + m.x238*m.x65 + m.x238*m.x68 + 
                         m.x238*m.x70 + m.x238*m.x72 + m.x192*m.x92 - m.x238*m.x191 - 0.72*m.x10 == 0)

m.c573 = Constraint(expr=m.x239*m.x21 + m.x239*m.x24 + m.x239*m.x27 + m.x239*m.x29 + m.x239*m.x31 - m.x241*m.x34 - 
                         m.x243*m.x48 - m.x245*m.x61 - m.x239*m.x176 + m.x240*m.x185 - 0.05*m.x12 == 0)

m.c574 = Constraint(expr=m.x240*m.x22 + m.x240*m.x25 + m.x240*m.x28 + m.x240*m.x30 + m.x240*m.x32 - m.x242*m.x35 - 
                         m.x244*m.x49 - m.x246*m.x62 + m.x186*m.x93 - m.x240*m.x185 - 0.05*m.x13 == 0)

m.c575 = Constraint(expr=m.x241*m.x34 - m.x239*m.x21 + m.x241*m.x37 + m.x241*m.x40 + m.x241*m.x43 + m.x241*m.x45 - 
                         m.x243*m.x51 - m.x245*m.x64 - m.x241*m.x177 + m.x242*m.x187 - 0.22*m.x3 - 0.05*m.x15 == 0)

m.c576 = Constraint(expr=m.x242*m.x35 - m.x240*m.x22 + m.x242*m.x38 + m.x242*m.x41 + m.x242*m.x44 + m.x242*m.x46 - 
                         m.x244*m.x52 - m.x246*m.x65 + m.x188*m.x94 - m.x242*m.x187 - 0.22*m.x4 - 0.05*m.x16 == 0)

m.c577 = Constraint(expr=(-m.x239*m.x24) - m.x241*m.x37 + m.x243*m.x48 + m.x243*m.x51 + m.x243*m.x54 + m.x243*m.x56 + 
                         m.x243*m.x58 - m.x245*m.x67 - m.x243*m.x178 + m.x244*m.x189 - 0.22*m.x6 - 0.05*m.x18 == 0)

m.c578 = Constraint(expr=(-m.x240*m.x25) - m.x242*m.x38 + m.x244*m.x49 + m.x244*m.x52 + m.x244*m.x55 + m.x244*m.x57 + 
                         m.x244*m.x59 - m.x246*m.x68 + m.x190*m.x95 - m.x244*m.x189 - 0.22*m.x7 - 0.05*m.x19 == 0)

m.c579 = Constraint(expr=(-m.x239*m.x27) - m.x241*m.x40 - m.x243*m.x54 + m.x245*m.x61 + m.x245*m.x64 + m.x245*m.x67 + 
                         m.x245*m.x69 + m.x245*m.x71 - m.x245*m.x179 + m.x246*m.x191 - 0.22*m.x9 == 0)

m.c580 = Constraint(expr=(-m.x240*m.x28) - m.x242*m.x41 - m.x244*m.x55 + m.x246*m.x62 + m.x246*m.x65 + m.x246*m.x68 + 
                         m.x246*m.x70 + m.x246*m.x72 + m.x192*m.x96 - m.x246*m.x191 - 0.22*m.x10 == 0)

m.c581 = Constraint(expr=m.x247*m.x21 + m.x247*m.x24 + m.x247*m.x27 + m.x247*m.x29 + m.x247*m.x31 - m.x249*m.x34 - 
                         m.x251*m.x48 - m.x253*m.x61 - m.x247*m.x176 + m.x248*m.x185 - 0.87*m.x12 == 0)

m.c582 = Constraint(expr=m.x248*m.x22 + m.x248*m.x25 + m.x248*m.x28 + m.x248*m.x30 + m.x248*m.x32 - m.x250*m.x35 - 
                         m.x252*m.x49 - m.x254*m.x62 + m.x186*m.x97 - m.x248*m.x185 - 0.87*m.x13 == 0)

m.c583 = Constraint(expr=m.x249*m.x34 - m.x247*m.x21 + m.x249*m.x37 + m.x249*m.x40 + m.x249*m.x43 + m.x249*m.x45 - 
                         m.x251*m.x51 - m.x253*m.x64 - m.x249*m.x177 + m.x250*m.x187 - 0.68*m.x3 - 0.87*m.x15 == 0)

m.c584 = Constraint(expr=m.x250*m.x35 - m.x248*m.x22 + m.x250*m.x38 + m.x250*m.x41 + m.x250*m.x44 + m.x250*m.x46 - 
                         m.x252*m.x52 - m.x254*m.x65 + m.x188*m.x98 - m.x250*m.x187 - 0.68*m.x4 - 0.87*m.x16 == 0)

m.c585 = Constraint(expr=(-m.x247*m.x24) - m.x249*m.x37 + m.x251*m.x48 + m.x251*m.x51 + m.x251*m.x54 + m.x251*m.x56 + 
                         m.x251*m.x58 - m.x253*m.x67 - m.x251*m.x178 + m.x252*m.x189 - 0.68*m.x6 - 0.87*m.x18 == 0)

m.c586 = Constraint(expr=(-m.x248*m.x25) - m.x250*m.x38 + m.x252*m.x49 + m.x252*m.x52 + m.x252*m.x55 + m.x252*m.x57 + 
                         m.x252*m.x59 - m.x254*m.x68 + m.x190*m.x99 - m.x252*m.x189 - 0.68*m.x7 - 0.87*m.x19 == 0)

m.c587 = Constraint(expr=(-m.x247*m.x27) - m.x249*m.x40 - m.x251*m.x54 + m.x253*m.x61 + m.x253*m.x64 + m.x253*m.x67 + 
                         m.x253*m.x69 + m.x253*m.x71 - m.x253*m.x179 + m.x254*m.x191 - 0.68*m.x9 == 0)

m.c588 = Constraint(expr=(-m.x248*m.x28) - m.x250*m.x41 - m.x252*m.x55 + m.x254*m.x62 + m.x254*m.x65 + m.x254*m.x68 + 
                         m.x254*m.x70 + m.x254*m.x72 + m.x192*m.x100 - m.x254*m.x191 - 0.68*m.x10 == 0)

m.c589 = Constraint(expr=m.x257*m.x34 - m.x255*m.x21 + m.x257*m.x37 + m.x257*m.x40 + m.x257*m.x43 + m.x257*m.x45 - 
                         m.x259*m.x51 - m.x261*m.x64 - m.x257*m.x177 + m.x258*m.x187 - 0.21*m.x3 == 0)

m.c590 = Constraint(expr=m.x258*m.x35 - m.x256*m.x22 + m.x258*m.x38 + m.x258*m.x41 + m.x258*m.x44 + m.x258*m.x46 - 
                         m.x260*m.x52 - m.x262*m.x65 + m.x188*m.x102 - m.x258*m.x187 - 0.21*m.x4 == 0)

m.c591 = Constraint(expr=(-m.x255*m.x24) - m.x257*m.x37 + m.x259*m.x48 + m.x259*m.x51 + m.x259*m.x54 + m.x259*m.x56 + 
                         m.x259*m.x58 - m.x261*m.x67 - m.x259*m.x178 + m.x260*m.x189 - 0.21*m.x6 == 0)

m.c592 = Constraint(expr=(-m.x256*m.x25) - m.x258*m.x38 + m.x260*m.x49 + m.x260*m.x52 + m.x260*m.x55 + m.x260*m.x57 + 
                         m.x260*m.x59 - m.x262*m.x68 + m.x190*m.x103 - m.x260*m.x189 - 0.21*m.x7 == 0)

m.c593 = Constraint(expr=(-m.x255*m.x27) - m.x257*m.x40 - m.x259*m.x54 + m.x261*m.x61 + m.x261*m.x64 + m.x261*m.x67 + 
                         m.x261*m.x69 + m.x261*m.x71 - m.x261*m.x179 + m.x262*m.x191 - 0.21*m.x9 == 0)

m.c594 = Constraint(expr=(-m.x256*m.x28) - m.x258*m.x41 - m.x260*m.x55 + m.x262*m.x62 + m.x262*m.x65 + m.x262*m.x68 + 
                         m.x262*m.x70 + m.x262*m.x72 + m.x192*m.x104 - m.x262*m.x191 - 0.21*m.x10 == 0)

m.c595 = Constraint(expr=m.x223*m.x21 + m.x223*m.x24 + m.x223*m.x27 + m.x223*m.x29 + m.x223*m.x31 - m.x225*m.x34 - 
                         m.x227*m.x48 - m.x229*m.x61 - m.x223*m.x176 + m.x224*m.x185 == 0)

m.c596 = Constraint(expr=m.x224*m.x22 + m.x224*m.x25 + m.x224*m.x28 + m.x224*m.x30 + m.x224*m.x32 - m.x226*m.x35 - 
                         m.x228*m.x49 - m.x230*m.x62 + m.x186*m.x85 - m.x224*m.x185 == 0)

m.c597 = Constraint(expr=m.x255*m.x21 + m.x255*m.x24 + m.x255*m.x27 + m.x255*m.x29 + m.x255*m.x31 - m.x257*m.x34 - 
                         m.x259*m.x48 - m.x261*m.x61 - m.x255*m.x176 + m.x256*m.x185 == 0)

m.c598 = Constraint(expr=m.x256*m.x22 + m.x256*m.x25 + m.x256*m.x28 + m.x256*m.x30 + m.x256*m.x32 - m.x258*m.x35 - 
                         m.x260*m.x49 - m.x262*m.x62 + m.x186*m.x101 - m.x256*m.x185 == 0)
