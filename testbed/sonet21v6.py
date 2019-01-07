#  MINLP written by GAMS Convert at 01/04/19 10:34:20
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#       4012        1       21     3990        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        211        1      210        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#      12600    12180      420        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.b2 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b5 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b6 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b7 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b8 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b9 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b10 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b11 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b12 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b13 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b14 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b15 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b16 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b17 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b18 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b19 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b20 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b21 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b22 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b23 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b24 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b25 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b26 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b27 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b28 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b29 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b30 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b31 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b32 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b33 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b34 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b35 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b36 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b37 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b38 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b39 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b40 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b41 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b42 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b43 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b44 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b45 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b46 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b47 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b48 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b49 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b50 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b51 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b52 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b53 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b54 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b55 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b56 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b57 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b58 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b59 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b60 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b61 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b62 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b63 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b64 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b65 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b66 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b67 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b68 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b69 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b70 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b71 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b72 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b73 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b74 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b75 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b76 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b77 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b78 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b79 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b80 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b81 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b82 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b83 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b84 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b85 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b86 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b87 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b88 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b89 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b90 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b91 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b92 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b93 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b94 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b95 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b96 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b97 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b98 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b99 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b100 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b101 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b102 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b103 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b104 = Var(within=Binary,bounds=(0,1),initialize=0)
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
m.b174 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b175 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b176 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b177 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b178 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b179 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b180 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b181 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b182 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b183 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b184 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b185 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b186 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b187 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b188 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b189 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b190 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b191 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b192 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b193 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b194 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b195 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b196 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b197 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b198 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b199 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b200 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b201 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b202 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b203 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b204 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b205 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b206 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b207 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b208 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b209 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b210 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b211 = Var(within=Binary,bounds=(0,1),initialize=0)

m.obj = Objective(expr=   35250*m.b2 + 60450*m.b3 + 6500*m.b4 + 3900*m.b5 + 21620*m.b6 + 44080*m.b7 + 63800*m.b8
                        + 45600*m.b9 + 63220*m.b10 + 30940*m.b11 + 37400*m.b12 + 81840*m.b13 + 52200*m.b14 + 26690*m.b15
                        + 148750*m.b16 + 85910*m.b17 + 103790*m.b18 + 140270*m.b19 + 155430*m.b20 + 51840*m.b21
                        + 90210*m.b22 + 680*m.b23 + 59450*m.b24 + 35910*m.b25 + 66330*m.b26 + 5890*m.b27 + 630*m.b28
                        + 138450*m.b29 + 90640*m.b30 + 48230*m.b31 + 41500*m.b32 + 95130*m.b33 + 41400*m.b34
                        + 31030*m.b35 + 8820*m.b36 + 148780*m.b37 + 39330*m.b38 + 120450*m.b39 + 5220*m.b40
                        + 12150*m.b41 + 93810*m.b42 + 5850*m.b43 + 5250*m.b44 + 28310*m.b45 + 6160*m.b46 + 46640*m.b47
                        + 29670*m.b48 + 104310*m.b49 + 4830*m.b50 + 25380*m.b51 + 13230*m.b52 + 81360*m.b53
                        + 18340*m.b54 + 15540*m.b55 + 148770*m.b56 + 43890*m.b57 + 59340*m.b58 + 6160*m.b59 + 1320*m.b60
                        + 11220*m.b61 + 104780*m.b62 + 62700*m.b63 + 42630*m.b64 + 6960*m.b65 + 7560*m.b66 + 90450*m.b67
                        + 40050*m.b68 + 181350*m.b69 + 2790*m.b70 + 74970*m.b71 + 6000*m.b72 + 33800*m.b73 + 71820*m.b74
                        + 97920*m.b75 + 3120*m.b76 + 15820*m.b77 + 4360*m.b78 + 35530*m.b79 + 67450*m.b80 + 36120*m.b81
                        + 15080*m.b82 + 28350*m.b83 + 76440*m.b84 + 37130*m.b85 + 19030*m.b86 + 8400*m.b87 + 10200*m.b88
                        + 3990*m.b89 + 46560*m.b90 + 19720*m.b91 + 61490*m.b92 + 104780*m.b93 + 7440*m.b94 + 13050*m.b95
                        + 18270*m.b96 + 93000*m.b97 + 8040*m.b98 + 52140*m.b99 + 78970*m.b100 + 8650*m.b101
                        + 159570*m.b102 + 78690*m.b103 + 3700*m.b104 + 30800*m.b105 + 62370*m.b106 + 52020*m.b107
                        + 2940*m.b108 + 156620*m.b109 + 73670*m.b110 + 38220*m.b111 + 14260*m.b112 + 9900*m.b113
                        + 6390*m.b114 + 10220*m.b115 + 6790*m.b116 + 69700*m.b117 + 50220*m.b118 + 8190*m.b119
                        + 83720*m.b120 + 52250*m.b121 + 5460*m.b122 + 28710*m.b123 + 43470*m.b124 + 740*m.b125
                        + 52800*m.b126 + 22260*m.b127 + 13300*m.b128 + 60750*m.b129 + 79800*m.b130 + 30150*m.b131
                        + 220*m.b132 + 13860*m.b133 + 140130*m.b134 + 96640*m.b135 + 140220*m.b136 + 91060*m.b137
                        + 102900*m.b138 + 8280*m.b139 + 46920*m.b140 + 1290*m.b141 + 104780*m.b142 + 40500*m.b143
                        + 630*m.b144 + 68850*m.b145 + 101430*m.b146 + 79100*m.b147 + 33000*m.b148 + 108750*m.b149
                        + 2400*m.b150 + 19320*m.b151 + 31980*m.b152 + 11300*m.b153 + 96030*m.b154 + 200*m.b155
                        + 6890*m.b156 + 52920*m.b157 + 56840*m.b158 + 39690*m.b159 + 81810*m.b160 + 56050*m.b161
                        + 44650*m.b162 + 93790*m.b163 + 16430*m.b164 + 136800*m.b165 + 37450*m.b166 + 116100*m.b167
                        + 69580*m.b168 + 91590*m.b169 + 148570*m.b170 + 10260*m.b171 + 860*m.b172 + 139730*m.b173
                        + 5670*m.b174 + 57510*m.b175 + 900*m.b176 + 130340*m.b177 + 135590*m.b178 + 131580*m.b179
                        + 11700*m.b180 + 59950*m.b181 + 19000*m.b182 + 60400*m.b183 + 490*m.b184 + 75240*m.b185
                        + 56710*m.b186 + 157430*m.b187 + 45750*m.b188 + 17490*m.b189 + 127440*m.b190 + 19720*m.b191
                        + 16960*m.b192 + 13510*m.b193 + 79170*m.b194 + 14720*m.b195 + 11270*m.b196 + 145780*m.b197
                        + 29700*m.b198 + 17980*m.b199 + 28130*m.b200 + 123710*m.b201 + 18360*m.b202 + 24070*m.b203
                        + 75050*m.b204 + 30030*m.b205 + 910*m.b206 + 91670*m.b207 + 100570*m.b208 + 63700*m.b209
                        + 42930*m.b210, sense=minimize)

m.c2 = Constraint(expr= - m.b2 + m.b3 - m.b22 <= 0)

m.c3 = Constraint(expr= - m.b2 + m.b4 - m.b23 <= 0)

m.c4 = Constraint(expr= - m.b2 + m.b5 - m.b24 <= 0)

m.c5 = Constraint(expr= - m.b2 + m.b6 - m.b25 <= 0)

m.c6 = Constraint(expr= - m.b2 + m.b7 - m.b26 <= 0)

m.c7 = Constraint(expr= - m.b2 + m.b8 - m.b27 <= 0)

m.c8 = Constraint(expr= - m.b2 + m.b9 - m.b28 <= 0)

m.c9 = Constraint(expr= - m.b2 + m.b10 - m.b29 <= 0)

m.c10 = Constraint(expr= - m.b2 + m.b11 - m.b30 <= 0)

m.c11 = Constraint(expr= - m.b2 + m.b12 - m.b31 <= 0)

m.c12 = Constraint(expr= - m.b2 + m.b13 - m.b32 <= 0)

m.c13 = Constraint(expr= - m.b2 + m.b14 - m.b33 <= 0)

m.c14 = Constraint(expr= - m.b2 + m.b15 - m.b34 <= 0)

m.c15 = Constraint(expr= - m.b2 + m.b16 - m.b35 <= 0)

m.c16 = Constraint(expr= - m.b2 + m.b17 - m.b36 <= 0)

m.c17 = Constraint(expr= - m.b2 + m.b18 - m.b37 <= 0)

m.c18 = Constraint(expr= - m.b2 + m.b19 - m.b38 <= 0)

m.c19 = Constraint(expr= - m.b2 + m.b20 - m.b39 <= 0)

m.c20 = Constraint(expr= - m.b2 + m.b21 - m.b40 <= 0)

m.c21 = Constraint(expr= - m.b3 + m.b4 - m.b41 <= 0)

m.c22 = Constraint(expr= - m.b3 + m.b5 - m.b42 <= 0)

m.c23 = Constraint(expr= - m.b3 + m.b6 - m.b43 <= 0)

m.c24 = Constraint(expr= - m.b3 + m.b7 - m.b44 <= 0)

m.c25 = Constraint(expr= - m.b3 + m.b8 - m.b45 <= 0)

m.c26 = Constraint(expr= - m.b3 + m.b9 - m.b46 <= 0)

m.c27 = Constraint(expr= - m.b3 + m.b10 - m.b47 <= 0)

m.c28 = Constraint(expr= - m.b3 + m.b11 - m.b48 <= 0)

m.c29 = Constraint(expr= - m.b3 + m.b12 - m.b49 <= 0)

m.c30 = Constraint(expr= - m.b3 + m.b13 - m.b50 <= 0)

m.c31 = Constraint(expr= - m.b3 + m.b14 - m.b51 <= 0)

m.c32 = Constraint(expr= - m.b3 + m.b15 - m.b52 <= 0)

m.c33 = Constraint(expr= - m.b3 + m.b16 - m.b53 <= 0)

m.c34 = Constraint(expr= - m.b3 + m.b17 - m.b54 <= 0)

m.c35 = Constraint(expr= - m.b3 + m.b18 - m.b55 <= 0)

m.c36 = Constraint(expr= - m.b3 + m.b19 - m.b56 <= 0)

m.c37 = Constraint(expr= - m.b3 + m.b20 - m.b57 <= 0)

m.c38 = Constraint(expr= - m.b3 + m.b21 - m.b58 <= 0)

m.c39 = Constraint(expr= - m.b4 + m.b5 - m.b59 <= 0)

m.c40 = Constraint(expr= - m.b4 + m.b6 - m.b60 <= 0)

m.c41 = Constraint(expr= - m.b4 + m.b7 - m.b61 <= 0)

m.c42 = Constraint(expr= - m.b4 + m.b8 - m.b62 <= 0)

m.c43 = Constraint(expr= - m.b4 + m.b9 - m.b63 <= 0)

m.c44 = Constraint(expr= - m.b4 + m.b10 - m.b64 <= 0)

m.c45 = Constraint(expr= - m.b4 + m.b11 - m.b65 <= 0)

m.c46 = Constraint(expr= - m.b4 + m.b12 - m.b66 <= 0)

m.c47 = Constraint(expr= - m.b4 + m.b13 - m.b67 <= 0)

m.c48 = Constraint(expr= - m.b4 + m.b14 - m.b68 <= 0)

m.c49 = Constraint(expr= - m.b4 + m.b15 - m.b69 <= 0)

m.c50 = Constraint(expr= - m.b4 + m.b16 - m.b70 <= 0)

m.c51 = Constraint(expr= - m.b4 + m.b17 - m.b71 <= 0)

m.c52 = Constraint(expr= - m.b4 + m.b18 - m.b72 <= 0)

m.c53 = Constraint(expr= - m.b4 + m.b19 - m.b73 <= 0)

m.c54 = Constraint(expr= - m.b4 + m.b20 - m.b74 <= 0)

m.c55 = Constraint(expr= - m.b4 + m.b21 - m.b75 <= 0)

m.c56 = Constraint(expr= - m.b5 + m.b6 - m.b76 <= 0)

m.c57 = Constraint(expr= - m.b5 + m.b7 - m.b77 <= 0)

m.c58 = Constraint(expr= - m.b5 + m.b8 - m.b78 <= 0)

m.c59 = Constraint(expr= - m.b5 + m.b9 - m.b79 <= 0)

m.c60 = Constraint(expr= - m.b5 + m.b10 - m.b80 <= 0)

m.c61 = Constraint(expr= - m.b5 + m.b11 - m.b81 <= 0)

m.c62 = Constraint(expr= - m.b5 + m.b12 - m.b82 <= 0)

m.c63 = Constraint(expr= - m.b5 + m.b13 - m.b83 <= 0)

m.c64 = Constraint(expr= - m.b5 + m.b14 - m.b84 <= 0)

m.c65 = Constraint(expr= - m.b5 + m.b15 - m.b85 <= 0)

m.c66 = Constraint(expr= - m.b5 + m.b16 - m.b86 <= 0)

m.c67 = Constraint(expr= - m.b5 + m.b17 - m.b87 <= 0)

m.c68 = Constraint(expr= - m.b5 + m.b18 - m.b88 <= 0)

m.c69 = Constraint(expr= - m.b5 + m.b19 - m.b89 <= 0)

m.c70 = Constraint(expr= - m.b5 + m.b20 - m.b90 <= 0)

m.c71 = Constraint(expr= - m.b5 + m.b21 - m.b91 <= 0)

m.c72 = Constraint(expr= - m.b6 + m.b7 - m.b92 <= 0)

m.c73 = Constraint(expr= - m.b6 + m.b8 - m.b93 <= 0)

m.c74 = Constraint(expr= - m.b6 + m.b9 - m.b94 <= 0)

m.c75 = Constraint(expr= - m.b6 + m.b10 - m.b95 <= 0)

m.c76 = Constraint(expr= - m.b6 + m.b11 - m.b96 <= 0)

m.c77 = Constraint(expr= - m.b6 + m.b12 - m.b97 <= 0)

m.c78 = Constraint(expr= - m.b6 + m.b13 - m.b98 <= 0)

m.c79 = Constraint(expr= - m.b6 + m.b14 - m.b99 <= 0)

m.c80 = Constraint(expr= - m.b6 + m.b15 - m.b100 <= 0)

m.c81 = Constraint(expr= - m.b6 + m.b16 - m.b101 <= 0)

m.c82 = Constraint(expr= - m.b6 + m.b17 - m.b102 <= 0)

m.c83 = Constraint(expr= - m.b6 + m.b18 - m.b103 <= 0)

m.c84 = Constraint(expr= - m.b6 + m.b19 - m.b104 <= 0)

m.c85 = Constraint(expr= - m.b6 + m.b20 - m.b105 <= 0)

m.c86 = Constraint(expr= - m.b6 + m.b21 - m.b106 <= 0)

m.c87 = Constraint(expr= - m.b7 + m.b8 - m.b107 <= 0)

m.c88 = Constraint(expr= - m.b7 + m.b9 - m.b108 <= 0)

m.c89 = Constraint(expr= - m.b7 + m.b10 - m.b109 <= 0)

m.c90 = Constraint(expr= - m.b7 + m.b11 - m.b110 <= 0)

m.c91 = Constraint(expr= - m.b7 + m.b12 - m.b111 <= 0)

m.c92 = Constraint(expr= - m.b7 + m.b13 - m.b112 <= 0)

m.c93 = Constraint(expr= - m.b7 + m.b14 - m.b113 <= 0)

m.c94 = Constraint(expr= - m.b7 + m.b15 - m.b114 <= 0)

m.c95 = Constraint(expr= - m.b7 + m.b16 - m.b115 <= 0)

m.c96 = Constraint(expr= - m.b7 + m.b17 - m.b116 <= 0)

m.c97 = Constraint(expr= - m.b7 + m.b18 - m.b117 <= 0)

m.c98 = Constraint(expr= - m.b7 + m.b19 - m.b118 <= 0)

m.c99 = Constraint(expr= - m.b7 + m.b20 - m.b119 <= 0)

m.c100 = Constraint(expr= - m.b7 + m.b21 - m.b120 <= 0)

m.c101 = Constraint(expr= - m.b8 + m.b9 - m.b121 <= 0)

m.c102 = Constraint(expr= - m.b8 + m.b10 - m.b122 <= 0)

m.c103 = Constraint(expr= - m.b8 + m.b11 - m.b123 <= 0)

m.c104 = Constraint(expr= - m.b8 + m.b12 - m.b124 <= 0)

m.c105 = Constraint(expr= - m.b8 + m.b13 - m.b125 <= 0)

m.c106 = Constraint(expr= - m.b8 + m.b14 - m.b126 <= 0)

m.c107 = Constraint(expr= - m.b8 + m.b15 - m.b127 <= 0)

m.c108 = Constraint(expr= - m.b8 + m.b16 - m.b128 <= 0)

m.c109 = Constraint(expr= - m.b8 + m.b17 - m.b129 <= 0)

m.c110 = Constraint(expr= - m.b8 + m.b18 - m.b130 <= 0)

m.c111 = Constraint(expr= - m.b8 + m.b19 - m.b131 <= 0)

m.c112 = Constraint(expr= - m.b8 + m.b20 - m.b132 <= 0)

m.c113 = Constraint(expr= - m.b8 + m.b21 - m.b133 <= 0)

m.c114 = Constraint(expr= - m.b9 + m.b10 - m.b134 <= 0)

m.c115 = Constraint(expr= - m.b9 + m.b11 - m.b135 <= 0)

m.c116 = Constraint(expr= - m.b9 + m.b12 - m.b136 <= 0)

m.c117 = Constraint(expr= - m.b9 + m.b13 - m.b137 <= 0)

m.c118 = Constraint(expr= - m.b9 + m.b14 - m.b138 <= 0)

m.c119 = Constraint(expr= - m.b9 + m.b15 - m.b139 <= 0)

m.c120 = Constraint(expr= - m.b9 + m.b16 - m.b140 <= 0)

m.c121 = Constraint(expr= - m.b9 + m.b17 - m.b141 <= 0)

m.c122 = Constraint(expr= - m.b9 + m.b18 - m.b142 <= 0)

m.c123 = Constraint(expr= - m.b9 + m.b19 - m.b143 <= 0)

m.c124 = Constraint(expr= - m.b9 + m.b20 - m.b144 <= 0)

m.c125 = Constraint(expr= - m.b9 + m.b21 - m.b145 <= 0)

m.c126 = Constraint(expr= - m.b10 + m.b11 - m.b146 <= 0)

m.c127 = Constraint(expr= - m.b10 + m.b12 - m.b147 <= 0)

m.c128 = Constraint(expr= - m.b10 + m.b13 - m.b148 <= 0)

m.c129 = Constraint(expr= - m.b10 + m.b14 - m.b149 <= 0)

m.c130 = Constraint(expr= - m.b10 + m.b15 - m.b150 <= 0)

m.c131 = Constraint(expr= - m.b10 + m.b16 - m.b151 <= 0)

m.c132 = Constraint(expr= - m.b10 + m.b17 - m.b152 <= 0)

m.c133 = Constraint(expr= - m.b10 + m.b18 - m.b153 <= 0)

m.c134 = Constraint(expr= - m.b10 + m.b19 - m.b154 <= 0)

m.c135 = Constraint(expr= - m.b10 + m.b20 - m.b155 <= 0)

m.c136 = Constraint(expr= - m.b10 + m.b21 - m.b156 <= 0)

m.c137 = Constraint(expr= - m.b11 + m.b12 - m.b157 <= 0)

m.c138 = Constraint(expr= - m.b11 + m.b13 - m.b158 <= 0)

m.c139 = Constraint(expr= - m.b11 + m.b14 - m.b159 <= 0)

m.c140 = Constraint(expr= - m.b11 + m.b15 - m.b160 <= 0)

m.c141 = Constraint(expr= - m.b11 + m.b16 - m.b161 <= 0)

m.c142 = Constraint(expr= - m.b11 + m.b17 - m.b162 <= 0)

m.c143 = Constraint(expr= - m.b11 + m.b18 - m.b163 <= 0)

m.c144 = Constraint(expr= - m.b11 + m.b19 - m.b164 <= 0)

m.c145 = Constraint(expr= - m.b11 + m.b20 - m.b165 <= 0)

m.c146 = Constraint(expr= - m.b11 + m.b21 - m.b211 <= 0)

m.c147 = Constraint(expr= - m.b12 + m.b13 - m.b166 <= 0)

m.c148 = Constraint(expr= - m.b12 + m.b14 - m.b167 <= 0)

m.c149 = Constraint(expr= - m.b12 + m.b15 - m.b168 <= 0)

m.c150 = Constraint(expr= - m.b12 + m.b16 - m.b169 <= 0)

m.c151 = Constraint(expr= - m.b12 + m.b17 - m.b170 <= 0)

m.c152 = Constraint(expr= - m.b12 + m.b18 - m.b171 <= 0)

m.c153 = Constraint(expr= - m.b12 + m.b19 - m.b172 <= 0)

m.c154 = Constraint(expr= - m.b12 + m.b20 - m.b173 <= 0)

m.c155 = Constraint(expr= - m.b12 + m.b21 - m.b174 <= 0)

m.c156 = Constraint(expr= - m.b13 + m.b14 - m.b175 <= 0)

m.c157 = Constraint(expr= - m.b13 + m.b15 - m.b176 <= 0)

m.c158 = Constraint(expr= - m.b13 + m.b16 - m.b177 <= 0)

m.c159 = Constraint(expr= - m.b13 + m.b17 - m.b178 <= 0)

m.c160 = Constraint(expr= - m.b13 + m.b18 - m.b179 <= 0)

m.c161 = Constraint(expr= - m.b13 + m.b19 - m.b180 <= 0)

m.c162 = Constraint(expr= - m.b13 + m.b20 - m.b181 <= 0)

m.c163 = Constraint(expr= - m.b13 + m.b21 - m.b182 <= 0)

m.c164 = Constraint(expr= - m.b14 + m.b15 - m.b183 <= 0)

m.c165 = Constraint(expr= - m.b14 + m.b16 - m.b184 <= 0)

m.c166 = Constraint(expr= - m.b14 + m.b17 - m.b185 <= 0)

m.c167 = Constraint(expr= - m.b14 + m.b18 - m.b186 <= 0)

m.c168 = Constraint(expr= - m.b14 + m.b19 - m.b187 <= 0)

m.c169 = Constraint(expr= - m.b14 + m.b20 - m.b188 <= 0)

m.c170 = Constraint(expr= - m.b14 + m.b21 - m.b189 <= 0)

m.c171 = Constraint(expr= - m.b15 + m.b16 - m.b190 <= 0)

m.c172 = Constraint(expr= - m.b15 + m.b17 - m.b191 <= 0)

m.c173 = Constraint(expr= - m.b15 + m.b18 - m.b192 <= 0)

m.c174 = Constraint(expr= - m.b15 + m.b19 - m.b193 <= 0)

m.c175 = Constraint(expr= - m.b15 + m.b20 - m.b194 <= 0)

m.c176 = Constraint(expr= - m.b15 + m.b21 - m.b195 <= 0)

m.c177 = Constraint(expr= - m.b16 + m.b17 - m.b196 <= 0)

m.c178 = Constraint(expr= - m.b16 + m.b18 - m.b197 <= 0)

m.c179 = Constraint(expr= - m.b16 + m.b19 - m.b198 <= 0)

m.c180 = Constraint(expr= - m.b16 + m.b20 - m.b199 <= 0)

m.c181 = Constraint(expr= - m.b16 + m.b21 - m.b200 <= 0)

m.c182 = Constraint(expr= - m.b17 + m.b18 - m.b201 <= 0)

m.c183 = Constraint(expr= - m.b17 + m.b19 - m.b202 <= 0)

m.c184 = Constraint(expr= - m.b17 + m.b20 - m.b203 <= 0)

m.c185 = Constraint(expr= - m.b17 + m.b21 - m.b204 <= 0)

m.c186 = Constraint(expr= - m.b18 + m.b19 - m.b205 <= 0)

m.c187 = Constraint(expr= - m.b18 + m.b20 - m.b206 <= 0)

m.c188 = Constraint(expr= - m.b18 + m.b21 - m.b207 <= 0)

m.c189 = Constraint(expr= - m.b19 + m.b20 - m.b208 <= 0)

m.c190 = Constraint(expr= - m.b19 + m.b21 - m.b209 <= 0)

m.c191 = Constraint(expr= - m.b20 + m.b21 - m.b210 <= 0)

m.c192 = Constraint(expr= - m.b22 + m.b23 - m.b41 <= 0)

m.c193 = Constraint(expr= - m.b22 + m.b24 - m.b42 <= 0)

m.c194 = Constraint(expr= - m.b22 + m.b25 - m.b43 <= 0)

m.c195 = Constraint(expr= - m.b22 + m.b26 - m.b44 <= 0)

m.c196 = Constraint(expr= - m.b22 + m.b27 - m.b45 <= 0)

m.c197 = Constraint(expr= - m.b22 + m.b28 - m.b46 <= 0)

m.c198 = Constraint(expr= - m.b22 + m.b29 - m.b47 <= 0)

m.c199 = Constraint(expr= - m.b22 + m.b30 - m.b48 <= 0)

m.c200 = Constraint(expr= - m.b22 + m.b31 - m.b49 <= 0)

m.c201 = Constraint(expr= - m.b22 + m.b32 - m.b50 <= 0)

m.c202 = Constraint(expr= - m.b22 + m.b33 - m.b51 <= 0)

m.c203 = Constraint(expr= - m.b22 + m.b34 - m.b52 <= 0)

m.c204 = Constraint(expr= - m.b22 + m.b35 - m.b53 <= 0)

m.c205 = Constraint(expr= - m.b22 + m.b36 - m.b54 <= 0)

m.c206 = Constraint(expr= - m.b22 + m.b37 - m.b55 <= 0)

m.c207 = Constraint(expr= - m.b22 + m.b38 - m.b56 <= 0)

m.c208 = Constraint(expr= - m.b22 + m.b39 - m.b57 <= 0)

m.c209 = Constraint(expr= - m.b22 + m.b40 - m.b58 <= 0)

m.c210 = Constraint(expr= - m.b23 + m.b24 - m.b59 <= 0)

m.c211 = Constraint(expr= - m.b23 + m.b25 - m.b60 <= 0)

m.c212 = Constraint(expr= - m.b23 + m.b26 - m.b61 <= 0)

m.c213 = Constraint(expr= - m.b23 + m.b27 - m.b62 <= 0)

m.c214 = Constraint(expr= - m.b23 + m.b28 - m.b63 <= 0)

m.c215 = Constraint(expr= - m.b23 + m.b29 - m.b64 <= 0)

m.c216 = Constraint(expr= - m.b23 + m.b30 - m.b65 <= 0)

m.c217 = Constraint(expr= - m.b23 + m.b31 - m.b66 <= 0)

m.c218 = Constraint(expr= - m.b23 + m.b32 - m.b67 <= 0)

m.c219 = Constraint(expr= - m.b23 + m.b33 - m.b68 <= 0)

m.c220 = Constraint(expr= - m.b23 + m.b34 - m.b69 <= 0)

m.c221 = Constraint(expr= - m.b23 + m.b35 - m.b70 <= 0)

m.c222 = Constraint(expr= - m.b23 + m.b36 - m.b71 <= 0)

m.c223 = Constraint(expr= - m.b23 + m.b37 - m.b72 <= 0)

m.c224 = Constraint(expr= - m.b23 + m.b38 - m.b73 <= 0)

m.c225 = Constraint(expr= - m.b23 + m.b39 - m.b74 <= 0)

m.c226 = Constraint(expr= - m.b23 + m.b40 - m.b75 <= 0)

m.c227 = Constraint(expr= - m.b24 + m.b25 - m.b76 <= 0)

m.c228 = Constraint(expr= - m.b24 + m.b26 - m.b77 <= 0)

m.c229 = Constraint(expr= - m.b24 + m.b27 - m.b78 <= 0)

m.c230 = Constraint(expr= - m.b24 + m.b28 - m.b79 <= 0)

m.c231 = Constraint(expr= - m.b24 + m.b29 - m.b80 <= 0)

m.c232 = Constraint(expr= - m.b24 + m.b30 - m.b81 <= 0)

m.c233 = Constraint(expr= - m.b24 + m.b31 - m.b82 <= 0)

m.c234 = Constraint(expr= - m.b24 + m.b32 - m.b83 <= 0)

m.c235 = Constraint(expr= - m.b24 + m.b33 - m.b84 <= 0)

m.c236 = Constraint(expr= - m.b24 + m.b34 - m.b85 <= 0)

m.c237 = Constraint(expr= - m.b24 + m.b35 - m.b86 <= 0)

m.c238 = Constraint(expr= - m.b24 + m.b36 - m.b87 <= 0)

m.c239 = Constraint(expr= - m.b24 + m.b37 - m.b88 <= 0)

m.c240 = Constraint(expr= - m.b24 + m.b38 - m.b89 <= 0)

m.c241 = Constraint(expr= - m.b24 + m.b39 - m.b90 <= 0)

m.c242 = Constraint(expr= - m.b24 + m.b40 - m.b91 <= 0)

m.c243 = Constraint(expr= - m.b25 + m.b26 - m.b92 <= 0)

m.c244 = Constraint(expr= - m.b25 + m.b27 - m.b93 <= 0)

m.c245 = Constraint(expr= - m.b25 + m.b28 - m.b94 <= 0)

m.c246 = Constraint(expr= - m.b25 + m.b29 - m.b95 <= 0)

m.c247 = Constraint(expr= - m.b25 + m.b30 - m.b96 <= 0)

m.c248 = Constraint(expr= - m.b25 + m.b31 - m.b97 <= 0)

m.c249 = Constraint(expr= - m.b25 + m.b32 - m.b98 <= 0)

m.c250 = Constraint(expr= - m.b25 + m.b33 - m.b99 <= 0)

m.c251 = Constraint(expr= - m.b25 + m.b34 - m.b100 <= 0)

m.c252 = Constraint(expr= - m.b25 + m.b35 - m.b101 <= 0)

m.c253 = Constraint(expr= - m.b25 + m.b36 - m.b102 <= 0)

m.c254 = Constraint(expr= - m.b25 + m.b37 - m.b103 <= 0)

m.c255 = Constraint(expr= - m.b25 + m.b38 - m.b104 <= 0)

m.c256 = Constraint(expr= - m.b25 + m.b39 - m.b105 <= 0)

m.c257 = Constraint(expr= - m.b25 + m.b40 - m.b106 <= 0)

m.c258 = Constraint(expr= - m.b26 + m.b27 - m.b107 <= 0)

m.c259 = Constraint(expr= - m.b26 + m.b28 - m.b108 <= 0)

m.c260 = Constraint(expr= - m.b26 + m.b29 - m.b109 <= 0)

m.c261 = Constraint(expr= - m.b26 + m.b30 - m.b110 <= 0)

m.c262 = Constraint(expr= - m.b26 + m.b31 - m.b111 <= 0)

m.c263 = Constraint(expr= - m.b26 + m.b32 - m.b112 <= 0)

m.c264 = Constraint(expr= - m.b26 + m.b33 - m.b113 <= 0)

m.c265 = Constraint(expr= - m.b26 + m.b34 - m.b114 <= 0)

m.c266 = Constraint(expr= - m.b26 + m.b35 - m.b115 <= 0)

m.c267 = Constraint(expr= - m.b26 + m.b36 - m.b116 <= 0)

m.c268 = Constraint(expr= - m.b26 + m.b37 - m.b117 <= 0)

m.c269 = Constraint(expr= - m.b26 + m.b38 - m.b118 <= 0)

m.c270 = Constraint(expr= - m.b26 + m.b39 - m.b119 <= 0)

m.c271 = Constraint(expr= - m.b26 + m.b40 - m.b120 <= 0)

m.c272 = Constraint(expr= - m.b27 + m.b28 - m.b121 <= 0)

m.c273 = Constraint(expr= - m.b27 + m.b29 - m.b122 <= 0)

m.c274 = Constraint(expr= - m.b27 + m.b30 - m.b123 <= 0)

m.c275 = Constraint(expr= - m.b27 + m.b31 - m.b124 <= 0)

m.c276 = Constraint(expr= - m.b27 + m.b32 - m.b125 <= 0)

m.c277 = Constraint(expr= - m.b27 + m.b33 - m.b126 <= 0)

m.c278 = Constraint(expr= - m.b27 + m.b34 - m.b127 <= 0)

m.c279 = Constraint(expr= - m.b27 + m.b35 - m.b128 <= 0)

m.c280 = Constraint(expr= - m.b27 + m.b36 - m.b129 <= 0)

m.c281 = Constraint(expr= - m.b27 + m.b37 - m.b130 <= 0)

m.c282 = Constraint(expr= - m.b27 + m.b38 - m.b131 <= 0)

m.c283 = Constraint(expr= - m.b27 + m.b39 - m.b132 <= 0)

m.c284 = Constraint(expr= - m.b27 + m.b40 - m.b133 <= 0)

m.c285 = Constraint(expr= - m.b28 + m.b29 - m.b134 <= 0)

m.c286 = Constraint(expr= - m.b28 + m.b30 - m.b135 <= 0)

m.c287 = Constraint(expr= - m.b28 + m.b31 - m.b136 <= 0)

m.c288 = Constraint(expr= - m.b28 + m.b32 - m.b137 <= 0)

m.c289 = Constraint(expr= - m.b28 + m.b33 - m.b138 <= 0)

m.c290 = Constraint(expr= - m.b28 + m.b34 - m.b139 <= 0)

m.c291 = Constraint(expr= - m.b28 + m.b35 - m.b140 <= 0)

m.c292 = Constraint(expr= - m.b28 + m.b36 - m.b141 <= 0)

m.c293 = Constraint(expr= - m.b28 + m.b37 - m.b142 <= 0)

m.c294 = Constraint(expr= - m.b28 + m.b38 - m.b143 <= 0)

m.c295 = Constraint(expr= - m.b28 + m.b39 - m.b144 <= 0)

m.c296 = Constraint(expr= - m.b28 + m.b40 - m.b145 <= 0)

m.c297 = Constraint(expr= - m.b29 + m.b30 - m.b146 <= 0)

m.c298 = Constraint(expr= - m.b29 + m.b31 - m.b147 <= 0)

m.c299 = Constraint(expr= - m.b29 + m.b32 - m.b148 <= 0)

m.c300 = Constraint(expr= - m.b29 + m.b33 - m.b149 <= 0)

m.c301 = Constraint(expr= - m.b29 + m.b34 - m.b150 <= 0)

m.c302 = Constraint(expr= - m.b29 + m.b35 - m.b151 <= 0)

m.c303 = Constraint(expr= - m.b29 + m.b36 - m.b152 <= 0)

m.c304 = Constraint(expr= - m.b29 + m.b37 - m.b153 <= 0)

m.c305 = Constraint(expr= - m.b29 + m.b38 - m.b154 <= 0)

m.c306 = Constraint(expr= - m.b29 + m.b39 - m.b155 <= 0)

m.c307 = Constraint(expr= - m.b29 + m.b40 - m.b156 <= 0)

m.c308 = Constraint(expr= - m.b30 + m.b31 - m.b157 <= 0)

m.c309 = Constraint(expr= - m.b30 + m.b32 - m.b158 <= 0)

m.c310 = Constraint(expr= - m.b30 + m.b33 - m.b159 <= 0)

m.c311 = Constraint(expr= - m.b30 + m.b34 - m.b160 <= 0)

m.c312 = Constraint(expr= - m.b30 + m.b35 - m.b161 <= 0)

m.c313 = Constraint(expr= - m.b30 + m.b36 - m.b162 <= 0)

m.c314 = Constraint(expr= - m.b30 + m.b37 - m.b163 <= 0)

m.c315 = Constraint(expr= - m.b30 + m.b38 - m.b164 <= 0)

m.c316 = Constraint(expr= - m.b30 + m.b39 - m.b165 <= 0)

m.c317 = Constraint(expr= - m.b30 + m.b40 - m.b211 <= 0)

m.c318 = Constraint(expr= - m.b31 + m.b32 - m.b166 <= 0)

m.c319 = Constraint(expr= - m.b31 + m.b33 - m.b167 <= 0)

m.c320 = Constraint(expr= - m.b31 + m.b34 - m.b168 <= 0)

m.c321 = Constraint(expr= - m.b31 + m.b35 - m.b169 <= 0)

m.c322 = Constraint(expr= - m.b31 + m.b36 - m.b170 <= 0)

m.c323 = Constraint(expr= - m.b31 + m.b37 - m.b171 <= 0)

m.c324 = Constraint(expr= - m.b31 + m.b38 - m.b172 <= 0)

m.c325 = Constraint(expr= - m.b31 + m.b39 - m.b173 <= 0)

m.c326 = Constraint(expr= - m.b31 + m.b40 - m.b174 <= 0)

m.c327 = Constraint(expr= - m.b32 + m.b33 - m.b175 <= 0)

m.c328 = Constraint(expr= - m.b32 + m.b34 - m.b176 <= 0)

m.c329 = Constraint(expr= - m.b32 + m.b35 - m.b177 <= 0)

m.c330 = Constraint(expr= - m.b32 + m.b36 - m.b178 <= 0)

m.c331 = Constraint(expr= - m.b32 + m.b37 - m.b179 <= 0)

m.c332 = Constraint(expr= - m.b32 + m.b38 - m.b180 <= 0)

m.c333 = Constraint(expr= - m.b32 + m.b39 - m.b181 <= 0)

m.c334 = Constraint(expr= - m.b32 + m.b40 - m.b182 <= 0)

m.c335 = Constraint(expr= - m.b33 + m.b34 - m.b183 <= 0)

m.c336 = Constraint(expr= - m.b33 + m.b35 - m.b184 <= 0)

m.c337 = Constraint(expr= - m.b33 + m.b36 - m.b185 <= 0)

m.c338 = Constraint(expr= - m.b33 + m.b37 - m.b186 <= 0)

m.c339 = Constraint(expr= - m.b33 + m.b38 - m.b187 <= 0)

m.c340 = Constraint(expr= - m.b33 + m.b39 - m.b188 <= 0)

m.c341 = Constraint(expr= - m.b33 + m.b40 - m.b189 <= 0)

m.c342 = Constraint(expr= - m.b34 + m.b35 - m.b190 <= 0)

m.c343 = Constraint(expr= - m.b34 + m.b36 - m.b191 <= 0)

m.c344 = Constraint(expr= - m.b34 + m.b37 - m.b192 <= 0)

m.c345 = Constraint(expr= - m.b34 + m.b38 - m.b193 <= 0)

m.c346 = Constraint(expr= - m.b34 + m.b39 - m.b194 <= 0)

m.c347 = Constraint(expr= - m.b34 + m.b40 - m.b195 <= 0)

m.c348 = Constraint(expr= - m.b35 + m.b36 - m.b196 <= 0)

m.c349 = Constraint(expr= - m.b35 + m.b37 - m.b197 <= 0)

m.c350 = Constraint(expr= - m.b35 + m.b38 - m.b198 <= 0)

m.c351 = Constraint(expr= - m.b35 + m.b39 - m.b199 <= 0)

m.c352 = Constraint(expr= - m.b35 + m.b40 - m.b200 <= 0)

m.c353 = Constraint(expr= - m.b36 + m.b37 - m.b201 <= 0)

m.c354 = Constraint(expr= - m.b36 + m.b38 - m.b202 <= 0)

m.c355 = Constraint(expr= - m.b36 + m.b39 - m.b203 <= 0)

m.c356 = Constraint(expr= - m.b36 + m.b40 - m.b204 <= 0)

m.c357 = Constraint(expr= - m.b37 + m.b38 - m.b205 <= 0)

m.c358 = Constraint(expr= - m.b37 + m.b39 - m.b206 <= 0)

m.c359 = Constraint(expr= - m.b37 + m.b40 - m.b207 <= 0)

m.c360 = Constraint(expr= - m.b38 + m.b39 - m.b208 <= 0)

m.c361 = Constraint(expr= - m.b38 + m.b40 - m.b209 <= 0)

m.c362 = Constraint(expr= - m.b39 + m.b40 - m.b210 <= 0)

m.c363 = Constraint(expr= - m.b41 + m.b42 - m.b59 <= 0)

m.c364 = Constraint(expr= - m.b41 + m.b43 - m.b60 <= 0)

m.c365 = Constraint(expr= - m.b41 + m.b44 - m.b61 <= 0)

m.c366 = Constraint(expr= - m.b41 + m.b45 - m.b62 <= 0)

m.c367 = Constraint(expr= - m.b41 + m.b46 - m.b63 <= 0)

m.c368 = Constraint(expr= - m.b41 + m.b47 - m.b64 <= 0)

m.c369 = Constraint(expr= - m.b41 + m.b48 - m.b65 <= 0)

m.c370 = Constraint(expr= - m.b41 + m.b49 - m.b66 <= 0)

m.c371 = Constraint(expr= - m.b41 + m.b50 - m.b67 <= 0)

m.c372 = Constraint(expr= - m.b41 + m.b51 - m.b68 <= 0)

m.c373 = Constraint(expr= - m.b41 + m.b52 - m.b69 <= 0)

m.c374 = Constraint(expr= - m.b41 + m.b53 - m.b70 <= 0)

m.c375 = Constraint(expr= - m.b41 + m.b54 - m.b71 <= 0)

m.c376 = Constraint(expr= - m.b41 + m.b55 - m.b72 <= 0)

m.c377 = Constraint(expr= - m.b41 + m.b56 - m.b73 <= 0)

m.c378 = Constraint(expr= - m.b41 + m.b57 - m.b74 <= 0)

m.c379 = Constraint(expr= - m.b41 + m.b58 - m.b75 <= 0)

m.c380 = Constraint(expr= - m.b42 + m.b43 - m.b76 <= 0)

m.c381 = Constraint(expr= - m.b42 + m.b44 - m.b77 <= 0)

m.c382 = Constraint(expr= - m.b42 + m.b45 - m.b78 <= 0)

m.c383 = Constraint(expr= - m.b42 + m.b46 - m.b79 <= 0)

m.c384 = Constraint(expr= - m.b42 + m.b47 - m.b80 <= 0)

m.c385 = Constraint(expr= - m.b42 + m.b48 - m.b81 <= 0)

m.c386 = Constraint(expr= - m.b42 + m.b49 - m.b82 <= 0)

m.c387 = Constraint(expr= - m.b42 + m.b50 - m.b83 <= 0)

m.c388 = Constraint(expr= - m.b42 + m.b51 - m.b84 <= 0)

m.c389 = Constraint(expr= - m.b42 + m.b52 - m.b85 <= 0)

m.c390 = Constraint(expr= - m.b42 + m.b53 - m.b86 <= 0)

m.c391 = Constraint(expr= - m.b42 + m.b54 - m.b87 <= 0)

m.c392 = Constraint(expr= - m.b42 + m.b55 - m.b88 <= 0)

m.c393 = Constraint(expr= - m.b42 + m.b56 - m.b89 <= 0)

m.c394 = Constraint(expr= - m.b42 + m.b57 - m.b90 <= 0)

m.c395 = Constraint(expr= - m.b42 + m.b58 - m.b91 <= 0)

m.c396 = Constraint(expr= - m.b43 + m.b44 - m.b92 <= 0)

m.c397 = Constraint(expr= - m.b43 + m.b45 - m.b93 <= 0)

m.c398 = Constraint(expr= - m.b43 + m.b46 - m.b94 <= 0)

m.c399 = Constraint(expr= - m.b43 + m.b47 - m.b95 <= 0)

m.c400 = Constraint(expr= - m.b43 + m.b48 - m.b96 <= 0)

m.c401 = Constraint(expr= - m.b43 + m.b49 - m.b97 <= 0)

m.c402 = Constraint(expr= - m.b43 + m.b50 - m.b98 <= 0)

m.c403 = Constraint(expr= - m.b43 + m.b51 - m.b99 <= 0)

m.c404 = Constraint(expr= - m.b43 + m.b52 - m.b100 <= 0)

m.c405 = Constraint(expr= - m.b43 + m.b53 - m.b101 <= 0)

m.c406 = Constraint(expr= - m.b43 + m.b54 - m.b102 <= 0)

m.c407 = Constraint(expr= - m.b43 + m.b55 - m.b103 <= 0)

m.c408 = Constraint(expr= - m.b43 + m.b56 - m.b104 <= 0)

m.c409 = Constraint(expr= - m.b43 + m.b57 - m.b105 <= 0)

m.c410 = Constraint(expr= - m.b43 + m.b58 - m.b106 <= 0)

m.c411 = Constraint(expr= - m.b44 + m.b45 - m.b107 <= 0)

m.c412 = Constraint(expr= - m.b44 + m.b46 - m.b108 <= 0)

m.c413 = Constraint(expr= - m.b44 + m.b47 - m.b109 <= 0)

m.c414 = Constraint(expr= - m.b44 + m.b48 - m.b110 <= 0)

m.c415 = Constraint(expr= - m.b44 + m.b49 - m.b111 <= 0)

m.c416 = Constraint(expr= - m.b44 + m.b50 - m.b112 <= 0)

m.c417 = Constraint(expr= - m.b44 + m.b51 - m.b113 <= 0)

m.c418 = Constraint(expr= - m.b44 + m.b52 - m.b114 <= 0)

m.c419 = Constraint(expr= - m.b44 + m.b53 - m.b115 <= 0)

m.c420 = Constraint(expr= - m.b44 + m.b54 - m.b116 <= 0)

m.c421 = Constraint(expr= - m.b44 + m.b55 - m.b117 <= 0)

m.c422 = Constraint(expr= - m.b44 + m.b56 - m.b118 <= 0)

m.c423 = Constraint(expr= - m.b44 + m.b57 - m.b119 <= 0)

m.c424 = Constraint(expr= - m.b44 + m.b58 - m.b120 <= 0)

m.c425 = Constraint(expr= - m.b45 + m.b46 - m.b121 <= 0)

m.c426 = Constraint(expr= - m.b45 + m.b47 - m.b122 <= 0)

m.c427 = Constraint(expr= - m.b45 + m.b48 - m.b123 <= 0)

m.c428 = Constraint(expr= - m.b45 + m.b49 - m.b124 <= 0)

m.c429 = Constraint(expr= - m.b45 + m.b50 - m.b125 <= 0)

m.c430 = Constraint(expr= - m.b45 + m.b51 - m.b126 <= 0)

m.c431 = Constraint(expr= - m.b45 + m.b52 - m.b127 <= 0)

m.c432 = Constraint(expr= - m.b45 + m.b53 - m.b128 <= 0)

m.c433 = Constraint(expr= - m.b45 + m.b54 - m.b129 <= 0)

m.c434 = Constraint(expr= - m.b45 + m.b55 - m.b130 <= 0)

m.c435 = Constraint(expr= - m.b45 + m.b56 - m.b131 <= 0)

m.c436 = Constraint(expr= - m.b45 + m.b57 - m.b132 <= 0)

m.c437 = Constraint(expr= - m.b45 + m.b58 - m.b133 <= 0)

m.c438 = Constraint(expr= - m.b46 + m.b47 - m.b134 <= 0)

m.c439 = Constraint(expr= - m.b46 + m.b48 - m.b135 <= 0)

m.c440 = Constraint(expr= - m.b46 + m.b49 - m.b136 <= 0)

m.c441 = Constraint(expr= - m.b46 + m.b50 - m.b137 <= 0)

m.c442 = Constraint(expr= - m.b46 + m.b51 - m.b138 <= 0)

m.c443 = Constraint(expr= - m.b46 + m.b52 - m.b139 <= 0)

m.c444 = Constraint(expr= - m.b46 + m.b53 - m.b140 <= 0)

m.c445 = Constraint(expr= - m.b46 + m.b54 - m.b141 <= 0)

m.c446 = Constraint(expr= - m.b46 + m.b55 - m.b142 <= 0)

m.c447 = Constraint(expr= - m.b46 + m.b56 - m.b143 <= 0)

m.c448 = Constraint(expr= - m.b46 + m.b57 - m.b144 <= 0)

m.c449 = Constraint(expr= - m.b46 + m.b58 - m.b145 <= 0)

m.c450 = Constraint(expr= - m.b47 + m.b48 - m.b146 <= 0)

m.c451 = Constraint(expr= - m.b47 + m.b49 - m.b147 <= 0)

m.c452 = Constraint(expr= - m.b47 + m.b50 - m.b148 <= 0)

m.c453 = Constraint(expr= - m.b47 + m.b51 - m.b149 <= 0)

m.c454 = Constraint(expr= - m.b47 + m.b52 - m.b150 <= 0)

m.c455 = Constraint(expr= - m.b47 + m.b53 - m.b151 <= 0)

m.c456 = Constraint(expr= - m.b47 + m.b54 - m.b152 <= 0)

m.c457 = Constraint(expr= - m.b47 + m.b55 - m.b153 <= 0)

m.c458 = Constraint(expr= - m.b47 + m.b56 - m.b154 <= 0)

m.c459 = Constraint(expr= - m.b47 + m.b57 - m.b155 <= 0)

m.c460 = Constraint(expr= - m.b47 + m.b58 - m.b156 <= 0)

m.c461 = Constraint(expr= - m.b48 + m.b49 - m.b157 <= 0)

m.c462 = Constraint(expr= - m.b48 + m.b50 - m.b158 <= 0)

m.c463 = Constraint(expr= - m.b48 + m.b51 - m.b159 <= 0)

m.c464 = Constraint(expr= - m.b48 + m.b52 - m.b160 <= 0)

m.c465 = Constraint(expr= - m.b48 + m.b53 - m.b161 <= 0)

m.c466 = Constraint(expr= - m.b48 + m.b54 - m.b162 <= 0)

m.c467 = Constraint(expr= - m.b48 + m.b55 - m.b163 <= 0)

m.c468 = Constraint(expr= - m.b48 + m.b56 - m.b164 <= 0)

m.c469 = Constraint(expr= - m.b48 + m.b57 - m.b165 <= 0)

m.c470 = Constraint(expr= - m.b48 + m.b58 - m.b211 <= 0)

m.c471 = Constraint(expr= - m.b49 + m.b50 - m.b166 <= 0)

m.c472 = Constraint(expr= - m.b49 + m.b51 - m.b167 <= 0)

m.c473 = Constraint(expr= - m.b49 + m.b52 - m.b168 <= 0)

m.c474 = Constraint(expr= - m.b49 + m.b53 - m.b169 <= 0)

m.c475 = Constraint(expr= - m.b49 + m.b54 - m.b170 <= 0)

m.c476 = Constraint(expr= - m.b49 + m.b55 - m.b171 <= 0)

m.c477 = Constraint(expr= - m.b49 + m.b56 - m.b172 <= 0)

m.c478 = Constraint(expr= - m.b49 + m.b57 - m.b173 <= 0)

m.c479 = Constraint(expr= - m.b49 + m.b58 - m.b174 <= 0)

m.c480 = Constraint(expr= - m.b50 + m.b51 - m.b175 <= 0)

m.c481 = Constraint(expr= - m.b50 + m.b52 - m.b176 <= 0)

m.c482 = Constraint(expr= - m.b50 + m.b53 - m.b177 <= 0)

m.c483 = Constraint(expr= - m.b50 + m.b54 - m.b178 <= 0)

m.c484 = Constraint(expr= - m.b50 + m.b55 - m.b179 <= 0)

m.c485 = Constraint(expr= - m.b50 + m.b56 - m.b180 <= 0)

m.c486 = Constraint(expr= - m.b50 + m.b57 - m.b181 <= 0)

m.c487 = Constraint(expr= - m.b50 + m.b58 - m.b182 <= 0)

m.c488 = Constraint(expr= - m.b51 + m.b52 - m.b183 <= 0)

m.c489 = Constraint(expr= - m.b51 + m.b53 - m.b184 <= 0)

m.c490 = Constraint(expr= - m.b51 + m.b54 - m.b185 <= 0)

m.c491 = Constraint(expr= - m.b51 + m.b55 - m.b186 <= 0)

m.c492 = Constraint(expr= - m.b51 + m.b56 - m.b187 <= 0)

m.c493 = Constraint(expr= - m.b51 + m.b57 - m.b188 <= 0)

m.c494 = Constraint(expr= - m.b51 + m.b58 - m.b189 <= 0)

m.c495 = Constraint(expr= - m.b52 + m.b53 - m.b190 <= 0)

m.c496 = Constraint(expr= - m.b52 + m.b54 - m.b191 <= 0)

m.c497 = Constraint(expr= - m.b52 + m.b55 - m.b192 <= 0)

m.c498 = Constraint(expr= - m.b52 + m.b56 - m.b193 <= 0)

m.c499 = Constraint(expr= - m.b52 + m.b57 - m.b194 <= 0)

m.c500 = Constraint(expr= - m.b52 + m.b58 - m.b195 <= 0)

m.c501 = Constraint(expr= - m.b53 + m.b54 - m.b196 <= 0)

m.c502 = Constraint(expr= - m.b53 + m.b55 - m.b197 <= 0)

m.c503 = Constraint(expr= - m.b53 + m.b56 - m.b198 <= 0)

m.c504 = Constraint(expr= - m.b53 + m.b57 - m.b199 <= 0)

m.c505 = Constraint(expr= - m.b53 + m.b58 - m.b200 <= 0)

m.c506 = Constraint(expr= - m.b54 + m.b55 - m.b201 <= 0)

m.c507 = Constraint(expr= - m.b54 + m.b56 - m.b202 <= 0)

m.c508 = Constraint(expr= - m.b54 + m.b57 - m.b203 <= 0)

m.c509 = Constraint(expr= - m.b54 + m.b58 - m.b204 <= 0)

m.c510 = Constraint(expr= - m.b55 + m.b56 - m.b205 <= 0)

m.c511 = Constraint(expr= - m.b55 + m.b57 - m.b206 <= 0)

m.c512 = Constraint(expr= - m.b55 + m.b58 - m.b207 <= 0)

m.c513 = Constraint(expr= - m.b56 + m.b57 - m.b208 <= 0)

m.c514 = Constraint(expr= - m.b56 + m.b58 - m.b209 <= 0)

m.c515 = Constraint(expr= - m.b57 + m.b58 - m.b210 <= 0)

m.c516 = Constraint(expr= - m.b59 + m.b60 - m.b76 <= 0)

m.c517 = Constraint(expr= - m.b59 + m.b61 - m.b77 <= 0)

m.c518 = Constraint(expr= - m.b59 + m.b62 - m.b78 <= 0)

m.c519 = Constraint(expr= - m.b59 + m.b63 - m.b79 <= 0)

m.c520 = Constraint(expr= - m.b59 + m.b64 - m.b80 <= 0)

m.c521 = Constraint(expr= - m.b59 + m.b65 - m.b81 <= 0)

m.c522 = Constraint(expr= - m.b59 + m.b66 - m.b82 <= 0)

m.c523 = Constraint(expr= - m.b59 + m.b67 - m.b83 <= 0)

m.c524 = Constraint(expr= - m.b59 + m.b68 - m.b84 <= 0)

m.c525 = Constraint(expr= - m.b59 + m.b69 - m.b85 <= 0)

m.c526 = Constraint(expr= - m.b59 + m.b70 - m.b86 <= 0)

m.c527 = Constraint(expr= - m.b59 + m.b71 - m.b87 <= 0)

m.c528 = Constraint(expr= - m.b59 + m.b72 - m.b88 <= 0)

m.c529 = Constraint(expr= - m.b59 + m.b73 - m.b89 <= 0)

m.c530 = Constraint(expr= - m.b59 + m.b74 - m.b90 <= 0)

m.c531 = Constraint(expr= - m.b59 + m.b75 - m.b91 <= 0)

m.c532 = Constraint(expr= - m.b60 + m.b61 - m.b92 <= 0)

m.c533 = Constraint(expr= - m.b60 + m.b62 - m.b93 <= 0)

m.c534 = Constraint(expr= - m.b60 + m.b63 - m.b94 <= 0)

m.c535 = Constraint(expr= - m.b60 + m.b64 - m.b95 <= 0)

m.c536 = Constraint(expr= - m.b60 + m.b65 - m.b96 <= 0)

m.c537 = Constraint(expr= - m.b60 + m.b66 - m.b97 <= 0)

m.c538 = Constraint(expr= - m.b60 + m.b67 - m.b98 <= 0)

m.c539 = Constraint(expr= - m.b60 + m.b68 - m.b99 <= 0)

m.c540 = Constraint(expr= - m.b60 + m.b69 - m.b100 <= 0)

m.c541 = Constraint(expr= - m.b60 + m.b70 - m.b101 <= 0)

m.c542 = Constraint(expr= - m.b60 + m.b71 - m.b102 <= 0)

m.c543 = Constraint(expr= - m.b60 + m.b72 - m.b103 <= 0)

m.c544 = Constraint(expr= - m.b60 + m.b73 - m.b104 <= 0)

m.c545 = Constraint(expr= - m.b60 + m.b74 - m.b105 <= 0)

m.c546 = Constraint(expr= - m.b60 + m.b75 - m.b106 <= 0)

m.c547 = Constraint(expr= - m.b61 + m.b62 - m.b107 <= 0)

m.c548 = Constraint(expr= - m.b61 + m.b63 - m.b108 <= 0)

m.c549 = Constraint(expr= - m.b61 + m.b64 - m.b109 <= 0)

m.c550 = Constraint(expr= - m.b61 + m.b65 - m.b110 <= 0)

m.c551 = Constraint(expr= - m.b61 + m.b66 - m.b111 <= 0)

m.c552 = Constraint(expr= - m.b61 + m.b67 - m.b112 <= 0)

m.c553 = Constraint(expr= - m.b61 + m.b68 - m.b113 <= 0)

m.c554 = Constraint(expr= - m.b61 + m.b69 - m.b114 <= 0)

m.c555 = Constraint(expr= - m.b61 + m.b70 - m.b115 <= 0)

m.c556 = Constraint(expr= - m.b61 + m.b71 - m.b116 <= 0)

m.c557 = Constraint(expr= - m.b61 + m.b72 - m.b117 <= 0)

m.c558 = Constraint(expr= - m.b61 + m.b73 - m.b118 <= 0)

m.c559 = Constraint(expr= - m.b61 + m.b74 - m.b119 <= 0)

m.c560 = Constraint(expr= - m.b61 + m.b75 - m.b120 <= 0)

m.c561 = Constraint(expr= - m.b62 + m.b63 - m.b121 <= 0)

m.c562 = Constraint(expr= - m.b62 + m.b64 - m.b122 <= 0)

m.c563 = Constraint(expr= - m.b62 + m.b65 - m.b123 <= 0)

m.c564 = Constraint(expr= - m.b62 + m.b66 - m.b124 <= 0)

m.c565 = Constraint(expr= - m.b62 + m.b67 - m.b125 <= 0)

m.c566 = Constraint(expr= - m.b62 + m.b68 - m.b126 <= 0)

m.c567 = Constraint(expr= - m.b62 + m.b69 - m.b127 <= 0)

m.c568 = Constraint(expr= - m.b62 + m.b70 - m.b128 <= 0)

m.c569 = Constraint(expr= - m.b62 + m.b71 - m.b129 <= 0)

m.c570 = Constraint(expr= - m.b62 + m.b72 - m.b130 <= 0)

m.c571 = Constraint(expr= - m.b62 + m.b73 - m.b131 <= 0)

m.c572 = Constraint(expr= - m.b62 + m.b74 - m.b132 <= 0)

m.c573 = Constraint(expr= - m.b62 + m.b75 - m.b133 <= 0)

m.c574 = Constraint(expr= - m.b63 + m.b64 - m.b134 <= 0)

m.c575 = Constraint(expr= - m.b63 + m.b65 - m.b135 <= 0)

m.c576 = Constraint(expr= - m.b63 + m.b66 - m.b136 <= 0)

m.c577 = Constraint(expr= - m.b63 + m.b67 - m.b137 <= 0)

m.c578 = Constraint(expr= - m.b63 + m.b68 - m.b138 <= 0)

m.c579 = Constraint(expr= - m.b63 + m.b69 - m.b139 <= 0)

m.c580 = Constraint(expr= - m.b63 + m.b70 - m.b140 <= 0)

m.c581 = Constraint(expr= - m.b63 + m.b71 - m.b141 <= 0)

m.c582 = Constraint(expr= - m.b63 + m.b72 - m.b142 <= 0)

m.c583 = Constraint(expr= - m.b63 + m.b73 - m.b143 <= 0)

m.c584 = Constraint(expr= - m.b63 + m.b74 - m.b144 <= 0)

m.c585 = Constraint(expr= - m.b63 + m.b75 - m.b145 <= 0)

m.c586 = Constraint(expr= - m.b64 + m.b65 - m.b146 <= 0)

m.c587 = Constraint(expr= - m.b64 + m.b66 - m.b147 <= 0)

m.c588 = Constraint(expr= - m.b64 + m.b67 - m.b148 <= 0)

m.c589 = Constraint(expr= - m.b64 + m.b68 - m.b149 <= 0)

m.c590 = Constraint(expr= - m.b64 + m.b69 - m.b150 <= 0)

m.c591 = Constraint(expr= - m.b64 + m.b70 - m.b151 <= 0)

m.c592 = Constraint(expr= - m.b64 + m.b71 - m.b152 <= 0)

m.c593 = Constraint(expr= - m.b64 + m.b72 - m.b153 <= 0)

m.c594 = Constraint(expr= - m.b64 + m.b73 - m.b154 <= 0)

m.c595 = Constraint(expr= - m.b64 + m.b74 - m.b155 <= 0)

m.c596 = Constraint(expr= - m.b64 + m.b75 - m.b156 <= 0)

m.c597 = Constraint(expr= - m.b65 + m.b66 - m.b157 <= 0)

m.c598 = Constraint(expr= - m.b65 + m.b67 - m.b158 <= 0)

m.c599 = Constraint(expr= - m.b65 + m.b68 - m.b159 <= 0)

m.c600 = Constraint(expr= - m.b65 + m.b69 - m.b160 <= 0)

m.c601 = Constraint(expr= - m.b65 + m.b70 - m.b161 <= 0)

m.c602 = Constraint(expr= - m.b65 + m.b71 - m.b162 <= 0)

m.c603 = Constraint(expr= - m.b65 + m.b72 - m.b163 <= 0)

m.c604 = Constraint(expr= - m.b65 + m.b73 - m.b164 <= 0)

m.c605 = Constraint(expr= - m.b65 + m.b74 - m.b165 <= 0)

m.c606 = Constraint(expr= - m.b65 + m.b75 - m.b211 <= 0)

m.c607 = Constraint(expr= - m.b66 + m.b67 - m.b166 <= 0)

m.c608 = Constraint(expr= - m.b66 + m.b68 - m.b167 <= 0)

m.c609 = Constraint(expr= - m.b66 + m.b69 - m.b168 <= 0)

m.c610 = Constraint(expr= - m.b66 + m.b70 - m.b169 <= 0)

m.c611 = Constraint(expr= - m.b66 + m.b71 - m.b170 <= 0)

m.c612 = Constraint(expr= - m.b66 + m.b72 - m.b171 <= 0)

m.c613 = Constraint(expr= - m.b66 + m.b73 - m.b172 <= 0)

m.c614 = Constraint(expr= - m.b66 + m.b74 - m.b173 <= 0)

m.c615 = Constraint(expr= - m.b66 + m.b75 - m.b174 <= 0)

m.c616 = Constraint(expr= - m.b67 + m.b68 - m.b175 <= 0)

m.c617 = Constraint(expr= - m.b67 + m.b69 - m.b176 <= 0)

m.c618 = Constraint(expr= - m.b67 + m.b70 - m.b177 <= 0)

m.c619 = Constraint(expr= - m.b67 + m.b71 - m.b178 <= 0)

m.c620 = Constraint(expr= - m.b67 + m.b72 - m.b179 <= 0)

m.c621 = Constraint(expr= - m.b67 + m.b73 - m.b180 <= 0)

m.c622 = Constraint(expr= - m.b67 + m.b74 - m.b181 <= 0)

m.c623 = Constraint(expr= - m.b67 + m.b75 - m.b182 <= 0)

m.c624 = Constraint(expr= - m.b68 + m.b69 - m.b183 <= 0)

m.c625 = Constraint(expr= - m.b68 + m.b70 - m.b184 <= 0)

m.c626 = Constraint(expr= - m.b68 + m.b71 - m.b185 <= 0)

m.c627 = Constraint(expr= - m.b68 + m.b72 - m.b186 <= 0)

m.c628 = Constraint(expr= - m.b68 + m.b73 - m.b187 <= 0)

m.c629 = Constraint(expr= - m.b68 + m.b74 - m.b188 <= 0)

m.c630 = Constraint(expr= - m.b68 + m.b75 - m.b189 <= 0)

m.c631 = Constraint(expr= - m.b69 + m.b70 - m.b190 <= 0)

m.c632 = Constraint(expr= - m.b69 + m.b71 - m.b191 <= 0)

m.c633 = Constraint(expr= - m.b69 + m.b72 - m.b192 <= 0)

m.c634 = Constraint(expr= - m.b69 + m.b73 - m.b193 <= 0)

m.c635 = Constraint(expr= - m.b69 + m.b74 - m.b194 <= 0)

m.c636 = Constraint(expr= - m.b69 + m.b75 - m.b195 <= 0)

m.c637 = Constraint(expr= - m.b70 + m.b71 - m.b196 <= 0)

m.c638 = Constraint(expr= - m.b70 + m.b72 - m.b197 <= 0)

m.c639 = Constraint(expr= - m.b70 + m.b73 - m.b198 <= 0)

m.c640 = Constraint(expr= - m.b70 + m.b74 - m.b199 <= 0)

m.c641 = Constraint(expr= - m.b70 + m.b75 - m.b200 <= 0)

m.c642 = Constraint(expr= - m.b71 + m.b72 - m.b201 <= 0)

m.c643 = Constraint(expr= - m.b71 + m.b73 - m.b202 <= 0)

m.c644 = Constraint(expr= - m.b71 + m.b74 - m.b203 <= 0)

m.c645 = Constraint(expr= - m.b71 + m.b75 - m.b204 <= 0)

m.c646 = Constraint(expr= - m.b72 + m.b73 - m.b205 <= 0)

m.c647 = Constraint(expr= - m.b72 + m.b74 - m.b206 <= 0)

m.c648 = Constraint(expr= - m.b72 + m.b75 - m.b207 <= 0)

m.c649 = Constraint(expr= - m.b73 + m.b74 - m.b208 <= 0)

m.c650 = Constraint(expr= - m.b73 + m.b75 - m.b209 <= 0)

m.c651 = Constraint(expr= - m.b74 + m.b75 - m.b210 <= 0)

m.c652 = Constraint(expr= - m.b76 + m.b77 - m.b92 <= 0)

m.c653 = Constraint(expr= - m.b76 + m.b78 - m.b93 <= 0)

m.c654 = Constraint(expr= - m.b76 + m.b79 - m.b94 <= 0)

m.c655 = Constraint(expr= - m.b76 + m.b80 - m.b95 <= 0)

m.c656 = Constraint(expr= - m.b76 + m.b81 - m.b96 <= 0)

m.c657 = Constraint(expr= - m.b76 + m.b82 - m.b97 <= 0)

m.c658 = Constraint(expr= - m.b76 + m.b83 - m.b98 <= 0)

m.c659 = Constraint(expr= - m.b76 + m.b84 - m.b99 <= 0)

m.c660 = Constraint(expr= - m.b76 + m.b85 - m.b100 <= 0)

m.c661 = Constraint(expr= - m.b76 + m.b86 - m.b101 <= 0)

m.c662 = Constraint(expr= - m.b76 + m.b87 - m.b102 <= 0)

m.c663 = Constraint(expr= - m.b76 + m.b88 - m.b103 <= 0)

m.c664 = Constraint(expr= - m.b76 + m.b89 - m.b104 <= 0)

m.c665 = Constraint(expr= - m.b76 + m.b90 - m.b105 <= 0)

m.c666 = Constraint(expr= - m.b76 + m.b91 - m.b106 <= 0)

m.c667 = Constraint(expr= - m.b77 + m.b78 - m.b107 <= 0)

m.c668 = Constraint(expr= - m.b77 + m.b79 - m.b108 <= 0)

m.c669 = Constraint(expr= - m.b77 + m.b80 - m.b109 <= 0)

m.c670 = Constraint(expr= - m.b77 + m.b81 - m.b110 <= 0)

m.c671 = Constraint(expr= - m.b77 + m.b82 - m.b111 <= 0)

m.c672 = Constraint(expr= - m.b77 + m.b83 - m.b112 <= 0)

m.c673 = Constraint(expr= - m.b77 + m.b84 - m.b113 <= 0)

m.c674 = Constraint(expr= - m.b77 + m.b85 - m.b114 <= 0)

m.c675 = Constraint(expr= - m.b77 + m.b86 - m.b115 <= 0)

m.c676 = Constraint(expr= - m.b77 + m.b87 - m.b116 <= 0)

m.c677 = Constraint(expr= - m.b77 + m.b88 - m.b117 <= 0)

m.c678 = Constraint(expr= - m.b77 + m.b89 - m.b118 <= 0)

m.c679 = Constraint(expr= - m.b77 + m.b90 - m.b119 <= 0)

m.c680 = Constraint(expr= - m.b77 + m.b91 - m.b120 <= 0)

m.c681 = Constraint(expr= - m.b78 + m.b79 - m.b121 <= 0)

m.c682 = Constraint(expr= - m.b78 + m.b80 - m.b122 <= 0)

m.c683 = Constraint(expr= - m.b78 + m.b81 - m.b123 <= 0)

m.c684 = Constraint(expr= - m.b78 + m.b82 - m.b124 <= 0)

m.c685 = Constraint(expr= - m.b78 + m.b83 - m.b125 <= 0)

m.c686 = Constraint(expr= - m.b78 + m.b84 - m.b126 <= 0)

m.c687 = Constraint(expr= - m.b78 + m.b85 - m.b127 <= 0)

m.c688 = Constraint(expr= - m.b78 + m.b86 - m.b128 <= 0)

m.c689 = Constraint(expr= - m.b78 + m.b87 - m.b129 <= 0)

m.c690 = Constraint(expr= - m.b78 + m.b88 - m.b130 <= 0)

m.c691 = Constraint(expr= - m.b78 + m.b89 - m.b131 <= 0)

m.c692 = Constraint(expr= - m.b78 + m.b90 - m.b132 <= 0)

m.c693 = Constraint(expr= - m.b78 + m.b91 - m.b133 <= 0)

m.c694 = Constraint(expr= - m.b79 + m.b80 - m.b134 <= 0)

m.c695 = Constraint(expr= - m.b79 + m.b81 - m.b135 <= 0)

m.c696 = Constraint(expr= - m.b79 + m.b82 - m.b136 <= 0)

m.c697 = Constraint(expr= - m.b79 + m.b83 - m.b137 <= 0)

m.c698 = Constraint(expr= - m.b79 + m.b84 - m.b138 <= 0)

m.c699 = Constraint(expr= - m.b79 + m.b85 - m.b139 <= 0)

m.c700 = Constraint(expr= - m.b79 + m.b86 - m.b140 <= 0)

m.c701 = Constraint(expr= - m.b79 + m.b87 - m.b141 <= 0)

m.c702 = Constraint(expr= - m.b79 + m.b88 - m.b142 <= 0)

m.c703 = Constraint(expr= - m.b79 + m.b89 - m.b143 <= 0)

m.c704 = Constraint(expr= - m.b79 + m.b90 - m.b144 <= 0)

m.c705 = Constraint(expr= - m.b79 + m.b91 - m.b145 <= 0)

m.c706 = Constraint(expr= - m.b80 + m.b81 - m.b146 <= 0)

m.c707 = Constraint(expr= - m.b80 + m.b82 - m.b147 <= 0)

m.c708 = Constraint(expr= - m.b80 + m.b83 - m.b148 <= 0)

m.c709 = Constraint(expr= - m.b80 + m.b84 - m.b149 <= 0)

m.c710 = Constraint(expr= - m.b80 + m.b85 - m.b150 <= 0)

m.c711 = Constraint(expr= - m.b80 + m.b86 - m.b151 <= 0)

m.c712 = Constraint(expr= - m.b80 + m.b87 - m.b152 <= 0)

m.c713 = Constraint(expr= - m.b80 + m.b88 - m.b153 <= 0)

m.c714 = Constraint(expr= - m.b80 + m.b89 - m.b154 <= 0)

m.c715 = Constraint(expr= - m.b80 + m.b90 - m.b155 <= 0)

m.c716 = Constraint(expr= - m.b80 + m.b91 - m.b156 <= 0)

m.c717 = Constraint(expr= - m.b81 + m.b82 - m.b157 <= 0)

m.c718 = Constraint(expr= - m.b81 + m.b83 - m.b158 <= 0)

m.c719 = Constraint(expr= - m.b81 + m.b84 - m.b159 <= 0)

m.c720 = Constraint(expr= - m.b81 + m.b85 - m.b160 <= 0)

m.c721 = Constraint(expr= - m.b81 + m.b86 - m.b161 <= 0)

m.c722 = Constraint(expr= - m.b81 + m.b87 - m.b162 <= 0)

m.c723 = Constraint(expr= - m.b81 + m.b88 - m.b163 <= 0)

m.c724 = Constraint(expr= - m.b81 + m.b89 - m.b164 <= 0)

m.c725 = Constraint(expr= - m.b81 + m.b90 - m.b165 <= 0)

m.c726 = Constraint(expr= - m.b81 + m.b91 - m.b211 <= 0)

m.c727 = Constraint(expr= - m.b82 + m.b83 - m.b166 <= 0)

m.c728 = Constraint(expr= - m.b82 + m.b84 - m.b167 <= 0)

m.c729 = Constraint(expr= - m.b82 + m.b85 - m.b168 <= 0)

m.c730 = Constraint(expr= - m.b82 + m.b86 - m.b169 <= 0)

m.c731 = Constraint(expr= - m.b82 + m.b87 - m.b170 <= 0)

m.c732 = Constraint(expr= - m.b82 + m.b88 - m.b171 <= 0)

m.c733 = Constraint(expr= - m.b82 + m.b89 - m.b172 <= 0)

m.c734 = Constraint(expr= - m.b82 + m.b90 - m.b173 <= 0)

m.c735 = Constraint(expr= - m.b82 + m.b91 - m.b174 <= 0)

m.c736 = Constraint(expr= - m.b83 + m.b84 - m.b175 <= 0)

m.c737 = Constraint(expr= - m.b83 + m.b85 - m.b176 <= 0)

m.c738 = Constraint(expr= - m.b83 + m.b86 - m.b177 <= 0)

m.c739 = Constraint(expr= - m.b83 + m.b87 - m.b178 <= 0)

m.c740 = Constraint(expr= - m.b83 + m.b88 - m.b179 <= 0)

m.c741 = Constraint(expr= - m.b83 + m.b89 - m.b180 <= 0)

m.c742 = Constraint(expr= - m.b83 + m.b90 - m.b181 <= 0)

m.c743 = Constraint(expr= - m.b83 + m.b91 - m.b182 <= 0)

m.c744 = Constraint(expr= - m.b84 + m.b85 - m.b183 <= 0)

m.c745 = Constraint(expr= - m.b84 + m.b86 - m.b184 <= 0)

m.c746 = Constraint(expr= - m.b84 + m.b87 - m.b185 <= 0)

m.c747 = Constraint(expr= - m.b84 + m.b88 - m.b186 <= 0)

m.c748 = Constraint(expr= - m.b84 + m.b89 - m.b187 <= 0)

m.c749 = Constraint(expr= - m.b84 + m.b90 - m.b188 <= 0)

m.c750 = Constraint(expr= - m.b84 + m.b91 - m.b189 <= 0)

m.c751 = Constraint(expr= - m.b85 + m.b86 - m.b190 <= 0)

m.c752 = Constraint(expr= - m.b85 + m.b87 - m.b191 <= 0)

m.c753 = Constraint(expr= - m.b85 + m.b88 - m.b192 <= 0)

m.c754 = Constraint(expr= - m.b85 + m.b89 - m.b193 <= 0)

m.c755 = Constraint(expr= - m.b85 + m.b90 - m.b194 <= 0)

m.c756 = Constraint(expr= - m.b85 + m.b91 - m.b195 <= 0)

m.c757 = Constraint(expr= - m.b86 + m.b87 - m.b196 <= 0)

m.c758 = Constraint(expr= - m.b86 + m.b88 - m.b197 <= 0)

m.c759 = Constraint(expr= - m.b86 + m.b89 - m.b198 <= 0)

m.c760 = Constraint(expr= - m.b86 + m.b90 - m.b199 <= 0)

m.c761 = Constraint(expr= - m.b86 + m.b91 - m.b200 <= 0)

m.c762 = Constraint(expr= - m.b87 + m.b88 - m.b201 <= 0)

m.c763 = Constraint(expr= - m.b87 + m.b89 - m.b202 <= 0)

m.c764 = Constraint(expr= - m.b87 + m.b90 - m.b203 <= 0)

m.c765 = Constraint(expr= - m.b87 + m.b91 - m.b204 <= 0)

m.c766 = Constraint(expr= - m.b88 + m.b89 - m.b205 <= 0)

m.c767 = Constraint(expr= - m.b88 + m.b90 - m.b206 <= 0)

m.c768 = Constraint(expr= - m.b88 + m.b91 - m.b207 <= 0)

m.c769 = Constraint(expr= - m.b89 + m.b90 - m.b208 <= 0)

m.c770 = Constraint(expr= - m.b89 + m.b91 - m.b209 <= 0)

m.c771 = Constraint(expr= - m.b90 + m.b91 - m.b210 <= 0)

m.c772 = Constraint(expr= - m.b92 + m.b93 - m.b107 <= 0)

m.c773 = Constraint(expr= - m.b92 + m.b94 - m.b108 <= 0)

m.c774 = Constraint(expr= - m.b92 + m.b95 - m.b109 <= 0)

m.c775 = Constraint(expr= - m.b92 + m.b96 - m.b110 <= 0)

m.c776 = Constraint(expr= - m.b92 + m.b97 - m.b111 <= 0)

m.c777 = Constraint(expr= - m.b92 + m.b98 - m.b112 <= 0)

m.c778 = Constraint(expr= - m.b92 + m.b99 - m.b113 <= 0)

m.c779 = Constraint(expr= - m.b92 + m.b100 - m.b114 <= 0)

m.c780 = Constraint(expr= - m.b92 + m.b101 - m.b115 <= 0)

m.c781 = Constraint(expr= - m.b92 + m.b102 - m.b116 <= 0)

m.c782 = Constraint(expr= - m.b92 + m.b103 - m.b117 <= 0)

m.c783 = Constraint(expr= - m.b92 + m.b104 - m.b118 <= 0)

m.c784 = Constraint(expr= - m.b92 + m.b105 - m.b119 <= 0)

m.c785 = Constraint(expr= - m.b92 + m.b106 - m.b120 <= 0)

m.c786 = Constraint(expr= - m.b93 + m.b94 - m.b121 <= 0)

m.c787 = Constraint(expr= - m.b93 + m.b95 - m.b122 <= 0)

m.c788 = Constraint(expr= - m.b93 + m.b96 - m.b123 <= 0)

m.c789 = Constraint(expr= - m.b93 + m.b97 - m.b124 <= 0)

m.c790 = Constraint(expr= - m.b93 + m.b98 - m.b125 <= 0)

m.c791 = Constraint(expr= - m.b93 + m.b99 - m.b126 <= 0)

m.c792 = Constraint(expr= - m.b93 + m.b100 - m.b127 <= 0)

m.c793 = Constraint(expr= - m.b93 + m.b101 - m.b128 <= 0)

m.c794 = Constraint(expr= - m.b93 + m.b102 - m.b129 <= 0)

m.c795 = Constraint(expr= - m.b93 + m.b103 - m.b130 <= 0)

m.c796 = Constraint(expr= - m.b93 + m.b104 - m.b131 <= 0)

m.c797 = Constraint(expr= - m.b93 + m.b105 - m.b132 <= 0)

m.c798 = Constraint(expr= - m.b93 + m.b106 - m.b133 <= 0)

m.c799 = Constraint(expr= - m.b94 + m.b95 - m.b134 <= 0)

m.c800 = Constraint(expr= - m.b94 + m.b96 - m.b135 <= 0)

m.c801 = Constraint(expr= - m.b94 + m.b97 - m.b136 <= 0)

m.c802 = Constraint(expr= - m.b94 + m.b98 - m.b137 <= 0)

m.c803 = Constraint(expr= - m.b94 + m.b99 - m.b138 <= 0)

m.c804 = Constraint(expr= - m.b94 + m.b100 - m.b139 <= 0)

m.c805 = Constraint(expr= - m.b94 + m.b101 - m.b140 <= 0)

m.c806 = Constraint(expr= - m.b94 + m.b102 - m.b141 <= 0)

m.c807 = Constraint(expr= - m.b94 + m.b103 - m.b142 <= 0)

m.c808 = Constraint(expr= - m.b94 + m.b104 - m.b143 <= 0)

m.c809 = Constraint(expr= - m.b94 + m.b105 - m.b144 <= 0)

m.c810 = Constraint(expr= - m.b94 + m.b106 - m.b145 <= 0)

m.c811 = Constraint(expr= - m.b95 + m.b96 - m.b146 <= 0)

m.c812 = Constraint(expr= - m.b95 + m.b97 - m.b147 <= 0)

m.c813 = Constraint(expr= - m.b95 + m.b98 - m.b148 <= 0)

m.c814 = Constraint(expr= - m.b95 + m.b99 - m.b149 <= 0)

m.c815 = Constraint(expr= - m.b95 + m.b100 - m.b150 <= 0)

m.c816 = Constraint(expr= - m.b95 + m.b101 - m.b151 <= 0)

m.c817 = Constraint(expr= - m.b95 + m.b102 - m.b152 <= 0)

m.c818 = Constraint(expr= - m.b95 + m.b103 - m.b153 <= 0)

m.c819 = Constraint(expr= - m.b95 + m.b104 - m.b154 <= 0)

m.c820 = Constraint(expr= - m.b95 + m.b105 - m.b155 <= 0)

m.c821 = Constraint(expr= - m.b95 + m.b106 - m.b156 <= 0)

m.c822 = Constraint(expr= - m.b96 + m.b97 - m.b157 <= 0)

m.c823 = Constraint(expr= - m.b96 + m.b98 - m.b158 <= 0)

m.c824 = Constraint(expr= - m.b96 + m.b99 - m.b159 <= 0)

m.c825 = Constraint(expr= - m.b96 + m.b100 - m.b160 <= 0)

m.c826 = Constraint(expr= - m.b96 + m.b101 - m.b161 <= 0)

m.c827 = Constraint(expr= - m.b96 + m.b102 - m.b162 <= 0)

m.c828 = Constraint(expr= - m.b96 + m.b103 - m.b163 <= 0)

m.c829 = Constraint(expr= - m.b96 + m.b104 - m.b164 <= 0)

m.c830 = Constraint(expr= - m.b96 + m.b105 - m.b165 <= 0)

m.c831 = Constraint(expr= - m.b96 + m.b106 - m.b211 <= 0)

m.c832 = Constraint(expr= - m.b97 + m.b98 - m.b166 <= 0)

m.c833 = Constraint(expr= - m.b97 + m.b99 - m.b167 <= 0)

m.c834 = Constraint(expr= - m.b97 + m.b100 - m.b168 <= 0)

m.c835 = Constraint(expr= - m.b97 + m.b101 - m.b169 <= 0)

m.c836 = Constraint(expr= - m.b97 + m.b102 - m.b170 <= 0)

m.c837 = Constraint(expr= - m.b97 + m.b103 - m.b171 <= 0)

m.c838 = Constraint(expr= - m.b97 + m.b104 - m.b172 <= 0)

m.c839 = Constraint(expr= - m.b97 + m.b105 - m.b173 <= 0)

m.c840 = Constraint(expr= - m.b97 + m.b106 - m.b174 <= 0)

m.c841 = Constraint(expr= - m.b98 + m.b99 - m.b175 <= 0)

m.c842 = Constraint(expr= - m.b98 + m.b100 - m.b176 <= 0)

m.c843 = Constraint(expr= - m.b98 + m.b101 - m.b177 <= 0)

m.c844 = Constraint(expr= - m.b98 + m.b102 - m.b178 <= 0)

m.c845 = Constraint(expr= - m.b98 + m.b103 - m.b179 <= 0)

m.c846 = Constraint(expr= - m.b98 + m.b104 - m.b180 <= 0)

m.c847 = Constraint(expr= - m.b98 + m.b105 - m.b181 <= 0)

m.c848 = Constraint(expr= - m.b98 + m.b106 - m.b182 <= 0)

m.c849 = Constraint(expr= - m.b99 + m.b100 - m.b183 <= 0)

m.c850 = Constraint(expr= - m.b99 + m.b101 - m.b184 <= 0)

m.c851 = Constraint(expr= - m.b99 + m.b102 - m.b185 <= 0)

m.c852 = Constraint(expr= - m.b99 + m.b103 - m.b186 <= 0)

m.c853 = Constraint(expr= - m.b99 + m.b104 - m.b187 <= 0)

m.c854 = Constraint(expr= - m.b99 + m.b105 - m.b188 <= 0)

m.c855 = Constraint(expr= - m.b99 + m.b106 - m.b189 <= 0)

m.c856 = Constraint(expr= - m.b100 + m.b101 - m.b190 <= 0)

m.c857 = Constraint(expr= - m.b100 + m.b102 - m.b191 <= 0)

m.c858 = Constraint(expr= - m.b100 + m.b103 - m.b192 <= 0)

m.c859 = Constraint(expr= - m.b100 + m.b104 - m.b193 <= 0)

m.c860 = Constraint(expr= - m.b100 + m.b105 - m.b194 <= 0)

m.c861 = Constraint(expr= - m.b100 + m.b106 - m.b195 <= 0)

m.c862 = Constraint(expr= - m.b101 + m.b102 - m.b196 <= 0)

m.c863 = Constraint(expr= - m.b101 + m.b103 - m.b197 <= 0)

m.c864 = Constraint(expr= - m.b101 + m.b104 - m.b198 <= 0)

m.c865 = Constraint(expr= - m.b101 + m.b105 - m.b199 <= 0)

m.c866 = Constraint(expr= - m.b101 + m.b106 - m.b200 <= 0)

m.c867 = Constraint(expr= - m.b102 + m.b103 - m.b201 <= 0)

m.c868 = Constraint(expr= - m.b102 + m.b104 - m.b202 <= 0)

m.c869 = Constraint(expr= - m.b102 + m.b105 - m.b203 <= 0)

m.c870 = Constraint(expr= - m.b102 + m.b106 - m.b204 <= 0)

m.c871 = Constraint(expr= - m.b103 + m.b104 - m.b205 <= 0)

m.c872 = Constraint(expr= - m.b103 + m.b105 - m.b206 <= 0)

m.c873 = Constraint(expr= - m.b103 + m.b106 - m.b207 <= 0)

m.c874 = Constraint(expr= - m.b104 + m.b105 - m.b208 <= 0)

m.c875 = Constraint(expr= - m.b104 + m.b106 - m.b209 <= 0)

m.c876 = Constraint(expr= - m.b105 + m.b106 - m.b210 <= 0)

m.c877 = Constraint(expr= - m.b107 + m.b108 - m.b121 <= 0)

m.c878 = Constraint(expr= - m.b107 + m.b109 - m.b122 <= 0)

m.c879 = Constraint(expr= - m.b107 + m.b110 - m.b123 <= 0)

m.c880 = Constraint(expr= - m.b107 + m.b111 - m.b124 <= 0)

m.c881 = Constraint(expr= - m.b107 + m.b112 - m.b125 <= 0)

m.c882 = Constraint(expr= - m.b107 + m.b113 - m.b126 <= 0)

m.c883 = Constraint(expr= - m.b107 + m.b114 - m.b127 <= 0)

m.c884 = Constraint(expr= - m.b107 + m.b115 - m.b128 <= 0)

m.c885 = Constraint(expr= - m.b107 + m.b116 - m.b129 <= 0)

m.c886 = Constraint(expr= - m.b107 + m.b117 - m.b130 <= 0)

m.c887 = Constraint(expr= - m.b107 + m.b118 - m.b131 <= 0)

m.c888 = Constraint(expr= - m.b107 + m.b119 - m.b132 <= 0)

m.c889 = Constraint(expr= - m.b107 + m.b120 - m.b133 <= 0)

m.c890 = Constraint(expr= - m.b108 + m.b109 - m.b134 <= 0)

m.c891 = Constraint(expr= - m.b108 + m.b110 - m.b135 <= 0)

m.c892 = Constraint(expr= - m.b108 + m.b111 - m.b136 <= 0)

m.c893 = Constraint(expr= - m.b108 + m.b112 - m.b137 <= 0)

m.c894 = Constraint(expr= - m.b108 + m.b113 - m.b138 <= 0)

m.c895 = Constraint(expr= - m.b108 + m.b114 - m.b139 <= 0)

m.c896 = Constraint(expr= - m.b108 + m.b115 - m.b140 <= 0)

m.c897 = Constraint(expr= - m.b108 + m.b116 - m.b141 <= 0)

m.c898 = Constraint(expr= - m.b108 + m.b117 - m.b142 <= 0)

m.c899 = Constraint(expr= - m.b108 + m.b118 - m.b143 <= 0)

m.c900 = Constraint(expr= - m.b108 + m.b119 - m.b144 <= 0)

m.c901 = Constraint(expr= - m.b108 + m.b120 - m.b145 <= 0)

m.c902 = Constraint(expr= - m.b109 + m.b110 - m.b146 <= 0)

m.c903 = Constraint(expr= - m.b109 + m.b111 - m.b147 <= 0)

m.c904 = Constraint(expr= - m.b109 + m.b112 - m.b148 <= 0)

m.c905 = Constraint(expr= - m.b109 + m.b113 - m.b149 <= 0)

m.c906 = Constraint(expr= - m.b109 + m.b114 - m.b150 <= 0)

m.c907 = Constraint(expr= - m.b109 + m.b115 - m.b151 <= 0)

m.c908 = Constraint(expr= - m.b109 + m.b116 - m.b152 <= 0)

m.c909 = Constraint(expr= - m.b109 + m.b117 - m.b153 <= 0)

m.c910 = Constraint(expr= - m.b109 + m.b118 - m.b154 <= 0)

m.c911 = Constraint(expr= - m.b109 + m.b119 - m.b155 <= 0)

m.c912 = Constraint(expr= - m.b109 + m.b120 - m.b156 <= 0)

m.c913 = Constraint(expr= - m.b110 + m.b111 - m.b157 <= 0)

m.c914 = Constraint(expr= - m.b110 + m.b112 - m.b158 <= 0)

m.c915 = Constraint(expr= - m.b110 + m.b113 - m.b159 <= 0)

m.c916 = Constraint(expr= - m.b110 + m.b114 - m.b160 <= 0)

m.c917 = Constraint(expr= - m.b110 + m.b115 - m.b161 <= 0)

m.c918 = Constraint(expr= - m.b110 + m.b116 - m.b162 <= 0)

m.c919 = Constraint(expr= - m.b110 + m.b117 - m.b163 <= 0)

m.c920 = Constraint(expr= - m.b110 + m.b118 - m.b164 <= 0)

m.c921 = Constraint(expr= - m.b110 + m.b119 - m.b165 <= 0)

m.c922 = Constraint(expr= - m.b110 + m.b120 - m.b211 <= 0)

m.c923 = Constraint(expr= - m.b111 + m.b112 - m.b166 <= 0)

m.c924 = Constraint(expr= - m.b111 + m.b113 - m.b167 <= 0)

m.c925 = Constraint(expr= - m.b111 + m.b114 - m.b168 <= 0)

m.c926 = Constraint(expr= - m.b111 + m.b115 - m.b169 <= 0)

m.c927 = Constraint(expr= - m.b111 + m.b116 - m.b170 <= 0)

m.c928 = Constraint(expr= - m.b111 + m.b117 - m.b171 <= 0)

m.c929 = Constraint(expr= - m.b111 + m.b118 - m.b172 <= 0)

m.c930 = Constraint(expr= - m.b111 + m.b119 - m.b173 <= 0)

m.c931 = Constraint(expr= - m.b111 + m.b120 - m.b174 <= 0)

m.c932 = Constraint(expr= - m.b112 + m.b113 - m.b175 <= 0)

m.c933 = Constraint(expr= - m.b112 + m.b114 - m.b176 <= 0)

m.c934 = Constraint(expr= - m.b112 + m.b115 - m.b177 <= 0)

m.c935 = Constraint(expr= - m.b112 + m.b116 - m.b178 <= 0)

m.c936 = Constraint(expr= - m.b112 + m.b117 - m.b179 <= 0)

m.c937 = Constraint(expr= - m.b112 + m.b118 - m.b180 <= 0)

m.c938 = Constraint(expr= - m.b112 + m.b119 - m.b181 <= 0)

m.c939 = Constraint(expr= - m.b112 + m.b120 - m.b182 <= 0)

m.c940 = Constraint(expr= - m.b113 + m.b114 - m.b183 <= 0)

m.c941 = Constraint(expr= - m.b113 + m.b115 - m.b184 <= 0)

m.c942 = Constraint(expr= - m.b113 + m.b116 - m.b185 <= 0)

m.c943 = Constraint(expr= - m.b113 + m.b117 - m.b186 <= 0)

m.c944 = Constraint(expr= - m.b113 + m.b118 - m.b187 <= 0)

m.c945 = Constraint(expr= - m.b113 + m.b119 - m.b188 <= 0)

m.c946 = Constraint(expr= - m.b113 + m.b120 - m.b189 <= 0)

m.c947 = Constraint(expr= - m.b114 + m.b115 - m.b190 <= 0)

m.c948 = Constraint(expr= - m.b114 + m.b116 - m.b191 <= 0)

m.c949 = Constraint(expr= - m.b114 + m.b117 - m.b192 <= 0)

m.c950 = Constraint(expr= - m.b114 + m.b118 - m.b193 <= 0)

m.c951 = Constraint(expr= - m.b114 + m.b119 - m.b194 <= 0)

m.c952 = Constraint(expr= - m.b114 + m.b120 - m.b195 <= 0)

m.c953 = Constraint(expr= - m.b115 + m.b116 - m.b196 <= 0)

m.c954 = Constraint(expr= - m.b115 + m.b117 - m.b197 <= 0)

m.c955 = Constraint(expr= - m.b115 + m.b118 - m.b198 <= 0)

m.c956 = Constraint(expr= - m.b115 + m.b119 - m.b199 <= 0)

m.c957 = Constraint(expr= - m.b115 + m.b120 - m.b200 <= 0)

m.c958 = Constraint(expr= - m.b116 + m.b117 - m.b201 <= 0)

m.c959 = Constraint(expr= - m.b116 + m.b118 - m.b202 <= 0)

m.c960 = Constraint(expr= - m.b116 + m.b119 - m.b203 <= 0)

m.c961 = Constraint(expr= - m.b116 + m.b120 - m.b204 <= 0)

m.c962 = Constraint(expr= - m.b117 + m.b118 - m.b205 <= 0)

m.c963 = Constraint(expr= - m.b117 + m.b119 - m.b206 <= 0)

m.c964 = Constraint(expr= - m.b117 + m.b120 - m.b207 <= 0)

m.c965 = Constraint(expr= - m.b118 + m.b119 - m.b208 <= 0)

m.c966 = Constraint(expr= - m.b118 + m.b120 - m.b209 <= 0)

m.c967 = Constraint(expr= - m.b119 + m.b120 - m.b210 <= 0)

m.c968 = Constraint(expr= - m.b121 + m.b122 - m.b134 <= 0)

m.c969 = Constraint(expr= - m.b121 + m.b123 - m.b135 <= 0)

m.c970 = Constraint(expr= - m.b121 + m.b124 - m.b136 <= 0)

m.c971 = Constraint(expr= - m.b121 + m.b125 - m.b137 <= 0)

m.c972 = Constraint(expr= - m.b121 + m.b126 - m.b138 <= 0)

m.c973 = Constraint(expr= - m.b121 + m.b127 - m.b139 <= 0)

m.c974 = Constraint(expr= - m.b121 + m.b128 - m.b140 <= 0)

m.c975 = Constraint(expr= - m.b121 + m.b129 - m.b141 <= 0)

m.c976 = Constraint(expr= - m.b121 + m.b130 - m.b142 <= 0)

m.c977 = Constraint(expr= - m.b121 + m.b131 - m.b143 <= 0)

m.c978 = Constraint(expr= - m.b121 + m.b132 - m.b144 <= 0)

m.c979 = Constraint(expr= - m.b121 + m.b133 - m.b145 <= 0)

m.c980 = Constraint(expr= - m.b122 + m.b123 - m.b146 <= 0)

m.c981 = Constraint(expr= - m.b122 + m.b124 - m.b147 <= 0)

m.c982 = Constraint(expr= - m.b122 + m.b125 - m.b148 <= 0)

m.c983 = Constraint(expr= - m.b122 + m.b126 - m.b149 <= 0)

m.c984 = Constraint(expr= - m.b122 + m.b127 - m.b150 <= 0)

m.c985 = Constraint(expr= - m.b122 + m.b128 - m.b151 <= 0)

m.c986 = Constraint(expr= - m.b122 + m.b129 - m.b152 <= 0)

m.c987 = Constraint(expr= - m.b122 + m.b130 - m.b153 <= 0)

m.c988 = Constraint(expr= - m.b122 + m.b131 - m.b154 <= 0)

m.c989 = Constraint(expr= - m.b122 + m.b132 - m.b155 <= 0)

m.c990 = Constraint(expr= - m.b122 + m.b133 - m.b156 <= 0)

m.c991 = Constraint(expr= - m.b123 + m.b124 - m.b157 <= 0)

m.c992 = Constraint(expr= - m.b123 + m.b125 - m.b158 <= 0)

m.c993 = Constraint(expr= - m.b123 + m.b126 - m.b159 <= 0)

m.c994 = Constraint(expr= - m.b123 + m.b127 - m.b160 <= 0)

m.c995 = Constraint(expr= - m.b123 + m.b128 - m.b161 <= 0)

m.c996 = Constraint(expr= - m.b123 + m.b129 - m.b162 <= 0)

m.c997 = Constraint(expr= - m.b123 + m.b130 - m.b163 <= 0)

m.c998 = Constraint(expr= - m.b123 + m.b131 - m.b164 <= 0)

m.c999 = Constraint(expr= - m.b123 + m.b132 - m.b165 <= 0)

m.c1000 = Constraint(expr= - m.b123 + m.b133 - m.b211 <= 0)

m.c1001 = Constraint(expr= - m.b124 + m.b125 - m.b166 <= 0)

m.c1002 = Constraint(expr= - m.b124 + m.b126 - m.b167 <= 0)

m.c1003 = Constraint(expr= - m.b124 + m.b127 - m.b168 <= 0)

m.c1004 = Constraint(expr= - m.b124 + m.b128 - m.b169 <= 0)

m.c1005 = Constraint(expr= - m.b124 + m.b129 - m.b170 <= 0)

m.c1006 = Constraint(expr= - m.b124 + m.b130 - m.b171 <= 0)

m.c1007 = Constraint(expr= - m.b124 + m.b131 - m.b172 <= 0)

m.c1008 = Constraint(expr= - m.b124 + m.b132 - m.b173 <= 0)

m.c1009 = Constraint(expr= - m.b124 + m.b133 - m.b174 <= 0)

m.c1010 = Constraint(expr= - m.b125 + m.b126 - m.b175 <= 0)

m.c1011 = Constraint(expr= - m.b125 + m.b127 - m.b176 <= 0)

m.c1012 = Constraint(expr= - m.b125 + m.b128 - m.b177 <= 0)

m.c1013 = Constraint(expr= - m.b125 + m.b129 - m.b178 <= 0)

m.c1014 = Constraint(expr= - m.b125 + m.b130 - m.b179 <= 0)

m.c1015 = Constraint(expr= - m.b125 + m.b131 - m.b180 <= 0)

m.c1016 = Constraint(expr= - m.b125 + m.b132 - m.b181 <= 0)

m.c1017 = Constraint(expr= - m.b125 + m.b133 - m.b182 <= 0)

m.c1018 = Constraint(expr= - m.b126 + m.b127 - m.b183 <= 0)

m.c1019 = Constraint(expr= - m.b126 + m.b128 - m.b184 <= 0)

m.c1020 = Constraint(expr= - m.b126 + m.b129 - m.b185 <= 0)

m.c1021 = Constraint(expr= - m.b126 + m.b130 - m.b186 <= 0)

m.c1022 = Constraint(expr= - m.b126 + m.b131 - m.b187 <= 0)

m.c1023 = Constraint(expr= - m.b126 + m.b132 - m.b188 <= 0)

m.c1024 = Constraint(expr= - m.b126 + m.b133 - m.b189 <= 0)

m.c1025 = Constraint(expr= - m.b127 + m.b128 - m.b190 <= 0)

m.c1026 = Constraint(expr= - m.b127 + m.b129 - m.b191 <= 0)

m.c1027 = Constraint(expr= - m.b127 + m.b130 - m.b192 <= 0)

m.c1028 = Constraint(expr= - m.b127 + m.b131 - m.b193 <= 0)

m.c1029 = Constraint(expr= - m.b127 + m.b132 - m.b194 <= 0)

m.c1030 = Constraint(expr= - m.b127 + m.b133 - m.b195 <= 0)

m.c1031 = Constraint(expr= - m.b128 + m.b129 - m.b196 <= 0)

m.c1032 = Constraint(expr= - m.b128 + m.b130 - m.b197 <= 0)

m.c1033 = Constraint(expr= - m.b128 + m.b131 - m.b198 <= 0)

m.c1034 = Constraint(expr= - m.b128 + m.b132 - m.b199 <= 0)

m.c1035 = Constraint(expr= - m.b128 + m.b133 - m.b200 <= 0)

m.c1036 = Constraint(expr= - m.b129 + m.b130 - m.b201 <= 0)

m.c1037 = Constraint(expr= - m.b129 + m.b131 - m.b202 <= 0)

m.c1038 = Constraint(expr= - m.b129 + m.b132 - m.b203 <= 0)

m.c1039 = Constraint(expr= - m.b129 + m.b133 - m.b204 <= 0)

m.c1040 = Constraint(expr= - m.b130 + m.b131 - m.b205 <= 0)

m.c1041 = Constraint(expr= - m.b130 + m.b132 - m.b206 <= 0)

m.c1042 = Constraint(expr= - m.b130 + m.b133 - m.b207 <= 0)

m.c1043 = Constraint(expr= - m.b131 + m.b132 - m.b208 <= 0)

m.c1044 = Constraint(expr= - m.b131 + m.b133 - m.b209 <= 0)

m.c1045 = Constraint(expr= - m.b132 + m.b133 - m.b210 <= 0)

m.c1046 = Constraint(expr= - m.b134 + m.b135 - m.b146 <= 0)

m.c1047 = Constraint(expr= - m.b134 + m.b136 - m.b147 <= 0)

m.c1048 = Constraint(expr= - m.b134 + m.b137 - m.b148 <= 0)

m.c1049 = Constraint(expr= - m.b134 + m.b138 - m.b149 <= 0)

m.c1050 = Constraint(expr= - m.b134 + m.b139 - m.b150 <= 0)

m.c1051 = Constraint(expr= - m.b134 + m.b140 - m.b151 <= 0)

m.c1052 = Constraint(expr= - m.b134 + m.b141 - m.b152 <= 0)

m.c1053 = Constraint(expr= - m.b134 + m.b142 - m.b153 <= 0)

m.c1054 = Constraint(expr= - m.b134 + m.b143 - m.b154 <= 0)

m.c1055 = Constraint(expr= - m.b134 + m.b144 - m.b155 <= 0)

m.c1056 = Constraint(expr= - m.b134 + m.b145 - m.b156 <= 0)

m.c1057 = Constraint(expr= - m.b135 + m.b136 - m.b157 <= 0)

m.c1058 = Constraint(expr= - m.b135 + m.b137 - m.b158 <= 0)

m.c1059 = Constraint(expr= - m.b135 + m.b138 - m.b159 <= 0)

m.c1060 = Constraint(expr= - m.b135 + m.b139 - m.b160 <= 0)

m.c1061 = Constraint(expr= - m.b135 + m.b140 - m.b161 <= 0)

m.c1062 = Constraint(expr= - m.b135 + m.b141 - m.b162 <= 0)

m.c1063 = Constraint(expr= - m.b135 + m.b142 - m.b163 <= 0)

m.c1064 = Constraint(expr= - m.b135 + m.b143 - m.b164 <= 0)

m.c1065 = Constraint(expr= - m.b135 + m.b144 - m.b165 <= 0)

m.c1066 = Constraint(expr= - m.b135 + m.b145 - m.b211 <= 0)

m.c1067 = Constraint(expr= - m.b136 + m.b137 - m.b166 <= 0)

m.c1068 = Constraint(expr= - m.b136 + m.b138 - m.b167 <= 0)

m.c1069 = Constraint(expr= - m.b136 + m.b139 - m.b168 <= 0)

m.c1070 = Constraint(expr= - m.b136 + m.b140 - m.b169 <= 0)

m.c1071 = Constraint(expr= - m.b136 + m.b141 - m.b170 <= 0)

m.c1072 = Constraint(expr= - m.b136 + m.b142 - m.b171 <= 0)

m.c1073 = Constraint(expr= - m.b136 + m.b143 - m.b172 <= 0)

m.c1074 = Constraint(expr= - m.b136 + m.b144 - m.b173 <= 0)

m.c1075 = Constraint(expr= - m.b136 + m.b145 - m.b174 <= 0)

m.c1076 = Constraint(expr= - m.b137 + m.b138 - m.b175 <= 0)

m.c1077 = Constraint(expr= - m.b137 + m.b139 - m.b176 <= 0)

m.c1078 = Constraint(expr= - m.b137 + m.b140 - m.b177 <= 0)

m.c1079 = Constraint(expr= - m.b137 + m.b141 - m.b178 <= 0)

m.c1080 = Constraint(expr= - m.b137 + m.b142 - m.b179 <= 0)

m.c1081 = Constraint(expr= - m.b137 + m.b143 - m.b180 <= 0)

m.c1082 = Constraint(expr= - m.b137 + m.b144 - m.b181 <= 0)

m.c1083 = Constraint(expr= - m.b137 + m.b145 - m.b182 <= 0)

m.c1084 = Constraint(expr= - m.b138 + m.b139 - m.b183 <= 0)

m.c1085 = Constraint(expr= - m.b138 + m.b140 - m.b184 <= 0)

m.c1086 = Constraint(expr= - m.b138 + m.b141 - m.b185 <= 0)

m.c1087 = Constraint(expr= - m.b138 + m.b142 - m.b186 <= 0)

m.c1088 = Constraint(expr= - m.b138 + m.b143 - m.b187 <= 0)

m.c1089 = Constraint(expr= - m.b138 + m.b144 - m.b188 <= 0)

m.c1090 = Constraint(expr= - m.b138 + m.b145 - m.b189 <= 0)

m.c1091 = Constraint(expr= - m.b139 + m.b140 - m.b190 <= 0)

m.c1092 = Constraint(expr= - m.b139 + m.b141 - m.b191 <= 0)

m.c1093 = Constraint(expr= - m.b139 + m.b142 - m.b192 <= 0)

m.c1094 = Constraint(expr= - m.b139 + m.b143 - m.b193 <= 0)

m.c1095 = Constraint(expr= - m.b139 + m.b144 - m.b194 <= 0)

m.c1096 = Constraint(expr= - m.b139 + m.b145 - m.b195 <= 0)

m.c1097 = Constraint(expr= - m.b140 + m.b141 - m.b196 <= 0)

m.c1098 = Constraint(expr= - m.b140 + m.b142 - m.b197 <= 0)

m.c1099 = Constraint(expr= - m.b140 + m.b143 - m.b198 <= 0)

m.c1100 = Constraint(expr= - m.b140 + m.b144 - m.b199 <= 0)

m.c1101 = Constraint(expr= - m.b140 + m.b145 - m.b200 <= 0)

m.c1102 = Constraint(expr= - m.b141 + m.b142 - m.b201 <= 0)

m.c1103 = Constraint(expr= - m.b141 + m.b143 - m.b202 <= 0)

m.c1104 = Constraint(expr= - m.b141 + m.b144 - m.b203 <= 0)

m.c1105 = Constraint(expr= - m.b141 + m.b145 - m.b204 <= 0)

m.c1106 = Constraint(expr= - m.b142 + m.b143 - m.b205 <= 0)

m.c1107 = Constraint(expr= - m.b142 + m.b144 - m.b206 <= 0)

m.c1108 = Constraint(expr= - m.b142 + m.b145 - m.b207 <= 0)

m.c1109 = Constraint(expr= - m.b143 + m.b144 - m.b208 <= 0)

m.c1110 = Constraint(expr= - m.b143 + m.b145 - m.b209 <= 0)

m.c1111 = Constraint(expr= - m.b144 + m.b145 - m.b210 <= 0)

m.c1112 = Constraint(expr= - m.b146 + m.b147 - m.b157 <= 0)

m.c1113 = Constraint(expr= - m.b146 + m.b148 - m.b158 <= 0)

m.c1114 = Constraint(expr= - m.b146 + m.b149 - m.b159 <= 0)

m.c1115 = Constraint(expr= - m.b146 + m.b150 - m.b160 <= 0)

m.c1116 = Constraint(expr= - m.b146 + m.b151 - m.b161 <= 0)

m.c1117 = Constraint(expr= - m.b146 + m.b152 - m.b162 <= 0)

m.c1118 = Constraint(expr= - m.b146 + m.b153 - m.b163 <= 0)

m.c1119 = Constraint(expr= - m.b146 + m.b154 - m.b164 <= 0)

m.c1120 = Constraint(expr= - m.b146 + m.b155 - m.b165 <= 0)

m.c1121 = Constraint(expr= - m.b146 + m.b156 - m.b211 <= 0)

m.c1122 = Constraint(expr= - m.b147 + m.b148 - m.b166 <= 0)

m.c1123 = Constraint(expr= - m.b147 + m.b149 - m.b167 <= 0)

m.c1124 = Constraint(expr= - m.b147 + m.b150 - m.b168 <= 0)

m.c1125 = Constraint(expr= - m.b147 + m.b151 - m.b169 <= 0)

m.c1126 = Constraint(expr= - m.b147 + m.b152 - m.b170 <= 0)

m.c1127 = Constraint(expr= - m.b147 + m.b153 - m.b171 <= 0)

m.c1128 = Constraint(expr= - m.b147 + m.b154 - m.b172 <= 0)

m.c1129 = Constraint(expr= - m.b147 + m.b155 - m.b173 <= 0)

m.c1130 = Constraint(expr= - m.b147 + m.b156 - m.b174 <= 0)

m.c1131 = Constraint(expr= - m.b148 + m.b149 - m.b175 <= 0)

m.c1132 = Constraint(expr= - m.b148 + m.b150 - m.b176 <= 0)

m.c1133 = Constraint(expr= - m.b148 + m.b151 - m.b177 <= 0)

m.c1134 = Constraint(expr= - m.b148 + m.b152 - m.b178 <= 0)

m.c1135 = Constraint(expr= - m.b148 + m.b153 - m.b179 <= 0)

m.c1136 = Constraint(expr= - m.b148 + m.b154 - m.b180 <= 0)

m.c1137 = Constraint(expr= - m.b148 + m.b155 - m.b181 <= 0)

m.c1138 = Constraint(expr= - m.b148 + m.b156 - m.b182 <= 0)

m.c1139 = Constraint(expr= - m.b149 + m.b150 - m.b183 <= 0)

m.c1140 = Constraint(expr= - m.b149 + m.b151 - m.b184 <= 0)

m.c1141 = Constraint(expr= - m.b149 + m.b152 - m.b185 <= 0)

m.c1142 = Constraint(expr= - m.b149 + m.b153 - m.b186 <= 0)

m.c1143 = Constraint(expr= - m.b149 + m.b154 - m.b187 <= 0)

m.c1144 = Constraint(expr= - m.b149 + m.b155 - m.b188 <= 0)

m.c1145 = Constraint(expr= - m.b149 + m.b156 - m.b189 <= 0)

m.c1146 = Constraint(expr= - m.b150 + m.b151 - m.b190 <= 0)

m.c1147 = Constraint(expr= - m.b150 + m.b152 - m.b191 <= 0)

m.c1148 = Constraint(expr= - m.b150 + m.b153 - m.b192 <= 0)

m.c1149 = Constraint(expr= - m.b150 + m.b154 - m.b193 <= 0)

m.c1150 = Constraint(expr= - m.b150 + m.b155 - m.b194 <= 0)

m.c1151 = Constraint(expr= - m.b150 + m.b156 - m.b195 <= 0)

m.c1152 = Constraint(expr= - m.b151 + m.b152 - m.b196 <= 0)

m.c1153 = Constraint(expr= - m.b151 + m.b153 - m.b197 <= 0)

m.c1154 = Constraint(expr= - m.b151 + m.b154 - m.b198 <= 0)

m.c1155 = Constraint(expr= - m.b151 + m.b155 - m.b199 <= 0)

m.c1156 = Constraint(expr= - m.b151 + m.b156 - m.b200 <= 0)

m.c1157 = Constraint(expr= - m.b152 + m.b153 - m.b201 <= 0)

m.c1158 = Constraint(expr= - m.b152 + m.b154 - m.b202 <= 0)

m.c1159 = Constraint(expr= - m.b152 + m.b155 - m.b203 <= 0)

m.c1160 = Constraint(expr= - m.b152 + m.b156 - m.b204 <= 0)

m.c1161 = Constraint(expr= - m.b153 + m.b154 - m.b205 <= 0)

m.c1162 = Constraint(expr= - m.b153 + m.b155 - m.b206 <= 0)

m.c1163 = Constraint(expr= - m.b153 + m.b156 - m.b207 <= 0)

m.c1164 = Constraint(expr= - m.b154 + m.b155 - m.b208 <= 0)

m.c1165 = Constraint(expr= - m.b154 + m.b156 - m.b209 <= 0)

m.c1166 = Constraint(expr= - m.b155 + m.b156 - m.b210 <= 0)

m.c1167 = Constraint(expr= - m.b157 + m.b158 - m.b166 <= 0)

m.c1168 = Constraint(expr= - m.b157 + m.b159 - m.b167 <= 0)

m.c1169 = Constraint(expr= - m.b157 + m.b160 - m.b168 <= 0)

m.c1170 = Constraint(expr= - m.b157 + m.b161 - m.b169 <= 0)

m.c1171 = Constraint(expr= - m.b157 + m.b162 - m.b170 <= 0)

m.c1172 = Constraint(expr= - m.b157 + m.b163 - m.b171 <= 0)

m.c1173 = Constraint(expr= - m.b157 + m.b164 - m.b172 <= 0)

m.c1174 = Constraint(expr= - m.b157 + m.b165 - m.b173 <= 0)

m.c1175 = Constraint(expr= - m.b157 - m.b174 + m.b211 <= 0)

m.c1176 = Constraint(expr= - m.b158 + m.b159 - m.b175 <= 0)

m.c1177 = Constraint(expr= - m.b158 + m.b160 - m.b176 <= 0)

m.c1178 = Constraint(expr= - m.b158 + m.b161 - m.b177 <= 0)

m.c1179 = Constraint(expr= - m.b158 + m.b162 - m.b178 <= 0)

m.c1180 = Constraint(expr= - m.b158 + m.b163 - m.b179 <= 0)

m.c1181 = Constraint(expr= - m.b158 + m.b164 - m.b180 <= 0)

m.c1182 = Constraint(expr= - m.b158 + m.b165 - m.b181 <= 0)

m.c1183 = Constraint(expr= - m.b158 - m.b182 + m.b211 <= 0)

m.c1184 = Constraint(expr= - m.b159 + m.b160 - m.b183 <= 0)

m.c1185 = Constraint(expr= - m.b159 + m.b161 - m.b184 <= 0)

m.c1186 = Constraint(expr= - m.b159 + m.b162 - m.b185 <= 0)

m.c1187 = Constraint(expr= - m.b159 + m.b163 - m.b186 <= 0)

m.c1188 = Constraint(expr= - m.b159 + m.b164 - m.b187 <= 0)

m.c1189 = Constraint(expr= - m.b159 + m.b165 - m.b188 <= 0)

m.c1190 = Constraint(expr= - m.b159 - m.b189 + m.b211 <= 0)

m.c1191 = Constraint(expr= - m.b160 + m.b161 - m.b190 <= 0)

m.c1192 = Constraint(expr= - m.b160 + m.b162 - m.b191 <= 0)

m.c1193 = Constraint(expr= - m.b160 + m.b163 - m.b192 <= 0)

m.c1194 = Constraint(expr= - m.b160 + m.b164 - m.b193 <= 0)

m.c1195 = Constraint(expr= - m.b160 + m.b165 - m.b194 <= 0)

m.c1196 = Constraint(expr= - m.b160 - m.b195 + m.b211 <= 0)

m.c1197 = Constraint(expr= - m.b161 + m.b162 - m.b196 <= 0)

m.c1198 = Constraint(expr= - m.b161 + m.b163 - m.b197 <= 0)

m.c1199 = Constraint(expr= - m.b161 + m.b164 - m.b198 <= 0)

m.c1200 = Constraint(expr= - m.b161 + m.b165 - m.b199 <= 0)

m.c1201 = Constraint(expr= - m.b161 - m.b200 + m.b211 <= 0)

m.c1202 = Constraint(expr= - m.b162 + m.b163 - m.b201 <= 0)

m.c1203 = Constraint(expr= - m.b162 + m.b164 - m.b202 <= 0)

m.c1204 = Constraint(expr= - m.b162 + m.b165 - m.b203 <= 0)

m.c1205 = Constraint(expr= - m.b162 - m.b204 + m.b211 <= 0)

m.c1206 = Constraint(expr= - m.b163 + m.b164 - m.b205 <= 0)

m.c1207 = Constraint(expr= - m.b163 + m.b165 - m.b206 <= 0)

m.c1208 = Constraint(expr= - m.b163 - m.b207 + m.b211 <= 0)

m.c1209 = Constraint(expr= - m.b164 + m.b165 - m.b208 <= 0)

m.c1210 = Constraint(expr= - m.b164 - m.b209 + m.b211 <= 0)

m.c1211 = Constraint(expr= - m.b165 - m.b210 + m.b211 <= 0)

m.c1212 = Constraint(expr= - m.b166 + m.b167 - m.b175 <= 0)

m.c1213 = Constraint(expr= - m.b166 + m.b168 - m.b176 <= 0)

m.c1214 = Constraint(expr= - m.b166 + m.b169 - m.b177 <= 0)

m.c1215 = Constraint(expr= - m.b166 + m.b170 - m.b178 <= 0)

m.c1216 = Constraint(expr= - m.b166 + m.b171 - m.b179 <= 0)

m.c1217 = Constraint(expr= - m.b166 + m.b172 - m.b180 <= 0)

m.c1218 = Constraint(expr= - m.b166 + m.b173 - m.b181 <= 0)

m.c1219 = Constraint(expr= - m.b166 + m.b174 - m.b182 <= 0)

m.c1220 = Constraint(expr= - m.b167 + m.b168 - m.b183 <= 0)

m.c1221 = Constraint(expr= - m.b167 + m.b169 - m.b184 <= 0)

m.c1222 = Constraint(expr= - m.b167 + m.b170 - m.b185 <= 0)

m.c1223 = Constraint(expr= - m.b167 + m.b171 - m.b186 <= 0)

m.c1224 = Constraint(expr= - m.b167 + m.b172 - m.b187 <= 0)

m.c1225 = Constraint(expr= - m.b167 + m.b173 - m.b188 <= 0)

m.c1226 = Constraint(expr= - m.b167 + m.b174 - m.b189 <= 0)

m.c1227 = Constraint(expr= - m.b168 + m.b169 - m.b190 <= 0)

m.c1228 = Constraint(expr= - m.b168 + m.b170 - m.b191 <= 0)

m.c1229 = Constraint(expr= - m.b168 + m.b171 - m.b192 <= 0)

m.c1230 = Constraint(expr= - m.b168 + m.b172 - m.b193 <= 0)

m.c1231 = Constraint(expr= - m.b168 + m.b173 - m.b194 <= 0)

m.c1232 = Constraint(expr= - m.b168 + m.b174 - m.b195 <= 0)

m.c1233 = Constraint(expr= - m.b169 + m.b170 - m.b196 <= 0)

m.c1234 = Constraint(expr= - m.b169 + m.b171 - m.b197 <= 0)

m.c1235 = Constraint(expr= - m.b169 + m.b172 - m.b198 <= 0)

m.c1236 = Constraint(expr= - m.b169 + m.b173 - m.b199 <= 0)

m.c1237 = Constraint(expr= - m.b169 + m.b174 - m.b200 <= 0)

m.c1238 = Constraint(expr= - m.b170 + m.b171 - m.b201 <= 0)

m.c1239 = Constraint(expr= - m.b170 + m.b172 - m.b202 <= 0)

m.c1240 = Constraint(expr= - m.b170 + m.b173 - m.b203 <= 0)

m.c1241 = Constraint(expr= - m.b170 + m.b174 - m.b204 <= 0)

m.c1242 = Constraint(expr= - m.b171 + m.b172 - m.b205 <= 0)

m.c1243 = Constraint(expr= - m.b171 + m.b173 - m.b206 <= 0)

m.c1244 = Constraint(expr= - m.b171 + m.b174 - m.b207 <= 0)

m.c1245 = Constraint(expr= - m.b172 + m.b173 - m.b208 <= 0)

m.c1246 = Constraint(expr= - m.b172 + m.b174 - m.b209 <= 0)

m.c1247 = Constraint(expr= - m.b173 + m.b174 - m.b210 <= 0)

m.c1248 = Constraint(expr= - m.b175 + m.b176 - m.b183 <= 0)

m.c1249 = Constraint(expr= - m.b175 + m.b177 - m.b184 <= 0)

m.c1250 = Constraint(expr= - m.b175 + m.b178 - m.b185 <= 0)

m.c1251 = Constraint(expr= - m.b175 + m.b179 - m.b186 <= 0)

m.c1252 = Constraint(expr= - m.b175 + m.b180 - m.b187 <= 0)

m.c1253 = Constraint(expr= - m.b175 + m.b181 - m.b188 <= 0)

m.c1254 = Constraint(expr= - m.b175 + m.b182 - m.b189 <= 0)

m.c1255 = Constraint(expr= - m.b176 + m.b177 - m.b190 <= 0)

m.c1256 = Constraint(expr= - m.b176 + m.b178 - m.b191 <= 0)

m.c1257 = Constraint(expr= - m.b176 + m.b179 - m.b192 <= 0)

m.c1258 = Constraint(expr= - m.b176 + m.b180 - m.b193 <= 0)

m.c1259 = Constraint(expr= - m.b176 + m.b181 - m.b194 <= 0)

m.c1260 = Constraint(expr= - m.b176 + m.b182 - m.b195 <= 0)

m.c1261 = Constraint(expr= - m.b177 + m.b178 - m.b196 <= 0)

m.c1262 = Constraint(expr= - m.b177 + m.b179 - m.b197 <= 0)

m.c1263 = Constraint(expr= - m.b177 + m.b180 - m.b198 <= 0)

m.c1264 = Constraint(expr= - m.b177 + m.b181 - m.b199 <= 0)

m.c1265 = Constraint(expr= - m.b177 + m.b182 - m.b200 <= 0)

m.c1266 = Constraint(expr= - m.b178 + m.b179 - m.b201 <= 0)

m.c1267 = Constraint(expr= - m.b178 + m.b180 - m.b202 <= 0)

m.c1268 = Constraint(expr= - m.b178 + m.b181 - m.b203 <= 0)

m.c1269 = Constraint(expr= - m.b178 + m.b182 - m.b204 <= 0)

m.c1270 = Constraint(expr= - m.b179 + m.b180 - m.b205 <= 0)

m.c1271 = Constraint(expr= - m.b179 + m.b181 - m.b206 <= 0)

m.c1272 = Constraint(expr= - m.b179 + m.b182 - m.b207 <= 0)

m.c1273 = Constraint(expr= - m.b180 + m.b181 - m.b208 <= 0)

m.c1274 = Constraint(expr= - m.b180 + m.b182 - m.b209 <= 0)

m.c1275 = Constraint(expr= - m.b181 + m.b182 - m.b210 <= 0)

m.c1276 = Constraint(expr= - m.b183 + m.b184 - m.b190 <= 0)

m.c1277 = Constraint(expr= - m.b183 + m.b185 - m.b191 <= 0)

m.c1278 = Constraint(expr= - m.b183 + m.b186 - m.b192 <= 0)

m.c1279 = Constraint(expr= - m.b183 + m.b187 - m.b193 <= 0)

m.c1280 = Constraint(expr= - m.b183 + m.b188 - m.b194 <= 0)

m.c1281 = Constraint(expr= - m.b183 + m.b189 - m.b195 <= 0)

m.c1282 = Constraint(expr= - m.b184 + m.b185 - m.b196 <= 0)

m.c1283 = Constraint(expr= - m.b184 + m.b186 - m.b197 <= 0)

m.c1284 = Constraint(expr= - m.b184 + m.b187 - m.b198 <= 0)

m.c1285 = Constraint(expr= - m.b184 + m.b188 - m.b199 <= 0)

m.c1286 = Constraint(expr= - m.b184 + m.b189 - m.b200 <= 0)

m.c1287 = Constraint(expr= - m.b185 + m.b186 - m.b201 <= 0)

m.c1288 = Constraint(expr= - m.b185 + m.b187 - m.b202 <= 0)

m.c1289 = Constraint(expr= - m.b185 + m.b188 - m.b203 <= 0)

m.c1290 = Constraint(expr= - m.b185 + m.b189 - m.b204 <= 0)

m.c1291 = Constraint(expr= - m.b186 + m.b187 - m.b205 <= 0)

m.c1292 = Constraint(expr= - m.b186 + m.b188 - m.b206 <= 0)

m.c1293 = Constraint(expr= - m.b186 + m.b189 - m.b207 <= 0)

m.c1294 = Constraint(expr= - m.b187 + m.b188 - m.b208 <= 0)

m.c1295 = Constraint(expr= - m.b187 + m.b189 - m.b209 <= 0)

m.c1296 = Constraint(expr= - m.b188 + m.b189 - m.b210 <= 0)

m.c1297 = Constraint(expr= - m.b190 + m.b191 - m.b196 <= 0)

m.c1298 = Constraint(expr= - m.b190 + m.b192 - m.b197 <= 0)

m.c1299 = Constraint(expr= - m.b190 + m.b193 - m.b198 <= 0)

m.c1300 = Constraint(expr= - m.b190 + m.b194 - m.b199 <= 0)

m.c1301 = Constraint(expr= - m.b190 + m.b195 - m.b200 <= 0)

m.c1302 = Constraint(expr= - m.b191 + m.b192 - m.b201 <= 0)

m.c1303 = Constraint(expr= - m.b191 + m.b193 - m.b202 <= 0)

m.c1304 = Constraint(expr= - m.b191 + m.b194 - m.b203 <= 0)

m.c1305 = Constraint(expr= - m.b191 + m.b195 - m.b204 <= 0)

m.c1306 = Constraint(expr= - m.b192 + m.b193 - m.b205 <= 0)

m.c1307 = Constraint(expr= - m.b192 + m.b194 - m.b206 <= 0)

m.c1308 = Constraint(expr= - m.b192 + m.b195 - m.b207 <= 0)

m.c1309 = Constraint(expr= - m.b193 + m.b194 - m.b208 <= 0)

m.c1310 = Constraint(expr= - m.b193 + m.b195 - m.b209 <= 0)

m.c1311 = Constraint(expr= - m.b194 + m.b195 - m.b210 <= 0)

m.c1312 = Constraint(expr= - m.b196 + m.b197 - m.b201 <= 0)

m.c1313 = Constraint(expr= - m.b196 + m.b198 - m.b202 <= 0)

m.c1314 = Constraint(expr= - m.b196 + m.b199 - m.b203 <= 0)

m.c1315 = Constraint(expr= - m.b196 + m.b200 - m.b204 <= 0)

m.c1316 = Constraint(expr= - m.b197 + m.b198 - m.b205 <= 0)

m.c1317 = Constraint(expr= - m.b197 + m.b199 - m.b206 <= 0)

m.c1318 = Constraint(expr= - m.b197 + m.b200 - m.b207 <= 0)

m.c1319 = Constraint(expr= - m.b198 + m.b199 - m.b208 <= 0)

m.c1320 = Constraint(expr= - m.b198 + m.b200 - m.b209 <= 0)

m.c1321 = Constraint(expr= - m.b199 + m.b200 - m.b210 <= 0)

m.c1322 = Constraint(expr= - m.b201 + m.b202 - m.b205 <= 0)

m.c1323 = Constraint(expr= - m.b201 + m.b203 - m.b206 <= 0)

m.c1324 = Constraint(expr= - m.b201 + m.b204 - m.b207 <= 0)

m.c1325 = Constraint(expr= - m.b202 + m.b203 - m.b208 <= 0)

m.c1326 = Constraint(expr= - m.b202 + m.b204 - m.b209 <= 0)

m.c1327 = Constraint(expr= - m.b203 + m.b204 - m.b210 <= 0)

m.c1328 = Constraint(expr= - m.b205 + m.b206 - m.b208 <= 0)

m.c1329 = Constraint(expr= - m.b205 + m.b207 - m.b209 <= 0)

m.c1330 = Constraint(expr= - m.b206 + m.b207 - m.b210 <= 0)

m.c1331 = Constraint(expr= - m.b208 + m.b209 - m.b210 <= 0)

m.c1332 = Constraint(expr=   m.b2 - m.b3 - m.b22 <= 0)

m.c1333 = Constraint(expr=   m.b2 - m.b4 - m.b23 <= 0)

m.c1334 = Constraint(expr=   m.b2 - m.b5 - m.b24 <= 0)

m.c1335 = Constraint(expr=   m.b2 - m.b6 - m.b25 <= 0)

m.c1336 = Constraint(expr=   m.b2 - m.b7 - m.b26 <= 0)

m.c1337 = Constraint(expr=   m.b2 - m.b8 - m.b27 <= 0)

m.c1338 = Constraint(expr=   m.b2 - m.b9 - m.b28 <= 0)

m.c1339 = Constraint(expr=   m.b2 - m.b10 - m.b29 <= 0)

m.c1340 = Constraint(expr=   m.b2 - m.b11 - m.b30 <= 0)

m.c1341 = Constraint(expr=   m.b2 - m.b12 - m.b31 <= 0)

m.c1342 = Constraint(expr=   m.b2 - m.b13 - m.b32 <= 0)

m.c1343 = Constraint(expr=   m.b2 - m.b14 - m.b33 <= 0)

m.c1344 = Constraint(expr=   m.b2 - m.b15 - m.b34 <= 0)

m.c1345 = Constraint(expr=   m.b2 - m.b16 - m.b35 <= 0)

m.c1346 = Constraint(expr=   m.b2 - m.b17 - m.b36 <= 0)

m.c1347 = Constraint(expr=   m.b2 - m.b18 - m.b37 <= 0)

m.c1348 = Constraint(expr=   m.b2 - m.b19 - m.b38 <= 0)

m.c1349 = Constraint(expr=   m.b2 - m.b20 - m.b39 <= 0)

m.c1350 = Constraint(expr=   m.b2 - m.b21 - m.b40 <= 0)

m.c1351 = Constraint(expr=   m.b3 - m.b4 - m.b41 <= 0)

m.c1352 = Constraint(expr=   m.b3 - m.b5 - m.b42 <= 0)

m.c1353 = Constraint(expr=   m.b3 - m.b6 - m.b43 <= 0)

m.c1354 = Constraint(expr=   m.b3 - m.b7 - m.b44 <= 0)

m.c1355 = Constraint(expr=   m.b3 - m.b8 - m.b45 <= 0)

m.c1356 = Constraint(expr=   m.b3 - m.b9 - m.b46 <= 0)

m.c1357 = Constraint(expr=   m.b3 - m.b10 - m.b47 <= 0)

m.c1358 = Constraint(expr=   m.b3 - m.b11 - m.b48 <= 0)

m.c1359 = Constraint(expr=   m.b3 - m.b12 - m.b49 <= 0)

m.c1360 = Constraint(expr=   m.b3 - m.b13 - m.b50 <= 0)

m.c1361 = Constraint(expr=   m.b3 - m.b14 - m.b51 <= 0)

m.c1362 = Constraint(expr=   m.b3 - m.b15 - m.b52 <= 0)

m.c1363 = Constraint(expr=   m.b3 - m.b16 - m.b53 <= 0)

m.c1364 = Constraint(expr=   m.b3 - m.b17 - m.b54 <= 0)

m.c1365 = Constraint(expr=   m.b3 - m.b18 - m.b55 <= 0)

m.c1366 = Constraint(expr=   m.b3 - m.b19 - m.b56 <= 0)

m.c1367 = Constraint(expr=   m.b3 - m.b20 - m.b57 <= 0)

m.c1368 = Constraint(expr=   m.b3 - m.b21 - m.b58 <= 0)

m.c1369 = Constraint(expr=   m.b4 - m.b5 - m.b59 <= 0)

m.c1370 = Constraint(expr=   m.b4 - m.b6 - m.b60 <= 0)

m.c1371 = Constraint(expr=   m.b4 - m.b7 - m.b61 <= 0)

m.c1372 = Constraint(expr=   m.b4 - m.b8 - m.b62 <= 0)

m.c1373 = Constraint(expr=   m.b4 - m.b9 - m.b63 <= 0)

m.c1374 = Constraint(expr=   m.b4 - m.b10 - m.b64 <= 0)

m.c1375 = Constraint(expr=   m.b4 - m.b11 - m.b65 <= 0)

m.c1376 = Constraint(expr=   m.b4 - m.b12 - m.b66 <= 0)

m.c1377 = Constraint(expr=   m.b4 - m.b13 - m.b67 <= 0)

m.c1378 = Constraint(expr=   m.b4 - m.b14 - m.b68 <= 0)

m.c1379 = Constraint(expr=   m.b4 - m.b15 - m.b69 <= 0)

m.c1380 = Constraint(expr=   m.b4 - m.b16 - m.b70 <= 0)

m.c1381 = Constraint(expr=   m.b4 - m.b17 - m.b71 <= 0)

m.c1382 = Constraint(expr=   m.b4 - m.b18 - m.b72 <= 0)

m.c1383 = Constraint(expr=   m.b4 - m.b19 - m.b73 <= 0)

m.c1384 = Constraint(expr=   m.b4 - m.b20 - m.b74 <= 0)

m.c1385 = Constraint(expr=   m.b4 - m.b21 - m.b75 <= 0)

m.c1386 = Constraint(expr=   m.b5 - m.b6 - m.b76 <= 0)

m.c1387 = Constraint(expr=   m.b5 - m.b7 - m.b77 <= 0)

m.c1388 = Constraint(expr=   m.b5 - m.b8 - m.b78 <= 0)

m.c1389 = Constraint(expr=   m.b5 - m.b9 - m.b79 <= 0)

m.c1390 = Constraint(expr=   m.b5 - m.b10 - m.b80 <= 0)

m.c1391 = Constraint(expr=   m.b5 - m.b11 - m.b81 <= 0)

m.c1392 = Constraint(expr=   m.b5 - m.b12 - m.b82 <= 0)

m.c1393 = Constraint(expr=   m.b5 - m.b13 - m.b83 <= 0)

m.c1394 = Constraint(expr=   m.b5 - m.b14 - m.b84 <= 0)

m.c1395 = Constraint(expr=   m.b5 - m.b15 - m.b85 <= 0)

m.c1396 = Constraint(expr=   m.b5 - m.b16 - m.b86 <= 0)

m.c1397 = Constraint(expr=   m.b5 - m.b17 - m.b87 <= 0)

m.c1398 = Constraint(expr=   m.b5 - m.b18 - m.b88 <= 0)

m.c1399 = Constraint(expr=   m.b5 - m.b19 - m.b89 <= 0)

m.c1400 = Constraint(expr=   m.b5 - m.b20 - m.b90 <= 0)

m.c1401 = Constraint(expr=   m.b5 - m.b21 - m.b91 <= 0)

m.c1402 = Constraint(expr=   m.b6 - m.b7 - m.b92 <= 0)

m.c1403 = Constraint(expr=   m.b6 - m.b8 - m.b93 <= 0)

m.c1404 = Constraint(expr=   m.b6 - m.b9 - m.b94 <= 0)

m.c1405 = Constraint(expr=   m.b6 - m.b10 - m.b95 <= 0)

m.c1406 = Constraint(expr=   m.b6 - m.b11 - m.b96 <= 0)

m.c1407 = Constraint(expr=   m.b6 - m.b12 - m.b97 <= 0)

m.c1408 = Constraint(expr=   m.b6 - m.b13 - m.b98 <= 0)

m.c1409 = Constraint(expr=   m.b6 - m.b14 - m.b99 <= 0)

m.c1410 = Constraint(expr=   m.b6 - m.b15 - m.b100 <= 0)

m.c1411 = Constraint(expr=   m.b6 - m.b16 - m.b101 <= 0)

m.c1412 = Constraint(expr=   m.b6 - m.b17 - m.b102 <= 0)

m.c1413 = Constraint(expr=   m.b6 - m.b18 - m.b103 <= 0)

m.c1414 = Constraint(expr=   m.b6 - m.b19 - m.b104 <= 0)

m.c1415 = Constraint(expr=   m.b6 - m.b20 - m.b105 <= 0)

m.c1416 = Constraint(expr=   m.b6 - m.b21 - m.b106 <= 0)

m.c1417 = Constraint(expr=   m.b7 - m.b8 - m.b107 <= 0)

m.c1418 = Constraint(expr=   m.b7 - m.b9 - m.b108 <= 0)

m.c1419 = Constraint(expr=   m.b7 - m.b10 - m.b109 <= 0)

m.c1420 = Constraint(expr=   m.b7 - m.b11 - m.b110 <= 0)

m.c1421 = Constraint(expr=   m.b7 - m.b12 - m.b111 <= 0)

m.c1422 = Constraint(expr=   m.b7 - m.b13 - m.b112 <= 0)

m.c1423 = Constraint(expr=   m.b7 - m.b14 - m.b113 <= 0)

m.c1424 = Constraint(expr=   m.b7 - m.b15 - m.b114 <= 0)

m.c1425 = Constraint(expr=   m.b7 - m.b16 - m.b115 <= 0)

m.c1426 = Constraint(expr=   m.b7 - m.b17 - m.b116 <= 0)

m.c1427 = Constraint(expr=   m.b7 - m.b18 - m.b117 <= 0)

m.c1428 = Constraint(expr=   m.b7 - m.b19 - m.b118 <= 0)

m.c1429 = Constraint(expr=   m.b7 - m.b20 - m.b119 <= 0)

m.c1430 = Constraint(expr=   m.b7 - m.b21 - m.b120 <= 0)

m.c1431 = Constraint(expr=   m.b8 - m.b9 - m.b121 <= 0)

m.c1432 = Constraint(expr=   m.b8 - m.b10 - m.b122 <= 0)

m.c1433 = Constraint(expr=   m.b8 - m.b11 - m.b123 <= 0)

m.c1434 = Constraint(expr=   m.b8 - m.b12 - m.b124 <= 0)

m.c1435 = Constraint(expr=   m.b8 - m.b13 - m.b125 <= 0)

m.c1436 = Constraint(expr=   m.b8 - m.b14 - m.b126 <= 0)

m.c1437 = Constraint(expr=   m.b8 - m.b15 - m.b127 <= 0)

m.c1438 = Constraint(expr=   m.b8 - m.b16 - m.b128 <= 0)

m.c1439 = Constraint(expr=   m.b8 - m.b17 - m.b129 <= 0)

m.c1440 = Constraint(expr=   m.b8 - m.b18 - m.b130 <= 0)

m.c1441 = Constraint(expr=   m.b8 - m.b19 - m.b131 <= 0)

m.c1442 = Constraint(expr=   m.b8 - m.b20 - m.b132 <= 0)

m.c1443 = Constraint(expr=   m.b8 - m.b21 - m.b133 <= 0)

m.c1444 = Constraint(expr=   m.b9 - m.b10 - m.b134 <= 0)

m.c1445 = Constraint(expr=   m.b9 - m.b11 - m.b135 <= 0)

m.c1446 = Constraint(expr=   m.b9 - m.b12 - m.b136 <= 0)

m.c1447 = Constraint(expr=   m.b9 - m.b13 - m.b137 <= 0)

m.c1448 = Constraint(expr=   m.b9 - m.b14 - m.b138 <= 0)

m.c1449 = Constraint(expr=   m.b9 - m.b15 - m.b139 <= 0)

m.c1450 = Constraint(expr=   m.b9 - m.b16 - m.b140 <= 0)

m.c1451 = Constraint(expr=   m.b9 - m.b17 - m.b141 <= 0)

m.c1452 = Constraint(expr=   m.b9 - m.b18 - m.b142 <= 0)

m.c1453 = Constraint(expr=   m.b9 - m.b19 - m.b143 <= 0)

m.c1454 = Constraint(expr=   m.b9 - m.b20 - m.b144 <= 0)

m.c1455 = Constraint(expr=   m.b9 - m.b21 - m.b145 <= 0)

m.c1456 = Constraint(expr=   m.b10 - m.b11 - m.b146 <= 0)

m.c1457 = Constraint(expr=   m.b10 - m.b12 - m.b147 <= 0)

m.c1458 = Constraint(expr=   m.b10 - m.b13 - m.b148 <= 0)

m.c1459 = Constraint(expr=   m.b10 - m.b14 - m.b149 <= 0)

m.c1460 = Constraint(expr=   m.b10 - m.b15 - m.b150 <= 0)

m.c1461 = Constraint(expr=   m.b10 - m.b16 - m.b151 <= 0)

m.c1462 = Constraint(expr=   m.b10 - m.b17 - m.b152 <= 0)

m.c1463 = Constraint(expr=   m.b10 - m.b18 - m.b153 <= 0)

m.c1464 = Constraint(expr=   m.b10 - m.b19 - m.b154 <= 0)

m.c1465 = Constraint(expr=   m.b10 - m.b20 - m.b155 <= 0)

m.c1466 = Constraint(expr=   m.b10 - m.b21 - m.b156 <= 0)

m.c1467 = Constraint(expr=   m.b11 - m.b12 - m.b157 <= 0)

m.c1468 = Constraint(expr=   m.b11 - m.b13 - m.b158 <= 0)

m.c1469 = Constraint(expr=   m.b11 - m.b14 - m.b159 <= 0)

m.c1470 = Constraint(expr=   m.b11 - m.b15 - m.b160 <= 0)

m.c1471 = Constraint(expr=   m.b11 - m.b16 - m.b161 <= 0)

m.c1472 = Constraint(expr=   m.b11 - m.b17 - m.b162 <= 0)

m.c1473 = Constraint(expr=   m.b11 - m.b18 - m.b163 <= 0)

m.c1474 = Constraint(expr=   m.b11 - m.b19 - m.b164 <= 0)

m.c1475 = Constraint(expr=   m.b11 - m.b20 - m.b165 <= 0)

m.c1476 = Constraint(expr=   m.b11 - m.b21 - m.b211 <= 0)

m.c1477 = Constraint(expr=   m.b12 - m.b13 - m.b166 <= 0)

m.c1478 = Constraint(expr=   m.b12 - m.b14 - m.b167 <= 0)

m.c1479 = Constraint(expr=   m.b12 - m.b15 - m.b168 <= 0)

m.c1480 = Constraint(expr=   m.b12 - m.b16 - m.b169 <= 0)

m.c1481 = Constraint(expr=   m.b12 - m.b17 - m.b170 <= 0)

m.c1482 = Constraint(expr=   m.b12 - m.b18 - m.b171 <= 0)

m.c1483 = Constraint(expr=   m.b12 - m.b19 - m.b172 <= 0)

m.c1484 = Constraint(expr=   m.b12 - m.b20 - m.b173 <= 0)

m.c1485 = Constraint(expr=   m.b12 - m.b21 - m.b174 <= 0)

m.c1486 = Constraint(expr=   m.b13 - m.b14 - m.b175 <= 0)

m.c1487 = Constraint(expr=   m.b13 - m.b15 - m.b176 <= 0)

m.c1488 = Constraint(expr=   m.b13 - m.b16 - m.b177 <= 0)

m.c1489 = Constraint(expr=   m.b13 - m.b17 - m.b178 <= 0)

m.c1490 = Constraint(expr=   m.b13 - m.b18 - m.b179 <= 0)

m.c1491 = Constraint(expr=   m.b13 - m.b19 - m.b180 <= 0)

m.c1492 = Constraint(expr=   m.b13 - m.b20 - m.b181 <= 0)

m.c1493 = Constraint(expr=   m.b13 - m.b21 - m.b182 <= 0)

m.c1494 = Constraint(expr=   m.b14 - m.b15 - m.b183 <= 0)

m.c1495 = Constraint(expr=   m.b14 - m.b16 - m.b184 <= 0)

m.c1496 = Constraint(expr=   m.b14 - m.b17 - m.b185 <= 0)

m.c1497 = Constraint(expr=   m.b14 - m.b18 - m.b186 <= 0)

m.c1498 = Constraint(expr=   m.b14 - m.b19 - m.b187 <= 0)

m.c1499 = Constraint(expr=   m.b14 - m.b20 - m.b188 <= 0)

m.c1500 = Constraint(expr=   m.b14 - m.b21 - m.b189 <= 0)

m.c1501 = Constraint(expr=   m.b15 - m.b16 - m.b190 <= 0)

m.c1502 = Constraint(expr=   m.b15 - m.b17 - m.b191 <= 0)

m.c1503 = Constraint(expr=   m.b15 - m.b18 - m.b192 <= 0)

m.c1504 = Constraint(expr=   m.b15 - m.b19 - m.b193 <= 0)

m.c1505 = Constraint(expr=   m.b15 - m.b20 - m.b194 <= 0)

m.c1506 = Constraint(expr=   m.b15 - m.b21 - m.b195 <= 0)

m.c1507 = Constraint(expr=   m.b16 - m.b17 - m.b196 <= 0)

m.c1508 = Constraint(expr=   m.b16 - m.b18 - m.b197 <= 0)

m.c1509 = Constraint(expr=   m.b16 - m.b19 - m.b198 <= 0)

m.c1510 = Constraint(expr=   m.b16 - m.b20 - m.b199 <= 0)

m.c1511 = Constraint(expr=   m.b16 - m.b21 - m.b200 <= 0)

m.c1512 = Constraint(expr=   m.b17 - m.b18 - m.b201 <= 0)

m.c1513 = Constraint(expr=   m.b17 - m.b19 - m.b202 <= 0)

m.c1514 = Constraint(expr=   m.b17 - m.b20 - m.b203 <= 0)

m.c1515 = Constraint(expr=   m.b17 - m.b21 - m.b204 <= 0)

m.c1516 = Constraint(expr=   m.b18 - m.b19 - m.b205 <= 0)

m.c1517 = Constraint(expr=   m.b18 - m.b20 - m.b206 <= 0)

m.c1518 = Constraint(expr=   m.b18 - m.b21 - m.b207 <= 0)

m.c1519 = Constraint(expr=   m.b19 - m.b20 - m.b208 <= 0)

m.c1520 = Constraint(expr=   m.b19 - m.b21 - m.b209 <= 0)

m.c1521 = Constraint(expr=   m.b20 - m.b21 - m.b210 <= 0)

m.c1522 = Constraint(expr=   m.b22 - m.b23 - m.b41 <= 0)

m.c1523 = Constraint(expr=   m.b22 - m.b24 - m.b42 <= 0)

m.c1524 = Constraint(expr=   m.b22 - m.b25 - m.b43 <= 0)

m.c1525 = Constraint(expr=   m.b22 - m.b26 - m.b44 <= 0)

m.c1526 = Constraint(expr=   m.b22 - m.b27 - m.b45 <= 0)

m.c1527 = Constraint(expr=   m.b22 - m.b28 - m.b46 <= 0)

m.c1528 = Constraint(expr=   m.b22 - m.b29 - m.b47 <= 0)

m.c1529 = Constraint(expr=   m.b22 - m.b30 - m.b48 <= 0)

m.c1530 = Constraint(expr=   m.b22 - m.b31 - m.b49 <= 0)

m.c1531 = Constraint(expr=   m.b22 - m.b32 - m.b50 <= 0)

m.c1532 = Constraint(expr=   m.b22 - m.b33 - m.b51 <= 0)

m.c1533 = Constraint(expr=   m.b22 - m.b34 - m.b52 <= 0)

m.c1534 = Constraint(expr=   m.b22 - m.b35 - m.b53 <= 0)

m.c1535 = Constraint(expr=   m.b22 - m.b36 - m.b54 <= 0)

m.c1536 = Constraint(expr=   m.b22 - m.b37 - m.b55 <= 0)

m.c1537 = Constraint(expr=   m.b22 - m.b38 - m.b56 <= 0)

m.c1538 = Constraint(expr=   m.b22 - m.b39 - m.b57 <= 0)

m.c1539 = Constraint(expr=   m.b22 - m.b40 - m.b58 <= 0)

m.c1540 = Constraint(expr=   m.b23 - m.b24 - m.b59 <= 0)

m.c1541 = Constraint(expr=   m.b23 - m.b25 - m.b60 <= 0)

m.c1542 = Constraint(expr=   m.b23 - m.b26 - m.b61 <= 0)

m.c1543 = Constraint(expr=   m.b23 - m.b27 - m.b62 <= 0)

m.c1544 = Constraint(expr=   m.b23 - m.b28 - m.b63 <= 0)

m.c1545 = Constraint(expr=   m.b23 - m.b29 - m.b64 <= 0)

m.c1546 = Constraint(expr=   m.b23 - m.b30 - m.b65 <= 0)

m.c1547 = Constraint(expr=   m.b23 - m.b31 - m.b66 <= 0)

m.c1548 = Constraint(expr=   m.b23 - m.b32 - m.b67 <= 0)

m.c1549 = Constraint(expr=   m.b23 - m.b33 - m.b68 <= 0)

m.c1550 = Constraint(expr=   m.b23 - m.b34 - m.b69 <= 0)

m.c1551 = Constraint(expr=   m.b23 - m.b35 - m.b70 <= 0)

m.c1552 = Constraint(expr=   m.b23 - m.b36 - m.b71 <= 0)

m.c1553 = Constraint(expr=   m.b23 - m.b37 - m.b72 <= 0)

m.c1554 = Constraint(expr=   m.b23 - m.b38 - m.b73 <= 0)

m.c1555 = Constraint(expr=   m.b23 - m.b39 - m.b74 <= 0)

m.c1556 = Constraint(expr=   m.b23 - m.b40 - m.b75 <= 0)

m.c1557 = Constraint(expr=   m.b24 - m.b25 - m.b76 <= 0)

m.c1558 = Constraint(expr=   m.b24 - m.b26 - m.b77 <= 0)

m.c1559 = Constraint(expr=   m.b24 - m.b27 - m.b78 <= 0)

m.c1560 = Constraint(expr=   m.b24 - m.b28 - m.b79 <= 0)

m.c1561 = Constraint(expr=   m.b24 - m.b29 - m.b80 <= 0)

m.c1562 = Constraint(expr=   m.b24 - m.b30 - m.b81 <= 0)

m.c1563 = Constraint(expr=   m.b24 - m.b31 - m.b82 <= 0)

m.c1564 = Constraint(expr=   m.b24 - m.b32 - m.b83 <= 0)

m.c1565 = Constraint(expr=   m.b24 - m.b33 - m.b84 <= 0)

m.c1566 = Constraint(expr=   m.b24 - m.b34 - m.b85 <= 0)

m.c1567 = Constraint(expr=   m.b24 - m.b35 - m.b86 <= 0)

m.c1568 = Constraint(expr=   m.b24 - m.b36 - m.b87 <= 0)

m.c1569 = Constraint(expr=   m.b24 - m.b37 - m.b88 <= 0)

m.c1570 = Constraint(expr=   m.b24 - m.b38 - m.b89 <= 0)

m.c1571 = Constraint(expr=   m.b24 - m.b39 - m.b90 <= 0)

m.c1572 = Constraint(expr=   m.b24 - m.b40 - m.b91 <= 0)

m.c1573 = Constraint(expr=   m.b25 - m.b26 - m.b92 <= 0)

m.c1574 = Constraint(expr=   m.b25 - m.b27 - m.b93 <= 0)

m.c1575 = Constraint(expr=   m.b25 - m.b28 - m.b94 <= 0)

m.c1576 = Constraint(expr=   m.b25 - m.b29 - m.b95 <= 0)

m.c1577 = Constraint(expr=   m.b25 - m.b30 - m.b96 <= 0)

m.c1578 = Constraint(expr=   m.b25 - m.b31 - m.b97 <= 0)

m.c1579 = Constraint(expr=   m.b25 - m.b32 - m.b98 <= 0)

m.c1580 = Constraint(expr=   m.b25 - m.b33 - m.b99 <= 0)

m.c1581 = Constraint(expr=   m.b25 - m.b34 - m.b100 <= 0)

m.c1582 = Constraint(expr=   m.b25 - m.b35 - m.b101 <= 0)

m.c1583 = Constraint(expr=   m.b25 - m.b36 - m.b102 <= 0)

m.c1584 = Constraint(expr=   m.b25 - m.b37 - m.b103 <= 0)

m.c1585 = Constraint(expr=   m.b25 - m.b38 - m.b104 <= 0)

m.c1586 = Constraint(expr=   m.b25 - m.b39 - m.b105 <= 0)

m.c1587 = Constraint(expr=   m.b25 - m.b40 - m.b106 <= 0)

m.c1588 = Constraint(expr=   m.b26 - m.b27 - m.b107 <= 0)

m.c1589 = Constraint(expr=   m.b26 - m.b28 - m.b108 <= 0)

m.c1590 = Constraint(expr=   m.b26 - m.b29 - m.b109 <= 0)

m.c1591 = Constraint(expr=   m.b26 - m.b30 - m.b110 <= 0)

m.c1592 = Constraint(expr=   m.b26 - m.b31 - m.b111 <= 0)

m.c1593 = Constraint(expr=   m.b26 - m.b32 - m.b112 <= 0)

m.c1594 = Constraint(expr=   m.b26 - m.b33 - m.b113 <= 0)

m.c1595 = Constraint(expr=   m.b26 - m.b34 - m.b114 <= 0)

m.c1596 = Constraint(expr=   m.b26 - m.b35 - m.b115 <= 0)

m.c1597 = Constraint(expr=   m.b26 - m.b36 - m.b116 <= 0)

m.c1598 = Constraint(expr=   m.b26 - m.b37 - m.b117 <= 0)

m.c1599 = Constraint(expr=   m.b26 - m.b38 - m.b118 <= 0)

m.c1600 = Constraint(expr=   m.b26 - m.b39 - m.b119 <= 0)

m.c1601 = Constraint(expr=   m.b26 - m.b40 - m.b120 <= 0)

m.c1602 = Constraint(expr=   m.b27 - m.b28 - m.b121 <= 0)

m.c1603 = Constraint(expr=   m.b27 - m.b29 - m.b122 <= 0)

m.c1604 = Constraint(expr=   m.b27 - m.b30 - m.b123 <= 0)

m.c1605 = Constraint(expr=   m.b27 - m.b31 - m.b124 <= 0)

m.c1606 = Constraint(expr=   m.b27 - m.b32 - m.b125 <= 0)

m.c1607 = Constraint(expr=   m.b27 - m.b33 - m.b126 <= 0)

m.c1608 = Constraint(expr=   m.b27 - m.b34 - m.b127 <= 0)

m.c1609 = Constraint(expr=   m.b27 - m.b35 - m.b128 <= 0)

m.c1610 = Constraint(expr=   m.b27 - m.b36 - m.b129 <= 0)

m.c1611 = Constraint(expr=   m.b27 - m.b37 - m.b130 <= 0)

m.c1612 = Constraint(expr=   m.b27 - m.b38 - m.b131 <= 0)

m.c1613 = Constraint(expr=   m.b27 - m.b39 - m.b132 <= 0)

m.c1614 = Constraint(expr=   m.b27 - m.b40 - m.b133 <= 0)

m.c1615 = Constraint(expr=   m.b28 - m.b29 - m.b134 <= 0)

m.c1616 = Constraint(expr=   m.b28 - m.b30 - m.b135 <= 0)

m.c1617 = Constraint(expr=   m.b28 - m.b31 - m.b136 <= 0)

m.c1618 = Constraint(expr=   m.b28 - m.b32 - m.b137 <= 0)

m.c1619 = Constraint(expr=   m.b28 - m.b33 - m.b138 <= 0)

m.c1620 = Constraint(expr=   m.b28 - m.b34 - m.b139 <= 0)

m.c1621 = Constraint(expr=   m.b28 - m.b35 - m.b140 <= 0)

m.c1622 = Constraint(expr=   m.b28 - m.b36 - m.b141 <= 0)

m.c1623 = Constraint(expr=   m.b28 - m.b37 - m.b142 <= 0)

m.c1624 = Constraint(expr=   m.b28 - m.b38 - m.b143 <= 0)

m.c1625 = Constraint(expr=   m.b28 - m.b39 - m.b144 <= 0)

m.c1626 = Constraint(expr=   m.b28 - m.b40 - m.b145 <= 0)

m.c1627 = Constraint(expr=   m.b29 - m.b30 - m.b146 <= 0)

m.c1628 = Constraint(expr=   m.b29 - m.b31 - m.b147 <= 0)

m.c1629 = Constraint(expr=   m.b29 - m.b32 - m.b148 <= 0)

m.c1630 = Constraint(expr=   m.b29 - m.b33 - m.b149 <= 0)

m.c1631 = Constraint(expr=   m.b29 - m.b34 - m.b150 <= 0)

m.c1632 = Constraint(expr=   m.b29 - m.b35 - m.b151 <= 0)

m.c1633 = Constraint(expr=   m.b29 - m.b36 - m.b152 <= 0)

m.c1634 = Constraint(expr=   m.b29 - m.b37 - m.b153 <= 0)

m.c1635 = Constraint(expr=   m.b29 - m.b38 - m.b154 <= 0)

m.c1636 = Constraint(expr=   m.b29 - m.b39 - m.b155 <= 0)

m.c1637 = Constraint(expr=   m.b29 - m.b40 - m.b156 <= 0)

m.c1638 = Constraint(expr=   m.b30 - m.b31 - m.b157 <= 0)

m.c1639 = Constraint(expr=   m.b30 - m.b32 - m.b158 <= 0)

m.c1640 = Constraint(expr=   m.b30 - m.b33 - m.b159 <= 0)

m.c1641 = Constraint(expr=   m.b30 - m.b34 - m.b160 <= 0)

m.c1642 = Constraint(expr=   m.b30 - m.b35 - m.b161 <= 0)

m.c1643 = Constraint(expr=   m.b30 - m.b36 - m.b162 <= 0)

m.c1644 = Constraint(expr=   m.b30 - m.b37 - m.b163 <= 0)

m.c1645 = Constraint(expr=   m.b30 - m.b38 - m.b164 <= 0)

m.c1646 = Constraint(expr=   m.b30 - m.b39 - m.b165 <= 0)

m.c1647 = Constraint(expr=   m.b30 - m.b40 - m.b211 <= 0)

m.c1648 = Constraint(expr=   m.b31 - m.b32 - m.b166 <= 0)

m.c1649 = Constraint(expr=   m.b31 - m.b33 - m.b167 <= 0)

m.c1650 = Constraint(expr=   m.b31 - m.b34 - m.b168 <= 0)

m.c1651 = Constraint(expr=   m.b31 - m.b35 - m.b169 <= 0)

m.c1652 = Constraint(expr=   m.b31 - m.b36 - m.b170 <= 0)

m.c1653 = Constraint(expr=   m.b31 - m.b37 - m.b171 <= 0)

m.c1654 = Constraint(expr=   m.b31 - m.b38 - m.b172 <= 0)

m.c1655 = Constraint(expr=   m.b31 - m.b39 - m.b173 <= 0)

m.c1656 = Constraint(expr=   m.b31 - m.b40 - m.b174 <= 0)

m.c1657 = Constraint(expr=   m.b32 - m.b33 - m.b175 <= 0)

m.c1658 = Constraint(expr=   m.b32 - m.b34 - m.b176 <= 0)

m.c1659 = Constraint(expr=   m.b32 - m.b35 - m.b177 <= 0)

m.c1660 = Constraint(expr=   m.b32 - m.b36 - m.b178 <= 0)

m.c1661 = Constraint(expr=   m.b32 - m.b37 - m.b179 <= 0)

m.c1662 = Constraint(expr=   m.b32 - m.b38 - m.b180 <= 0)

m.c1663 = Constraint(expr=   m.b32 - m.b39 - m.b181 <= 0)

m.c1664 = Constraint(expr=   m.b32 - m.b40 - m.b182 <= 0)

m.c1665 = Constraint(expr=   m.b33 - m.b34 - m.b183 <= 0)

m.c1666 = Constraint(expr=   m.b33 - m.b35 - m.b184 <= 0)

m.c1667 = Constraint(expr=   m.b33 - m.b36 - m.b185 <= 0)

m.c1668 = Constraint(expr=   m.b33 - m.b37 - m.b186 <= 0)

m.c1669 = Constraint(expr=   m.b33 - m.b38 - m.b187 <= 0)

m.c1670 = Constraint(expr=   m.b33 - m.b39 - m.b188 <= 0)

m.c1671 = Constraint(expr=   m.b33 - m.b40 - m.b189 <= 0)

m.c1672 = Constraint(expr=   m.b34 - m.b35 - m.b190 <= 0)

m.c1673 = Constraint(expr=   m.b34 - m.b36 - m.b191 <= 0)

m.c1674 = Constraint(expr=   m.b34 - m.b37 - m.b192 <= 0)

m.c1675 = Constraint(expr=   m.b34 - m.b38 - m.b193 <= 0)

m.c1676 = Constraint(expr=   m.b34 - m.b39 - m.b194 <= 0)

m.c1677 = Constraint(expr=   m.b34 - m.b40 - m.b195 <= 0)

m.c1678 = Constraint(expr=   m.b35 - m.b36 - m.b196 <= 0)

m.c1679 = Constraint(expr=   m.b35 - m.b37 - m.b197 <= 0)

m.c1680 = Constraint(expr=   m.b35 - m.b38 - m.b198 <= 0)

m.c1681 = Constraint(expr=   m.b35 - m.b39 - m.b199 <= 0)

m.c1682 = Constraint(expr=   m.b35 - m.b40 - m.b200 <= 0)

m.c1683 = Constraint(expr=   m.b36 - m.b37 - m.b201 <= 0)

m.c1684 = Constraint(expr=   m.b36 - m.b38 - m.b202 <= 0)

m.c1685 = Constraint(expr=   m.b36 - m.b39 - m.b203 <= 0)

m.c1686 = Constraint(expr=   m.b36 - m.b40 - m.b204 <= 0)

m.c1687 = Constraint(expr=   m.b37 - m.b38 - m.b205 <= 0)

m.c1688 = Constraint(expr=   m.b37 - m.b39 - m.b206 <= 0)

m.c1689 = Constraint(expr=   m.b37 - m.b40 - m.b207 <= 0)

m.c1690 = Constraint(expr=   m.b38 - m.b39 - m.b208 <= 0)

m.c1691 = Constraint(expr=   m.b38 - m.b40 - m.b209 <= 0)

m.c1692 = Constraint(expr=   m.b39 - m.b40 - m.b210 <= 0)

m.c1693 = Constraint(expr=   m.b41 - m.b42 - m.b59 <= 0)

m.c1694 = Constraint(expr=   m.b41 - m.b43 - m.b60 <= 0)

m.c1695 = Constraint(expr=   m.b41 - m.b44 - m.b61 <= 0)

m.c1696 = Constraint(expr=   m.b41 - m.b45 - m.b62 <= 0)

m.c1697 = Constraint(expr=   m.b41 - m.b46 - m.b63 <= 0)

m.c1698 = Constraint(expr=   m.b41 - m.b47 - m.b64 <= 0)

m.c1699 = Constraint(expr=   m.b41 - m.b48 - m.b65 <= 0)

m.c1700 = Constraint(expr=   m.b41 - m.b49 - m.b66 <= 0)

m.c1701 = Constraint(expr=   m.b41 - m.b50 - m.b67 <= 0)

m.c1702 = Constraint(expr=   m.b41 - m.b51 - m.b68 <= 0)

m.c1703 = Constraint(expr=   m.b41 - m.b52 - m.b69 <= 0)

m.c1704 = Constraint(expr=   m.b41 - m.b53 - m.b70 <= 0)

m.c1705 = Constraint(expr=   m.b41 - m.b54 - m.b71 <= 0)

m.c1706 = Constraint(expr=   m.b41 - m.b55 - m.b72 <= 0)

m.c1707 = Constraint(expr=   m.b41 - m.b56 - m.b73 <= 0)

m.c1708 = Constraint(expr=   m.b41 - m.b57 - m.b74 <= 0)

m.c1709 = Constraint(expr=   m.b41 - m.b58 - m.b75 <= 0)

m.c1710 = Constraint(expr=   m.b42 - m.b43 - m.b76 <= 0)

m.c1711 = Constraint(expr=   m.b42 - m.b44 - m.b77 <= 0)

m.c1712 = Constraint(expr=   m.b42 - m.b45 - m.b78 <= 0)

m.c1713 = Constraint(expr=   m.b42 - m.b46 - m.b79 <= 0)

m.c1714 = Constraint(expr=   m.b42 - m.b47 - m.b80 <= 0)

m.c1715 = Constraint(expr=   m.b42 - m.b48 - m.b81 <= 0)

m.c1716 = Constraint(expr=   m.b42 - m.b49 - m.b82 <= 0)

m.c1717 = Constraint(expr=   m.b42 - m.b50 - m.b83 <= 0)

m.c1718 = Constraint(expr=   m.b42 - m.b51 - m.b84 <= 0)

m.c1719 = Constraint(expr=   m.b42 - m.b52 - m.b85 <= 0)

m.c1720 = Constraint(expr=   m.b42 - m.b53 - m.b86 <= 0)

m.c1721 = Constraint(expr=   m.b42 - m.b54 - m.b87 <= 0)

m.c1722 = Constraint(expr=   m.b42 - m.b55 - m.b88 <= 0)

m.c1723 = Constraint(expr=   m.b42 - m.b56 - m.b89 <= 0)

m.c1724 = Constraint(expr=   m.b42 - m.b57 - m.b90 <= 0)

m.c1725 = Constraint(expr=   m.b42 - m.b58 - m.b91 <= 0)

m.c1726 = Constraint(expr=   m.b43 - m.b44 - m.b92 <= 0)

m.c1727 = Constraint(expr=   m.b43 - m.b45 - m.b93 <= 0)

m.c1728 = Constraint(expr=   m.b43 - m.b46 - m.b94 <= 0)

m.c1729 = Constraint(expr=   m.b43 - m.b47 - m.b95 <= 0)

m.c1730 = Constraint(expr=   m.b43 - m.b48 - m.b96 <= 0)

m.c1731 = Constraint(expr=   m.b43 - m.b49 - m.b97 <= 0)

m.c1732 = Constraint(expr=   m.b43 - m.b50 - m.b98 <= 0)

m.c1733 = Constraint(expr=   m.b43 - m.b51 - m.b99 <= 0)

m.c1734 = Constraint(expr=   m.b43 - m.b52 - m.b100 <= 0)

m.c1735 = Constraint(expr=   m.b43 - m.b53 - m.b101 <= 0)

m.c1736 = Constraint(expr=   m.b43 - m.b54 - m.b102 <= 0)

m.c1737 = Constraint(expr=   m.b43 - m.b55 - m.b103 <= 0)

m.c1738 = Constraint(expr=   m.b43 - m.b56 - m.b104 <= 0)

m.c1739 = Constraint(expr=   m.b43 - m.b57 - m.b105 <= 0)

m.c1740 = Constraint(expr=   m.b43 - m.b58 - m.b106 <= 0)

m.c1741 = Constraint(expr=   m.b44 - m.b45 - m.b107 <= 0)

m.c1742 = Constraint(expr=   m.b44 - m.b46 - m.b108 <= 0)

m.c1743 = Constraint(expr=   m.b44 - m.b47 - m.b109 <= 0)

m.c1744 = Constraint(expr=   m.b44 - m.b48 - m.b110 <= 0)

m.c1745 = Constraint(expr=   m.b44 - m.b49 - m.b111 <= 0)

m.c1746 = Constraint(expr=   m.b44 - m.b50 - m.b112 <= 0)

m.c1747 = Constraint(expr=   m.b44 - m.b51 - m.b113 <= 0)

m.c1748 = Constraint(expr=   m.b44 - m.b52 - m.b114 <= 0)

m.c1749 = Constraint(expr=   m.b44 - m.b53 - m.b115 <= 0)

m.c1750 = Constraint(expr=   m.b44 - m.b54 - m.b116 <= 0)

m.c1751 = Constraint(expr=   m.b44 - m.b55 - m.b117 <= 0)

m.c1752 = Constraint(expr=   m.b44 - m.b56 - m.b118 <= 0)

m.c1753 = Constraint(expr=   m.b44 - m.b57 - m.b119 <= 0)

m.c1754 = Constraint(expr=   m.b44 - m.b58 - m.b120 <= 0)

m.c1755 = Constraint(expr=   m.b45 - m.b46 - m.b121 <= 0)

m.c1756 = Constraint(expr=   m.b45 - m.b47 - m.b122 <= 0)

m.c1757 = Constraint(expr=   m.b45 - m.b48 - m.b123 <= 0)

m.c1758 = Constraint(expr=   m.b45 - m.b49 - m.b124 <= 0)

m.c1759 = Constraint(expr=   m.b45 - m.b50 - m.b125 <= 0)

m.c1760 = Constraint(expr=   m.b45 - m.b51 - m.b126 <= 0)

m.c1761 = Constraint(expr=   m.b45 - m.b52 - m.b127 <= 0)

m.c1762 = Constraint(expr=   m.b45 - m.b53 - m.b128 <= 0)

m.c1763 = Constraint(expr=   m.b45 - m.b54 - m.b129 <= 0)

m.c1764 = Constraint(expr=   m.b45 - m.b55 - m.b130 <= 0)

m.c1765 = Constraint(expr=   m.b45 - m.b56 - m.b131 <= 0)

m.c1766 = Constraint(expr=   m.b45 - m.b57 - m.b132 <= 0)

m.c1767 = Constraint(expr=   m.b45 - m.b58 - m.b133 <= 0)

m.c1768 = Constraint(expr=   m.b46 - m.b47 - m.b134 <= 0)

m.c1769 = Constraint(expr=   m.b46 - m.b48 - m.b135 <= 0)

m.c1770 = Constraint(expr=   m.b46 - m.b49 - m.b136 <= 0)

m.c1771 = Constraint(expr=   m.b46 - m.b50 - m.b137 <= 0)

m.c1772 = Constraint(expr=   m.b46 - m.b51 - m.b138 <= 0)

m.c1773 = Constraint(expr=   m.b46 - m.b52 - m.b139 <= 0)

m.c1774 = Constraint(expr=   m.b46 - m.b53 - m.b140 <= 0)

m.c1775 = Constraint(expr=   m.b46 - m.b54 - m.b141 <= 0)

m.c1776 = Constraint(expr=   m.b46 - m.b55 - m.b142 <= 0)

m.c1777 = Constraint(expr=   m.b46 - m.b56 - m.b143 <= 0)

m.c1778 = Constraint(expr=   m.b46 - m.b57 - m.b144 <= 0)

m.c1779 = Constraint(expr=   m.b46 - m.b58 - m.b145 <= 0)

m.c1780 = Constraint(expr=   m.b47 - m.b48 - m.b146 <= 0)

m.c1781 = Constraint(expr=   m.b47 - m.b49 - m.b147 <= 0)

m.c1782 = Constraint(expr=   m.b47 - m.b50 - m.b148 <= 0)

m.c1783 = Constraint(expr=   m.b47 - m.b51 - m.b149 <= 0)

m.c1784 = Constraint(expr=   m.b47 - m.b52 - m.b150 <= 0)

m.c1785 = Constraint(expr=   m.b47 - m.b53 - m.b151 <= 0)

m.c1786 = Constraint(expr=   m.b47 - m.b54 - m.b152 <= 0)

m.c1787 = Constraint(expr=   m.b47 - m.b55 - m.b153 <= 0)

m.c1788 = Constraint(expr=   m.b47 - m.b56 - m.b154 <= 0)

m.c1789 = Constraint(expr=   m.b47 - m.b57 - m.b155 <= 0)

m.c1790 = Constraint(expr=   m.b47 - m.b58 - m.b156 <= 0)

m.c1791 = Constraint(expr=   m.b48 - m.b49 - m.b157 <= 0)

m.c1792 = Constraint(expr=   m.b48 - m.b50 - m.b158 <= 0)

m.c1793 = Constraint(expr=   m.b48 - m.b51 - m.b159 <= 0)

m.c1794 = Constraint(expr=   m.b48 - m.b52 - m.b160 <= 0)

m.c1795 = Constraint(expr=   m.b48 - m.b53 - m.b161 <= 0)

m.c1796 = Constraint(expr=   m.b48 - m.b54 - m.b162 <= 0)

m.c1797 = Constraint(expr=   m.b48 - m.b55 - m.b163 <= 0)

m.c1798 = Constraint(expr=   m.b48 - m.b56 - m.b164 <= 0)

m.c1799 = Constraint(expr=   m.b48 - m.b57 - m.b165 <= 0)

m.c1800 = Constraint(expr=   m.b48 - m.b58 - m.b211 <= 0)

m.c1801 = Constraint(expr=   m.b49 - m.b50 - m.b166 <= 0)

m.c1802 = Constraint(expr=   m.b49 - m.b51 - m.b167 <= 0)

m.c1803 = Constraint(expr=   m.b49 - m.b52 - m.b168 <= 0)

m.c1804 = Constraint(expr=   m.b49 - m.b53 - m.b169 <= 0)

m.c1805 = Constraint(expr=   m.b49 - m.b54 - m.b170 <= 0)

m.c1806 = Constraint(expr=   m.b49 - m.b55 - m.b171 <= 0)

m.c1807 = Constraint(expr=   m.b49 - m.b56 - m.b172 <= 0)

m.c1808 = Constraint(expr=   m.b49 - m.b57 - m.b173 <= 0)

m.c1809 = Constraint(expr=   m.b49 - m.b58 - m.b174 <= 0)

m.c1810 = Constraint(expr=   m.b50 - m.b51 - m.b175 <= 0)

m.c1811 = Constraint(expr=   m.b50 - m.b52 - m.b176 <= 0)

m.c1812 = Constraint(expr=   m.b50 - m.b53 - m.b177 <= 0)

m.c1813 = Constraint(expr=   m.b50 - m.b54 - m.b178 <= 0)

m.c1814 = Constraint(expr=   m.b50 - m.b55 - m.b179 <= 0)

m.c1815 = Constraint(expr=   m.b50 - m.b56 - m.b180 <= 0)

m.c1816 = Constraint(expr=   m.b50 - m.b57 - m.b181 <= 0)

m.c1817 = Constraint(expr=   m.b50 - m.b58 - m.b182 <= 0)

m.c1818 = Constraint(expr=   m.b51 - m.b52 - m.b183 <= 0)

m.c1819 = Constraint(expr=   m.b51 - m.b53 - m.b184 <= 0)

m.c1820 = Constraint(expr=   m.b51 - m.b54 - m.b185 <= 0)

m.c1821 = Constraint(expr=   m.b51 - m.b55 - m.b186 <= 0)

m.c1822 = Constraint(expr=   m.b51 - m.b56 - m.b187 <= 0)

m.c1823 = Constraint(expr=   m.b51 - m.b57 - m.b188 <= 0)

m.c1824 = Constraint(expr=   m.b51 - m.b58 - m.b189 <= 0)

m.c1825 = Constraint(expr=   m.b52 - m.b53 - m.b190 <= 0)

m.c1826 = Constraint(expr=   m.b52 - m.b54 - m.b191 <= 0)

m.c1827 = Constraint(expr=   m.b52 - m.b55 - m.b192 <= 0)

m.c1828 = Constraint(expr=   m.b52 - m.b56 - m.b193 <= 0)

m.c1829 = Constraint(expr=   m.b52 - m.b57 - m.b194 <= 0)

m.c1830 = Constraint(expr=   m.b52 - m.b58 - m.b195 <= 0)

m.c1831 = Constraint(expr=   m.b53 - m.b54 - m.b196 <= 0)

m.c1832 = Constraint(expr=   m.b53 - m.b55 - m.b197 <= 0)

m.c1833 = Constraint(expr=   m.b53 - m.b56 - m.b198 <= 0)

m.c1834 = Constraint(expr=   m.b53 - m.b57 - m.b199 <= 0)

m.c1835 = Constraint(expr=   m.b53 - m.b58 - m.b200 <= 0)

m.c1836 = Constraint(expr=   m.b54 - m.b55 - m.b201 <= 0)

m.c1837 = Constraint(expr=   m.b54 - m.b56 - m.b202 <= 0)

m.c1838 = Constraint(expr=   m.b54 - m.b57 - m.b203 <= 0)

m.c1839 = Constraint(expr=   m.b54 - m.b58 - m.b204 <= 0)

m.c1840 = Constraint(expr=   m.b55 - m.b56 - m.b205 <= 0)

m.c1841 = Constraint(expr=   m.b55 - m.b57 - m.b206 <= 0)

m.c1842 = Constraint(expr=   m.b55 - m.b58 - m.b207 <= 0)

m.c1843 = Constraint(expr=   m.b56 - m.b57 - m.b208 <= 0)

m.c1844 = Constraint(expr=   m.b56 - m.b58 - m.b209 <= 0)

m.c1845 = Constraint(expr=   m.b57 - m.b58 - m.b210 <= 0)

m.c1846 = Constraint(expr=   m.b59 - m.b60 - m.b76 <= 0)

m.c1847 = Constraint(expr=   m.b59 - m.b61 - m.b77 <= 0)

m.c1848 = Constraint(expr=   m.b59 - m.b62 - m.b78 <= 0)

m.c1849 = Constraint(expr=   m.b59 - m.b63 - m.b79 <= 0)

m.c1850 = Constraint(expr=   m.b59 - m.b64 - m.b80 <= 0)

m.c1851 = Constraint(expr=   m.b59 - m.b65 - m.b81 <= 0)

m.c1852 = Constraint(expr=   m.b59 - m.b66 - m.b82 <= 0)

m.c1853 = Constraint(expr=   m.b59 - m.b67 - m.b83 <= 0)

m.c1854 = Constraint(expr=   m.b59 - m.b68 - m.b84 <= 0)

m.c1855 = Constraint(expr=   m.b59 - m.b69 - m.b85 <= 0)

m.c1856 = Constraint(expr=   m.b59 - m.b70 - m.b86 <= 0)

m.c1857 = Constraint(expr=   m.b59 - m.b71 - m.b87 <= 0)

m.c1858 = Constraint(expr=   m.b59 - m.b72 - m.b88 <= 0)

m.c1859 = Constraint(expr=   m.b59 - m.b73 - m.b89 <= 0)

m.c1860 = Constraint(expr=   m.b59 - m.b74 - m.b90 <= 0)

m.c1861 = Constraint(expr=   m.b59 - m.b75 - m.b91 <= 0)

m.c1862 = Constraint(expr=   m.b60 - m.b61 - m.b92 <= 0)

m.c1863 = Constraint(expr=   m.b60 - m.b62 - m.b93 <= 0)

m.c1864 = Constraint(expr=   m.b60 - m.b63 - m.b94 <= 0)

m.c1865 = Constraint(expr=   m.b60 - m.b64 - m.b95 <= 0)

m.c1866 = Constraint(expr=   m.b60 - m.b65 - m.b96 <= 0)

m.c1867 = Constraint(expr=   m.b60 - m.b66 - m.b97 <= 0)

m.c1868 = Constraint(expr=   m.b60 - m.b67 - m.b98 <= 0)

m.c1869 = Constraint(expr=   m.b60 - m.b68 - m.b99 <= 0)

m.c1870 = Constraint(expr=   m.b60 - m.b69 - m.b100 <= 0)

m.c1871 = Constraint(expr=   m.b60 - m.b70 - m.b101 <= 0)

m.c1872 = Constraint(expr=   m.b60 - m.b71 - m.b102 <= 0)

m.c1873 = Constraint(expr=   m.b60 - m.b72 - m.b103 <= 0)

m.c1874 = Constraint(expr=   m.b60 - m.b73 - m.b104 <= 0)

m.c1875 = Constraint(expr=   m.b60 - m.b74 - m.b105 <= 0)

m.c1876 = Constraint(expr=   m.b60 - m.b75 - m.b106 <= 0)

m.c1877 = Constraint(expr=   m.b61 - m.b62 - m.b107 <= 0)

m.c1878 = Constraint(expr=   m.b61 - m.b63 - m.b108 <= 0)

m.c1879 = Constraint(expr=   m.b61 - m.b64 - m.b109 <= 0)

m.c1880 = Constraint(expr=   m.b61 - m.b65 - m.b110 <= 0)

m.c1881 = Constraint(expr=   m.b61 - m.b66 - m.b111 <= 0)

m.c1882 = Constraint(expr=   m.b61 - m.b67 - m.b112 <= 0)

m.c1883 = Constraint(expr=   m.b61 - m.b68 - m.b113 <= 0)

m.c1884 = Constraint(expr=   m.b61 - m.b69 - m.b114 <= 0)

m.c1885 = Constraint(expr=   m.b61 - m.b70 - m.b115 <= 0)

m.c1886 = Constraint(expr=   m.b61 - m.b71 - m.b116 <= 0)

m.c1887 = Constraint(expr=   m.b61 - m.b72 - m.b117 <= 0)

m.c1888 = Constraint(expr=   m.b61 - m.b73 - m.b118 <= 0)

m.c1889 = Constraint(expr=   m.b61 - m.b74 - m.b119 <= 0)

m.c1890 = Constraint(expr=   m.b61 - m.b75 - m.b120 <= 0)

m.c1891 = Constraint(expr=   m.b62 - m.b63 - m.b121 <= 0)

m.c1892 = Constraint(expr=   m.b62 - m.b64 - m.b122 <= 0)

m.c1893 = Constraint(expr=   m.b62 - m.b65 - m.b123 <= 0)

m.c1894 = Constraint(expr=   m.b62 - m.b66 - m.b124 <= 0)

m.c1895 = Constraint(expr=   m.b62 - m.b67 - m.b125 <= 0)

m.c1896 = Constraint(expr=   m.b62 - m.b68 - m.b126 <= 0)

m.c1897 = Constraint(expr=   m.b62 - m.b69 - m.b127 <= 0)

m.c1898 = Constraint(expr=   m.b62 - m.b70 - m.b128 <= 0)

m.c1899 = Constraint(expr=   m.b62 - m.b71 - m.b129 <= 0)

m.c1900 = Constraint(expr=   m.b62 - m.b72 - m.b130 <= 0)

m.c1901 = Constraint(expr=   m.b62 - m.b73 - m.b131 <= 0)

m.c1902 = Constraint(expr=   m.b62 - m.b74 - m.b132 <= 0)

m.c1903 = Constraint(expr=   m.b62 - m.b75 - m.b133 <= 0)

m.c1904 = Constraint(expr=   m.b63 - m.b64 - m.b134 <= 0)

m.c1905 = Constraint(expr=   m.b63 - m.b65 - m.b135 <= 0)

m.c1906 = Constraint(expr=   m.b63 - m.b66 - m.b136 <= 0)

m.c1907 = Constraint(expr=   m.b63 - m.b67 - m.b137 <= 0)

m.c1908 = Constraint(expr=   m.b63 - m.b68 - m.b138 <= 0)

m.c1909 = Constraint(expr=   m.b63 - m.b69 - m.b139 <= 0)

m.c1910 = Constraint(expr=   m.b63 - m.b70 - m.b140 <= 0)

m.c1911 = Constraint(expr=   m.b63 - m.b71 - m.b141 <= 0)

m.c1912 = Constraint(expr=   m.b63 - m.b72 - m.b142 <= 0)

m.c1913 = Constraint(expr=   m.b63 - m.b73 - m.b143 <= 0)

m.c1914 = Constraint(expr=   m.b63 - m.b74 - m.b144 <= 0)

m.c1915 = Constraint(expr=   m.b63 - m.b75 - m.b145 <= 0)

m.c1916 = Constraint(expr=   m.b64 - m.b65 - m.b146 <= 0)

m.c1917 = Constraint(expr=   m.b64 - m.b66 - m.b147 <= 0)

m.c1918 = Constraint(expr=   m.b64 - m.b67 - m.b148 <= 0)

m.c1919 = Constraint(expr=   m.b64 - m.b68 - m.b149 <= 0)

m.c1920 = Constraint(expr=   m.b64 - m.b69 - m.b150 <= 0)

m.c1921 = Constraint(expr=   m.b64 - m.b70 - m.b151 <= 0)

m.c1922 = Constraint(expr=   m.b64 - m.b71 - m.b152 <= 0)

m.c1923 = Constraint(expr=   m.b64 - m.b72 - m.b153 <= 0)

m.c1924 = Constraint(expr=   m.b64 - m.b73 - m.b154 <= 0)

m.c1925 = Constraint(expr=   m.b64 - m.b74 - m.b155 <= 0)

m.c1926 = Constraint(expr=   m.b64 - m.b75 - m.b156 <= 0)

m.c1927 = Constraint(expr=   m.b65 - m.b66 - m.b157 <= 0)

m.c1928 = Constraint(expr=   m.b65 - m.b67 - m.b158 <= 0)

m.c1929 = Constraint(expr=   m.b65 - m.b68 - m.b159 <= 0)

m.c1930 = Constraint(expr=   m.b65 - m.b69 - m.b160 <= 0)

m.c1931 = Constraint(expr=   m.b65 - m.b70 - m.b161 <= 0)

m.c1932 = Constraint(expr=   m.b65 - m.b71 - m.b162 <= 0)

m.c1933 = Constraint(expr=   m.b65 - m.b72 - m.b163 <= 0)

m.c1934 = Constraint(expr=   m.b65 - m.b73 - m.b164 <= 0)

m.c1935 = Constraint(expr=   m.b65 - m.b74 - m.b165 <= 0)

m.c1936 = Constraint(expr=   m.b65 - m.b75 - m.b211 <= 0)

m.c1937 = Constraint(expr=   m.b66 - m.b67 - m.b166 <= 0)

m.c1938 = Constraint(expr=   m.b66 - m.b68 - m.b167 <= 0)

m.c1939 = Constraint(expr=   m.b66 - m.b69 - m.b168 <= 0)

m.c1940 = Constraint(expr=   m.b66 - m.b70 - m.b169 <= 0)

m.c1941 = Constraint(expr=   m.b66 - m.b71 - m.b170 <= 0)

m.c1942 = Constraint(expr=   m.b66 - m.b72 - m.b171 <= 0)

m.c1943 = Constraint(expr=   m.b66 - m.b73 - m.b172 <= 0)

m.c1944 = Constraint(expr=   m.b66 - m.b74 - m.b173 <= 0)

m.c1945 = Constraint(expr=   m.b66 - m.b75 - m.b174 <= 0)

m.c1946 = Constraint(expr=   m.b67 - m.b68 - m.b175 <= 0)

m.c1947 = Constraint(expr=   m.b67 - m.b69 - m.b176 <= 0)

m.c1948 = Constraint(expr=   m.b67 - m.b70 - m.b177 <= 0)

m.c1949 = Constraint(expr=   m.b67 - m.b71 - m.b178 <= 0)

m.c1950 = Constraint(expr=   m.b67 - m.b72 - m.b179 <= 0)

m.c1951 = Constraint(expr=   m.b67 - m.b73 - m.b180 <= 0)

m.c1952 = Constraint(expr=   m.b67 - m.b74 - m.b181 <= 0)

m.c1953 = Constraint(expr=   m.b67 - m.b75 - m.b182 <= 0)

m.c1954 = Constraint(expr=   m.b68 - m.b69 - m.b183 <= 0)

m.c1955 = Constraint(expr=   m.b68 - m.b70 - m.b184 <= 0)

m.c1956 = Constraint(expr=   m.b68 - m.b71 - m.b185 <= 0)

m.c1957 = Constraint(expr=   m.b68 - m.b72 - m.b186 <= 0)

m.c1958 = Constraint(expr=   m.b68 - m.b73 - m.b187 <= 0)

m.c1959 = Constraint(expr=   m.b68 - m.b74 - m.b188 <= 0)

m.c1960 = Constraint(expr=   m.b68 - m.b75 - m.b189 <= 0)

m.c1961 = Constraint(expr=   m.b69 - m.b70 - m.b190 <= 0)

m.c1962 = Constraint(expr=   m.b69 - m.b71 - m.b191 <= 0)

m.c1963 = Constraint(expr=   m.b69 - m.b72 - m.b192 <= 0)

m.c1964 = Constraint(expr=   m.b69 - m.b73 - m.b193 <= 0)

m.c1965 = Constraint(expr=   m.b69 - m.b74 - m.b194 <= 0)

m.c1966 = Constraint(expr=   m.b69 - m.b75 - m.b195 <= 0)

m.c1967 = Constraint(expr=   m.b70 - m.b71 - m.b196 <= 0)

m.c1968 = Constraint(expr=   m.b70 - m.b72 - m.b197 <= 0)

m.c1969 = Constraint(expr=   m.b70 - m.b73 - m.b198 <= 0)

m.c1970 = Constraint(expr=   m.b70 - m.b74 - m.b199 <= 0)

m.c1971 = Constraint(expr=   m.b70 - m.b75 - m.b200 <= 0)

m.c1972 = Constraint(expr=   m.b71 - m.b72 - m.b201 <= 0)

m.c1973 = Constraint(expr=   m.b71 - m.b73 - m.b202 <= 0)

m.c1974 = Constraint(expr=   m.b71 - m.b74 - m.b203 <= 0)

m.c1975 = Constraint(expr=   m.b71 - m.b75 - m.b204 <= 0)

m.c1976 = Constraint(expr=   m.b72 - m.b73 - m.b205 <= 0)

m.c1977 = Constraint(expr=   m.b72 - m.b74 - m.b206 <= 0)

m.c1978 = Constraint(expr=   m.b72 - m.b75 - m.b207 <= 0)

m.c1979 = Constraint(expr=   m.b73 - m.b74 - m.b208 <= 0)

m.c1980 = Constraint(expr=   m.b73 - m.b75 - m.b209 <= 0)

m.c1981 = Constraint(expr=   m.b74 - m.b75 - m.b210 <= 0)

m.c1982 = Constraint(expr=   m.b76 - m.b77 - m.b92 <= 0)

m.c1983 = Constraint(expr=   m.b76 - m.b78 - m.b93 <= 0)

m.c1984 = Constraint(expr=   m.b76 - m.b79 - m.b94 <= 0)

m.c1985 = Constraint(expr=   m.b76 - m.b80 - m.b95 <= 0)

m.c1986 = Constraint(expr=   m.b76 - m.b81 - m.b96 <= 0)

m.c1987 = Constraint(expr=   m.b76 - m.b82 - m.b97 <= 0)

m.c1988 = Constraint(expr=   m.b76 - m.b83 - m.b98 <= 0)

m.c1989 = Constraint(expr=   m.b76 - m.b84 - m.b99 <= 0)

m.c1990 = Constraint(expr=   m.b76 - m.b85 - m.b100 <= 0)

m.c1991 = Constraint(expr=   m.b76 - m.b86 - m.b101 <= 0)

m.c1992 = Constraint(expr=   m.b76 - m.b87 - m.b102 <= 0)

m.c1993 = Constraint(expr=   m.b76 - m.b88 - m.b103 <= 0)

m.c1994 = Constraint(expr=   m.b76 - m.b89 - m.b104 <= 0)

m.c1995 = Constraint(expr=   m.b76 - m.b90 - m.b105 <= 0)

m.c1996 = Constraint(expr=   m.b76 - m.b91 - m.b106 <= 0)

m.c1997 = Constraint(expr=   m.b77 - m.b78 - m.b107 <= 0)

m.c1998 = Constraint(expr=   m.b77 - m.b79 - m.b108 <= 0)

m.c1999 = Constraint(expr=   m.b77 - m.b80 - m.b109 <= 0)

m.c2000 = Constraint(expr=   m.b77 - m.b81 - m.b110 <= 0)

m.c2001 = Constraint(expr=   m.b77 - m.b82 - m.b111 <= 0)

m.c2002 = Constraint(expr=   m.b77 - m.b83 - m.b112 <= 0)

m.c2003 = Constraint(expr=   m.b77 - m.b84 - m.b113 <= 0)

m.c2004 = Constraint(expr=   m.b77 - m.b85 - m.b114 <= 0)

m.c2005 = Constraint(expr=   m.b77 - m.b86 - m.b115 <= 0)

m.c2006 = Constraint(expr=   m.b77 - m.b87 - m.b116 <= 0)

m.c2007 = Constraint(expr=   m.b77 - m.b88 - m.b117 <= 0)

m.c2008 = Constraint(expr=   m.b77 - m.b89 - m.b118 <= 0)

m.c2009 = Constraint(expr=   m.b77 - m.b90 - m.b119 <= 0)

m.c2010 = Constraint(expr=   m.b77 - m.b91 - m.b120 <= 0)

m.c2011 = Constraint(expr=   m.b78 - m.b79 - m.b121 <= 0)

m.c2012 = Constraint(expr=   m.b78 - m.b80 - m.b122 <= 0)

m.c2013 = Constraint(expr=   m.b78 - m.b81 - m.b123 <= 0)

m.c2014 = Constraint(expr=   m.b78 - m.b82 - m.b124 <= 0)

m.c2015 = Constraint(expr=   m.b78 - m.b83 - m.b125 <= 0)

m.c2016 = Constraint(expr=   m.b78 - m.b84 - m.b126 <= 0)

m.c2017 = Constraint(expr=   m.b78 - m.b85 - m.b127 <= 0)

m.c2018 = Constraint(expr=   m.b78 - m.b86 - m.b128 <= 0)

m.c2019 = Constraint(expr=   m.b78 - m.b87 - m.b129 <= 0)

m.c2020 = Constraint(expr=   m.b78 - m.b88 - m.b130 <= 0)

m.c2021 = Constraint(expr=   m.b78 - m.b89 - m.b131 <= 0)

m.c2022 = Constraint(expr=   m.b78 - m.b90 - m.b132 <= 0)

m.c2023 = Constraint(expr=   m.b78 - m.b91 - m.b133 <= 0)

m.c2024 = Constraint(expr=   m.b79 - m.b80 - m.b134 <= 0)

m.c2025 = Constraint(expr=   m.b79 - m.b81 - m.b135 <= 0)

m.c2026 = Constraint(expr=   m.b79 - m.b82 - m.b136 <= 0)

m.c2027 = Constraint(expr=   m.b79 - m.b83 - m.b137 <= 0)

m.c2028 = Constraint(expr=   m.b79 - m.b84 - m.b138 <= 0)

m.c2029 = Constraint(expr=   m.b79 - m.b85 - m.b139 <= 0)

m.c2030 = Constraint(expr=   m.b79 - m.b86 - m.b140 <= 0)

m.c2031 = Constraint(expr=   m.b79 - m.b87 - m.b141 <= 0)

m.c2032 = Constraint(expr=   m.b79 - m.b88 - m.b142 <= 0)

m.c2033 = Constraint(expr=   m.b79 - m.b89 - m.b143 <= 0)

m.c2034 = Constraint(expr=   m.b79 - m.b90 - m.b144 <= 0)

m.c2035 = Constraint(expr=   m.b79 - m.b91 - m.b145 <= 0)

m.c2036 = Constraint(expr=   m.b80 - m.b81 - m.b146 <= 0)

m.c2037 = Constraint(expr=   m.b80 - m.b82 - m.b147 <= 0)

m.c2038 = Constraint(expr=   m.b80 - m.b83 - m.b148 <= 0)

m.c2039 = Constraint(expr=   m.b80 - m.b84 - m.b149 <= 0)

m.c2040 = Constraint(expr=   m.b80 - m.b85 - m.b150 <= 0)

m.c2041 = Constraint(expr=   m.b80 - m.b86 - m.b151 <= 0)

m.c2042 = Constraint(expr=   m.b80 - m.b87 - m.b152 <= 0)

m.c2043 = Constraint(expr=   m.b80 - m.b88 - m.b153 <= 0)

m.c2044 = Constraint(expr=   m.b80 - m.b89 - m.b154 <= 0)

m.c2045 = Constraint(expr=   m.b80 - m.b90 - m.b155 <= 0)

m.c2046 = Constraint(expr=   m.b80 - m.b91 - m.b156 <= 0)

m.c2047 = Constraint(expr=   m.b81 - m.b82 - m.b157 <= 0)

m.c2048 = Constraint(expr=   m.b81 - m.b83 - m.b158 <= 0)

m.c2049 = Constraint(expr=   m.b81 - m.b84 - m.b159 <= 0)

m.c2050 = Constraint(expr=   m.b81 - m.b85 - m.b160 <= 0)

m.c2051 = Constraint(expr=   m.b81 - m.b86 - m.b161 <= 0)

m.c2052 = Constraint(expr=   m.b81 - m.b87 - m.b162 <= 0)

m.c2053 = Constraint(expr=   m.b81 - m.b88 - m.b163 <= 0)

m.c2054 = Constraint(expr=   m.b81 - m.b89 - m.b164 <= 0)

m.c2055 = Constraint(expr=   m.b81 - m.b90 - m.b165 <= 0)

m.c2056 = Constraint(expr=   m.b81 - m.b91 - m.b211 <= 0)

m.c2057 = Constraint(expr=   m.b82 - m.b83 - m.b166 <= 0)

m.c2058 = Constraint(expr=   m.b82 - m.b84 - m.b167 <= 0)

m.c2059 = Constraint(expr=   m.b82 - m.b85 - m.b168 <= 0)

m.c2060 = Constraint(expr=   m.b82 - m.b86 - m.b169 <= 0)

m.c2061 = Constraint(expr=   m.b82 - m.b87 - m.b170 <= 0)

m.c2062 = Constraint(expr=   m.b82 - m.b88 - m.b171 <= 0)

m.c2063 = Constraint(expr=   m.b82 - m.b89 - m.b172 <= 0)

m.c2064 = Constraint(expr=   m.b82 - m.b90 - m.b173 <= 0)

m.c2065 = Constraint(expr=   m.b82 - m.b91 - m.b174 <= 0)

m.c2066 = Constraint(expr=   m.b83 - m.b84 - m.b175 <= 0)

m.c2067 = Constraint(expr=   m.b83 - m.b85 - m.b176 <= 0)

m.c2068 = Constraint(expr=   m.b83 - m.b86 - m.b177 <= 0)

m.c2069 = Constraint(expr=   m.b83 - m.b87 - m.b178 <= 0)

m.c2070 = Constraint(expr=   m.b83 - m.b88 - m.b179 <= 0)

m.c2071 = Constraint(expr=   m.b83 - m.b89 - m.b180 <= 0)

m.c2072 = Constraint(expr=   m.b83 - m.b90 - m.b181 <= 0)

m.c2073 = Constraint(expr=   m.b83 - m.b91 - m.b182 <= 0)

m.c2074 = Constraint(expr=   m.b84 - m.b85 - m.b183 <= 0)

m.c2075 = Constraint(expr=   m.b84 - m.b86 - m.b184 <= 0)

m.c2076 = Constraint(expr=   m.b84 - m.b87 - m.b185 <= 0)

m.c2077 = Constraint(expr=   m.b84 - m.b88 - m.b186 <= 0)

m.c2078 = Constraint(expr=   m.b84 - m.b89 - m.b187 <= 0)

m.c2079 = Constraint(expr=   m.b84 - m.b90 - m.b188 <= 0)

m.c2080 = Constraint(expr=   m.b84 - m.b91 - m.b189 <= 0)

m.c2081 = Constraint(expr=   m.b85 - m.b86 - m.b190 <= 0)

m.c2082 = Constraint(expr=   m.b85 - m.b87 - m.b191 <= 0)

m.c2083 = Constraint(expr=   m.b85 - m.b88 - m.b192 <= 0)

m.c2084 = Constraint(expr=   m.b85 - m.b89 - m.b193 <= 0)

m.c2085 = Constraint(expr=   m.b85 - m.b90 - m.b194 <= 0)

m.c2086 = Constraint(expr=   m.b85 - m.b91 - m.b195 <= 0)

m.c2087 = Constraint(expr=   m.b86 - m.b87 - m.b196 <= 0)

m.c2088 = Constraint(expr=   m.b86 - m.b88 - m.b197 <= 0)

m.c2089 = Constraint(expr=   m.b86 - m.b89 - m.b198 <= 0)

m.c2090 = Constraint(expr=   m.b86 - m.b90 - m.b199 <= 0)

m.c2091 = Constraint(expr=   m.b86 - m.b91 - m.b200 <= 0)

m.c2092 = Constraint(expr=   m.b87 - m.b88 - m.b201 <= 0)

m.c2093 = Constraint(expr=   m.b87 - m.b89 - m.b202 <= 0)

m.c2094 = Constraint(expr=   m.b87 - m.b90 - m.b203 <= 0)

m.c2095 = Constraint(expr=   m.b87 - m.b91 - m.b204 <= 0)

m.c2096 = Constraint(expr=   m.b88 - m.b89 - m.b205 <= 0)

m.c2097 = Constraint(expr=   m.b88 - m.b90 - m.b206 <= 0)

m.c2098 = Constraint(expr=   m.b88 - m.b91 - m.b207 <= 0)

m.c2099 = Constraint(expr=   m.b89 - m.b90 - m.b208 <= 0)

m.c2100 = Constraint(expr=   m.b89 - m.b91 - m.b209 <= 0)

m.c2101 = Constraint(expr=   m.b90 - m.b91 - m.b210 <= 0)

m.c2102 = Constraint(expr=   m.b92 - m.b93 - m.b107 <= 0)

m.c2103 = Constraint(expr=   m.b92 - m.b94 - m.b108 <= 0)

m.c2104 = Constraint(expr=   m.b92 - m.b95 - m.b109 <= 0)

m.c2105 = Constraint(expr=   m.b92 - m.b96 - m.b110 <= 0)

m.c2106 = Constraint(expr=   m.b92 - m.b97 - m.b111 <= 0)

m.c2107 = Constraint(expr=   m.b92 - m.b98 - m.b112 <= 0)

m.c2108 = Constraint(expr=   m.b92 - m.b99 - m.b113 <= 0)

m.c2109 = Constraint(expr=   m.b92 - m.b100 - m.b114 <= 0)

m.c2110 = Constraint(expr=   m.b92 - m.b101 - m.b115 <= 0)

m.c2111 = Constraint(expr=   m.b92 - m.b102 - m.b116 <= 0)

m.c2112 = Constraint(expr=   m.b92 - m.b103 - m.b117 <= 0)

m.c2113 = Constraint(expr=   m.b92 - m.b104 - m.b118 <= 0)

m.c2114 = Constraint(expr=   m.b92 - m.b105 - m.b119 <= 0)

m.c2115 = Constraint(expr=   m.b92 - m.b106 - m.b120 <= 0)

m.c2116 = Constraint(expr=   m.b93 - m.b94 - m.b121 <= 0)

m.c2117 = Constraint(expr=   m.b93 - m.b95 - m.b122 <= 0)

m.c2118 = Constraint(expr=   m.b93 - m.b96 - m.b123 <= 0)

m.c2119 = Constraint(expr=   m.b93 - m.b97 - m.b124 <= 0)

m.c2120 = Constraint(expr=   m.b93 - m.b98 - m.b125 <= 0)

m.c2121 = Constraint(expr=   m.b93 - m.b99 - m.b126 <= 0)

m.c2122 = Constraint(expr=   m.b93 - m.b100 - m.b127 <= 0)

m.c2123 = Constraint(expr=   m.b93 - m.b101 - m.b128 <= 0)

m.c2124 = Constraint(expr=   m.b93 - m.b102 - m.b129 <= 0)

m.c2125 = Constraint(expr=   m.b93 - m.b103 - m.b130 <= 0)

m.c2126 = Constraint(expr=   m.b93 - m.b104 - m.b131 <= 0)

m.c2127 = Constraint(expr=   m.b93 - m.b105 - m.b132 <= 0)

m.c2128 = Constraint(expr=   m.b93 - m.b106 - m.b133 <= 0)

m.c2129 = Constraint(expr=   m.b94 - m.b95 - m.b134 <= 0)

m.c2130 = Constraint(expr=   m.b94 - m.b96 - m.b135 <= 0)

m.c2131 = Constraint(expr=   m.b94 - m.b97 - m.b136 <= 0)

m.c2132 = Constraint(expr=   m.b94 - m.b98 - m.b137 <= 0)

m.c2133 = Constraint(expr=   m.b94 - m.b99 - m.b138 <= 0)

m.c2134 = Constraint(expr=   m.b94 - m.b100 - m.b139 <= 0)

m.c2135 = Constraint(expr=   m.b94 - m.b101 - m.b140 <= 0)

m.c2136 = Constraint(expr=   m.b94 - m.b102 - m.b141 <= 0)

m.c2137 = Constraint(expr=   m.b94 - m.b103 - m.b142 <= 0)

m.c2138 = Constraint(expr=   m.b94 - m.b104 - m.b143 <= 0)

m.c2139 = Constraint(expr=   m.b94 - m.b105 - m.b144 <= 0)

m.c2140 = Constraint(expr=   m.b94 - m.b106 - m.b145 <= 0)

m.c2141 = Constraint(expr=   m.b95 - m.b96 - m.b146 <= 0)

m.c2142 = Constraint(expr=   m.b95 - m.b97 - m.b147 <= 0)

m.c2143 = Constraint(expr=   m.b95 - m.b98 - m.b148 <= 0)

m.c2144 = Constraint(expr=   m.b95 - m.b99 - m.b149 <= 0)

m.c2145 = Constraint(expr=   m.b95 - m.b100 - m.b150 <= 0)

m.c2146 = Constraint(expr=   m.b95 - m.b101 - m.b151 <= 0)

m.c2147 = Constraint(expr=   m.b95 - m.b102 - m.b152 <= 0)

m.c2148 = Constraint(expr=   m.b95 - m.b103 - m.b153 <= 0)

m.c2149 = Constraint(expr=   m.b95 - m.b104 - m.b154 <= 0)

m.c2150 = Constraint(expr=   m.b95 - m.b105 - m.b155 <= 0)

m.c2151 = Constraint(expr=   m.b95 - m.b106 - m.b156 <= 0)

m.c2152 = Constraint(expr=   m.b96 - m.b97 - m.b157 <= 0)

m.c2153 = Constraint(expr=   m.b96 - m.b98 - m.b158 <= 0)

m.c2154 = Constraint(expr=   m.b96 - m.b99 - m.b159 <= 0)

m.c2155 = Constraint(expr=   m.b96 - m.b100 - m.b160 <= 0)

m.c2156 = Constraint(expr=   m.b96 - m.b101 - m.b161 <= 0)

m.c2157 = Constraint(expr=   m.b96 - m.b102 - m.b162 <= 0)

m.c2158 = Constraint(expr=   m.b96 - m.b103 - m.b163 <= 0)

m.c2159 = Constraint(expr=   m.b96 - m.b104 - m.b164 <= 0)

m.c2160 = Constraint(expr=   m.b96 - m.b105 - m.b165 <= 0)

m.c2161 = Constraint(expr=   m.b96 - m.b106 - m.b211 <= 0)

m.c2162 = Constraint(expr=   m.b97 - m.b98 - m.b166 <= 0)

m.c2163 = Constraint(expr=   m.b97 - m.b99 - m.b167 <= 0)

m.c2164 = Constraint(expr=   m.b97 - m.b100 - m.b168 <= 0)

m.c2165 = Constraint(expr=   m.b97 - m.b101 - m.b169 <= 0)

m.c2166 = Constraint(expr=   m.b97 - m.b102 - m.b170 <= 0)

m.c2167 = Constraint(expr=   m.b97 - m.b103 - m.b171 <= 0)

m.c2168 = Constraint(expr=   m.b97 - m.b104 - m.b172 <= 0)

m.c2169 = Constraint(expr=   m.b97 - m.b105 - m.b173 <= 0)

m.c2170 = Constraint(expr=   m.b97 - m.b106 - m.b174 <= 0)

m.c2171 = Constraint(expr=   m.b98 - m.b99 - m.b175 <= 0)

m.c2172 = Constraint(expr=   m.b98 - m.b100 - m.b176 <= 0)

m.c2173 = Constraint(expr=   m.b98 - m.b101 - m.b177 <= 0)

m.c2174 = Constraint(expr=   m.b98 - m.b102 - m.b178 <= 0)

m.c2175 = Constraint(expr=   m.b98 - m.b103 - m.b179 <= 0)

m.c2176 = Constraint(expr=   m.b98 - m.b104 - m.b180 <= 0)

m.c2177 = Constraint(expr=   m.b98 - m.b105 - m.b181 <= 0)

m.c2178 = Constraint(expr=   m.b98 - m.b106 - m.b182 <= 0)

m.c2179 = Constraint(expr=   m.b99 - m.b100 - m.b183 <= 0)

m.c2180 = Constraint(expr=   m.b99 - m.b101 - m.b184 <= 0)

m.c2181 = Constraint(expr=   m.b99 - m.b102 - m.b185 <= 0)

m.c2182 = Constraint(expr=   m.b99 - m.b103 - m.b186 <= 0)

m.c2183 = Constraint(expr=   m.b99 - m.b104 - m.b187 <= 0)

m.c2184 = Constraint(expr=   m.b99 - m.b105 - m.b188 <= 0)

m.c2185 = Constraint(expr=   m.b99 - m.b106 - m.b189 <= 0)

m.c2186 = Constraint(expr=   m.b100 - m.b101 - m.b190 <= 0)

m.c2187 = Constraint(expr=   m.b100 - m.b102 - m.b191 <= 0)

m.c2188 = Constraint(expr=   m.b100 - m.b103 - m.b192 <= 0)

m.c2189 = Constraint(expr=   m.b100 - m.b104 - m.b193 <= 0)

m.c2190 = Constraint(expr=   m.b100 - m.b105 - m.b194 <= 0)

m.c2191 = Constraint(expr=   m.b100 - m.b106 - m.b195 <= 0)

m.c2192 = Constraint(expr=   m.b101 - m.b102 - m.b196 <= 0)

m.c2193 = Constraint(expr=   m.b101 - m.b103 - m.b197 <= 0)

m.c2194 = Constraint(expr=   m.b101 - m.b104 - m.b198 <= 0)

m.c2195 = Constraint(expr=   m.b101 - m.b105 - m.b199 <= 0)

m.c2196 = Constraint(expr=   m.b101 - m.b106 - m.b200 <= 0)

m.c2197 = Constraint(expr=   m.b102 - m.b103 - m.b201 <= 0)

m.c2198 = Constraint(expr=   m.b102 - m.b104 - m.b202 <= 0)

m.c2199 = Constraint(expr=   m.b102 - m.b105 - m.b203 <= 0)

m.c2200 = Constraint(expr=   m.b102 - m.b106 - m.b204 <= 0)

m.c2201 = Constraint(expr=   m.b103 - m.b104 - m.b205 <= 0)

m.c2202 = Constraint(expr=   m.b103 - m.b105 - m.b206 <= 0)

m.c2203 = Constraint(expr=   m.b103 - m.b106 - m.b207 <= 0)

m.c2204 = Constraint(expr=   m.b104 - m.b105 - m.b208 <= 0)

m.c2205 = Constraint(expr=   m.b104 - m.b106 - m.b209 <= 0)

m.c2206 = Constraint(expr=   m.b105 - m.b106 - m.b210 <= 0)

m.c2207 = Constraint(expr=   m.b107 - m.b108 - m.b121 <= 0)

m.c2208 = Constraint(expr=   m.b107 - m.b109 - m.b122 <= 0)

m.c2209 = Constraint(expr=   m.b107 - m.b110 - m.b123 <= 0)

m.c2210 = Constraint(expr=   m.b107 - m.b111 - m.b124 <= 0)

m.c2211 = Constraint(expr=   m.b107 - m.b112 - m.b125 <= 0)

m.c2212 = Constraint(expr=   m.b107 - m.b113 - m.b126 <= 0)

m.c2213 = Constraint(expr=   m.b107 - m.b114 - m.b127 <= 0)

m.c2214 = Constraint(expr=   m.b107 - m.b115 - m.b128 <= 0)

m.c2215 = Constraint(expr=   m.b107 - m.b116 - m.b129 <= 0)

m.c2216 = Constraint(expr=   m.b107 - m.b117 - m.b130 <= 0)

m.c2217 = Constraint(expr=   m.b107 - m.b118 - m.b131 <= 0)

m.c2218 = Constraint(expr=   m.b107 - m.b119 - m.b132 <= 0)

m.c2219 = Constraint(expr=   m.b107 - m.b120 - m.b133 <= 0)

m.c2220 = Constraint(expr=   m.b108 - m.b109 - m.b134 <= 0)

m.c2221 = Constraint(expr=   m.b108 - m.b110 - m.b135 <= 0)

m.c2222 = Constraint(expr=   m.b108 - m.b111 - m.b136 <= 0)

m.c2223 = Constraint(expr=   m.b108 - m.b112 - m.b137 <= 0)

m.c2224 = Constraint(expr=   m.b108 - m.b113 - m.b138 <= 0)

m.c2225 = Constraint(expr=   m.b108 - m.b114 - m.b139 <= 0)

m.c2226 = Constraint(expr=   m.b108 - m.b115 - m.b140 <= 0)

m.c2227 = Constraint(expr=   m.b108 - m.b116 - m.b141 <= 0)

m.c2228 = Constraint(expr=   m.b108 - m.b117 - m.b142 <= 0)

m.c2229 = Constraint(expr=   m.b108 - m.b118 - m.b143 <= 0)

m.c2230 = Constraint(expr=   m.b108 - m.b119 - m.b144 <= 0)

m.c2231 = Constraint(expr=   m.b108 - m.b120 - m.b145 <= 0)

m.c2232 = Constraint(expr=   m.b109 - m.b110 - m.b146 <= 0)

m.c2233 = Constraint(expr=   m.b109 - m.b111 - m.b147 <= 0)

m.c2234 = Constraint(expr=   m.b109 - m.b112 - m.b148 <= 0)

m.c2235 = Constraint(expr=   m.b109 - m.b113 - m.b149 <= 0)

m.c2236 = Constraint(expr=   m.b109 - m.b114 - m.b150 <= 0)

m.c2237 = Constraint(expr=   m.b109 - m.b115 - m.b151 <= 0)

m.c2238 = Constraint(expr=   m.b109 - m.b116 - m.b152 <= 0)

m.c2239 = Constraint(expr=   m.b109 - m.b117 - m.b153 <= 0)

m.c2240 = Constraint(expr=   m.b109 - m.b118 - m.b154 <= 0)

m.c2241 = Constraint(expr=   m.b109 - m.b119 - m.b155 <= 0)

m.c2242 = Constraint(expr=   m.b109 - m.b120 - m.b156 <= 0)

m.c2243 = Constraint(expr=   m.b110 - m.b111 - m.b157 <= 0)

m.c2244 = Constraint(expr=   m.b110 - m.b112 - m.b158 <= 0)

m.c2245 = Constraint(expr=   m.b110 - m.b113 - m.b159 <= 0)

m.c2246 = Constraint(expr=   m.b110 - m.b114 - m.b160 <= 0)

m.c2247 = Constraint(expr=   m.b110 - m.b115 - m.b161 <= 0)

m.c2248 = Constraint(expr=   m.b110 - m.b116 - m.b162 <= 0)

m.c2249 = Constraint(expr=   m.b110 - m.b117 - m.b163 <= 0)

m.c2250 = Constraint(expr=   m.b110 - m.b118 - m.b164 <= 0)

m.c2251 = Constraint(expr=   m.b110 - m.b119 - m.b165 <= 0)

m.c2252 = Constraint(expr=   m.b110 - m.b120 - m.b211 <= 0)

m.c2253 = Constraint(expr=   m.b111 - m.b112 - m.b166 <= 0)

m.c2254 = Constraint(expr=   m.b111 - m.b113 - m.b167 <= 0)

m.c2255 = Constraint(expr=   m.b111 - m.b114 - m.b168 <= 0)

m.c2256 = Constraint(expr=   m.b111 - m.b115 - m.b169 <= 0)

m.c2257 = Constraint(expr=   m.b111 - m.b116 - m.b170 <= 0)

m.c2258 = Constraint(expr=   m.b111 - m.b117 - m.b171 <= 0)

m.c2259 = Constraint(expr=   m.b111 - m.b118 - m.b172 <= 0)

m.c2260 = Constraint(expr=   m.b111 - m.b119 - m.b173 <= 0)

m.c2261 = Constraint(expr=   m.b111 - m.b120 - m.b174 <= 0)

m.c2262 = Constraint(expr=   m.b112 - m.b113 - m.b175 <= 0)

m.c2263 = Constraint(expr=   m.b112 - m.b114 - m.b176 <= 0)

m.c2264 = Constraint(expr=   m.b112 - m.b115 - m.b177 <= 0)

m.c2265 = Constraint(expr=   m.b112 - m.b116 - m.b178 <= 0)

m.c2266 = Constraint(expr=   m.b112 - m.b117 - m.b179 <= 0)

m.c2267 = Constraint(expr=   m.b112 - m.b118 - m.b180 <= 0)

m.c2268 = Constraint(expr=   m.b112 - m.b119 - m.b181 <= 0)

m.c2269 = Constraint(expr=   m.b112 - m.b120 - m.b182 <= 0)

m.c2270 = Constraint(expr=   m.b113 - m.b114 - m.b183 <= 0)

m.c2271 = Constraint(expr=   m.b113 - m.b115 - m.b184 <= 0)

m.c2272 = Constraint(expr=   m.b113 - m.b116 - m.b185 <= 0)

m.c2273 = Constraint(expr=   m.b113 - m.b117 - m.b186 <= 0)

m.c2274 = Constraint(expr=   m.b113 - m.b118 - m.b187 <= 0)

m.c2275 = Constraint(expr=   m.b113 - m.b119 - m.b188 <= 0)

m.c2276 = Constraint(expr=   m.b113 - m.b120 - m.b189 <= 0)

m.c2277 = Constraint(expr=   m.b114 - m.b115 - m.b190 <= 0)

m.c2278 = Constraint(expr=   m.b114 - m.b116 - m.b191 <= 0)

m.c2279 = Constraint(expr=   m.b114 - m.b117 - m.b192 <= 0)

m.c2280 = Constraint(expr=   m.b114 - m.b118 - m.b193 <= 0)

m.c2281 = Constraint(expr=   m.b114 - m.b119 - m.b194 <= 0)

m.c2282 = Constraint(expr=   m.b114 - m.b120 - m.b195 <= 0)

m.c2283 = Constraint(expr=   m.b115 - m.b116 - m.b196 <= 0)

m.c2284 = Constraint(expr=   m.b115 - m.b117 - m.b197 <= 0)

m.c2285 = Constraint(expr=   m.b115 - m.b118 - m.b198 <= 0)

m.c2286 = Constraint(expr=   m.b115 - m.b119 - m.b199 <= 0)

m.c2287 = Constraint(expr=   m.b115 - m.b120 - m.b200 <= 0)

m.c2288 = Constraint(expr=   m.b116 - m.b117 - m.b201 <= 0)

m.c2289 = Constraint(expr=   m.b116 - m.b118 - m.b202 <= 0)

m.c2290 = Constraint(expr=   m.b116 - m.b119 - m.b203 <= 0)

m.c2291 = Constraint(expr=   m.b116 - m.b120 - m.b204 <= 0)

m.c2292 = Constraint(expr=   m.b117 - m.b118 - m.b205 <= 0)

m.c2293 = Constraint(expr=   m.b117 - m.b119 - m.b206 <= 0)

m.c2294 = Constraint(expr=   m.b117 - m.b120 - m.b207 <= 0)

m.c2295 = Constraint(expr=   m.b118 - m.b119 - m.b208 <= 0)

m.c2296 = Constraint(expr=   m.b118 - m.b120 - m.b209 <= 0)

m.c2297 = Constraint(expr=   m.b119 - m.b120 - m.b210 <= 0)

m.c2298 = Constraint(expr=   m.b121 - m.b122 - m.b134 <= 0)

m.c2299 = Constraint(expr=   m.b121 - m.b123 - m.b135 <= 0)

m.c2300 = Constraint(expr=   m.b121 - m.b124 - m.b136 <= 0)

m.c2301 = Constraint(expr=   m.b121 - m.b125 - m.b137 <= 0)

m.c2302 = Constraint(expr=   m.b121 - m.b126 - m.b138 <= 0)

m.c2303 = Constraint(expr=   m.b121 - m.b127 - m.b139 <= 0)

m.c2304 = Constraint(expr=   m.b121 - m.b128 - m.b140 <= 0)

m.c2305 = Constraint(expr=   m.b121 - m.b129 - m.b141 <= 0)

m.c2306 = Constraint(expr=   m.b121 - m.b130 - m.b142 <= 0)

m.c2307 = Constraint(expr=   m.b121 - m.b131 - m.b143 <= 0)

m.c2308 = Constraint(expr=   m.b121 - m.b132 - m.b144 <= 0)

m.c2309 = Constraint(expr=   m.b121 - m.b133 - m.b145 <= 0)

m.c2310 = Constraint(expr=   m.b122 - m.b123 - m.b146 <= 0)

m.c2311 = Constraint(expr=   m.b122 - m.b124 - m.b147 <= 0)

m.c2312 = Constraint(expr=   m.b122 - m.b125 - m.b148 <= 0)

m.c2313 = Constraint(expr=   m.b122 - m.b126 - m.b149 <= 0)

m.c2314 = Constraint(expr=   m.b122 - m.b127 - m.b150 <= 0)

m.c2315 = Constraint(expr=   m.b122 - m.b128 - m.b151 <= 0)

m.c2316 = Constraint(expr=   m.b122 - m.b129 - m.b152 <= 0)

m.c2317 = Constraint(expr=   m.b122 - m.b130 - m.b153 <= 0)

m.c2318 = Constraint(expr=   m.b122 - m.b131 - m.b154 <= 0)

m.c2319 = Constraint(expr=   m.b122 - m.b132 - m.b155 <= 0)

m.c2320 = Constraint(expr=   m.b122 - m.b133 - m.b156 <= 0)

m.c2321 = Constraint(expr=   m.b123 - m.b124 - m.b157 <= 0)

m.c2322 = Constraint(expr=   m.b123 - m.b125 - m.b158 <= 0)

m.c2323 = Constraint(expr=   m.b123 - m.b126 - m.b159 <= 0)

m.c2324 = Constraint(expr=   m.b123 - m.b127 - m.b160 <= 0)

m.c2325 = Constraint(expr=   m.b123 - m.b128 - m.b161 <= 0)

m.c2326 = Constraint(expr=   m.b123 - m.b129 - m.b162 <= 0)

m.c2327 = Constraint(expr=   m.b123 - m.b130 - m.b163 <= 0)

m.c2328 = Constraint(expr=   m.b123 - m.b131 - m.b164 <= 0)

m.c2329 = Constraint(expr=   m.b123 - m.b132 - m.b165 <= 0)

m.c2330 = Constraint(expr=   m.b123 - m.b133 - m.b211 <= 0)

m.c2331 = Constraint(expr=   m.b124 - m.b125 - m.b166 <= 0)

m.c2332 = Constraint(expr=   m.b124 - m.b126 - m.b167 <= 0)

m.c2333 = Constraint(expr=   m.b124 - m.b127 - m.b168 <= 0)

m.c2334 = Constraint(expr=   m.b124 - m.b128 - m.b169 <= 0)

m.c2335 = Constraint(expr=   m.b124 - m.b129 - m.b170 <= 0)

m.c2336 = Constraint(expr=   m.b124 - m.b130 - m.b171 <= 0)

m.c2337 = Constraint(expr=   m.b124 - m.b131 - m.b172 <= 0)

m.c2338 = Constraint(expr=   m.b124 - m.b132 - m.b173 <= 0)

m.c2339 = Constraint(expr=   m.b124 - m.b133 - m.b174 <= 0)

m.c2340 = Constraint(expr=   m.b125 - m.b126 - m.b175 <= 0)

m.c2341 = Constraint(expr=   m.b125 - m.b127 - m.b176 <= 0)

m.c2342 = Constraint(expr=   m.b125 - m.b128 - m.b177 <= 0)

m.c2343 = Constraint(expr=   m.b125 - m.b129 - m.b178 <= 0)

m.c2344 = Constraint(expr=   m.b125 - m.b130 - m.b179 <= 0)

m.c2345 = Constraint(expr=   m.b125 - m.b131 - m.b180 <= 0)

m.c2346 = Constraint(expr=   m.b125 - m.b132 - m.b181 <= 0)

m.c2347 = Constraint(expr=   m.b125 - m.b133 - m.b182 <= 0)

m.c2348 = Constraint(expr=   m.b126 - m.b127 - m.b183 <= 0)

m.c2349 = Constraint(expr=   m.b126 - m.b128 - m.b184 <= 0)

m.c2350 = Constraint(expr=   m.b126 - m.b129 - m.b185 <= 0)

m.c2351 = Constraint(expr=   m.b126 - m.b130 - m.b186 <= 0)

m.c2352 = Constraint(expr=   m.b126 - m.b131 - m.b187 <= 0)

m.c2353 = Constraint(expr=   m.b126 - m.b132 - m.b188 <= 0)

m.c2354 = Constraint(expr=   m.b126 - m.b133 - m.b189 <= 0)

m.c2355 = Constraint(expr=   m.b127 - m.b128 - m.b190 <= 0)

m.c2356 = Constraint(expr=   m.b127 - m.b129 - m.b191 <= 0)

m.c2357 = Constraint(expr=   m.b127 - m.b130 - m.b192 <= 0)

m.c2358 = Constraint(expr=   m.b127 - m.b131 - m.b193 <= 0)

m.c2359 = Constraint(expr=   m.b127 - m.b132 - m.b194 <= 0)

m.c2360 = Constraint(expr=   m.b127 - m.b133 - m.b195 <= 0)

m.c2361 = Constraint(expr=   m.b128 - m.b129 - m.b196 <= 0)

m.c2362 = Constraint(expr=   m.b128 - m.b130 - m.b197 <= 0)

m.c2363 = Constraint(expr=   m.b128 - m.b131 - m.b198 <= 0)

m.c2364 = Constraint(expr=   m.b128 - m.b132 - m.b199 <= 0)

m.c2365 = Constraint(expr=   m.b128 - m.b133 - m.b200 <= 0)

m.c2366 = Constraint(expr=   m.b129 - m.b130 - m.b201 <= 0)

m.c2367 = Constraint(expr=   m.b129 - m.b131 - m.b202 <= 0)

m.c2368 = Constraint(expr=   m.b129 - m.b132 - m.b203 <= 0)

m.c2369 = Constraint(expr=   m.b129 - m.b133 - m.b204 <= 0)

m.c2370 = Constraint(expr=   m.b130 - m.b131 - m.b205 <= 0)

m.c2371 = Constraint(expr=   m.b130 - m.b132 - m.b206 <= 0)

m.c2372 = Constraint(expr=   m.b130 - m.b133 - m.b207 <= 0)

m.c2373 = Constraint(expr=   m.b131 - m.b132 - m.b208 <= 0)

m.c2374 = Constraint(expr=   m.b131 - m.b133 - m.b209 <= 0)

m.c2375 = Constraint(expr=   m.b132 - m.b133 - m.b210 <= 0)

m.c2376 = Constraint(expr=   m.b134 - m.b135 - m.b146 <= 0)

m.c2377 = Constraint(expr=   m.b134 - m.b136 - m.b147 <= 0)

m.c2378 = Constraint(expr=   m.b134 - m.b137 - m.b148 <= 0)

m.c2379 = Constraint(expr=   m.b134 - m.b138 - m.b149 <= 0)

m.c2380 = Constraint(expr=   m.b134 - m.b139 - m.b150 <= 0)

m.c2381 = Constraint(expr=   m.b134 - m.b140 - m.b151 <= 0)

m.c2382 = Constraint(expr=   m.b134 - m.b141 - m.b152 <= 0)

m.c2383 = Constraint(expr=   m.b134 - m.b142 - m.b153 <= 0)

m.c2384 = Constraint(expr=   m.b134 - m.b143 - m.b154 <= 0)

m.c2385 = Constraint(expr=   m.b134 - m.b144 - m.b155 <= 0)

m.c2386 = Constraint(expr=   m.b134 - m.b145 - m.b156 <= 0)

m.c2387 = Constraint(expr=   m.b135 - m.b136 - m.b157 <= 0)

m.c2388 = Constraint(expr=   m.b135 - m.b137 - m.b158 <= 0)

m.c2389 = Constraint(expr=   m.b135 - m.b138 - m.b159 <= 0)

m.c2390 = Constraint(expr=   m.b135 - m.b139 - m.b160 <= 0)

m.c2391 = Constraint(expr=   m.b135 - m.b140 - m.b161 <= 0)

m.c2392 = Constraint(expr=   m.b135 - m.b141 - m.b162 <= 0)

m.c2393 = Constraint(expr=   m.b135 - m.b142 - m.b163 <= 0)

m.c2394 = Constraint(expr=   m.b135 - m.b143 - m.b164 <= 0)

m.c2395 = Constraint(expr=   m.b135 - m.b144 - m.b165 <= 0)

m.c2396 = Constraint(expr=   m.b135 - m.b145 - m.b211 <= 0)

m.c2397 = Constraint(expr=   m.b136 - m.b137 - m.b166 <= 0)

m.c2398 = Constraint(expr=   m.b136 - m.b138 - m.b167 <= 0)

m.c2399 = Constraint(expr=   m.b136 - m.b139 - m.b168 <= 0)

m.c2400 = Constraint(expr=   m.b136 - m.b140 - m.b169 <= 0)

m.c2401 = Constraint(expr=   m.b136 - m.b141 - m.b170 <= 0)

m.c2402 = Constraint(expr=   m.b136 - m.b142 - m.b171 <= 0)

m.c2403 = Constraint(expr=   m.b136 - m.b143 - m.b172 <= 0)

m.c2404 = Constraint(expr=   m.b136 - m.b144 - m.b173 <= 0)

m.c2405 = Constraint(expr=   m.b136 - m.b145 - m.b174 <= 0)

m.c2406 = Constraint(expr=   m.b137 - m.b138 - m.b175 <= 0)

m.c2407 = Constraint(expr=   m.b137 - m.b139 - m.b176 <= 0)

m.c2408 = Constraint(expr=   m.b137 - m.b140 - m.b177 <= 0)

m.c2409 = Constraint(expr=   m.b137 - m.b141 - m.b178 <= 0)

m.c2410 = Constraint(expr=   m.b137 - m.b142 - m.b179 <= 0)

m.c2411 = Constraint(expr=   m.b137 - m.b143 - m.b180 <= 0)

m.c2412 = Constraint(expr=   m.b137 - m.b144 - m.b181 <= 0)

m.c2413 = Constraint(expr=   m.b137 - m.b145 - m.b182 <= 0)

m.c2414 = Constraint(expr=   m.b138 - m.b139 - m.b183 <= 0)

m.c2415 = Constraint(expr=   m.b138 - m.b140 - m.b184 <= 0)

m.c2416 = Constraint(expr=   m.b138 - m.b141 - m.b185 <= 0)

m.c2417 = Constraint(expr=   m.b138 - m.b142 - m.b186 <= 0)

m.c2418 = Constraint(expr=   m.b138 - m.b143 - m.b187 <= 0)

m.c2419 = Constraint(expr=   m.b138 - m.b144 - m.b188 <= 0)

m.c2420 = Constraint(expr=   m.b138 - m.b145 - m.b189 <= 0)

m.c2421 = Constraint(expr=   m.b139 - m.b140 - m.b190 <= 0)

m.c2422 = Constraint(expr=   m.b139 - m.b141 - m.b191 <= 0)

m.c2423 = Constraint(expr=   m.b139 - m.b142 - m.b192 <= 0)

m.c2424 = Constraint(expr=   m.b139 - m.b143 - m.b193 <= 0)

m.c2425 = Constraint(expr=   m.b139 - m.b144 - m.b194 <= 0)

m.c2426 = Constraint(expr=   m.b139 - m.b145 - m.b195 <= 0)

m.c2427 = Constraint(expr=   m.b140 - m.b141 - m.b196 <= 0)

m.c2428 = Constraint(expr=   m.b140 - m.b142 - m.b197 <= 0)

m.c2429 = Constraint(expr=   m.b140 - m.b143 - m.b198 <= 0)

m.c2430 = Constraint(expr=   m.b140 - m.b144 - m.b199 <= 0)

m.c2431 = Constraint(expr=   m.b140 - m.b145 - m.b200 <= 0)

m.c2432 = Constraint(expr=   m.b141 - m.b142 - m.b201 <= 0)

m.c2433 = Constraint(expr=   m.b141 - m.b143 - m.b202 <= 0)

m.c2434 = Constraint(expr=   m.b141 - m.b144 - m.b203 <= 0)

m.c2435 = Constraint(expr=   m.b141 - m.b145 - m.b204 <= 0)

m.c2436 = Constraint(expr=   m.b142 - m.b143 - m.b205 <= 0)

m.c2437 = Constraint(expr=   m.b142 - m.b144 - m.b206 <= 0)

m.c2438 = Constraint(expr=   m.b142 - m.b145 - m.b207 <= 0)

m.c2439 = Constraint(expr=   m.b143 - m.b144 - m.b208 <= 0)

m.c2440 = Constraint(expr=   m.b143 - m.b145 - m.b209 <= 0)

m.c2441 = Constraint(expr=   m.b144 - m.b145 - m.b210 <= 0)

m.c2442 = Constraint(expr=   m.b146 - m.b147 - m.b157 <= 0)

m.c2443 = Constraint(expr=   m.b146 - m.b148 - m.b158 <= 0)

m.c2444 = Constraint(expr=   m.b146 - m.b149 - m.b159 <= 0)

m.c2445 = Constraint(expr=   m.b146 - m.b150 - m.b160 <= 0)

m.c2446 = Constraint(expr=   m.b146 - m.b151 - m.b161 <= 0)

m.c2447 = Constraint(expr=   m.b146 - m.b152 - m.b162 <= 0)

m.c2448 = Constraint(expr=   m.b146 - m.b153 - m.b163 <= 0)

m.c2449 = Constraint(expr=   m.b146 - m.b154 - m.b164 <= 0)

m.c2450 = Constraint(expr=   m.b146 - m.b155 - m.b165 <= 0)

m.c2451 = Constraint(expr=   m.b146 - m.b156 - m.b211 <= 0)

m.c2452 = Constraint(expr=   m.b147 - m.b148 - m.b166 <= 0)

m.c2453 = Constraint(expr=   m.b147 - m.b149 - m.b167 <= 0)

m.c2454 = Constraint(expr=   m.b147 - m.b150 - m.b168 <= 0)

m.c2455 = Constraint(expr=   m.b147 - m.b151 - m.b169 <= 0)

m.c2456 = Constraint(expr=   m.b147 - m.b152 - m.b170 <= 0)

m.c2457 = Constraint(expr=   m.b147 - m.b153 - m.b171 <= 0)

m.c2458 = Constraint(expr=   m.b147 - m.b154 - m.b172 <= 0)

m.c2459 = Constraint(expr=   m.b147 - m.b155 - m.b173 <= 0)

m.c2460 = Constraint(expr=   m.b147 - m.b156 - m.b174 <= 0)

m.c2461 = Constraint(expr=   m.b148 - m.b149 - m.b175 <= 0)

m.c2462 = Constraint(expr=   m.b148 - m.b150 - m.b176 <= 0)

m.c2463 = Constraint(expr=   m.b148 - m.b151 - m.b177 <= 0)

m.c2464 = Constraint(expr=   m.b148 - m.b152 - m.b178 <= 0)

m.c2465 = Constraint(expr=   m.b148 - m.b153 - m.b179 <= 0)

m.c2466 = Constraint(expr=   m.b148 - m.b154 - m.b180 <= 0)

m.c2467 = Constraint(expr=   m.b148 - m.b155 - m.b181 <= 0)

m.c2468 = Constraint(expr=   m.b148 - m.b156 - m.b182 <= 0)

m.c2469 = Constraint(expr=   m.b149 - m.b150 - m.b183 <= 0)

m.c2470 = Constraint(expr=   m.b149 - m.b151 - m.b184 <= 0)

m.c2471 = Constraint(expr=   m.b149 - m.b152 - m.b185 <= 0)

m.c2472 = Constraint(expr=   m.b149 - m.b153 - m.b186 <= 0)

m.c2473 = Constraint(expr=   m.b149 - m.b154 - m.b187 <= 0)

m.c2474 = Constraint(expr=   m.b149 - m.b155 - m.b188 <= 0)

m.c2475 = Constraint(expr=   m.b149 - m.b156 - m.b189 <= 0)

m.c2476 = Constraint(expr=   m.b150 - m.b151 - m.b190 <= 0)

m.c2477 = Constraint(expr=   m.b150 - m.b152 - m.b191 <= 0)

m.c2478 = Constraint(expr=   m.b150 - m.b153 - m.b192 <= 0)

m.c2479 = Constraint(expr=   m.b150 - m.b154 - m.b193 <= 0)

m.c2480 = Constraint(expr=   m.b150 - m.b155 - m.b194 <= 0)

m.c2481 = Constraint(expr=   m.b150 - m.b156 - m.b195 <= 0)

m.c2482 = Constraint(expr=   m.b151 - m.b152 - m.b196 <= 0)

m.c2483 = Constraint(expr=   m.b151 - m.b153 - m.b197 <= 0)

m.c2484 = Constraint(expr=   m.b151 - m.b154 - m.b198 <= 0)

m.c2485 = Constraint(expr=   m.b151 - m.b155 - m.b199 <= 0)

m.c2486 = Constraint(expr=   m.b151 - m.b156 - m.b200 <= 0)

m.c2487 = Constraint(expr=   m.b152 - m.b153 - m.b201 <= 0)

m.c2488 = Constraint(expr=   m.b152 - m.b154 - m.b202 <= 0)

m.c2489 = Constraint(expr=   m.b152 - m.b155 - m.b203 <= 0)

m.c2490 = Constraint(expr=   m.b152 - m.b156 - m.b204 <= 0)

m.c2491 = Constraint(expr=   m.b153 - m.b154 - m.b205 <= 0)

m.c2492 = Constraint(expr=   m.b153 - m.b155 - m.b206 <= 0)

m.c2493 = Constraint(expr=   m.b153 - m.b156 - m.b207 <= 0)

m.c2494 = Constraint(expr=   m.b154 - m.b155 - m.b208 <= 0)

m.c2495 = Constraint(expr=   m.b154 - m.b156 - m.b209 <= 0)

m.c2496 = Constraint(expr=   m.b155 - m.b156 - m.b210 <= 0)

m.c2497 = Constraint(expr=   m.b157 - m.b158 - m.b166 <= 0)

m.c2498 = Constraint(expr=   m.b157 - m.b159 - m.b167 <= 0)

m.c2499 = Constraint(expr=   m.b157 - m.b160 - m.b168 <= 0)

m.c2500 = Constraint(expr=   m.b157 - m.b161 - m.b169 <= 0)

m.c2501 = Constraint(expr=   m.b157 - m.b162 - m.b170 <= 0)

m.c2502 = Constraint(expr=   m.b157 - m.b163 - m.b171 <= 0)

m.c2503 = Constraint(expr=   m.b157 - m.b164 - m.b172 <= 0)

m.c2504 = Constraint(expr=   m.b157 - m.b165 - m.b173 <= 0)

m.c2505 = Constraint(expr=   m.b157 - m.b174 - m.b211 <= 0)

m.c2506 = Constraint(expr=   m.b158 - m.b159 - m.b175 <= 0)

m.c2507 = Constraint(expr=   m.b158 - m.b160 - m.b176 <= 0)

m.c2508 = Constraint(expr=   m.b158 - m.b161 - m.b177 <= 0)

m.c2509 = Constraint(expr=   m.b158 - m.b162 - m.b178 <= 0)

m.c2510 = Constraint(expr=   m.b158 - m.b163 - m.b179 <= 0)

m.c2511 = Constraint(expr=   m.b158 - m.b164 - m.b180 <= 0)

m.c2512 = Constraint(expr=   m.b158 - m.b165 - m.b181 <= 0)

m.c2513 = Constraint(expr=   m.b158 - m.b182 - m.b211 <= 0)

m.c2514 = Constraint(expr=   m.b159 - m.b160 - m.b183 <= 0)

m.c2515 = Constraint(expr=   m.b159 - m.b161 - m.b184 <= 0)

m.c2516 = Constraint(expr=   m.b159 - m.b162 - m.b185 <= 0)

m.c2517 = Constraint(expr=   m.b159 - m.b163 - m.b186 <= 0)

m.c2518 = Constraint(expr=   m.b159 - m.b164 - m.b187 <= 0)

m.c2519 = Constraint(expr=   m.b159 - m.b165 - m.b188 <= 0)

m.c2520 = Constraint(expr=   m.b159 - m.b189 - m.b211 <= 0)

m.c2521 = Constraint(expr=   m.b160 - m.b161 - m.b190 <= 0)

m.c2522 = Constraint(expr=   m.b160 - m.b162 - m.b191 <= 0)

m.c2523 = Constraint(expr=   m.b160 - m.b163 - m.b192 <= 0)

m.c2524 = Constraint(expr=   m.b160 - m.b164 - m.b193 <= 0)

m.c2525 = Constraint(expr=   m.b160 - m.b165 - m.b194 <= 0)

m.c2526 = Constraint(expr=   m.b160 - m.b195 - m.b211 <= 0)

m.c2527 = Constraint(expr=   m.b161 - m.b162 - m.b196 <= 0)

m.c2528 = Constraint(expr=   m.b161 - m.b163 - m.b197 <= 0)

m.c2529 = Constraint(expr=   m.b161 - m.b164 - m.b198 <= 0)

m.c2530 = Constraint(expr=   m.b161 - m.b165 - m.b199 <= 0)

m.c2531 = Constraint(expr=   m.b161 - m.b200 - m.b211 <= 0)

m.c2532 = Constraint(expr=   m.b162 - m.b163 - m.b201 <= 0)

m.c2533 = Constraint(expr=   m.b162 - m.b164 - m.b202 <= 0)

m.c2534 = Constraint(expr=   m.b162 - m.b165 - m.b203 <= 0)

m.c2535 = Constraint(expr=   m.b162 - m.b204 - m.b211 <= 0)

m.c2536 = Constraint(expr=   m.b163 - m.b164 - m.b205 <= 0)

m.c2537 = Constraint(expr=   m.b163 - m.b165 - m.b206 <= 0)

m.c2538 = Constraint(expr=   m.b163 - m.b207 - m.b211 <= 0)

m.c2539 = Constraint(expr=   m.b164 - m.b165 - m.b208 <= 0)

m.c2540 = Constraint(expr=   m.b164 - m.b209 - m.b211 <= 0)

m.c2541 = Constraint(expr=   m.b165 - m.b210 - m.b211 <= 0)

m.c2542 = Constraint(expr=   m.b166 - m.b167 - m.b175 <= 0)

m.c2543 = Constraint(expr=   m.b166 - m.b168 - m.b176 <= 0)

m.c2544 = Constraint(expr=   m.b166 - m.b169 - m.b177 <= 0)

m.c2545 = Constraint(expr=   m.b166 - m.b170 - m.b178 <= 0)

m.c2546 = Constraint(expr=   m.b166 - m.b171 - m.b179 <= 0)

m.c2547 = Constraint(expr=   m.b166 - m.b172 - m.b180 <= 0)

m.c2548 = Constraint(expr=   m.b166 - m.b173 - m.b181 <= 0)

m.c2549 = Constraint(expr=   m.b166 - m.b174 - m.b182 <= 0)

m.c2550 = Constraint(expr=   m.b167 - m.b168 - m.b183 <= 0)

m.c2551 = Constraint(expr=   m.b167 - m.b169 - m.b184 <= 0)

m.c2552 = Constraint(expr=   m.b167 - m.b170 - m.b185 <= 0)

m.c2553 = Constraint(expr=   m.b167 - m.b171 - m.b186 <= 0)

m.c2554 = Constraint(expr=   m.b167 - m.b172 - m.b187 <= 0)

m.c2555 = Constraint(expr=   m.b167 - m.b173 - m.b188 <= 0)

m.c2556 = Constraint(expr=   m.b167 - m.b174 - m.b189 <= 0)

m.c2557 = Constraint(expr=   m.b168 - m.b169 - m.b190 <= 0)

m.c2558 = Constraint(expr=   m.b168 - m.b170 - m.b191 <= 0)

m.c2559 = Constraint(expr=   m.b168 - m.b171 - m.b192 <= 0)

m.c2560 = Constraint(expr=   m.b168 - m.b172 - m.b193 <= 0)

m.c2561 = Constraint(expr=   m.b168 - m.b173 - m.b194 <= 0)

m.c2562 = Constraint(expr=   m.b168 - m.b174 - m.b195 <= 0)

m.c2563 = Constraint(expr=   m.b169 - m.b170 - m.b196 <= 0)

m.c2564 = Constraint(expr=   m.b169 - m.b171 - m.b197 <= 0)

m.c2565 = Constraint(expr=   m.b169 - m.b172 - m.b198 <= 0)

m.c2566 = Constraint(expr=   m.b169 - m.b173 - m.b199 <= 0)

m.c2567 = Constraint(expr=   m.b169 - m.b174 - m.b200 <= 0)

m.c2568 = Constraint(expr=   m.b170 - m.b171 - m.b201 <= 0)

m.c2569 = Constraint(expr=   m.b170 - m.b172 - m.b202 <= 0)

m.c2570 = Constraint(expr=   m.b170 - m.b173 - m.b203 <= 0)

m.c2571 = Constraint(expr=   m.b170 - m.b174 - m.b204 <= 0)

m.c2572 = Constraint(expr=   m.b171 - m.b172 - m.b205 <= 0)

m.c2573 = Constraint(expr=   m.b171 - m.b173 - m.b206 <= 0)

m.c2574 = Constraint(expr=   m.b171 - m.b174 - m.b207 <= 0)

m.c2575 = Constraint(expr=   m.b172 - m.b173 - m.b208 <= 0)

m.c2576 = Constraint(expr=   m.b172 - m.b174 - m.b209 <= 0)

m.c2577 = Constraint(expr=   m.b173 - m.b174 - m.b210 <= 0)

m.c2578 = Constraint(expr=   m.b175 - m.b176 - m.b183 <= 0)

m.c2579 = Constraint(expr=   m.b175 - m.b177 - m.b184 <= 0)

m.c2580 = Constraint(expr=   m.b175 - m.b178 - m.b185 <= 0)

m.c2581 = Constraint(expr=   m.b175 - m.b179 - m.b186 <= 0)

m.c2582 = Constraint(expr=   m.b175 - m.b180 - m.b187 <= 0)

m.c2583 = Constraint(expr=   m.b175 - m.b181 - m.b188 <= 0)

m.c2584 = Constraint(expr=   m.b175 - m.b182 - m.b189 <= 0)

m.c2585 = Constraint(expr=   m.b176 - m.b177 - m.b190 <= 0)

m.c2586 = Constraint(expr=   m.b176 - m.b178 - m.b191 <= 0)

m.c2587 = Constraint(expr=   m.b176 - m.b179 - m.b192 <= 0)

m.c2588 = Constraint(expr=   m.b176 - m.b180 - m.b193 <= 0)

m.c2589 = Constraint(expr=   m.b176 - m.b181 - m.b194 <= 0)

m.c2590 = Constraint(expr=   m.b176 - m.b182 - m.b195 <= 0)

m.c2591 = Constraint(expr=   m.b177 - m.b178 - m.b196 <= 0)

m.c2592 = Constraint(expr=   m.b177 - m.b179 - m.b197 <= 0)

m.c2593 = Constraint(expr=   m.b177 - m.b180 - m.b198 <= 0)

m.c2594 = Constraint(expr=   m.b177 - m.b181 - m.b199 <= 0)

m.c2595 = Constraint(expr=   m.b177 - m.b182 - m.b200 <= 0)

m.c2596 = Constraint(expr=   m.b178 - m.b179 - m.b201 <= 0)

m.c2597 = Constraint(expr=   m.b178 - m.b180 - m.b202 <= 0)

m.c2598 = Constraint(expr=   m.b178 - m.b181 - m.b203 <= 0)

m.c2599 = Constraint(expr=   m.b178 - m.b182 - m.b204 <= 0)

m.c2600 = Constraint(expr=   m.b179 - m.b180 - m.b205 <= 0)

m.c2601 = Constraint(expr=   m.b179 - m.b181 - m.b206 <= 0)

m.c2602 = Constraint(expr=   m.b179 - m.b182 - m.b207 <= 0)

m.c2603 = Constraint(expr=   m.b180 - m.b181 - m.b208 <= 0)

m.c2604 = Constraint(expr=   m.b180 - m.b182 - m.b209 <= 0)

m.c2605 = Constraint(expr=   m.b181 - m.b182 - m.b210 <= 0)

m.c2606 = Constraint(expr=   m.b183 - m.b184 - m.b190 <= 0)

m.c2607 = Constraint(expr=   m.b183 - m.b185 - m.b191 <= 0)

m.c2608 = Constraint(expr=   m.b183 - m.b186 - m.b192 <= 0)

m.c2609 = Constraint(expr=   m.b183 - m.b187 - m.b193 <= 0)

m.c2610 = Constraint(expr=   m.b183 - m.b188 - m.b194 <= 0)

m.c2611 = Constraint(expr=   m.b183 - m.b189 - m.b195 <= 0)

m.c2612 = Constraint(expr=   m.b184 - m.b185 - m.b196 <= 0)

m.c2613 = Constraint(expr=   m.b184 - m.b186 - m.b197 <= 0)

m.c2614 = Constraint(expr=   m.b184 - m.b187 - m.b198 <= 0)

m.c2615 = Constraint(expr=   m.b184 - m.b188 - m.b199 <= 0)

m.c2616 = Constraint(expr=   m.b184 - m.b189 - m.b200 <= 0)

m.c2617 = Constraint(expr=   m.b185 - m.b186 - m.b201 <= 0)

m.c2618 = Constraint(expr=   m.b185 - m.b187 - m.b202 <= 0)

m.c2619 = Constraint(expr=   m.b185 - m.b188 - m.b203 <= 0)

m.c2620 = Constraint(expr=   m.b185 - m.b189 - m.b204 <= 0)

m.c2621 = Constraint(expr=   m.b186 - m.b187 - m.b205 <= 0)

m.c2622 = Constraint(expr=   m.b186 - m.b188 - m.b206 <= 0)

m.c2623 = Constraint(expr=   m.b186 - m.b189 - m.b207 <= 0)

m.c2624 = Constraint(expr=   m.b187 - m.b188 - m.b208 <= 0)

m.c2625 = Constraint(expr=   m.b187 - m.b189 - m.b209 <= 0)

m.c2626 = Constraint(expr=   m.b188 - m.b189 - m.b210 <= 0)

m.c2627 = Constraint(expr=   m.b190 - m.b191 - m.b196 <= 0)

m.c2628 = Constraint(expr=   m.b190 - m.b192 - m.b197 <= 0)

m.c2629 = Constraint(expr=   m.b190 - m.b193 - m.b198 <= 0)

m.c2630 = Constraint(expr=   m.b190 - m.b194 - m.b199 <= 0)

m.c2631 = Constraint(expr=   m.b190 - m.b195 - m.b200 <= 0)

m.c2632 = Constraint(expr=   m.b191 - m.b192 - m.b201 <= 0)

m.c2633 = Constraint(expr=   m.b191 - m.b193 - m.b202 <= 0)

m.c2634 = Constraint(expr=   m.b191 - m.b194 - m.b203 <= 0)

m.c2635 = Constraint(expr=   m.b191 - m.b195 - m.b204 <= 0)

m.c2636 = Constraint(expr=   m.b192 - m.b193 - m.b205 <= 0)

m.c2637 = Constraint(expr=   m.b192 - m.b194 - m.b206 <= 0)

m.c2638 = Constraint(expr=   m.b192 - m.b195 - m.b207 <= 0)

m.c2639 = Constraint(expr=   m.b193 - m.b194 - m.b208 <= 0)

m.c2640 = Constraint(expr=   m.b193 - m.b195 - m.b209 <= 0)

m.c2641 = Constraint(expr=   m.b194 - m.b195 - m.b210 <= 0)

m.c2642 = Constraint(expr=   m.b196 - m.b197 - m.b201 <= 0)

m.c2643 = Constraint(expr=   m.b196 - m.b198 - m.b202 <= 0)

m.c2644 = Constraint(expr=   m.b196 - m.b199 - m.b203 <= 0)

m.c2645 = Constraint(expr=   m.b196 - m.b200 - m.b204 <= 0)

m.c2646 = Constraint(expr=   m.b197 - m.b198 - m.b205 <= 0)

m.c2647 = Constraint(expr=   m.b197 - m.b199 - m.b206 <= 0)

m.c2648 = Constraint(expr=   m.b197 - m.b200 - m.b207 <= 0)

m.c2649 = Constraint(expr=   m.b198 - m.b199 - m.b208 <= 0)

m.c2650 = Constraint(expr=   m.b198 - m.b200 - m.b209 <= 0)

m.c2651 = Constraint(expr=   m.b199 - m.b200 - m.b210 <= 0)

m.c2652 = Constraint(expr=   m.b201 - m.b202 - m.b205 <= 0)

m.c2653 = Constraint(expr=   m.b201 - m.b203 - m.b206 <= 0)

m.c2654 = Constraint(expr=   m.b201 - m.b204 - m.b207 <= 0)

m.c2655 = Constraint(expr=   m.b202 - m.b203 - m.b208 <= 0)

m.c2656 = Constraint(expr=   m.b202 - m.b204 - m.b209 <= 0)

m.c2657 = Constraint(expr=   m.b203 - m.b204 - m.b210 <= 0)

m.c2658 = Constraint(expr=   m.b205 - m.b206 - m.b208 <= 0)

m.c2659 = Constraint(expr=   m.b205 - m.b207 - m.b209 <= 0)

m.c2660 = Constraint(expr=   m.b206 - m.b207 - m.b210 <= 0)

m.c2661 = Constraint(expr=   m.b208 - m.b209 - m.b210 <= 0)

m.c2662 = Constraint(expr= - m.b2 - m.b3 + m.b22 <= 0)

m.c2663 = Constraint(expr= - m.b2 - m.b4 + m.b23 <= 0)

m.c2664 = Constraint(expr= - m.b2 - m.b5 + m.b24 <= 0)

m.c2665 = Constraint(expr= - m.b2 - m.b6 + m.b25 <= 0)

m.c2666 = Constraint(expr= - m.b2 - m.b7 + m.b26 <= 0)

m.c2667 = Constraint(expr= - m.b2 - m.b8 + m.b27 <= 0)

m.c2668 = Constraint(expr= - m.b2 - m.b9 + m.b28 <= 0)

m.c2669 = Constraint(expr= - m.b2 - m.b10 + m.b29 <= 0)

m.c2670 = Constraint(expr= - m.b2 - m.b11 + m.b30 <= 0)

m.c2671 = Constraint(expr= - m.b2 - m.b12 + m.b31 <= 0)

m.c2672 = Constraint(expr= - m.b2 - m.b13 + m.b32 <= 0)

m.c2673 = Constraint(expr= - m.b2 - m.b14 + m.b33 <= 0)

m.c2674 = Constraint(expr= - m.b2 - m.b15 + m.b34 <= 0)

m.c2675 = Constraint(expr= - m.b2 - m.b16 + m.b35 <= 0)

m.c2676 = Constraint(expr= - m.b2 - m.b17 + m.b36 <= 0)

m.c2677 = Constraint(expr= - m.b2 - m.b18 + m.b37 <= 0)

m.c2678 = Constraint(expr= - m.b2 - m.b19 + m.b38 <= 0)

m.c2679 = Constraint(expr= - m.b2 - m.b20 + m.b39 <= 0)

m.c2680 = Constraint(expr= - m.b2 - m.b21 + m.b40 <= 0)

m.c2681 = Constraint(expr= - m.b3 - m.b4 + m.b41 <= 0)

m.c2682 = Constraint(expr= - m.b3 - m.b5 + m.b42 <= 0)

m.c2683 = Constraint(expr= - m.b3 - m.b6 + m.b43 <= 0)

m.c2684 = Constraint(expr= - m.b3 - m.b7 + m.b44 <= 0)

m.c2685 = Constraint(expr= - m.b3 - m.b8 + m.b45 <= 0)

m.c2686 = Constraint(expr= - m.b3 - m.b9 + m.b46 <= 0)

m.c2687 = Constraint(expr= - m.b3 - m.b10 + m.b47 <= 0)

m.c2688 = Constraint(expr= - m.b3 - m.b11 + m.b48 <= 0)

m.c2689 = Constraint(expr= - m.b3 - m.b12 + m.b49 <= 0)

m.c2690 = Constraint(expr= - m.b3 - m.b13 + m.b50 <= 0)

m.c2691 = Constraint(expr= - m.b3 - m.b14 + m.b51 <= 0)

m.c2692 = Constraint(expr= - m.b3 - m.b15 + m.b52 <= 0)

m.c2693 = Constraint(expr= - m.b3 - m.b16 + m.b53 <= 0)

m.c2694 = Constraint(expr= - m.b3 - m.b17 + m.b54 <= 0)

m.c2695 = Constraint(expr= - m.b3 - m.b18 + m.b55 <= 0)

m.c2696 = Constraint(expr= - m.b3 - m.b19 + m.b56 <= 0)

m.c2697 = Constraint(expr= - m.b3 - m.b20 + m.b57 <= 0)

m.c2698 = Constraint(expr= - m.b3 - m.b21 + m.b58 <= 0)

m.c2699 = Constraint(expr= - m.b4 - m.b5 + m.b59 <= 0)

m.c2700 = Constraint(expr= - m.b4 - m.b6 + m.b60 <= 0)

m.c2701 = Constraint(expr= - m.b4 - m.b7 + m.b61 <= 0)

m.c2702 = Constraint(expr= - m.b4 - m.b8 + m.b62 <= 0)

m.c2703 = Constraint(expr= - m.b4 - m.b9 + m.b63 <= 0)

m.c2704 = Constraint(expr= - m.b4 - m.b10 + m.b64 <= 0)

m.c2705 = Constraint(expr= - m.b4 - m.b11 + m.b65 <= 0)

m.c2706 = Constraint(expr= - m.b4 - m.b12 + m.b66 <= 0)

m.c2707 = Constraint(expr= - m.b4 - m.b13 + m.b67 <= 0)

m.c2708 = Constraint(expr= - m.b4 - m.b14 + m.b68 <= 0)

m.c2709 = Constraint(expr= - m.b4 - m.b15 + m.b69 <= 0)

m.c2710 = Constraint(expr= - m.b4 - m.b16 + m.b70 <= 0)

m.c2711 = Constraint(expr= - m.b4 - m.b17 + m.b71 <= 0)

m.c2712 = Constraint(expr= - m.b4 - m.b18 + m.b72 <= 0)

m.c2713 = Constraint(expr= - m.b4 - m.b19 + m.b73 <= 0)

m.c2714 = Constraint(expr= - m.b4 - m.b20 + m.b74 <= 0)

m.c2715 = Constraint(expr= - m.b4 - m.b21 + m.b75 <= 0)

m.c2716 = Constraint(expr= - m.b5 - m.b6 + m.b76 <= 0)

m.c2717 = Constraint(expr= - m.b5 - m.b7 + m.b77 <= 0)

m.c2718 = Constraint(expr= - m.b5 - m.b8 + m.b78 <= 0)

m.c2719 = Constraint(expr= - m.b5 - m.b9 + m.b79 <= 0)

m.c2720 = Constraint(expr= - m.b5 - m.b10 + m.b80 <= 0)

m.c2721 = Constraint(expr= - m.b5 - m.b11 + m.b81 <= 0)

m.c2722 = Constraint(expr= - m.b5 - m.b12 + m.b82 <= 0)

m.c2723 = Constraint(expr= - m.b5 - m.b13 + m.b83 <= 0)

m.c2724 = Constraint(expr= - m.b5 - m.b14 + m.b84 <= 0)

m.c2725 = Constraint(expr= - m.b5 - m.b15 + m.b85 <= 0)

m.c2726 = Constraint(expr= - m.b5 - m.b16 + m.b86 <= 0)

m.c2727 = Constraint(expr= - m.b5 - m.b17 + m.b87 <= 0)

m.c2728 = Constraint(expr= - m.b5 - m.b18 + m.b88 <= 0)

m.c2729 = Constraint(expr= - m.b5 - m.b19 + m.b89 <= 0)

m.c2730 = Constraint(expr= - m.b5 - m.b20 + m.b90 <= 0)

m.c2731 = Constraint(expr= - m.b5 - m.b21 + m.b91 <= 0)

m.c2732 = Constraint(expr= - m.b6 - m.b7 + m.b92 <= 0)

m.c2733 = Constraint(expr= - m.b6 - m.b8 + m.b93 <= 0)

m.c2734 = Constraint(expr= - m.b6 - m.b9 + m.b94 <= 0)

m.c2735 = Constraint(expr= - m.b6 - m.b10 + m.b95 <= 0)

m.c2736 = Constraint(expr= - m.b6 - m.b11 + m.b96 <= 0)

m.c2737 = Constraint(expr= - m.b6 - m.b12 + m.b97 <= 0)

m.c2738 = Constraint(expr= - m.b6 - m.b13 + m.b98 <= 0)

m.c2739 = Constraint(expr= - m.b6 - m.b14 + m.b99 <= 0)

m.c2740 = Constraint(expr= - m.b6 - m.b15 + m.b100 <= 0)

m.c2741 = Constraint(expr= - m.b6 - m.b16 + m.b101 <= 0)

m.c2742 = Constraint(expr= - m.b6 - m.b17 + m.b102 <= 0)

m.c2743 = Constraint(expr= - m.b6 - m.b18 + m.b103 <= 0)

m.c2744 = Constraint(expr= - m.b6 - m.b19 + m.b104 <= 0)

m.c2745 = Constraint(expr= - m.b6 - m.b20 + m.b105 <= 0)

m.c2746 = Constraint(expr= - m.b6 - m.b21 + m.b106 <= 0)

m.c2747 = Constraint(expr= - m.b7 - m.b8 + m.b107 <= 0)

m.c2748 = Constraint(expr= - m.b7 - m.b9 + m.b108 <= 0)

m.c2749 = Constraint(expr= - m.b7 - m.b10 + m.b109 <= 0)

m.c2750 = Constraint(expr= - m.b7 - m.b11 + m.b110 <= 0)

m.c2751 = Constraint(expr= - m.b7 - m.b12 + m.b111 <= 0)

m.c2752 = Constraint(expr= - m.b7 - m.b13 + m.b112 <= 0)

m.c2753 = Constraint(expr= - m.b7 - m.b14 + m.b113 <= 0)

m.c2754 = Constraint(expr= - m.b7 - m.b15 + m.b114 <= 0)

m.c2755 = Constraint(expr= - m.b7 - m.b16 + m.b115 <= 0)

m.c2756 = Constraint(expr= - m.b7 - m.b17 + m.b116 <= 0)

m.c2757 = Constraint(expr= - m.b7 - m.b18 + m.b117 <= 0)

m.c2758 = Constraint(expr= - m.b7 - m.b19 + m.b118 <= 0)

m.c2759 = Constraint(expr= - m.b7 - m.b20 + m.b119 <= 0)

m.c2760 = Constraint(expr= - m.b7 - m.b21 + m.b120 <= 0)

m.c2761 = Constraint(expr= - m.b8 - m.b9 + m.b121 <= 0)

m.c2762 = Constraint(expr= - m.b8 - m.b10 + m.b122 <= 0)

m.c2763 = Constraint(expr= - m.b8 - m.b11 + m.b123 <= 0)

m.c2764 = Constraint(expr= - m.b8 - m.b12 + m.b124 <= 0)

m.c2765 = Constraint(expr= - m.b8 - m.b13 + m.b125 <= 0)

m.c2766 = Constraint(expr= - m.b8 - m.b14 + m.b126 <= 0)

m.c2767 = Constraint(expr= - m.b8 - m.b15 + m.b127 <= 0)

m.c2768 = Constraint(expr= - m.b8 - m.b16 + m.b128 <= 0)

m.c2769 = Constraint(expr= - m.b8 - m.b17 + m.b129 <= 0)

m.c2770 = Constraint(expr= - m.b8 - m.b18 + m.b130 <= 0)

m.c2771 = Constraint(expr= - m.b8 - m.b19 + m.b131 <= 0)

m.c2772 = Constraint(expr= - m.b8 - m.b20 + m.b132 <= 0)

m.c2773 = Constraint(expr= - m.b8 - m.b21 + m.b133 <= 0)

m.c2774 = Constraint(expr= - m.b9 - m.b10 + m.b134 <= 0)

m.c2775 = Constraint(expr= - m.b9 - m.b11 + m.b135 <= 0)

m.c2776 = Constraint(expr= - m.b9 - m.b12 + m.b136 <= 0)

m.c2777 = Constraint(expr= - m.b9 - m.b13 + m.b137 <= 0)

m.c2778 = Constraint(expr= - m.b9 - m.b14 + m.b138 <= 0)

m.c2779 = Constraint(expr= - m.b9 - m.b15 + m.b139 <= 0)

m.c2780 = Constraint(expr= - m.b9 - m.b16 + m.b140 <= 0)

m.c2781 = Constraint(expr= - m.b9 - m.b17 + m.b141 <= 0)

m.c2782 = Constraint(expr= - m.b9 - m.b18 + m.b142 <= 0)

m.c2783 = Constraint(expr= - m.b9 - m.b19 + m.b143 <= 0)

m.c2784 = Constraint(expr= - m.b9 - m.b20 + m.b144 <= 0)

m.c2785 = Constraint(expr= - m.b9 - m.b21 + m.b145 <= 0)

m.c2786 = Constraint(expr= - m.b10 - m.b11 + m.b146 <= 0)

m.c2787 = Constraint(expr= - m.b10 - m.b12 + m.b147 <= 0)

m.c2788 = Constraint(expr= - m.b10 - m.b13 + m.b148 <= 0)

m.c2789 = Constraint(expr= - m.b10 - m.b14 + m.b149 <= 0)

m.c2790 = Constraint(expr= - m.b10 - m.b15 + m.b150 <= 0)

m.c2791 = Constraint(expr= - m.b10 - m.b16 + m.b151 <= 0)

m.c2792 = Constraint(expr= - m.b10 - m.b17 + m.b152 <= 0)

m.c2793 = Constraint(expr= - m.b10 - m.b18 + m.b153 <= 0)

m.c2794 = Constraint(expr= - m.b10 - m.b19 + m.b154 <= 0)

m.c2795 = Constraint(expr= - m.b10 - m.b20 + m.b155 <= 0)

m.c2796 = Constraint(expr= - m.b10 - m.b21 + m.b156 <= 0)

m.c2797 = Constraint(expr= - m.b11 - m.b12 + m.b157 <= 0)

m.c2798 = Constraint(expr= - m.b11 - m.b13 + m.b158 <= 0)

m.c2799 = Constraint(expr= - m.b11 - m.b14 + m.b159 <= 0)

m.c2800 = Constraint(expr= - m.b11 - m.b15 + m.b160 <= 0)

m.c2801 = Constraint(expr= - m.b11 - m.b16 + m.b161 <= 0)

m.c2802 = Constraint(expr= - m.b11 - m.b17 + m.b162 <= 0)

m.c2803 = Constraint(expr= - m.b11 - m.b18 + m.b163 <= 0)

m.c2804 = Constraint(expr= - m.b11 - m.b19 + m.b164 <= 0)

m.c2805 = Constraint(expr= - m.b11 - m.b20 + m.b165 <= 0)

m.c2806 = Constraint(expr= - m.b11 - m.b21 + m.b211 <= 0)

m.c2807 = Constraint(expr= - m.b12 - m.b13 + m.b166 <= 0)

m.c2808 = Constraint(expr= - m.b12 - m.b14 + m.b167 <= 0)

m.c2809 = Constraint(expr= - m.b12 - m.b15 + m.b168 <= 0)

m.c2810 = Constraint(expr= - m.b12 - m.b16 + m.b169 <= 0)

m.c2811 = Constraint(expr= - m.b12 - m.b17 + m.b170 <= 0)

m.c2812 = Constraint(expr= - m.b12 - m.b18 + m.b171 <= 0)

m.c2813 = Constraint(expr= - m.b12 - m.b19 + m.b172 <= 0)

m.c2814 = Constraint(expr= - m.b12 - m.b20 + m.b173 <= 0)

m.c2815 = Constraint(expr= - m.b12 - m.b21 + m.b174 <= 0)

m.c2816 = Constraint(expr= - m.b13 - m.b14 + m.b175 <= 0)

m.c2817 = Constraint(expr= - m.b13 - m.b15 + m.b176 <= 0)

m.c2818 = Constraint(expr= - m.b13 - m.b16 + m.b177 <= 0)

m.c2819 = Constraint(expr= - m.b13 - m.b17 + m.b178 <= 0)

m.c2820 = Constraint(expr= - m.b13 - m.b18 + m.b179 <= 0)

m.c2821 = Constraint(expr= - m.b13 - m.b19 + m.b180 <= 0)

m.c2822 = Constraint(expr= - m.b13 - m.b20 + m.b181 <= 0)

m.c2823 = Constraint(expr= - m.b13 - m.b21 + m.b182 <= 0)

m.c2824 = Constraint(expr= - m.b14 - m.b15 + m.b183 <= 0)

m.c2825 = Constraint(expr= - m.b14 - m.b16 + m.b184 <= 0)

m.c2826 = Constraint(expr= - m.b14 - m.b17 + m.b185 <= 0)

m.c2827 = Constraint(expr= - m.b14 - m.b18 + m.b186 <= 0)

m.c2828 = Constraint(expr= - m.b14 - m.b19 + m.b187 <= 0)

m.c2829 = Constraint(expr= - m.b14 - m.b20 + m.b188 <= 0)

m.c2830 = Constraint(expr= - m.b14 - m.b21 + m.b189 <= 0)

m.c2831 = Constraint(expr= - m.b15 - m.b16 + m.b190 <= 0)

m.c2832 = Constraint(expr= - m.b15 - m.b17 + m.b191 <= 0)

m.c2833 = Constraint(expr= - m.b15 - m.b18 + m.b192 <= 0)

m.c2834 = Constraint(expr= - m.b15 - m.b19 + m.b193 <= 0)

m.c2835 = Constraint(expr= - m.b15 - m.b20 + m.b194 <= 0)

m.c2836 = Constraint(expr= - m.b15 - m.b21 + m.b195 <= 0)

m.c2837 = Constraint(expr= - m.b16 - m.b17 + m.b196 <= 0)

m.c2838 = Constraint(expr= - m.b16 - m.b18 + m.b197 <= 0)

m.c2839 = Constraint(expr= - m.b16 - m.b19 + m.b198 <= 0)

m.c2840 = Constraint(expr= - m.b16 - m.b20 + m.b199 <= 0)

m.c2841 = Constraint(expr= - m.b16 - m.b21 + m.b200 <= 0)

m.c2842 = Constraint(expr= - m.b17 - m.b18 + m.b201 <= 0)

m.c2843 = Constraint(expr= - m.b17 - m.b19 + m.b202 <= 0)

m.c2844 = Constraint(expr= - m.b17 - m.b20 + m.b203 <= 0)

m.c2845 = Constraint(expr= - m.b17 - m.b21 + m.b204 <= 0)

m.c2846 = Constraint(expr= - m.b18 - m.b19 + m.b205 <= 0)

m.c2847 = Constraint(expr= - m.b18 - m.b20 + m.b206 <= 0)

m.c2848 = Constraint(expr= - m.b18 - m.b21 + m.b207 <= 0)

m.c2849 = Constraint(expr= - m.b19 - m.b20 + m.b208 <= 0)

m.c2850 = Constraint(expr= - m.b19 - m.b21 + m.b209 <= 0)

m.c2851 = Constraint(expr= - m.b20 - m.b21 + m.b210 <= 0)

m.c2852 = Constraint(expr= - m.b22 - m.b23 + m.b41 <= 0)

m.c2853 = Constraint(expr= - m.b22 - m.b24 + m.b42 <= 0)

m.c2854 = Constraint(expr= - m.b22 - m.b25 + m.b43 <= 0)

m.c2855 = Constraint(expr= - m.b22 - m.b26 + m.b44 <= 0)

m.c2856 = Constraint(expr= - m.b22 - m.b27 + m.b45 <= 0)

m.c2857 = Constraint(expr= - m.b22 - m.b28 + m.b46 <= 0)

m.c2858 = Constraint(expr= - m.b22 - m.b29 + m.b47 <= 0)

m.c2859 = Constraint(expr= - m.b22 - m.b30 + m.b48 <= 0)

m.c2860 = Constraint(expr= - m.b22 - m.b31 + m.b49 <= 0)

m.c2861 = Constraint(expr= - m.b22 - m.b32 + m.b50 <= 0)

m.c2862 = Constraint(expr= - m.b22 - m.b33 + m.b51 <= 0)

m.c2863 = Constraint(expr= - m.b22 - m.b34 + m.b52 <= 0)

m.c2864 = Constraint(expr= - m.b22 - m.b35 + m.b53 <= 0)

m.c2865 = Constraint(expr= - m.b22 - m.b36 + m.b54 <= 0)

m.c2866 = Constraint(expr= - m.b22 - m.b37 + m.b55 <= 0)

m.c2867 = Constraint(expr= - m.b22 - m.b38 + m.b56 <= 0)

m.c2868 = Constraint(expr= - m.b22 - m.b39 + m.b57 <= 0)

m.c2869 = Constraint(expr= - m.b22 - m.b40 + m.b58 <= 0)

m.c2870 = Constraint(expr= - m.b23 - m.b24 + m.b59 <= 0)

m.c2871 = Constraint(expr= - m.b23 - m.b25 + m.b60 <= 0)

m.c2872 = Constraint(expr= - m.b23 - m.b26 + m.b61 <= 0)

m.c2873 = Constraint(expr= - m.b23 - m.b27 + m.b62 <= 0)

m.c2874 = Constraint(expr= - m.b23 - m.b28 + m.b63 <= 0)

m.c2875 = Constraint(expr= - m.b23 - m.b29 + m.b64 <= 0)

m.c2876 = Constraint(expr= - m.b23 - m.b30 + m.b65 <= 0)

m.c2877 = Constraint(expr= - m.b23 - m.b31 + m.b66 <= 0)

m.c2878 = Constraint(expr= - m.b23 - m.b32 + m.b67 <= 0)

m.c2879 = Constraint(expr= - m.b23 - m.b33 + m.b68 <= 0)

m.c2880 = Constraint(expr= - m.b23 - m.b34 + m.b69 <= 0)

m.c2881 = Constraint(expr= - m.b23 - m.b35 + m.b70 <= 0)

m.c2882 = Constraint(expr= - m.b23 - m.b36 + m.b71 <= 0)

m.c2883 = Constraint(expr= - m.b23 - m.b37 + m.b72 <= 0)

m.c2884 = Constraint(expr= - m.b23 - m.b38 + m.b73 <= 0)

m.c2885 = Constraint(expr= - m.b23 - m.b39 + m.b74 <= 0)

m.c2886 = Constraint(expr= - m.b23 - m.b40 + m.b75 <= 0)

m.c2887 = Constraint(expr= - m.b24 - m.b25 + m.b76 <= 0)

m.c2888 = Constraint(expr= - m.b24 - m.b26 + m.b77 <= 0)

m.c2889 = Constraint(expr= - m.b24 - m.b27 + m.b78 <= 0)

m.c2890 = Constraint(expr= - m.b24 - m.b28 + m.b79 <= 0)

m.c2891 = Constraint(expr= - m.b24 - m.b29 + m.b80 <= 0)

m.c2892 = Constraint(expr= - m.b24 - m.b30 + m.b81 <= 0)

m.c2893 = Constraint(expr= - m.b24 - m.b31 + m.b82 <= 0)

m.c2894 = Constraint(expr= - m.b24 - m.b32 + m.b83 <= 0)

m.c2895 = Constraint(expr= - m.b24 - m.b33 + m.b84 <= 0)

m.c2896 = Constraint(expr= - m.b24 - m.b34 + m.b85 <= 0)

m.c2897 = Constraint(expr= - m.b24 - m.b35 + m.b86 <= 0)

m.c2898 = Constraint(expr= - m.b24 - m.b36 + m.b87 <= 0)

m.c2899 = Constraint(expr= - m.b24 - m.b37 + m.b88 <= 0)

m.c2900 = Constraint(expr= - m.b24 - m.b38 + m.b89 <= 0)

m.c2901 = Constraint(expr= - m.b24 - m.b39 + m.b90 <= 0)

m.c2902 = Constraint(expr= - m.b24 - m.b40 + m.b91 <= 0)

m.c2903 = Constraint(expr= - m.b25 - m.b26 + m.b92 <= 0)

m.c2904 = Constraint(expr= - m.b25 - m.b27 + m.b93 <= 0)

m.c2905 = Constraint(expr= - m.b25 - m.b28 + m.b94 <= 0)

m.c2906 = Constraint(expr= - m.b25 - m.b29 + m.b95 <= 0)

m.c2907 = Constraint(expr= - m.b25 - m.b30 + m.b96 <= 0)

m.c2908 = Constraint(expr= - m.b25 - m.b31 + m.b97 <= 0)

m.c2909 = Constraint(expr= - m.b25 - m.b32 + m.b98 <= 0)

m.c2910 = Constraint(expr= - m.b25 - m.b33 + m.b99 <= 0)

m.c2911 = Constraint(expr= - m.b25 - m.b34 + m.b100 <= 0)

m.c2912 = Constraint(expr= - m.b25 - m.b35 + m.b101 <= 0)

m.c2913 = Constraint(expr= - m.b25 - m.b36 + m.b102 <= 0)

m.c2914 = Constraint(expr= - m.b25 - m.b37 + m.b103 <= 0)

m.c2915 = Constraint(expr= - m.b25 - m.b38 + m.b104 <= 0)

m.c2916 = Constraint(expr= - m.b25 - m.b39 + m.b105 <= 0)

m.c2917 = Constraint(expr= - m.b25 - m.b40 + m.b106 <= 0)

m.c2918 = Constraint(expr= - m.b26 - m.b27 + m.b107 <= 0)

m.c2919 = Constraint(expr= - m.b26 - m.b28 + m.b108 <= 0)

m.c2920 = Constraint(expr= - m.b26 - m.b29 + m.b109 <= 0)

m.c2921 = Constraint(expr= - m.b26 - m.b30 + m.b110 <= 0)

m.c2922 = Constraint(expr= - m.b26 - m.b31 + m.b111 <= 0)

m.c2923 = Constraint(expr= - m.b26 - m.b32 + m.b112 <= 0)

m.c2924 = Constraint(expr= - m.b26 - m.b33 + m.b113 <= 0)

m.c2925 = Constraint(expr= - m.b26 - m.b34 + m.b114 <= 0)

m.c2926 = Constraint(expr= - m.b26 - m.b35 + m.b115 <= 0)

m.c2927 = Constraint(expr= - m.b26 - m.b36 + m.b116 <= 0)

m.c2928 = Constraint(expr= - m.b26 - m.b37 + m.b117 <= 0)

m.c2929 = Constraint(expr= - m.b26 - m.b38 + m.b118 <= 0)

m.c2930 = Constraint(expr= - m.b26 - m.b39 + m.b119 <= 0)

m.c2931 = Constraint(expr= - m.b26 - m.b40 + m.b120 <= 0)

m.c2932 = Constraint(expr= - m.b27 - m.b28 + m.b121 <= 0)

m.c2933 = Constraint(expr= - m.b27 - m.b29 + m.b122 <= 0)

m.c2934 = Constraint(expr= - m.b27 - m.b30 + m.b123 <= 0)

m.c2935 = Constraint(expr= - m.b27 - m.b31 + m.b124 <= 0)

m.c2936 = Constraint(expr= - m.b27 - m.b32 + m.b125 <= 0)

m.c2937 = Constraint(expr= - m.b27 - m.b33 + m.b126 <= 0)

m.c2938 = Constraint(expr= - m.b27 - m.b34 + m.b127 <= 0)

m.c2939 = Constraint(expr= - m.b27 - m.b35 + m.b128 <= 0)

m.c2940 = Constraint(expr= - m.b27 - m.b36 + m.b129 <= 0)

m.c2941 = Constraint(expr= - m.b27 - m.b37 + m.b130 <= 0)

m.c2942 = Constraint(expr= - m.b27 - m.b38 + m.b131 <= 0)

m.c2943 = Constraint(expr= - m.b27 - m.b39 + m.b132 <= 0)

m.c2944 = Constraint(expr= - m.b27 - m.b40 + m.b133 <= 0)

m.c2945 = Constraint(expr= - m.b28 - m.b29 + m.b134 <= 0)

m.c2946 = Constraint(expr= - m.b28 - m.b30 + m.b135 <= 0)

m.c2947 = Constraint(expr= - m.b28 - m.b31 + m.b136 <= 0)

m.c2948 = Constraint(expr= - m.b28 - m.b32 + m.b137 <= 0)

m.c2949 = Constraint(expr= - m.b28 - m.b33 + m.b138 <= 0)

m.c2950 = Constraint(expr= - m.b28 - m.b34 + m.b139 <= 0)

m.c2951 = Constraint(expr= - m.b28 - m.b35 + m.b140 <= 0)

m.c2952 = Constraint(expr= - m.b28 - m.b36 + m.b141 <= 0)

m.c2953 = Constraint(expr= - m.b28 - m.b37 + m.b142 <= 0)

m.c2954 = Constraint(expr= - m.b28 - m.b38 + m.b143 <= 0)

m.c2955 = Constraint(expr= - m.b28 - m.b39 + m.b144 <= 0)

m.c2956 = Constraint(expr= - m.b28 - m.b40 + m.b145 <= 0)

m.c2957 = Constraint(expr= - m.b29 - m.b30 + m.b146 <= 0)

m.c2958 = Constraint(expr= - m.b29 - m.b31 + m.b147 <= 0)

m.c2959 = Constraint(expr= - m.b29 - m.b32 + m.b148 <= 0)

m.c2960 = Constraint(expr= - m.b29 - m.b33 + m.b149 <= 0)

m.c2961 = Constraint(expr= - m.b29 - m.b34 + m.b150 <= 0)

m.c2962 = Constraint(expr= - m.b29 - m.b35 + m.b151 <= 0)

m.c2963 = Constraint(expr= - m.b29 - m.b36 + m.b152 <= 0)

m.c2964 = Constraint(expr= - m.b29 - m.b37 + m.b153 <= 0)

m.c2965 = Constraint(expr= - m.b29 - m.b38 + m.b154 <= 0)

m.c2966 = Constraint(expr= - m.b29 - m.b39 + m.b155 <= 0)

m.c2967 = Constraint(expr= - m.b29 - m.b40 + m.b156 <= 0)

m.c2968 = Constraint(expr= - m.b30 - m.b31 + m.b157 <= 0)

m.c2969 = Constraint(expr= - m.b30 - m.b32 + m.b158 <= 0)

m.c2970 = Constraint(expr= - m.b30 - m.b33 + m.b159 <= 0)

m.c2971 = Constraint(expr= - m.b30 - m.b34 + m.b160 <= 0)

m.c2972 = Constraint(expr= - m.b30 - m.b35 + m.b161 <= 0)

m.c2973 = Constraint(expr= - m.b30 - m.b36 + m.b162 <= 0)

m.c2974 = Constraint(expr= - m.b30 - m.b37 + m.b163 <= 0)

m.c2975 = Constraint(expr= - m.b30 - m.b38 + m.b164 <= 0)

m.c2976 = Constraint(expr= - m.b30 - m.b39 + m.b165 <= 0)

m.c2977 = Constraint(expr= - m.b30 - m.b40 + m.b211 <= 0)

m.c2978 = Constraint(expr= - m.b31 - m.b32 + m.b166 <= 0)

m.c2979 = Constraint(expr= - m.b31 - m.b33 + m.b167 <= 0)

m.c2980 = Constraint(expr= - m.b31 - m.b34 + m.b168 <= 0)

m.c2981 = Constraint(expr= - m.b31 - m.b35 + m.b169 <= 0)

m.c2982 = Constraint(expr= - m.b31 - m.b36 + m.b170 <= 0)

m.c2983 = Constraint(expr= - m.b31 - m.b37 + m.b171 <= 0)

m.c2984 = Constraint(expr= - m.b31 - m.b38 + m.b172 <= 0)

m.c2985 = Constraint(expr= - m.b31 - m.b39 + m.b173 <= 0)

m.c2986 = Constraint(expr= - m.b31 - m.b40 + m.b174 <= 0)

m.c2987 = Constraint(expr= - m.b32 - m.b33 + m.b175 <= 0)

m.c2988 = Constraint(expr= - m.b32 - m.b34 + m.b176 <= 0)

m.c2989 = Constraint(expr= - m.b32 - m.b35 + m.b177 <= 0)

m.c2990 = Constraint(expr= - m.b32 - m.b36 + m.b178 <= 0)

m.c2991 = Constraint(expr= - m.b32 - m.b37 + m.b179 <= 0)

m.c2992 = Constraint(expr= - m.b32 - m.b38 + m.b180 <= 0)

m.c2993 = Constraint(expr= - m.b32 - m.b39 + m.b181 <= 0)

m.c2994 = Constraint(expr= - m.b32 - m.b40 + m.b182 <= 0)

m.c2995 = Constraint(expr= - m.b33 - m.b34 + m.b183 <= 0)

m.c2996 = Constraint(expr= - m.b33 - m.b35 + m.b184 <= 0)

m.c2997 = Constraint(expr= - m.b33 - m.b36 + m.b185 <= 0)

m.c2998 = Constraint(expr= - m.b33 - m.b37 + m.b186 <= 0)

m.c2999 = Constraint(expr= - m.b33 - m.b38 + m.b187 <= 0)

m.c3000 = Constraint(expr= - m.b33 - m.b39 + m.b188 <= 0)

m.c3001 = Constraint(expr= - m.b33 - m.b40 + m.b189 <= 0)

m.c3002 = Constraint(expr= - m.b34 - m.b35 + m.b190 <= 0)

m.c3003 = Constraint(expr= - m.b34 - m.b36 + m.b191 <= 0)

m.c3004 = Constraint(expr= - m.b34 - m.b37 + m.b192 <= 0)

m.c3005 = Constraint(expr= - m.b34 - m.b38 + m.b193 <= 0)

m.c3006 = Constraint(expr= - m.b34 - m.b39 + m.b194 <= 0)

m.c3007 = Constraint(expr= - m.b34 - m.b40 + m.b195 <= 0)

m.c3008 = Constraint(expr= - m.b35 - m.b36 + m.b196 <= 0)

m.c3009 = Constraint(expr= - m.b35 - m.b37 + m.b197 <= 0)

m.c3010 = Constraint(expr= - m.b35 - m.b38 + m.b198 <= 0)

m.c3011 = Constraint(expr= - m.b35 - m.b39 + m.b199 <= 0)

m.c3012 = Constraint(expr= - m.b35 - m.b40 + m.b200 <= 0)

m.c3013 = Constraint(expr= - m.b36 - m.b37 + m.b201 <= 0)

m.c3014 = Constraint(expr= - m.b36 - m.b38 + m.b202 <= 0)

m.c3015 = Constraint(expr= - m.b36 - m.b39 + m.b203 <= 0)

m.c3016 = Constraint(expr= - m.b36 - m.b40 + m.b204 <= 0)

m.c3017 = Constraint(expr= - m.b37 - m.b38 + m.b205 <= 0)

m.c3018 = Constraint(expr= - m.b37 - m.b39 + m.b206 <= 0)

m.c3019 = Constraint(expr= - m.b37 - m.b40 + m.b207 <= 0)

m.c3020 = Constraint(expr= - m.b38 - m.b39 + m.b208 <= 0)

m.c3021 = Constraint(expr= - m.b38 - m.b40 + m.b209 <= 0)

m.c3022 = Constraint(expr= - m.b39 - m.b40 + m.b210 <= 0)

m.c3023 = Constraint(expr= - m.b41 - m.b42 + m.b59 <= 0)

m.c3024 = Constraint(expr= - m.b41 - m.b43 + m.b60 <= 0)

m.c3025 = Constraint(expr= - m.b41 - m.b44 + m.b61 <= 0)

m.c3026 = Constraint(expr= - m.b41 - m.b45 + m.b62 <= 0)

m.c3027 = Constraint(expr= - m.b41 - m.b46 + m.b63 <= 0)

m.c3028 = Constraint(expr= - m.b41 - m.b47 + m.b64 <= 0)

m.c3029 = Constraint(expr= - m.b41 - m.b48 + m.b65 <= 0)

m.c3030 = Constraint(expr= - m.b41 - m.b49 + m.b66 <= 0)

m.c3031 = Constraint(expr= - m.b41 - m.b50 + m.b67 <= 0)

m.c3032 = Constraint(expr= - m.b41 - m.b51 + m.b68 <= 0)

m.c3033 = Constraint(expr= - m.b41 - m.b52 + m.b69 <= 0)

m.c3034 = Constraint(expr= - m.b41 - m.b53 + m.b70 <= 0)

m.c3035 = Constraint(expr= - m.b41 - m.b54 + m.b71 <= 0)

m.c3036 = Constraint(expr= - m.b41 - m.b55 + m.b72 <= 0)

m.c3037 = Constraint(expr= - m.b41 - m.b56 + m.b73 <= 0)

m.c3038 = Constraint(expr= - m.b41 - m.b57 + m.b74 <= 0)

m.c3039 = Constraint(expr= - m.b41 - m.b58 + m.b75 <= 0)

m.c3040 = Constraint(expr= - m.b42 - m.b43 + m.b76 <= 0)

m.c3041 = Constraint(expr= - m.b42 - m.b44 + m.b77 <= 0)

m.c3042 = Constraint(expr= - m.b42 - m.b45 + m.b78 <= 0)

m.c3043 = Constraint(expr= - m.b42 - m.b46 + m.b79 <= 0)

m.c3044 = Constraint(expr= - m.b42 - m.b47 + m.b80 <= 0)

m.c3045 = Constraint(expr= - m.b42 - m.b48 + m.b81 <= 0)

m.c3046 = Constraint(expr= - m.b42 - m.b49 + m.b82 <= 0)

m.c3047 = Constraint(expr= - m.b42 - m.b50 + m.b83 <= 0)

m.c3048 = Constraint(expr= - m.b42 - m.b51 + m.b84 <= 0)

m.c3049 = Constraint(expr= - m.b42 - m.b52 + m.b85 <= 0)

m.c3050 = Constraint(expr= - m.b42 - m.b53 + m.b86 <= 0)

m.c3051 = Constraint(expr= - m.b42 - m.b54 + m.b87 <= 0)

m.c3052 = Constraint(expr= - m.b42 - m.b55 + m.b88 <= 0)

m.c3053 = Constraint(expr= - m.b42 - m.b56 + m.b89 <= 0)

m.c3054 = Constraint(expr= - m.b42 - m.b57 + m.b90 <= 0)

m.c3055 = Constraint(expr= - m.b42 - m.b58 + m.b91 <= 0)

m.c3056 = Constraint(expr= - m.b43 - m.b44 + m.b92 <= 0)

m.c3057 = Constraint(expr= - m.b43 - m.b45 + m.b93 <= 0)

m.c3058 = Constraint(expr= - m.b43 - m.b46 + m.b94 <= 0)

m.c3059 = Constraint(expr= - m.b43 - m.b47 + m.b95 <= 0)

m.c3060 = Constraint(expr= - m.b43 - m.b48 + m.b96 <= 0)

m.c3061 = Constraint(expr= - m.b43 - m.b49 + m.b97 <= 0)

m.c3062 = Constraint(expr= - m.b43 - m.b50 + m.b98 <= 0)

m.c3063 = Constraint(expr= - m.b43 - m.b51 + m.b99 <= 0)

m.c3064 = Constraint(expr= - m.b43 - m.b52 + m.b100 <= 0)

m.c3065 = Constraint(expr= - m.b43 - m.b53 + m.b101 <= 0)

m.c3066 = Constraint(expr= - m.b43 - m.b54 + m.b102 <= 0)

m.c3067 = Constraint(expr= - m.b43 - m.b55 + m.b103 <= 0)

m.c3068 = Constraint(expr= - m.b43 - m.b56 + m.b104 <= 0)

m.c3069 = Constraint(expr= - m.b43 - m.b57 + m.b105 <= 0)

m.c3070 = Constraint(expr= - m.b43 - m.b58 + m.b106 <= 0)

m.c3071 = Constraint(expr= - m.b44 - m.b45 + m.b107 <= 0)

m.c3072 = Constraint(expr= - m.b44 - m.b46 + m.b108 <= 0)

m.c3073 = Constraint(expr= - m.b44 - m.b47 + m.b109 <= 0)

m.c3074 = Constraint(expr= - m.b44 - m.b48 + m.b110 <= 0)

m.c3075 = Constraint(expr= - m.b44 - m.b49 + m.b111 <= 0)

m.c3076 = Constraint(expr= - m.b44 - m.b50 + m.b112 <= 0)

m.c3077 = Constraint(expr= - m.b44 - m.b51 + m.b113 <= 0)

m.c3078 = Constraint(expr= - m.b44 - m.b52 + m.b114 <= 0)

m.c3079 = Constraint(expr= - m.b44 - m.b53 + m.b115 <= 0)

m.c3080 = Constraint(expr= - m.b44 - m.b54 + m.b116 <= 0)

m.c3081 = Constraint(expr= - m.b44 - m.b55 + m.b117 <= 0)

m.c3082 = Constraint(expr= - m.b44 - m.b56 + m.b118 <= 0)

m.c3083 = Constraint(expr= - m.b44 - m.b57 + m.b119 <= 0)

m.c3084 = Constraint(expr= - m.b44 - m.b58 + m.b120 <= 0)

m.c3085 = Constraint(expr= - m.b45 - m.b46 + m.b121 <= 0)

m.c3086 = Constraint(expr= - m.b45 - m.b47 + m.b122 <= 0)

m.c3087 = Constraint(expr= - m.b45 - m.b48 + m.b123 <= 0)

m.c3088 = Constraint(expr= - m.b45 - m.b49 + m.b124 <= 0)

m.c3089 = Constraint(expr= - m.b45 - m.b50 + m.b125 <= 0)

m.c3090 = Constraint(expr= - m.b45 - m.b51 + m.b126 <= 0)

m.c3091 = Constraint(expr= - m.b45 - m.b52 + m.b127 <= 0)

m.c3092 = Constraint(expr= - m.b45 - m.b53 + m.b128 <= 0)

m.c3093 = Constraint(expr= - m.b45 - m.b54 + m.b129 <= 0)

m.c3094 = Constraint(expr= - m.b45 - m.b55 + m.b130 <= 0)

m.c3095 = Constraint(expr= - m.b45 - m.b56 + m.b131 <= 0)

m.c3096 = Constraint(expr= - m.b45 - m.b57 + m.b132 <= 0)

m.c3097 = Constraint(expr= - m.b45 - m.b58 + m.b133 <= 0)

m.c3098 = Constraint(expr= - m.b46 - m.b47 + m.b134 <= 0)

m.c3099 = Constraint(expr= - m.b46 - m.b48 + m.b135 <= 0)

m.c3100 = Constraint(expr= - m.b46 - m.b49 + m.b136 <= 0)

m.c3101 = Constraint(expr= - m.b46 - m.b50 + m.b137 <= 0)

m.c3102 = Constraint(expr= - m.b46 - m.b51 + m.b138 <= 0)

m.c3103 = Constraint(expr= - m.b46 - m.b52 + m.b139 <= 0)

m.c3104 = Constraint(expr= - m.b46 - m.b53 + m.b140 <= 0)

m.c3105 = Constraint(expr= - m.b46 - m.b54 + m.b141 <= 0)

m.c3106 = Constraint(expr= - m.b46 - m.b55 + m.b142 <= 0)

m.c3107 = Constraint(expr= - m.b46 - m.b56 + m.b143 <= 0)

m.c3108 = Constraint(expr= - m.b46 - m.b57 + m.b144 <= 0)

m.c3109 = Constraint(expr= - m.b46 - m.b58 + m.b145 <= 0)

m.c3110 = Constraint(expr= - m.b47 - m.b48 + m.b146 <= 0)

m.c3111 = Constraint(expr= - m.b47 - m.b49 + m.b147 <= 0)

m.c3112 = Constraint(expr= - m.b47 - m.b50 + m.b148 <= 0)

m.c3113 = Constraint(expr= - m.b47 - m.b51 + m.b149 <= 0)

m.c3114 = Constraint(expr= - m.b47 - m.b52 + m.b150 <= 0)

m.c3115 = Constraint(expr= - m.b47 - m.b53 + m.b151 <= 0)

m.c3116 = Constraint(expr= - m.b47 - m.b54 + m.b152 <= 0)

m.c3117 = Constraint(expr= - m.b47 - m.b55 + m.b153 <= 0)

m.c3118 = Constraint(expr= - m.b47 - m.b56 + m.b154 <= 0)

m.c3119 = Constraint(expr= - m.b47 - m.b57 + m.b155 <= 0)

m.c3120 = Constraint(expr= - m.b47 - m.b58 + m.b156 <= 0)

m.c3121 = Constraint(expr= - m.b48 - m.b49 + m.b157 <= 0)

m.c3122 = Constraint(expr= - m.b48 - m.b50 + m.b158 <= 0)

m.c3123 = Constraint(expr= - m.b48 - m.b51 + m.b159 <= 0)

m.c3124 = Constraint(expr= - m.b48 - m.b52 + m.b160 <= 0)

m.c3125 = Constraint(expr= - m.b48 - m.b53 + m.b161 <= 0)

m.c3126 = Constraint(expr= - m.b48 - m.b54 + m.b162 <= 0)

m.c3127 = Constraint(expr= - m.b48 - m.b55 + m.b163 <= 0)

m.c3128 = Constraint(expr= - m.b48 - m.b56 + m.b164 <= 0)

m.c3129 = Constraint(expr= - m.b48 - m.b57 + m.b165 <= 0)

m.c3130 = Constraint(expr= - m.b48 - m.b58 + m.b211 <= 0)

m.c3131 = Constraint(expr= - m.b49 - m.b50 + m.b166 <= 0)

m.c3132 = Constraint(expr= - m.b49 - m.b51 + m.b167 <= 0)

m.c3133 = Constraint(expr= - m.b49 - m.b52 + m.b168 <= 0)

m.c3134 = Constraint(expr= - m.b49 - m.b53 + m.b169 <= 0)

m.c3135 = Constraint(expr= - m.b49 - m.b54 + m.b170 <= 0)

m.c3136 = Constraint(expr= - m.b49 - m.b55 + m.b171 <= 0)

m.c3137 = Constraint(expr= - m.b49 - m.b56 + m.b172 <= 0)

m.c3138 = Constraint(expr= - m.b49 - m.b57 + m.b173 <= 0)

m.c3139 = Constraint(expr= - m.b49 - m.b58 + m.b174 <= 0)

m.c3140 = Constraint(expr= - m.b50 - m.b51 + m.b175 <= 0)

m.c3141 = Constraint(expr= - m.b50 - m.b52 + m.b176 <= 0)

m.c3142 = Constraint(expr= - m.b50 - m.b53 + m.b177 <= 0)

m.c3143 = Constraint(expr= - m.b50 - m.b54 + m.b178 <= 0)

m.c3144 = Constraint(expr= - m.b50 - m.b55 + m.b179 <= 0)

m.c3145 = Constraint(expr= - m.b50 - m.b56 + m.b180 <= 0)

m.c3146 = Constraint(expr= - m.b50 - m.b57 + m.b181 <= 0)

m.c3147 = Constraint(expr= - m.b50 - m.b58 + m.b182 <= 0)

m.c3148 = Constraint(expr= - m.b51 - m.b52 + m.b183 <= 0)

m.c3149 = Constraint(expr= - m.b51 - m.b53 + m.b184 <= 0)

m.c3150 = Constraint(expr= - m.b51 - m.b54 + m.b185 <= 0)

m.c3151 = Constraint(expr= - m.b51 - m.b55 + m.b186 <= 0)

m.c3152 = Constraint(expr= - m.b51 - m.b56 + m.b187 <= 0)

m.c3153 = Constraint(expr= - m.b51 - m.b57 + m.b188 <= 0)

m.c3154 = Constraint(expr= - m.b51 - m.b58 + m.b189 <= 0)

m.c3155 = Constraint(expr= - m.b52 - m.b53 + m.b190 <= 0)

m.c3156 = Constraint(expr= - m.b52 - m.b54 + m.b191 <= 0)

m.c3157 = Constraint(expr= - m.b52 - m.b55 + m.b192 <= 0)

m.c3158 = Constraint(expr= - m.b52 - m.b56 + m.b193 <= 0)

m.c3159 = Constraint(expr= - m.b52 - m.b57 + m.b194 <= 0)

m.c3160 = Constraint(expr= - m.b52 - m.b58 + m.b195 <= 0)

m.c3161 = Constraint(expr= - m.b53 - m.b54 + m.b196 <= 0)

m.c3162 = Constraint(expr= - m.b53 - m.b55 + m.b197 <= 0)

m.c3163 = Constraint(expr= - m.b53 - m.b56 + m.b198 <= 0)

m.c3164 = Constraint(expr= - m.b53 - m.b57 + m.b199 <= 0)

m.c3165 = Constraint(expr= - m.b53 - m.b58 + m.b200 <= 0)

m.c3166 = Constraint(expr= - m.b54 - m.b55 + m.b201 <= 0)

m.c3167 = Constraint(expr= - m.b54 - m.b56 + m.b202 <= 0)

m.c3168 = Constraint(expr= - m.b54 - m.b57 + m.b203 <= 0)

m.c3169 = Constraint(expr= - m.b54 - m.b58 + m.b204 <= 0)

m.c3170 = Constraint(expr= - m.b55 - m.b56 + m.b205 <= 0)

m.c3171 = Constraint(expr= - m.b55 - m.b57 + m.b206 <= 0)

m.c3172 = Constraint(expr= - m.b55 - m.b58 + m.b207 <= 0)

m.c3173 = Constraint(expr= - m.b56 - m.b57 + m.b208 <= 0)

m.c3174 = Constraint(expr= - m.b56 - m.b58 + m.b209 <= 0)

m.c3175 = Constraint(expr= - m.b57 - m.b58 + m.b210 <= 0)

m.c3176 = Constraint(expr= - m.b59 - m.b60 + m.b76 <= 0)

m.c3177 = Constraint(expr= - m.b59 - m.b61 + m.b77 <= 0)

m.c3178 = Constraint(expr= - m.b59 - m.b62 + m.b78 <= 0)

m.c3179 = Constraint(expr= - m.b59 - m.b63 + m.b79 <= 0)

m.c3180 = Constraint(expr= - m.b59 - m.b64 + m.b80 <= 0)

m.c3181 = Constraint(expr= - m.b59 - m.b65 + m.b81 <= 0)

m.c3182 = Constraint(expr= - m.b59 - m.b66 + m.b82 <= 0)

m.c3183 = Constraint(expr= - m.b59 - m.b67 + m.b83 <= 0)

m.c3184 = Constraint(expr= - m.b59 - m.b68 + m.b84 <= 0)

m.c3185 = Constraint(expr= - m.b59 - m.b69 + m.b85 <= 0)

m.c3186 = Constraint(expr= - m.b59 - m.b70 + m.b86 <= 0)

m.c3187 = Constraint(expr= - m.b59 - m.b71 + m.b87 <= 0)

m.c3188 = Constraint(expr= - m.b59 - m.b72 + m.b88 <= 0)

m.c3189 = Constraint(expr= - m.b59 - m.b73 + m.b89 <= 0)

m.c3190 = Constraint(expr= - m.b59 - m.b74 + m.b90 <= 0)

m.c3191 = Constraint(expr= - m.b59 - m.b75 + m.b91 <= 0)

m.c3192 = Constraint(expr= - m.b60 - m.b61 + m.b92 <= 0)

m.c3193 = Constraint(expr= - m.b60 - m.b62 + m.b93 <= 0)

m.c3194 = Constraint(expr= - m.b60 - m.b63 + m.b94 <= 0)

m.c3195 = Constraint(expr= - m.b60 - m.b64 + m.b95 <= 0)

m.c3196 = Constraint(expr= - m.b60 - m.b65 + m.b96 <= 0)

m.c3197 = Constraint(expr= - m.b60 - m.b66 + m.b97 <= 0)

m.c3198 = Constraint(expr= - m.b60 - m.b67 + m.b98 <= 0)

m.c3199 = Constraint(expr= - m.b60 - m.b68 + m.b99 <= 0)

m.c3200 = Constraint(expr= - m.b60 - m.b69 + m.b100 <= 0)

m.c3201 = Constraint(expr= - m.b60 - m.b70 + m.b101 <= 0)

m.c3202 = Constraint(expr= - m.b60 - m.b71 + m.b102 <= 0)

m.c3203 = Constraint(expr= - m.b60 - m.b72 + m.b103 <= 0)

m.c3204 = Constraint(expr= - m.b60 - m.b73 + m.b104 <= 0)

m.c3205 = Constraint(expr= - m.b60 - m.b74 + m.b105 <= 0)

m.c3206 = Constraint(expr= - m.b60 - m.b75 + m.b106 <= 0)

m.c3207 = Constraint(expr= - m.b61 - m.b62 + m.b107 <= 0)

m.c3208 = Constraint(expr= - m.b61 - m.b63 + m.b108 <= 0)

m.c3209 = Constraint(expr= - m.b61 - m.b64 + m.b109 <= 0)

m.c3210 = Constraint(expr= - m.b61 - m.b65 + m.b110 <= 0)

m.c3211 = Constraint(expr= - m.b61 - m.b66 + m.b111 <= 0)

m.c3212 = Constraint(expr= - m.b61 - m.b67 + m.b112 <= 0)

m.c3213 = Constraint(expr= - m.b61 - m.b68 + m.b113 <= 0)

m.c3214 = Constraint(expr= - m.b61 - m.b69 + m.b114 <= 0)

m.c3215 = Constraint(expr= - m.b61 - m.b70 + m.b115 <= 0)

m.c3216 = Constraint(expr= - m.b61 - m.b71 + m.b116 <= 0)

m.c3217 = Constraint(expr= - m.b61 - m.b72 + m.b117 <= 0)

m.c3218 = Constraint(expr= - m.b61 - m.b73 + m.b118 <= 0)

m.c3219 = Constraint(expr= - m.b61 - m.b74 + m.b119 <= 0)

m.c3220 = Constraint(expr= - m.b61 - m.b75 + m.b120 <= 0)

m.c3221 = Constraint(expr= - m.b62 - m.b63 + m.b121 <= 0)

m.c3222 = Constraint(expr= - m.b62 - m.b64 + m.b122 <= 0)

m.c3223 = Constraint(expr= - m.b62 - m.b65 + m.b123 <= 0)

m.c3224 = Constraint(expr= - m.b62 - m.b66 + m.b124 <= 0)

m.c3225 = Constraint(expr= - m.b62 - m.b67 + m.b125 <= 0)

m.c3226 = Constraint(expr= - m.b62 - m.b68 + m.b126 <= 0)

m.c3227 = Constraint(expr= - m.b62 - m.b69 + m.b127 <= 0)

m.c3228 = Constraint(expr= - m.b62 - m.b70 + m.b128 <= 0)

m.c3229 = Constraint(expr= - m.b62 - m.b71 + m.b129 <= 0)

m.c3230 = Constraint(expr= - m.b62 - m.b72 + m.b130 <= 0)

m.c3231 = Constraint(expr= - m.b62 - m.b73 + m.b131 <= 0)

m.c3232 = Constraint(expr= - m.b62 - m.b74 + m.b132 <= 0)

m.c3233 = Constraint(expr= - m.b62 - m.b75 + m.b133 <= 0)

m.c3234 = Constraint(expr= - m.b63 - m.b64 + m.b134 <= 0)

m.c3235 = Constraint(expr= - m.b63 - m.b65 + m.b135 <= 0)

m.c3236 = Constraint(expr= - m.b63 - m.b66 + m.b136 <= 0)

m.c3237 = Constraint(expr= - m.b63 - m.b67 + m.b137 <= 0)

m.c3238 = Constraint(expr= - m.b63 - m.b68 + m.b138 <= 0)

m.c3239 = Constraint(expr= - m.b63 - m.b69 + m.b139 <= 0)

m.c3240 = Constraint(expr= - m.b63 - m.b70 + m.b140 <= 0)

m.c3241 = Constraint(expr= - m.b63 - m.b71 + m.b141 <= 0)

m.c3242 = Constraint(expr= - m.b63 - m.b72 + m.b142 <= 0)

m.c3243 = Constraint(expr= - m.b63 - m.b73 + m.b143 <= 0)

m.c3244 = Constraint(expr= - m.b63 - m.b74 + m.b144 <= 0)

m.c3245 = Constraint(expr= - m.b63 - m.b75 + m.b145 <= 0)

m.c3246 = Constraint(expr= - m.b64 - m.b65 + m.b146 <= 0)

m.c3247 = Constraint(expr= - m.b64 - m.b66 + m.b147 <= 0)

m.c3248 = Constraint(expr= - m.b64 - m.b67 + m.b148 <= 0)

m.c3249 = Constraint(expr= - m.b64 - m.b68 + m.b149 <= 0)

m.c3250 = Constraint(expr= - m.b64 - m.b69 + m.b150 <= 0)

m.c3251 = Constraint(expr= - m.b64 - m.b70 + m.b151 <= 0)

m.c3252 = Constraint(expr= - m.b64 - m.b71 + m.b152 <= 0)

m.c3253 = Constraint(expr= - m.b64 - m.b72 + m.b153 <= 0)

m.c3254 = Constraint(expr= - m.b64 - m.b73 + m.b154 <= 0)

m.c3255 = Constraint(expr= - m.b64 - m.b74 + m.b155 <= 0)

m.c3256 = Constraint(expr= - m.b64 - m.b75 + m.b156 <= 0)

m.c3257 = Constraint(expr= - m.b65 - m.b66 + m.b157 <= 0)

m.c3258 = Constraint(expr= - m.b65 - m.b67 + m.b158 <= 0)

m.c3259 = Constraint(expr= - m.b65 - m.b68 + m.b159 <= 0)

m.c3260 = Constraint(expr= - m.b65 - m.b69 + m.b160 <= 0)

m.c3261 = Constraint(expr= - m.b65 - m.b70 + m.b161 <= 0)

m.c3262 = Constraint(expr= - m.b65 - m.b71 + m.b162 <= 0)

m.c3263 = Constraint(expr= - m.b65 - m.b72 + m.b163 <= 0)

m.c3264 = Constraint(expr= - m.b65 - m.b73 + m.b164 <= 0)

m.c3265 = Constraint(expr= - m.b65 - m.b74 + m.b165 <= 0)

m.c3266 = Constraint(expr= - m.b65 - m.b75 + m.b211 <= 0)

m.c3267 = Constraint(expr= - m.b66 - m.b67 + m.b166 <= 0)

m.c3268 = Constraint(expr= - m.b66 - m.b68 + m.b167 <= 0)

m.c3269 = Constraint(expr= - m.b66 - m.b69 + m.b168 <= 0)

m.c3270 = Constraint(expr= - m.b66 - m.b70 + m.b169 <= 0)

m.c3271 = Constraint(expr= - m.b66 - m.b71 + m.b170 <= 0)

m.c3272 = Constraint(expr= - m.b66 - m.b72 + m.b171 <= 0)

m.c3273 = Constraint(expr= - m.b66 - m.b73 + m.b172 <= 0)

m.c3274 = Constraint(expr= - m.b66 - m.b74 + m.b173 <= 0)

m.c3275 = Constraint(expr= - m.b66 - m.b75 + m.b174 <= 0)

m.c3276 = Constraint(expr= - m.b67 - m.b68 + m.b175 <= 0)

m.c3277 = Constraint(expr= - m.b67 - m.b69 + m.b176 <= 0)

m.c3278 = Constraint(expr= - m.b67 - m.b70 + m.b177 <= 0)

m.c3279 = Constraint(expr= - m.b67 - m.b71 + m.b178 <= 0)

m.c3280 = Constraint(expr= - m.b67 - m.b72 + m.b179 <= 0)

m.c3281 = Constraint(expr= - m.b67 - m.b73 + m.b180 <= 0)

m.c3282 = Constraint(expr= - m.b67 - m.b74 + m.b181 <= 0)

m.c3283 = Constraint(expr= - m.b67 - m.b75 + m.b182 <= 0)

m.c3284 = Constraint(expr= - m.b68 - m.b69 + m.b183 <= 0)

m.c3285 = Constraint(expr= - m.b68 - m.b70 + m.b184 <= 0)

m.c3286 = Constraint(expr= - m.b68 - m.b71 + m.b185 <= 0)

m.c3287 = Constraint(expr= - m.b68 - m.b72 + m.b186 <= 0)

m.c3288 = Constraint(expr= - m.b68 - m.b73 + m.b187 <= 0)

m.c3289 = Constraint(expr= - m.b68 - m.b74 + m.b188 <= 0)

m.c3290 = Constraint(expr= - m.b68 - m.b75 + m.b189 <= 0)

m.c3291 = Constraint(expr= - m.b69 - m.b70 + m.b190 <= 0)

m.c3292 = Constraint(expr= - m.b69 - m.b71 + m.b191 <= 0)

m.c3293 = Constraint(expr= - m.b69 - m.b72 + m.b192 <= 0)

m.c3294 = Constraint(expr= - m.b69 - m.b73 + m.b193 <= 0)

m.c3295 = Constraint(expr= - m.b69 - m.b74 + m.b194 <= 0)

m.c3296 = Constraint(expr= - m.b69 - m.b75 + m.b195 <= 0)

m.c3297 = Constraint(expr= - m.b70 - m.b71 + m.b196 <= 0)

m.c3298 = Constraint(expr= - m.b70 - m.b72 + m.b197 <= 0)

m.c3299 = Constraint(expr= - m.b70 - m.b73 + m.b198 <= 0)

m.c3300 = Constraint(expr= - m.b70 - m.b74 + m.b199 <= 0)

m.c3301 = Constraint(expr= - m.b70 - m.b75 + m.b200 <= 0)

m.c3302 = Constraint(expr= - m.b71 - m.b72 + m.b201 <= 0)

m.c3303 = Constraint(expr= - m.b71 - m.b73 + m.b202 <= 0)

m.c3304 = Constraint(expr= - m.b71 - m.b74 + m.b203 <= 0)

m.c3305 = Constraint(expr= - m.b71 - m.b75 + m.b204 <= 0)

m.c3306 = Constraint(expr= - m.b72 - m.b73 + m.b205 <= 0)

m.c3307 = Constraint(expr= - m.b72 - m.b74 + m.b206 <= 0)

m.c3308 = Constraint(expr= - m.b72 - m.b75 + m.b207 <= 0)

m.c3309 = Constraint(expr= - m.b73 - m.b74 + m.b208 <= 0)

m.c3310 = Constraint(expr= - m.b73 - m.b75 + m.b209 <= 0)

m.c3311 = Constraint(expr= - m.b74 - m.b75 + m.b210 <= 0)

m.c3312 = Constraint(expr= - m.b76 - m.b77 + m.b92 <= 0)

m.c3313 = Constraint(expr= - m.b76 - m.b78 + m.b93 <= 0)

m.c3314 = Constraint(expr= - m.b76 - m.b79 + m.b94 <= 0)

m.c3315 = Constraint(expr= - m.b76 - m.b80 + m.b95 <= 0)

m.c3316 = Constraint(expr= - m.b76 - m.b81 + m.b96 <= 0)

m.c3317 = Constraint(expr= - m.b76 - m.b82 + m.b97 <= 0)

m.c3318 = Constraint(expr= - m.b76 - m.b83 + m.b98 <= 0)

m.c3319 = Constraint(expr= - m.b76 - m.b84 + m.b99 <= 0)

m.c3320 = Constraint(expr= - m.b76 - m.b85 + m.b100 <= 0)

m.c3321 = Constraint(expr= - m.b76 - m.b86 + m.b101 <= 0)

m.c3322 = Constraint(expr= - m.b76 - m.b87 + m.b102 <= 0)

m.c3323 = Constraint(expr= - m.b76 - m.b88 + m.b103 <= 0)

m.c3324 = Constraint(expr= - m.b76 - m.b89 + m.b104 <= 0)

m.c3325 = Constraint(expr= - m.b76 - m.b90 + m.b105 <= 0)

m.c3326 = Constraint(expr= - m.b76 - m.b91 + m.b106 <= 0)

m.c3327 = Constraint(expr= - m.b77 - m.b78 + m.b107 <= 0)

m.c3328 = Constraint(expr= - m.b77 - m.b79 + m.b108 <= 0)

m.c3329 = Constraint(expr= - m.b77 - m.b80 + m.b109 <= 0)

m.c3330 = Constraint(expr= - m.b77 - m.b81 + m.b110 <= 0)

m.c3331 = Constraint(expr= - m.b77 - m.b82 + m.b111 <= 0)

m.c3332 = Constraint(expr= - m.b77 - m.b83 + m.b112 <= 0)

m.c3333 = Constraint(expr= - m.b77 - m.b84 + m.b113 <= 0)

m.c3334 = Constraint(expr= - m.b77 - m.b85 + m.b114 <= 0)

m.c3335 = Constraint(expr= - m.b77 - m.b86 + m.b115 <= 0)

m.c3336 = Constraint(expr= - m.b77 - m.b87 + m.b116 <= 0)

m.c3337 = Constraint(expr= - m.b77 - m.b88 + m.b117 <= 0)

m.c3338 = Constraint(expr= - m.b77 - m.b89 + m.b118 <= 0)

m.c3339 = Constraint(expr= - m.b77 - m.b90 + m.b119 <= 0)

m.c3340 = Constraint(expr= - m.b77 - m.b91 + m.b120 <= 0)

m.c3341 = Constraint(expr= - m.b78 - m.b79 + m.b121 <= 0)

m.c3342 = Constraint(expr= - m.b78 - m.b80 + m.b122 <= 0)

m.c3343 = Constraint(expr= - m.b78 - m.b81 + m.b123 <= 0)

m.c3344 = Constraint(expr= - m.b78 - m.b82 + m.b124 <= 0)

m.c3345 = Constraint(expr= - m.b78 - m.b83 + m.b125 <= 0)

m.c3346 = Constraint(expr= - m.b78 - m.b84 + m.b126 <= 0)

m.c3347 = Constraint(expr= - m.b78 - m.b85 + m.b127 <= 0)

m.c3348 = Constraint(expr= - m.b78 - m.b86 + m.b128 <= 0)

m.c3349 = Constraint(expr= - m.b78 - m.b87 + m.b129 <= 0)

m.c3350 = Constraint(expr= - m.b78 - m.b88 + m.b130 <= 0)

m.c3351 = Constraint(expr= - m.b78 - m.b89 + m.b131 <= 0)

m.c3352 = Constraint(expr= - m.b78 - m.b90 + m.b132 <= 0)

m.c3353 = Constraint(expr= - m.b78 - m.b91 + m.b133 <= 0)

m.c3354 = Constraint(expr= - m.b79 - m.b80 + m.b134 <= 0)

m.c3355 = Constraint(expr= - m.b79 - m.b81 + m.b135 <= 0)

m.c3356 = Constraint(expr= - m.b79 - m.b82 + m.b136 <= 0)

m.c3357 = Constraint(expr= - m.b79 - m.b83 + m.b137 <= 0)

m.c3358 = Constraint(expr= - m.b79 - m.b84 + m.b138 <= 0)

m.c3359 = Constraint(expr= - m.b79 - m.b85 + m.b139 <= 0)

m.c3360 = Constraint(expr= - m.b79 - m.b86 + m.b140 <= 0)

m.c3361 = Constraint(expr= - m.b79 - m.b87 + m.b141 <= 0)

m.c3362 = Constraint(expr= - m.b79 - m.b88 + m.b142 <= 0)

m.c3363 = Constraint(expr= - m.b79 - m.b89 + m.b143 <= 0)

m.c3364 = Constraint(expr= - m.b79 - m.b90 + m.b144 <= 0)

m.c3365 = Constraint(expr= - m.b79 - m.b91 + m.b145 <= 0)

m.c3366 = Constraint(expr= - m.b80 - m.b81 + m.b146 <= 0)

m.c3367 = Constraint(expr= - m.b80 - m.b82 + m.b147 <= 0)

m.c3368 = Constraint(expr= - m.b80 - m.b83 + m.b148 <= 0)

m.c3369 = Constraint(expr= - m.b80 - m.b84 + m.b149 <= 0)

m.c3370 = Constraint(expr= - m.b80 - m.b85 + m.b150 <= 0)

m.c3371 = Constraint(expr= - m.b80 - m.b86 + m.b151 <= 0)

m.c3372 = Constraint(expr= - m.b80 - m.b87 + m.b152 <= 0)

m.c3373 = Constraint(expr= - m.b80 - m.b88 + m.b153 <= 0)

m.c3374 = Constraint(expr= - m.b80 - m.b89 + m.b154 <= 0)

m.c3375 = Constraint(expr= - m.b80 - m.b90 + m.b155 <= 0)

m.c3376 = Constraint(expr= - m.b80 - m.b91 + m.b156 <= 0)

m.c3377 = Constraint(expr= - m.b81 - m.b82 + m.b157 <= 0)

m.c3378 = Constraint(expr= - m.b81 - m.b83 + m.b158 <= 0)

m.c3379 = Constraint(expr= - m.b81 - m.b84 + m.b159 <= 0)

m.c3380 = Constraint(expr= - m.b81 - m.b85 + m.b160 <= 0)

m.c3381 = Constraint(expr= - m.b81 - m.b86 + m.b161 <= 0)

m.c3382 = Constraint(expr= - m.b81 - m.b87 + m.b162 <= 0)

m.c3383 = Constraint(expr= - m.b81 - m.b88 + m.b163 <= 0)

m.c3384 = Constraint(expr= - m.b81 - m.b89 + m.b164 <= 0)

m.c3385 = Constraint(expr= - m.b81 - m.b90 + m.b165 <= 0)

m.c3386 = Constraint(expr= - m.b81 - m.b91 + m.b211 <= 0)

m.c3387 = Constraint(expr= - m.b82 - m.b83 + m.b166 <= 0)

m.c3388 = Constraint(expr= - m.b82 - m.b84 + m.b167 <= 0)

m.c3389 = Constraint(expr= - m.b82 - m.b85 + m.b168 <= 0)

m.c3390 = Constraint(expr= - m.b82 - m.b86 + m.b169 <= 0)

m.c3391 = Constraint(expr= - m.b82 - m.b87 + m.b170 <= 0)

m.c3392 = Constraint(expr= - m.b82 - m.b88 + m.b171 <= 0)

m.c3393 = Constraint(expr= - m.b82 - m.b89 + m.b172 <= 0)

m.c3394 = Constraint(expr= - m.b82 - m.b90 + m.b173 <= 0)

m.c3395 = Constraint(expr= - m.b82 - m.b91 + m.b174 <= 0)

m.c3396 = Constraint(expr= - m.b83 - m.b84 + m.b175 <= 0)

m.c3397 = Constraint(expr= - m.b83 - m.b85 + m.b176 <= 0)

m.c3398 = Constraint(expr= - m.b83 - m.b86 + m.b177 <= 0)

m.c3399 = Constraint(expr= - m.b83 - m.b87 + m.b178 <= 0)

m.c3400 = Constraint(expr= - m.b83 - m.b88 + m.b179 <= 0)

m.c3401 = Constraint(expr= - m.b83 - m.b89 + m.b180 <= 0)

m.c3402 = Constraint(expr= - m.b83 - m.b90 + m.b181 <= 0)

m.c3403 = Constraint(expr= - m.b83 - m.b91 + m.b182 <= 0)

m.c3404 = Constraint(expr= - m.b84 - m.b85 + m.b183 <= 0)

m.c3405 = Constraint(expr= - m.b84 - m.b86 + m.b184 <= 0)

m.c3406 = Constraint(expr= - m.b84 - m.b87 + m.b185 <= 0)

m.c3407 = Constraint(expr= - m.b84 - m.b88 + m.b186 <= 0)

m.c3408 = Constraint(expr= - m.b84 - m.b89 + m.b187 <= 0)

m.c3409 = Constraint(expr= - m.b84 - m.b90 + m.b188 <= 0)

m.c3410 = Constraint(expr= - m.b84 - m.b91 + m.b189 <= 0)

m.c3411 = Constraint(expr= - m.b85 - m.b86 + m.b190 <= 0)

m.c3412 = Constraint(expr= - m.b85 - m.b87 + m.b191 <= 0)

m.c3413 = Constraint(expr= - m.b85 - m.b88 + m.b192 <= 0)

m.c3414 = Constraint(expr= - m.b85 - m.b89 + m.b193 <= 0)

m.c3415 = Constraint(expr= - m.b85 - m.b90 + m.b194 <= 0)

m.c3416 = Constraint(expr= - m.b85 - m.b91 + m.b195 <= 0)

m.c3417 = Constraint(expr= - m.b86 - m.b87 + m.b196 <= 0)

m.c3418 = Constraint(expr= - m.b86 - m.b88 + m.b197 <= 0)

m.c3419 = Constraint(expr= - m.b86 - m.b89 + m.b198 <= 0)

m.c3420 = Constraint(expr= - m.b86 - m.b90 + m.b199 <= 0)

m.c3421 = Constraint(expr= - m.b86 - m.b91 + m.b200 <= 0)

m.c3422 = Constraint(expr= - m.b87 - m.b88 + m.b201 <= 0)

m.c3423 = Constraint(expr= - m.b87 - m.b89 + m.b202 <= 0)

m.c3424 = Constraint(expr= - m.b87 - m.b90 + m.b203 <= 0)

m.c3425 = Constraint(expr= - m.b87 - m.b91 + m.b204 <= 0)

m.c3426 = Constraint(expr= - m.b88 - m.b89 + m.b205 <= 0)

m.c3427 = Constraint(expr= - m.b88 - m.b90 + m.b206 <= 0)

m.c3428 = Constraint(expr= - m.b88 - m.b91 + m.b207 <= 0)

m.c3429 = Constraint(expr= - m.b89 - m.b90 + m.b208 <= 0)

m.c3430 = Constraint(expr= - m.b89 - m.b91 + m.b209 <= 0)

m.c3431 = Constraint(expr= - m.b90 - m.b91 + m.b210 <= 0)

m.c3432 = Constraint(expr= - m.b92 - m.b93 + m.b107 <= 0)

m.c3433 = Constraint(expr= - m.b92 - m.b94 + m.b108 <= 0)

m.c3434 = Constraint(expr= - m.b92 - m.b95 + m.b109 <= 0)

m.c3435 = Constraint(expr= - m.b92 - m.b96 + m.b110 <= 0)

m.c3436 = Constraint(expr= - m.b92 - m.b97 + m.b111 <= 0)

m.c3437 = Constraint(expr= - m.b92 - m.b98 + m.b112 <= 0)

m.c3438 = Constraint(expr= - m.b92 - m.b99 + m.b113 <= 0)

m.c3439 = Constraint(expr= - m.b92 - m.b100 + m.b114 <= 0)

m.c3440 = Constraint(expr= - m.b92 - m.b101 + m.b115 <= 0)

m.c3441 = Constraint(expr= - m.b92 - m.b102 + m.b116 <= 0)

m.c3442 = Constraint(expr= - m.b92 - m.b103 + m.b117 <= 0)

m.c3443 = Constraint(expr= - m.b92 - m.b104 + m.b118 <= 0)

m.c3444 = Constraint(expr= - m.b92 - m.b105 + m.b119 <= 0)

m.c3445 = Constraint(expr= - m.b92 - m.b106 + m.b120 <= 0)

m.c3446 = Constraint(expr= - m.b93 - m.b94 + m.b121 <= 0)

m.c3447 = Constraint(expr= - m.b93 - m.b95 + m.b122 <= 0)

m.c3448 = Constraint(expr= - m.b93 - m.b96 + m.b123 <= 0)

m.c3449 = Constraint(expr= - m.b93 - m.b97 + m.b124 <= 0)

m.c3450 = Constraint(expr= - m.b93 - m.b98 + m.b125 <= 0)

m.c3451 = Constraint(expr= - m.b93 - m.b99 + m.b126 <= 0)

m.c3452 = Constraint(expr= - m.b93 - m.b100 + m.b127 <= 0)

m.c3453 = Constraint(expr= - m.b93 - m.b101 + m.b128 <= 0)

m.c3454 = Constraint(expr= - m.b93 - m.b102 + m.b129 <= 0)

m.c3455 = Constraint(expr= - m.b93 - m.b103 + m.b130 <= 0)

m.c3456 = Constraint(expr= - m.b93 - m.b104 + m.b131 <= 0)

m.c3457 = Constraint(expr= - m.b93 - m.b105 + m.b132 <= 0)

m.c3458 = Constraint(expr= - m.b93 - m.b106 + m.b133 <= 0)

m.c3459 = Constraint(expr= - m.b94 - m.b95 + m.b134 <= 0)

m.c3460 = Constraint(expr= - m.b94 - m.b96 + m.b135 <= 0)

m.c3461 = Constraint(expr= - m.b94 - m.b97 + m.b136 <= 0)

m.c3462 = Constraint(expr= - m.b94 - m.b98 + m.b137 <= 0)

m.c3463 = Constraint(expr= - m.b94 - m.b99 + m.b138 <= 0)

m.c3464 = Constraint(expr= - m.b94 - m.b100 + m.b139 <= 0)

m.c3465 = Constraint(expr= - m.b94 - m.b101 + m.b140 <= 0)

m.c3466 = Constraint(expr= - m.b94 - m.b102 + m.b141 <= 0)

m.c3467 = Constraint(expr= - m.b94 - m.b103 + m.b142 <= 0)

m.c3468 = Constraint(expr= - m.b94 - m.b104 + m.b143 <= 0)

m.c3469 = Constraint(expr= - m.b94 - m.b105 + m.b144 <= 0)

m.c3470 = Constraint(expr= - m.b94 - m.b106 + m.b145 <= 0)

m.c3471 = Constraint(expr= - m.b95 - m.b96 + m.b146 <= 0)

m.c3472 = Constraint(expr= - m.b95 - m.b97 + m.b147 <= 0)

m.c3473 = Constraint(expr= - m.b95 - m.b98 + m.b148 <= 0)

m.c3474 = Constraint(expr= - m.b95 - m.b99 + m.b149 <= 0)

m.c3475 = Constraint(expr= - m.b95 - m.b100 + m.b150 <= 0)

m.c3476 = Constraint(expr= - m.b95 - m.b101 + m.b151 <= 0)

m.c3477 = Constraint(expr= - m.b95 - m.b102 + m.b152 <= 0)

m.c3478 = Constraint(expr= - m.b95 - m.b103 + m.b153 <= 0)

m.c3479 = Constraint(expr= - m.b95 - m.b104 + m.b154 <= 0)

m.c3480 = Constraint(expr= - m.b95 - m.b105 + m.b155 <= 0)

m.c3481 = Constraint(expr= - m.b95 - m.b106 + m.b156 <= 0)

m.c3482 = Constraint(expr= - m.b96 - m.b97 + m.b157 <= 0)

m.c3483 = Constraint(expr= - m.b96 - m.b98 + m.b158 <= 0)

m.c3484 = Constraint(expr= - m.b96 - m.b99 + m.b159 <= 0)

m.c3485 = Constraint(expr= - m.b96 - m.b100 + m.b160 <= 0)

m.c3486 = Constraint(expr= - m.b96 - m.b101 + m.b161 <= 0)

m.c3487 = Constraint(expr= - m.b96 - m.b102 + m.b162 <= 0)

m.c3488 = Constraint(expr= - m.b96 - m.b103 + m.b163 <= 0)

m.c3489 = Constraint(expr= - m.b96 - m.b104 + m.b164 <= 0)

m.c3490 = Constraint(expr= - m.b96 - m.b105 + m.b165 <= 0)

m.c3491 = Constraint(expr= - m.b96 - m.b106 + m.b211 <= 0)

m.c3492 = Constraint(expr= - m.b97 - m.b98 + m.b166 <= 0)

m.c3493 = Constraint(expr= - m.b97 - m.b99 + m.b167 <= 0)

m.c3494 = Constraint(expr= - m.b97 - m.b100 + m.b168 <= 0)

m.c3495 = Constraint(expr= - m.b97 - m.b101 + m.b169 <= 0)

m.c3496 = Constraint(expr= - m.b97 - m.b102 + m.b170 <= 0)

m.c3497 = Constraint(expr= - m.b97 - m.b103 + m.b171 <= 0)

m.c3498 = Constraint(expr= - m.b97 - m.b104 + m.b172 <= 0)

m.c3499 = Constraint(expr= - m.b97 - m.b105 + m.b173 <= 0)

m.c3500 = Constraint(expr= - m.b97 - m.b106 + m.b174 <= 0)

m.c3501 = Constraint(expr= - m.b98 - m.b99 + m.b175 <= 0)

m.c3502 = Constraint(expr= - m.b98 - m.b100 + m.b176 <= 0)

m.c3503 = Constraint(expr= - m.b98 - m.b101 + m.b177 <= 0)

m.c3504 = Constraint(expr= - m.b98 - m.b102 + m.b178 <= 0)

m.c3505 = Constraint(expr= - m.b98 - m.b103 + m.b179 <= 0)

m.c3506 = Constraint(expr= - m.b98 - m.b104 + m.b180 <= 0)

m.c3507 = Constraint(expr= - m.b98 - m.b105 + m.b181 <= 0)

m.c3508 = Constraint(expr= - m.b98 - m.b106 + m.b182 <= 0)

m.c3509 = Constraint(expr= - m.b99 - m.b100 + m.b183 <= 0)

m.c3510 = Constraint(expr= - m.b99 - m.b101 + m.b184 <= 0)

m.c3511 = Constraint(expr= - m.b99 - m.b102 + m.b185 <= 0)

m.c3512 = Constraint(expr= - m.b99 - m.b103 + m.b186 <= 0)

m.c3513 = Constraint(expr= - m.b99 - m.b104 + m.b187 <= 0)

m.c3514 = Constraint(expr= - m.b99 - m.b105 + m.b188 <= 0)

m.c3515 = Constraint(expr= - m.b99 - m.b106 + m.b189 <= 0)

m.c3516 = Constraint(expr= - m.b100 - m.b101 + m.b190 <= 0)

m.c3517 = Constraint(expr= - m.b100 - m.b102 + m.b191 <= 0)

m.c3518 = Constraint(expr= - m.b100 - m.b103 + m.b192 <= 0)

m.c3519 = Constraint(expr= - m.b100 - m.b104 + m.b193 <= 0)

m.c3520 = Constraint(expr= - m.b100 - m.b105 + m.b194 <= 0)

m.c3521 = Constraint(expr= - m.b100 - m.b106 + m.b195 <= 0)

m.c3522 = Constraint(expr= - m.b101 - m.b102 + m.b196 <= 0)

m.c3523 = Constraint(expr= - m.b101 - m.b103 + m.b197 <= 0)

m.c3524 = Constraint(expr= - m.b101 - m.b104 + m.b198 <= 0)

m.c3525 = Constraint(expr= - m.b101 - m.b105 + m.b199 <= 0)

m.c3526 = Constraint(expr= - m.b101 - m.b106 + m.b200 <= 0)

m.c3527 = Constraint(expr= - m.b102 - m.b103 + m.b201 <= 0)

m.c3528 = Constraint(expr= - m.b102 - m.b104 + m.b202 <= 0)

m.c3529 = Constraint(expr= - m.b102 - m.b105 + m.b203 <= 0)

m.c3530 = Constraint(expr= - m.b102 - m.b106 + m.b204 <= 0)

m.c3531 = Constraint(expr= - m.b103 - m.b104 + m.b205 <= 0)

m.c3532 = Constraint(expr= - m.b103 - m.b105 + m.b206 <= 0)

m.c3533 = Constraint(expr= - m.b103 - m.b106 + m.b207 <= 0)

m.c3534 = Constraint(expr= - m.b104 - m.b105 + m.b208 <= 0)

m.c3535 = Constraint(expr= - m.b104 - m.b106 + m.b209 <= 0)

m.c3536 = Constraint(expr= - m.b105 - m.b106 + m.b210 <= 0)

m.c3537 = Constraint(expr= - m.b107 - m.b108 + m.b121 <= 0)

m.c3538 = Constraint(expr= - m.b107 - m.b109 + m.b122 <= 0)

m.c3539 = Constraint(expr= - m.b107 - m.b110 + m.b123 <= 0)

m.c3540 = Constraint(expr= - m.b107 - m.b111 + m.b124 <= 0)

m.c3541 = Constraint(expr= - m.b107 - m.b112 + m.b125 <= 0)

m.c3542 = Constraint(expr= - m.b107 - m.b113 + m.b126 <= 0)

m.c3543 = Constraint(expr= - m.b107 - m.b114 + m.b127 <= 0)

m.c3544 = Constraint(expr= - m.b107 - m.b115 + m.b128 <= 0)

m.c3545 = Constraint(expr= - m.b107 - m.b116 + m.b129 <= 0)

m.c3546 = Constraint(expr= - m.b107 - m.b117 + m.b130 <= 0)

m.c3547 = Constraint(expr= - m.b107 - m.b118 + m.b131 <= 0)

m.c3548 = Constraint(expr= - m.b107 - m.b119 + m.b132 <= 0)

m.c3549 = Constraint(expr= - m.b107 - m.b120 + m.b133 <= 0)

m.c3550 = Constraint(expr= - m.b108 - m.b109 + m.b134 <= 0)

m.c3551 = Constraint(expr= - m.b108 - m.b110 + m.b135 <= 0)

m.c3552 = Constraint(expr= - m.b108 - m.b111 + m.b136 <= 0)

m.c3553 = Constraint(expr= - m.b108 - m.b112 + m.b137 <= 0)

m.c3554 = Constraint(expr= - m.b108 - m.b113 + m.b138 <= 0)

m.c3555 = Constraint(expr= - m.b108 - m.b114 + m.b139 <= 0)

m.c3556 = Constraint(expr= - m.b108 - m.b115 + m.b140 <= 0)

m.c3557 = Constraint(expr= - m.b108 - m.b116 + m.b141 <= 0)

m.c3558 = Constraint(expr= - m.b108 - m.b117 + m.b142 <= 0)

m.c3559 = Constraint(expr= - m.b108 - m.b118 + m.b143 <= 0)

m.c3560 = Constraint(expr= - m.b108 - m.b119 + m.b144 <= 0)

m.c3561 = Constraint(expr= - m.b108 - m.b120 + m.b145 <= 0)

m.c3562 = Constraint(expr= - m.b109 - m.b110 + m.b146 <= 0)

m.c3563 = Constraint(expr= - m.b109 - m.b111 + m.b147 <= 0)

m.c3564 = Constraint(expr= - m.b109 - m.b112 + m.b148 <= 0)

m.c3565 = Constraint(expr= - m.b109 - m.b113 + m.b149 <= 0)

m.c3566 = Constraint(expr= - m.b109 - m.b114 + m.b150 <= 0)

m.c3567 = Constraint(expr= - m.b109 - m.b115 + m.b151 <= 0)

m.c3568 = Constraint(expr= - m.b109 - m.b116 + m.b152 <= 0)

m.c3569 = Constraint(expr= - m.b109 - m.b117 + m.b153 <= 0)

m.c3570 = Constraint(expr= - m.b109 - m.b118 + m.b154 <= 0)

m.c3571 = Constraint(expr= - m.b109 - m.b119 + m.b155 <= 0)

m.c3572 = Constraint(expr= - m.b109 - m.b120 + m.b156 <= 0)

m.c3573 = Constraint(expr= - m.b110 - m.b111 + m.b157 <= 0)

m.c3574 = Constraint(expr= - m.b110 - m.b112 + m.b158 <= 0)

m.c3575 = Constraint(expr= - m.b110 - m.b113 + m.b159 <= 0)

m.c3576 = Constraint(expr= - m.b110 - m.b114 + m.b160 <= 0)

m.c3577 = Constraint(expr= - m.b110 - m.b115 + m.b161 <= 0)

m.c3578 = Constraint(expr= - m.b110 - m.b116 + m.b162 <= 0)

m.c3579 = Constraint(expr= - m.b110 - m.b117 + m.b163 <= 0)

m.c3580 = Constraint(expr= - m.b110 - m.b118 + m.b164 <= 0)

m.c3581 = Constraint(expr= - m.b110 - m.b119 + m.b165 <= 0)

m.c3582 = Constraint(expr= - m.b110 - m.b120 + m.b211 <= 0)

m.c3583 = Constraint(expr= - m.b111 - m.b112 + m.b166 <= 0)

m.c3584 = Constraint(expr= - m.b111 - m.b113 + m.b167 <= 0)

m.c3585 = Constraint(expr= - m.b111 - m.b114 + m.b168 <= 0)

m.c3586 = Constraint(expr= - m.b111 - m.b115 + m.b169 <= 0)

m.c3587 = Constraint(expr= - m.b111 - m.b116 + m.b170 <= 0)

m.c3588 = Constraint(expr= - m.b111 - m.b117 + m.b171 <= 0)

m.c3589 = Constraint(expr= - m.b111 - m.b118 + m.b172 <= 0)

m.c3590 = Constraint(expr= - m.b111 - m.b119 + m.b173 <= 0)

m.c3591 = Constraint(expr= - m.b111 - m.b120 + m.b174 <= 0)

m.c3592 = Constraint(expr= - m.b112 - m.b113 + m.b175 <= 0)

m.c3593 = Constraint(expr= - m.b112 - m.b114 + m.b176 <= 0)

m.c3594 = Constraint(expr= - m.b112 - m.b115 + m.b177 <= 0)

m.c3595 = Constraint(expr= - m.b112 - m.b116 + m.b178 <= 0)

m.c3596 = Constraint(expr= - m.b112 - m.b117 + m.b179 <= 0)

m.c3597 = Constraint(expr= - m.b112 - m.b118 + m.b180 <= 0)

m.c3598 = Constraint(expr= - m.b112 - m.b119 + m.b181 <= 0)

m.c3599 = Constraint(expr= - m.b112 - m.b120 + m.b182 <= 0)

m.c3600 = Constraint(expr= - m.b113 - m.b114 + m.b183 <= 0)

m.c3601 = Constraint(expr= - m.b113 - m.b115 + m.b184 <= 0)

m.c3602 = Constraint(expr= - m.b113 - m.b116 + m.b185 <= 0)

m.c3603 = Constraint(expr= - m.b113 - m.b117 + m.b186 <= 0)

m.c3604 = Constraint(expr= - m.b113 - m.b118 + m.b187 <= 0)

m.c3605 = Constraint(expr= - m.b113 - m.b119 + m.b188 <= 0)

m.c3606 = Constraint(expr= - m.b113 - m.b120 + m.b189 <= 0)

m.c3607 = Constraint(expr= - m.b114 - m.b115 + m.b190 <= 0)

m.c3608 = Constraint(expr= - m.b114 - m.b116 + m.b191 <= 0)

m.c3609 = Constraint(expr= - m.b114 - m.b117 + m.b192 <= 0)

m.c3610 = Constraint(expr= - m.b114 - m.b118 + m.b193 <= 0)

m.c3611 = Constraint(expr= - m.b114 - m.b119 + m.b194 <= 0)

m.c3612 = Constraint(expr= - m.b114 - m.b120 + m.b195 <= 0)

m.c3613 = Constraint(expr= - m.b115 - m.b116 + m.b196 <= 0)

m.c3614 = Constraint(expr= - m.b115 - m.b117 + m.b197 <= 0)

m.c3615 = Constraint(expr= - m.b115 - m.b118 + m.b198 <= 0)

m.c3616 = Constraint(expr= - m.b115 - m.b119 + m.b199 <= 0)

m.c3617 = Constraint(expr= - m.b115 - m.b120 + m.b200 <= 0)

m.c3618 = Constraint(expr= - m.b116 - m.b117 + m.b201 <= 0)

m.c3619 = Constraint(expr= - m.b116 - m.b118 + m.b202 <= 0)

m.c3620 = Constraint(expr= - m.b116 - m.b119 + m.b203 <= 0)

m.c3621 = Constraint(expr= - m.b116 - m.b120 + m.b204 <= 0)

m.c3622 = Constraint(expr= - m.b117 - m.b118 + m.b205 <= 0)

m.c3623 = Constraint(expr= - m.b117 - m.b119 + m.b206 <= 0)

m.c3624 = Constraint(expr= - m.b117 - m.b120 + m.b207 <= 0)

m.c3625 = Constraint(expr= - m.b118 - m.b119 + m.b208 <= 0)

m.c3626 = Constraint(expr= - m.b118 - m.b120 + m.b209 <= 0)

m.c3627 = Constraint(expr= - m.b119 - m.b120 + m.b210 <= 0)

m.c3628 = Constraint(expr= - m.b121 - m.b122 + m.b134 <= 0)

m.c3629 = Constraint(expr= - m.b121 - m.b123 + m.b135 <= 0)

m.c3630 = Constraint(expr= - m.b121 - m.b124 + m.b136 <= 0)

m.c3631 = Constraint(expr= - m.b121 - m.b125 + m.b137 <= 0)

m.c3632 = Constraint(expr= - m.b121 - m.b126 + m.b138 <= 0)

m.c3633 = Constraint(expr= - m.b121 - m.b127 + m.b139 <= 0)

m.c3634 = Constraint(expr= - m.b121 - m.b128 + m.b140 <= 0)

m.c3635 = Constraint(expr= - m.b121 - m.b129 + m.b141 <= 0)

m.c3636 = Constraint(expr= - m.b121 - m.b130 + m.b142 <= 0)

m.c3637 = Constraint(expr= - m.b121 - m.b131 + m.b143 <= 0)

m.c3638 = Constraint(expr= - m.b121 - m.b132 + m.b144 <= 0)

m.c3639 = Constraint(expr= - m.b121 - m.b133 + m.b145 <= 0)

m.c3640 = Constraint(expr= - m.b122 - m.b123 + m.b146 <= 0)

m.c3641 = Constraint(expr= - m.b122 - m.b124 + m.b147 <= 0)

m.c3642 = Constraint(expr= - m.b122 - m.b125 + m.b148 <= 0)

m.c3643 = Constraint(expr= - m.b122 - m.b126 + m.b149 <= 0)

m.c3644 = Constraint(expr= - m.b122 - m.b127 + m.b150 <= 0)

m.c3645 = Constraint(expr= - m.b122 - m.b128 + m.b151 <= 0)

m.c3646 = Constraint(expr= - m.b122 - m.b129 + m.b152 <= 0)

m.c3647 = Constraint(expr= - m.b122 - m.b130 + m.b153 <= 0)

m.c3648 = Constraint(expr= - m.b122 - m.b131 + m.b154 <= 0)

m.c3649 = Constraint(expr= - m.b122 - m.b132 + m.b155 <= 0)

m.c3650 = Constraint(expr= - m.b122 - m.b133 + m.b156 <= 0)

m.c3651 = Constraint(expr= - m.b123 - m.b124 + m.b157 <= 0)

m.c3652 = Constraint(expr= - m.b123 - m.b125 + m.b158 <= 0)

m.c3653 = Constraint(expr= - m.b123 - m.b126 + m.b159 <= 0)

m.c3654 = Constraint(expr= - m.b123 - m.b127 + m.b160 <= 0)

m.c3655 = Constraint(expr= - m.b123 - m.b128 + m.b161 <= 0)

m.c3656 = Constraint(expr= - m.b123 - m.b129 + m.b162 <= 0)

m.c3657 = Constraint(expr= - m.b123 - m.b130 + m.b163 <= 0)

m.c3658 = Constraint(expr= - m.b123 - m.b131 + m.b164 <= 0)

m.c3659 = Constraint(expr= - m.b123 - m.b132 + m.b165 <= 0)

m.c3660 = Constraint(expr= - m.b123 - m.b133 + m.b211 <= 0)

m.c3661 = Constraint(expr= - m.b124 - m.b125 + m.b166 <= 0)

m.c3662 = Constraint(expr= - m.b124 - m.b126 + m.b167 <= 0)

m.c3663 = Constraint(expr= - m.b124 - m.b127 + m.b168 <= 0)

m.c3664 = Constraint(expr= - m.b124 - m.b128 + m.b169 <= 0)

m.c3665 = Constraint(expr= - m.b124 - m.b129 + m.b170 <= 0)

m.c3666 = Constraint(expr= - m.b124 - m.b130 + m.b171 <= 0)

m.c3667 = Constraint(expr= - m.b124 - m.b131 + m.b172 <= 0)

m.c3668 = Constraint(expr= - m.b124 - m.b132 + m.b173 <= 0)

m.c3669 = Constraint(expr= - m.b124 - m.b133 + m.b174 <= 0)

m.c3670 = Constraint(expr= - m.b125 - m.b126 + m.b175 <= 0)

m.c3671 = Constraint(expr= - m.b125 - m.b127 + m.b176 <= 0)

m.c3672 = Constraint(expr= - m.b125 - m.b128 + m.b177 <= 0)

m.c3673 = Constraint(expr= - m.b125 - m.b129 + m.b178 <= 0)

m.c3674 = Constraint(expr= - m.b125 - m.b130 + m.b179 <= 0)

m.c3675 = Constraint(expr= - m.b125 - m.b131 + m.b180 <= 0)

m.c3676 = Constraint(expr= - m.b125 - m.b132 + m.b181 <= 0)

m.c3677 = Constraint(expr= - m.b125 - m.b133 + m.b182 <= 0)

m.c3678 = Constraint(expr= - m.b126 - m.b127 + m.b183 <= 0)

m.c3679 = Constraint(expr= - m.b126 - m.b128 + m.b184 <= 0)

m.c3680 = Constraint(expr= - m.b126 - m.b129 + m.b185 <= 0)

m.c3681 = Constraint(expr= - m.b126 - m.b130 + m.b186 <= 0)

m.c3682 = Constraint(expr= - m.b126 - m.b131 + m.b187 <= 0)

m.c3683 = Constraint(expr= - m.b126 - m.b132 + m.b188 <= 0)

m.c3684 = Constraint(expr= - m.b126 - m.b133 + m.b189 <= 0)

m.c3685 = Constraint(expr= - m.b127 - m.b128 + m.b190 <= 0)

m.c3686 = Constraint(expr= - m.b127 - m.b129 + m.b191 <= 0)

m.c3687 = Constraint(expr= - m.b127 - m.b130 + m.b192 <= 0)

m.c3688 = Constraint(expr= - m.b127 - m.b131 + m.b193 <= 0)

m.c3689 = Constraint(expr= - m.b127 - m.b132 + m.b194 <= 0)

m.c3690 = Constraint(expr= - m.b127 - m.b133 + m.b195 <= 0)

m.c3691 = Constraint(expr= - m.b128 - m.b129 + m.b196 <= 0)

m.c3692 = Constraint(expr= - m.b128 - m.b130 + m.b197 <= 0)

m.c3693 = Constraint(expr= - m.b128 - m.b131 + m.b198 <= 0)

m.c3694 = Constraint(expr= - m.b128 - m.b132 + m.b199 <= 0)

m.c3695 = Constraint(expr= - m.b128 - m.b133 + m.b200 <= 0)

m.c3696 = Constraint(expr= - m.b129 - m.b130 + m.b201 <= 0)

m.c3697 = Constraint(expr= - m.b129 - m.b131 + m.b202 <= 0)

m.c3698 = Constraint(expr= - m.b129 - m.b132 + m.b203 <= 0)

m.c3699 = Constraint(expr= - m.b129 - m.b133 + m.b204 <= 0)

m.c3700 = Constraint(expr= - m.b130 - m.b131 + m.b205 <= 0)

m.c3701 = Constraint(expr= - m.b130 - m.b132 + m.b206 <= 0)

m.c3702 = Constraint(expr= - m.b130 - m.b133 + m.b207 <= 0)

m.c3703 = Constraint(expr= - m.b131 - m.b132 + m.b208 <= 0)

m.c3704 = Constraint(expr= - m.b131 - m.b133 + m.b209 <= 0)

m.c3705 = Constraint(expr= - m.b132 - m.b133 + m.b210 <= 0)

m.c3706 = Constraint(expr= - m.b134 - m.b135 + m.b146 <= 0)

m.c3707 = Constraint(expr= - m.b134 - m.b136 + m.b147 <= 0)

m.c3708 = Constraint(expr= - m.b134 - m.b137 + m.b148 <= 0)

m.c3709 = Constraint(expr= - m.b134 - m.b138 + m.b149 <= 0)

m.c3710 = Constraint(expr= - m.b134 - m.b139 + m.b150 <= 0)

m.c3711 = Constraint(expr= - m.b134 - m.b140 + m.b151 <= 0)

m.c3712 = Constraint(expr= - m.b134 - m.b141 + m.b152 <= 0)

m.c3713 = Constraint(expr= - m.b134 - m.b142 + m.b153 <= 0)

m.c3714 = Constraint(expr= - m.b134 - m.b143 + m.b154 <= 0)

m.c3715 = Constraint(expr= - m.b134 - m.b144 + m.b155 <= 0)

m.c3716 = Constraint(expr= - m.b134 - m.b145 + m.b156 <= 0)

m.c3717 = Constraint(expr= - m.b135 - m.b136 + m.b157 <= 0)

m.c3718 = Constraint(expr= - m.b135 - m.b137 + m.b158 <= 0)

m.c3719 = Constraint(expr= - m.b135 - m.b138 + m.b159 <= 0)

m.c3720 = Constraint(expr= - m.b135 - m.b139 + m.b160 <= 0)

m.c3721 = Constraint(expr= - m.b135 - m.b140 + m.b161 <= 0)

m.c3722 = Constraint(expr= - m.b135 - m.b141 + m.b162 <= 0)

m.c3723 = Constraint(expr= - m.b135 - m.b142 + m.b163 <= 0)

m.c3724 = Constraint(expr= - m.b135 - m.b143 + m.b164 <= 0)

m.c3725 = Constraint(expr= - m.b135 - m.b144 + m.b165 <= 0)

m.c3726 = Constraint(expr= - m.b135 - m.b145 + m.b211 <= 0)

m.c3727 = Constraint(expr= - m.b136 - m.b137 + m.b166 <= 0)

m.c3728 = Constraint(expr= - m.b136 - m.b138 + m.b167 <= 0)

m.c3729 = Constraint(expr= - m.b136 - m.b139 + m.b168 <= 0)

m.c3730 = Constraint(expr= - m.b136 - m.b140 + m.b169 <= 0)

m.c3731 = Constraint(expr= - m.b136 - m.b141 + m.b170 <= 0)

m.c3732 = Constraint(expr= - m.b136 - m.b142 + m.b171 <= 0)

m.c3733 = Constraint(expr= - m.b136 - m.b143 + m.b172 <= 0)

m.c3734 = Constraint(expr= - m.b136 - m.b144 + m.b173 <= 0)

m.c3735 = Constraint(expr= - m.b136 - m.b145 + m.b174 <= 0)

m.c3736 = Constraint(expr= - m.b137 - m.b138 + m.b175 <= 0)

m.c3737 = Constraint(expr= - m.b137 - m.b139 + m.b176 <= 0)

m.c3738 = Constraint(expr= - m.b137 - m.b140 + m.b177 <= 0)

m.c3739 = Constraint(expr= - m.b137 - m.b141 + m.b178 <= 0)

m.c3740 = Constraint(expr= - m.b137 - m.b142 + m.b179 <= 0)

m.c3741 = Constraint(expr= - m.b137 - m.b143 + m.b180 <= 0)

m.c3742 = Constraint(expr= - m.b137 - m.b144 + m.b181 <= 0)

m.c3743 = Constraint(expr= - m.b137 - m.b145 + m.b182 <= 0)

m.c3744 = Constraint(expr= - m.b138 - m.b139 + m.b183 <= 0)

m.c3745 = Constraint(expr= - m.b138 - m.b140 + m.b184 <= 0)

m.c3746 = Constraint(expr= - m.b138 - m.b141 + m.b185 <= 0)

m.c3747 = Constraint(expr= - m.b138 - m.b142 + m.b186 <= 0)

m.c3748 = Constraint(expr= - m.b138 - m.b143 + m.b187 <= 0)

m.c3749 = Constraint(expr= - m.b138 - m.b144 + m.b188 <= 0)

m.c3750 = Constraint(expr= - m.b138 - m.b145 + m.b189 <= 0)

m.c3751 = Constraint(expr= - m.b139 - m.b140 + m.b190 <= 0)

m.c3752 = Constraint(expr= - m.b139 - m.b141 + m.b191 <= 0)

m.c3753 = Constraint(expr= - m.b139 - m.b142 + m.b192 <= 0)

m.c3754 = Constraint(expr= - m.b139 - m.b143 + m.b193 <= 0)

m.c3755 = Constraint(expr= - m.b139 - m.b144 + m.b194 <= 0)

m.c3756 = Constraint(expr= - m.b139 - m.b145 + m.b195 <= 0)

m.c3757 = Constraint(expr= - m.b140 - m.b141 + m.b196 <= 0)

m.c3758 = Constraint(expr= - m.b140 - m.b142 + m.b197 <= 0)

m.c3759 = Constraint(expr= - m.b140 - m.b143 + m.b198 <= 0)

m.c3760 = Constraint(expr= - m.b140 - m.b144 + m.b199 <= 0)

m.c3761 = Constraint(expr= - m.b140 - m.b145 + m.b200 <= 0)

m.c3762 = Constraint(expr= - m.b141 - m.b142 + m.b201 <= 0)

m.c3763 = Constraint(expr= - m.b141 - m.b143 + m.b202 <= 0)

m.c3764 = Constraint(expr= - m.b141 - m.b144 + m.b203 <= 0)

m.c3765 = Constraint(expr= - m.b141 - m.b145 + m.b204 <= 0)

m.c3766 = Constraint(expr= - m.b142 - m.b143 + m.b205 <= 0)

m.c3767 = Constraint(expr= - m.b142 - m.b144 + m.b206 <= 0)

m.c3768 = Constraint(expr= - m.b142 - m.b145 + m.b207 <= 0)

m.c3769 = Constraint(expr= - m.b143 - m.b144 + m.b208 <= 0)

m.c3770 = Constraint(expr= - m.b143 - m.b145 + m.b209 <= 0)

m.c3771 = Constraint(expr= - m.b144 - m.b145 + m.b210 <= 0)

m.c3772 = Constraint(expr= - m.b146 - m.b147 + m.b157 <= 0)

m.c3773 = Constraint(expr= - m.b146 - m.b148 + m.b158 <= 0)

m.c3774 = Constraint(expr= - m.b146 - m.b149 + m.b159 <= 0)

m.c3775 = Constraint(expr= - m.b146 - m.b150 + m.b160 <= 0)

m.c3776 = Constraint(expr= - m.b146 - m.b151 + m.b161 <= 0)

m.c3777 = Constraint(expr= - m.b146 - m.b152 + m.b162 <= 0)

m.c3778 = Constraint(expr= - m.b146 - m.b153 + m.b163 <= 0)

m.c3779 = Constraint(expr= - m.b146 - m.b154 + m.b164 <= 0)

m.c3780 = Constraint(expr= - m.b146 - m.b155 + m.b165 <= 0)

m.c3781 = Constraint(expr= - m.b146 - m.b156 + m.b211 <= 0)

m.c3782 = Constraint(expr= - m.b147 - m.b148 + m.b166 <= 0)

m.c3783 = Constraint(expr= - m.b147 - m.b149 + m.b167 <= 0)

m.c3784 = Constraint(expr= - m.b147 - m.b150 + m.b168 <= 0)

m.c3785 = Constraint(expr= - m.b147 - m.b151 + m.b169 <= 0)

m.c3786 = Constraint(expr= - m.b147 - m.b152 + m.b170 <= 0)

m.c3787 = Constraint(expr= - m.b147 - m.b153 + m.b171 <= 0)

m.c3788 = Constraint(expr= - m.b147 - m.b154 + m.b172 <= 0)

m.c3789 = Constraint(expr= - m.b147 - m.b155 + m.b173 <= 0)

m.c3790 = Constraint(expr= - m.b147 - m.b156 + m.b174 <= 0)

m.c3791 = Constraint(expr= - m.b148 - m.b149 + m.b175 <= 0)

m.c3792 = Constraint(expr= - m.b148 - m.b150 + m.b176 <= 0)

m.c3793 = Constraint(expr= - m.b148 - m.b151 + m.b177 <= 0)

m.c3794 = Constraint(expr= - m.b148 - m.b152 + m.b178 <= 0)

m.c3795 = Constraint(expr= - m.b148 - m.b153 + m.b179 <= 0)

m.c3796 = Constraint(expr= - m.b148 - m.b154 + m.b180 <= 0)

m.c3797 = Constraint(expr= - m.b148 - m.b155 + m.b181 <= 0)

m.c3798 = Constraint(expr= - m.b148 - m.b156 + m.b182 <= 0)

m.c3799 = Constraint(expr= - m.b149 - m.b150 + m.b183 <= 0)

m.c3800 = Constraint(expr= - m.b149 - m.b151 + m.b184 <= 0)

m.c3801 = Constraint(expr= - m.b149 - m.b152 + m.b185 <= 0)

m.c3802 = Constraint(expr= - m.b149 - m.b153 + m.b186 <= 0)

m.c3803 = Constraint(expr= - m.b149 - m.b154 + m.b187 <= 0)

m.c3804 = Constraint(expr= - m.b149 - m.b155 + m.b188 <= 0)

m.c3805 = Constraint(expr= - m.b149 - m.b156 + m.b189 <= 0)

m.c3806 = Constraint(expr= - m.b150 - m.b151 + m.b190 <= 0)

m.c3807 = Constraint(expr= - m.b150 - m.b152 + m.b191 <= 0)

m.c3808 = Constraint(expr= - m.b150 - m.b153 + m.b192 <= 0)

m.c3809 = Constraint(expr= - m.b150 - m.b154 + m.b193 <= 0)

m.c3810 = Constraint(expr= - m.b150 - m.b155 + m.b194 <= 0)

m.c3811 = Constraint(expr= - m.b150 - m.b156 + m.b195 <= 0)

m.c3812 = Constraint(expr= - m.b151 - m.b152 + m.b196 <= 0)

m.c3813 = Constraint(expr= - m.b151 - m.b153 + m.b197 <= 0)

m.c3814 = Constraint(expr= - m.b151 - m.b154 + m.b198 <= 0)

m.c3815 = Constraint(expr= - m.b151 - m.b155 + m.b199 <= 0)

m.c3816 = Constraint(expr= - m.b151 - m.b156 + m.b200 <= 0)

m.c3817 = Constraint(expr= - m.b152 - m.b153 + m.b201 <= 0)

m.c3818 = Constraint(expr= - m.b152 - m.b154 + m.b202 <= 0)

m.c3819 = Constraint(expr= - m.b152 - m.b155 + m.b203 <= 0)

m.c3820 = Constraint(expr= - m.b152 - m.b156 + m.b204 <= 0)

m.c3821 = Constraint(expr= - m.b153 - m.b154 + m.b205 <= 0)

m.c3822 = Constraint(expr= - m.b153 - m.b155 + m.b206 <= 0)

m.c3823 = Constraint(expr= - m.b153 - m.b156 + m.b207 <= 0)

m.c3824 = Constraint(expr= - m.b154 - m.b155 + m.b208 <= 0)

m.c3825 = Constraint(expr= - m.b154 - m.b156 + m.b209 <= 0)

m.c3826 = Constraint(expr= - m.b155 - m.b156 + m.b210 <= 0)

m.c3827 = Constraint(expr= - m.b157 - m.b158 + m.b166 <= 0)

m.c3828 = Constraint(expr= - m.b157 - m.b159 + m.b167 <= 0)

m.c3829 = Constraint(expr= - m.b157 - m.b160 + m.b168 <= 0)

m.c3830 = Constraint(expr= - m.b157 - m.b161 + m.b169 <= 0)

m.c3831 = Constraint(expr= - m.b157 - m.b162 + m.b170 <= 0)

m.c3832 = Constraint(expr= - m.b157 - m.b163 + m.b171 <= 0)

m.c3833 = Constraint(expr= - m.b157 - m.b164 + m.b172 <= 0)

m.c3834 = Constraint(expr= - m.b157 - m.b165 + m.b173 <= 0)

m.c3835 = Constraint(expr= - m.b157 + m.b174 - m.b211 <= 0)

m.c3836 = Constraint(expr= - m.b158 - m.b159 + m.b175 <= 0)

m.c3837 = Constraint(expr= - m.b158 - m.b160 + m.b176 <= 0)

m.c3838 = Constraint(expr= - m.b158 - m.b161 + m.b177 <= 0)

m.c3839 = Constraint(expr= - m.b158 - m.b162 + m.b178 <= 0)

m.c3840 = Constraint(expr= - m.b158 - m.b163 + m.b179 <= 0)

m.c3841 = Constraint(expr= - m.b158 - m.b164 + m.b180 <= 0)

m.c3842 = Constraint(expr= - m.b158 - m.b165 + m.b181 <= 0)

m.c3843 = Constraint(expr= - m.b158 + m.b182 - m.b211 <= 0)

m.c3844 = Constraint(expr= - m.b159 - m.b160 + m.b183 <= 0)

m.c3845 = Constraint(expr= - m.b159 - m.b161 + m.b184 <= 0)

m.c3846 = Constraint(expr= - m.b159 - m.b162 + m.b185 <= 0)

m.c3847 = Constraint(expr= - m.b159 - m.b163 + m.b186 <= 0)

m.c3848 = Constraint(expr= - m.b159 - m.b164 + m.b187 <= 0)

m.c3849 = Constraint(expr= - m.b159 - m.b165 + m.b188 <= 0)

m.c3850 = Constraint(expr= - m.b159 + m.b189 - m.b211 <= 0)

m.c3851 = Constraint(expr= - m.b160 - m.b161 + m.b190 <= 0)

m.c3852 = Constraint(expr= - m.b160 - m.b162 + m.b191 <= 0)

m.c3853 = Constraint(expr= - m.b160 - m.b163 + m.b192 <= 0)

m.c3854 = Constraint(expr= - m.b160 - m.b164 + m.b193 <= 0)

m.c3855 = Constraint(expr= - m.b160 - m.b165 + m.b194 <= 0)

m.c3856 = Constraint(expr= - m.b160 + m.b195 - m.b211 <= 0)

m.c3857 = Constraint(expr= - m.b161 - m.b162 + m.b196 <= 0)

m.c3858 = Constraint(expr= - m.b161 - m.b163 + m.b197 <= 0)

m.c3859 = Constraint(expr= - m.b161 - m.b164 + m.b198 <= 0)

m.c3860 = Constraint(expr= - m.b161 - m.b165 + m.b199 <= 0)

m.c3861 = Constraint(expr= - m.b161 + m.b200 - m.b211 <= 0)

m.c3862 = Constraint(expr= - m.b162 - m.b163 + m.b201 <= 0)

m.c3863 = Constraint(expr= - m.b162 - m.b164 + m.b202 <= 0)

m.c3864 = Constraint(expr= - m.b162 - m.b165 + m.b203 <= 0)

m.c3865 = Constraint(expr= - m.b162 + m.b204 - m.b211 <= 0)

m.c3866 = Constraint(expr= - m.b163 - m.b164 + m.b205 <= 0)

m.c3867 = Constraint(expr= - m.b163 - m.b165 + m.b206 <= 0)

m.c3868 = Constraint(expr= - m.b163 + m.b207 - m.b211 <= 0)

m.c3869 = Constraint(expr= - m.b164 - m.b165 + m.b208 <= 0)

m.c3870 = Constraint(expr= - m.b164 + m.b209 - m.b211 <= 0)

m.c3871 = Constraint(expr= - m.b165 + m.b210 - m.b211 <= 0)

m.c3872 = Constraint(expr= - m.b166 - m.b167 + m.b175 <= 0)

m.c3873 = Constraint(expr= - m.b166 - m.b168 + m.b176 <= 0)

m.c3874 = Constraint(expr= - m.b166 - m.b169 + m.b177 <= 0)

m.c3875 = Constraint(expr= - m.b166 - m.b170 + m.b178 <= 0)

m.c3876 = Constraint(expr= - m.b166 - m.b171 + m.b179 <= 0)

m.c3877 = Constraint(expr= - m.b166 - m.b172 + m.b180 <= 0)

m.c3878 = Constraint(expr= - m.b166 - m.b173 + m.b181 <= 0)

m.c3879 = Constraint(expr= - m.b166 - m.b174 + m.b182 <= 0)

m.c3880 = Constraint(expr= - m.b167 - m.b168 + m.b183 <= 0)

m.c3881 = Constraint(expr= - m.b167 - m.b169 + m.b184 <= 0)

m.c3882 = Constraint(expr= - m.b167 - m.b170 + m.b185 <= 0)

m.c3883 = Constraint(expr= - m.b167 - m.b171 + m.b186 <= 0)

m.c3884 = Constraint(expr= - m.b167 - m.b172 + m.b187 <= 0)

m.c3885 = Constraint(expr= - m.b167 - m.b173 + m.b188 <= 0)

m.c3886 = Constraint(expr= - m.b167 - m.b174 + m.b189 <= 0)

m.c3887 = Constraint(expr= - m.b168 - m.b169 + m.b190 <= 0)

m.c3888 = Constraint(expr= - m.b168 - m.b170 + m.b191 <= 0)

m.c3889 = Constraint(expr= - m.b168 - m.b171 + m.b192 <= 0)

m.c3890 = Constraint(expr= - m.b168 - m.b172 + m.b193 <= 0)

m.c3891 = Constraint(expr= - m.b168 - m.b173 + m.b194 <= 0)

m.c3892 = Constraint(expr= - m.b168 - m.b174 + m.b195 <= 0)

m.c3893 = Constraint(expr= - m.b169 - m.b170 + m.b196 <= 0)

m.c3894 = Constraint(expr= - m.b169 - m.b171 + m.b197 <= 0)

m.c3895 = Constraint(expr= - m.b169 - m.b172 + m.b198 <= 0)

m.c3896 = Constraint(expr= - m.b169 - m.b173 + m.b199 <= 0)

m.c3897 = Constraint(expr= - m.b169 - m.b174 + m.b200 <= 0)

m.c3898 = Constraint(expr= - m.b170 - m.b171 + m.b201 <= 0)

m.c3899 = Constraint(expr= - m.b170 - m.b172 + m.b202 <= 0)

m.c3900 = Constraint(expr= - m.b170 - m.b173 + m.b203 <= 0)

m.c3901 = Constraint(expr= - m.b170 - m.b174 + m.b204 <= 0)

m.c3902 = Constraint(expr= - m.b171 - m.b172 + m.b205 <= 0)

m.c3903 = Constraint(expr= - m.b171 - m.b173 + m.b206 <= 0)

m.c3904 = Constraint(expr= - m.b171 - m.b174 + m.b207 <= 0)

m.c3905 = Constraint(expr= - m.b172 - m.b173 + m.b208 <= 0)

m.c3906 = Constraint(expr= - m.b172 - m.b174 + m.b209 <= 0)

m.c3907 = Constraint(expr= - m.b173 - m.b174 + m.b210 <= 0)

m.c3908 = Constraint(expr= - m.b175 - m.b176 + m.b183 <= 0)

m.c3909 = Constraint(expr= - m.b175 - m.b177 + m.b184 <= 0)

m.c3910 = Constraint(expr= - m.b175 - m.b178 + m.b185 <= 0)

m.c3911 = Constraint(expr= - m.b175 - m.b179 + m.b186 <= 0)

m.c3912 = Constraint(expr= - m.b175 - m.b180 + m.b187 <= 0)

m.c3913 = Constraint(expr= - m.b175 - m.b181 + m.b188 <= 0)

m.c3914 = Constraint(expr= - m.b175 - m.b182 + m.b189 <= 0)

m.c3915 = Constraint(expr= - m.b176 - m.b177 + m.b190 <= 0)

m.c3916 = Constraint(expr= - m.b176 - m.b178 + m.b191 <= 0)

m.c3917 = Constraint(expr= - m.b176 - m.b179 + m.b192 <= 0)

m.c3918 = Constraint(expr= - m.b176 - m.b180 + m.b193 <= 0)

m.c3919 = Constraint(expr= - m.b176 - m.b181 + m.b194 <= 0)

m.c3920 = Constraint(expr= - m.b176 - m.b182 + m.b195 <= 0)

m.c3921 = Constraint(expr= - m.b177 - m.b178 + m.b196 <= 0)

m.c3922 = Constraint(expr= - m.b177 - m.b179 + m.b197 <= 0)

m.c3923 = Constraint(expr= - m.b177 - m.b180 + m.b198 <= 0)

m.c3924 = Constraint(expr= - m.b177 - m.b181 + m.b199 <= 0)

m.c3925 = Constraint(expr= - m.b177 - m.b182 + m.b200 <= 0)

m.c3926 = Constraint(expr= - m.b178 - m.b179 + m.b201 <= 0)

m.c3927 = Constraint(expr= - m.b178 - m.b180 + m.b202 <= 0)

m.c3928 = Constraint(expr= - m.b178 - m.b181 + m.b203 <= 0)

m.c3929 = Constraint(expr= - m.b178 - m.b182 + m.b204 <= 0)

m.c3930 = Constraint(expr= - m.b179 - m.b180 + m.b205 <= 0)

m.c3931 = Constraint(expr= - m.b179 - m.b181 + m.b206 <= 0)

m.c3932 = Constraint(expr= - m.b179 - m.b182 + m.b207 <= 0)

m.c3933 = Constraint(expr= - m.b180 - m.b181 + m.b208 <= 0)

m.c3934 = Constraint(expr= - m.b180 - m.b182 + m.b209 <= 0)

m.c3935 = Constraint(expr= - m.b181 - m.b182 + m.b210 <= 0)

m.c3936 = Constraint(expr= - m.b183 - m.b184 + m.b190 <= 0)

m.c3937 = Constraint(expr= - m.b183 - m.b185 + m.b191 <= 0)

m.c3938 = Constraint(expr= - m.b183 - m.b186 + m.b192 <= 0)

m.c3939 = Constraint(expr= - m.b183 - m.b187 + m.b193 <= 0)

m.c3940 = Constraint(expr= - m.b183 - m.b188 + m.b194 <= 0)

m.c3941 = Constraint(expr= - m.b183 - m.b189 + m.b195 <= 0)

m.c3942 = Constraint(expr= - m.b184 - m.b185 + m.b196 <= 0)

m.c3943 = Constraint(expr= - m.b184 - m.b186 + m.b197 <= 0)

m.c3944 = Constraint(expr= - m.b184 - m.b187 + m.b198 <= 0)

m.c3945 = Constraint(expr= - m.b184 - m.b188 + m.b199 <= 0)

m.c3946 = Constraint(expr= - m.b184 - m.b189 + m.b200 <= 0)

m.c3947 = Constraint(expr= - m.b185 - m.b186 + m.b201 <= 0)

m.c3948 = Constraint(expr= - m.b185 - m.b187 + m.b202 <= 0)

m.c3949 = Constraint(expr= - m.b185 - m.b188 + m.b203 <= 0)

m.c3950 = Constraint(expr= - m.b185 - m.b189 + m.b204 <= 0)

m.c3951 = Constraint(expr= - m.b186 - m.b187 + m.b205 <= 0)

m.c3952 = Constraint(expr= - m.b186 - m.b188 + m.b206 <= 0)

m.c3953 = Constraint(expr= - m.b186 - m.b189 + m.b207 <= 0)

m.c3954 = Constraint(expr= - m.b187 - m.b188 + m.b208 <= 0)

m.c3955 = Constraint(expr= - m.b187 - m.b189 + m.b209 <= 0)

m.c3956 = Constraint(expr= - m.b188 - m.b189 + m.b210 <= 0)

m.c3957 = Constraint(expr= - m.b190 - m.b191 + m.b196 <= 0)

m.c3958 = Constraint(expr= - m.b190 - m.b192 + m.b197 <= 0)

m.c3959 = Constraint(expr= - m.b190 - m.b193 + m.b198 <= 0)

m.c3960 = Constraint(expr= - m.b190 - m.b194 + m.b199 <= 0)

m.c3961 = Constraint(expr= - m.b190 - m.b195 + m.b200 <= 0)

m.c3962 = Constraint(expr= - m.b191 - m.b192 + m.b201 <= 0)

m.c3963 = Constraint(expr= - m.b191 - m.b193 + m.b202 <= 0)

m.c3964 = Constraint(expr= - m.b191 - m.b194 + m.b203 <= 0)

m.c3965 = Constraint(expr= - m.b191 - m.b195 + m.b204 <= 0)

m.c3966 = Constraint(expr= - m.b192 - m.b193 + m.b205 <= 0)

m.c3967 = Constraint(expr= - m.b192 - m.b194 + m.b206 <= 0)

m.c3968 = Constraint(expr= - m.b192 - m.b195 + m.b207 <= 0)

m.c3969 = Constraint(expr= - m.b193 - m.b194 + m.b208 <= 0)

m.c3970 = Constraint(expr= - m.b193 - m.b195 + m.b209 <= 0)

m.c3971 = Constraint(expr= - m.b194 - m.b195 + m.b210 <= 0)

m.c3972 = Constraint(expr= - m.b196 - m.b197 + m.b201 <= 0)

m.c3973 = Constraint(expr= - m.b196 - m.b198 + m.b202 <= 0)

m.c3974 = Constraint(expr= - m.b196 - m.b199 + m.b203 <= 0)

m.c3975 = Constraint(expr= - m.b196 - m.b200 + m.b204 <= 0)

m.c3976 = Constraint(expr= - m.b197 - m.b198 + m.b205 <= 0)

m.c3977 = Constraint(expr= - m.b197 - m.b199 + m.b206 <= 0)

m.c3978 = Constraint(expr= - m.b197 - m.b200 + m.b207 <= 0)

m.c3979 = Constraint(expr= - m.b198 - m.b199 + m.b208 <= 0)

m.c3980 = Constraint(expr= - m.b198 - m.b200 + m.b209 <= 0)

m.c3981 = Constraint(expr= - m.b199 - m.b200 + m.b210 <= 0)

m.c3982 = Constraint(expr= - m.b201 - m.b202 + m.b205 <= 0)

m.c3983 = Constraint(expr= - m.b201 - m.b203 + m.b206 <= 0)

m.c3984 = Constraint(expr= - m.b201 - m.b204 + m.b207 <= 0)

m.c3985 = Constraint(expr= - m.b202 - m.b203 + m.b208 <= 0)

m.c3986 = Constraint(expr= - m.b202 - m.b204 + m.b209 <= 0)

m.c3987 = Constraint(expr= - m.b203 - m.b204 + m.b210 <= 0)

m.c3988 = Constraint(expr= - m.b205 - m.b206 + m.b208 <= 0)

m.c3989 = Constraint(expr= - m.b205 - m.b207 + m.b209 <= 0)

m.c3990 = Constraint(expr= - m.b206 - m.b207 + m.b210 <= 0)

m.c3991 = Constraint(expr= - m.b208 - m.b209 + m.b210 <= 0)

m.c3992 = Constraint(expr=970*m.b3*m.b2 + 680*m.b4*m.b2 + 410*m.b5*m.b2 + 630*m.b6*m.b2 + 670*m.b7*m.b2 + 310*m.b8*m.b2
                           + 210*m.b9*m.b2 + 710*m.b10*m.b2 + 880*m.b11*m.b2 + 530*m.b12*m.b2 + 500*m.b13*m.b2 + 630*
                          m.b14*m.b2 + 920*m.b15*m.b2 + 290*m.b16*m.b2 + 180*m.b17*m.b2 + 860*m.b18*m.b2 + 570*m.b19*
                          m.b2 + 730*m.b20*m.b2 + 180*m.b21*m.b2 + 150*m.b4*m.b3 + 590*m.b5*m.b3 + 390*m.b6*m.b3 + 30*
                          m.b7*m.b3 + 190*m.b8*m.b3 + 80*m.b9*m.b3 + 880*m.b10*m.b3 + 430*m.b11*m.b3 + 570*m.b12*m.b3 + 
                          230*m.b13*m.b3 + 940*m.b14*m.b3 + 210*m.b15*m.b3 + 720*m.b16*m.b3 + 140*m.b17*m.b3 + 140*m.b18
                          *m.b3 + 870*m.b19*m.b3 + 330*m.b20*m.b3 + 460*m.b21*m.b3 + 80*m.b5*m.b4 + 40*m.b6*m.b4 + 340*
                          m.b7*m.b4 + 620*m.b8*m.b4 + 550*m.b9*m.b4 + 490*m.b10*m.b4 + 60*m.b11*m.b4 + 360*m.b12*m.b4 + 
                          670*m.b13*m.b4 + 450*m.b14*m.b4 + 930*m.b15*m.b4 + 930*m.b16*m.b4 + 630*m.b17*m.b4 + 80*m.b18*
                          m.b4 + 520*m.b19*m.b4 + 540*m.b20*m.b4 + 640*m.b21*m.b4 + 240*m.b6*m.b5 + 140*m.b7*m.b5 + 40*
                          m.b8*m.b5 + 190*m.b9*m.b5 + 710*m.b10*m.b5 + 280*m.b11*m.b5 + 130*m.b12*m.b5 + 450*m.b13*m.b5
                           + 520*m.b14*m.b5 + 790*m.b15*m.b5 + 110*m.b16*m.b5 + 400*m.b17*m.b5 + 120*m.b18*m.b5 + 570*
                          m.b19*m.b5 + 480*m.b20*m.b5 + 170*m.b21*m.b5 + 430*m.b7*m.b6 + 620*m.b8*m.b6 + 240*m.b9*m.b6
                           + 450*m.b10*m.b6 + 210*m.b11*m.b6 + 600*m.b12*m.b6 + 120*m.b13*m.b6 + 660*m.b14*m.b6 + 530*
                          m.b15*m.b6 + 50*m.b16*m.b6 + 810*m.b17*m.b6 + 610*m.b18*m.b6 + 100*m.b19*m.b6 + 880*m.b20*m.b6
                           + 770*m.b21*m.b6 + 340*m.b8*m.b7 + 20*m.b9*m.b7 + 820*m.b10*m.b7 + 530*m.b11*m.b7 + 260*m.b12
                          *m.b7 + 620*m.b13*m.b7 + 180*m.b14*m.b7 + 710*m.b15*m.b7 + 140*m.b16*m.b7 + 970*m.b17*m.b7 + 
                          820*m.b18*m.b7 + 540*m.b19*m.b7 + 90*m.b20*m.b7 + 920*m.b21*m.b7 + 550*m.b9*m.b8 + 780*m.b10*
                          m.b8 + 870*m.b11*m.b8 + 690*m.b12*m.b8 + 20*m.b13*m.b8 + 320*m.b14*m.b8 + 420*m.b15*m.b8 + 140
                          *m.b16*m.b8 + 450*m.b17*m.b8 + 600*m.b18*m.b8 + 670*m.b19*m.b8 + 20*m.b20*m.b8 + 420*m.b21*
                          m.b8 + 810*m.b10*m.b9 + 640*m.b11*m.b9 + 820*m.b12*m.b9 + 580*m.b13*m.b9 + 980*m.b14*m.b9 + 
                          360*m.b15*m.b9 + 920*m.b16*m.b9 + 30*m.b17*m.b9 + 620*m.b18*m.b9 + 540*m.b19*m.b9 + 210*m.b20*
                          m.b9 + 850*m.b21*m.b9 + 690*m.b11*m.b10 + 700*m.b12*m.b10 + 200*m.b13*m.b10 + 750*m.b14*m.b10
                           + 800*m.b15*m.b10 + 120*m.b16*m.b10 + 820*m.b17*m.b10 + 100*m.b18*m.b10 + 990*m.b19*m.b10 + 
                          40*m.b20*m.b10 + 130*m.b21*m.b10 + 840*m.b12*m.b11 + 980*m.b13*m.b11 + 270*m.b14*m.b11 + 810*
                          m.b15*m.b11 + 590*m.b16*m.b11 + 470*m.b17*m.b11 + 830*m.b18*m.b11 + 530*m.b19*m.b11 + 800*
                          m.b20*m.b11 + 350*m.b13*m.b12 + 900*m.b14*m.b12 + 980*m.b15*m.b12 + 710*m.b16*m.b12 + 830*
                          m.b17*m.b12 + 540*m.b18*m.b12 + 860*m.b19*m.b12 + 890*m.b20*m.b12 + 270*m.b21*m.b12 + 710*
                          m.b14*m.b13 + 100*m.b15*m.b13 + 980*m.b16*m.b13 + 910*m.b17*m.b13 + 860*m.b18*m.b13 + 300*
                          m.b19*m.b13 + 550*m.b20*m.b13 + 200*m.b21*m.b13 + 400*m.b15*m.b14 + 70*m.b16*m.b14 + 760*m.b17
                          *m.b14 + 530*m.b18*m.b14 + 910*m.b19*m.b14 + 750*m.b20*m.b14 + 330*m.b21*m.b14 + 720*m.b16*
                          m.b15 + 340*m.b17*m.b15 + 320*m.b18*m.b15 + 70*m.b19*m.b15 + 870*m.b20*m.b15 + 640*m.b21*m.b15
                           + 70*m.b17*m.b16 + 740*m.b18*m.b16 + 540*m.b19*m.b16 + 580*m.b20*m.b16 + 970*m.b21*m.b16 + 
                          890*m.b18*m.b17 + 120*m.b19*m.b17 + 830*m.b20*m.b17 + 790*m.b21*m.b17 + 390*m.b19*m.b18 + 70*
                          m.b20*m.b18 + 890*m.b21*m.b18 + 890*m.b20*m.b19 + 980*m.b21*m.b19 + 270*m.b21*m.b20 >= 67751)

m.c3993 = Constraint(expr=390*m.b22*m.b2 + 260*m.b23*m.b2 + 20*m.b24*m.b2 + 940*m.b25*m.b2 + 760*m.b26*m.b2 + 550*m.b27*
                          m.b2 + 800*m.b28*m.b2 + 580*m.b29*m.b2 + 340*m.b30*m.b2 + 200*m.b31*m.b2 + 880*m.b32*m.b2 + 
                          600*m.b33*m.b2 + 170*m.b34*m.b2 + 850*m.b35*m.b2 + 710*m.b36*m.b2 + 970*m.b37*m.b2 + 830*m.b38
                          *m.b2 + 990*m.b39*m.b2 + 640*m.b40*m.b2 + 150*m.b23*m.b22 + 590*m.b24*m.b22 + 390*m.b25*m.b22
                           + 30*m.b26*m.b22 + 190*m.b27*m.b22 + 80*m.b28*m.b22 + 880*m.b29*m.b22 + 430*m.b30*m.b22 + 570
                          *m.b31*m.b22 + 230*m.b32*m.b22 + 940*m.b33*m.b22 + 210*m.b34*m.b22 + 720*m.b35*m.b22 + 140*
                          m.b36*m.b22 + 140*m.b37*m.b22 + 870*m.b38*m.b22 + 330*m.b39*m.b22 + 460*m.b40*m.b22 + 80*m.b24
                          *m.b23 + 40*m.b25*m.b23 + 340*m.b26*m.b23 + 620*m.b27*m.b23 + 550*m.b28*m.b23 + 490*m.b29*
                          m.b23 + 60*m.b30*m.b23 + 360*m.b31*m.b23 + 670*m.b32*m.b23 + 450*m.b33*m.b23 + 930*m.b34*m.b23
                           + 930*m.b35*m.b23 + 630*m.b36*m.b23 + 80*m.b37*m.b23 + 520*m.b38*m.b23 + 540*m.b39*m.b23 + 
                          640*m.b40*m.b23 + 240*m.b25*m.b24 + 140*m.b26*m.b24 + 40*m.b27*m.b24 + 190*m.b28*m.b24 + 710*
                          m.b29*m.b24 + 280*m.b30*m.b24 + 130*m.b31*m.b24 + 450*m.b32*m.b24 + 520*m.b33*m.b24 + 790*
                          m.b34*m.b24 + 110*m.b35*m.b24 + 400*m.b36*m.b24 + 120*m.b37*m.b24 + 570*m.b38*m.b24 + 480*
                          m.b39*m.b24 + 170*m.b40*m.b24 + 430*m.b26*m.b25 + 620*m.b27*m.b25 + 240*m.b28*m.b25 + 450*
                          m.b29*m.b25 + 210*m.b30*m.b25 + 600*m.b31*m.b25 + 120*m.b32*m.b25 + 660*m.b33*m.b25 + 530*
                          m.b34*m.b25 + 50*m.b35*m.b25 + 810*m.b36*m.b25 + 610*m.b37*m.b25 + 100*m.b38*m.b25 + 880*m.b39
                          *m.b25 + 770*m.b40*m.b25 + 340*m.b27*m.b26 + 20*m.b28*m.b26 + 820*m.b29*m.b26 + 530*m.b30*
                          m.b26 + 260*m.b31*m.b26 + 620*m.b32*m.b26 + 180*m.b33*m.b26 + 710*m.b34*m.b26 + 140*m.b35*
                          m.b26 + 970*m.b36*m.b26 + 820*m.b37*m.b26 + 540*m.b38*m.b26 + 90*m.b39*m.b26 + 920*m.b40*m.b26
                           + 550*m.b28*m.b27 + 780*m.b29*m.b27 + 870*m.b30*m.b27 + 690*m.b31*m.b27 + 20*m.b32*m.b27 + 
                          320*m.b33*m.b27 + 420*m.b34*m.b27 + 140*m.b35*m.b27 + 450*m.b36*m.b27 + 600*m.b37*m.b27 + 670*
                          m.b38*m.b27 + 20*m.b39*m.b27 + 420*m.b40*m.b27 + 810*m.b29*m.b28 + 640*m.b30*m.b28 + 820*m.b31
                          *m.b28 + 580*m.b32*m.b28 + 980*m.b33*m.b28 + 360*m.b34*m.b28 + 920*m.b35*m.b28 + 30*m.b36*
                          m.b28 + 620*m.b37*m.b28 + 540*m.b38*m.b28 + 210*m.b39*m.b28 + 850*m.b40*m.b28 + 690*m.b30*
                          m.b29 + 700*m.b31*m.b29 + 200*m.b32*m.b29 + 750*m.b33*m.b29 + 800*m.b34*m.b29 + 120*m.b35*
                          m.b29 + 820*m.b36*m.b29 + 100*m.b37*m.b29 + 990*m.b38*m.b29 + 40*m.b39*m.b29 + 130*m.b40*m.b29
                           + 840*m.b31*m.b30 + 980*m.b32*m.b30 + 270*m.b33*m.b30 + 810*m.b34*m.b30 + 590*m.b35*m.b30 + 
                          470*m.b36*m.b30 + 830*m.b37*m.b30 + 530*m.b38*m.b30 + 800*m.b39*m.b30 + 350*m.b32*m.b31 + 900*
                          m.b33*m.b31 + 980*m.b34*m.b31 + 710*m.b35*m.b31 + 830*m.b36*m.b31 + 540*m.b37*m.b31 + 860*
                          m.b38*m.b31 + 890*m.b39*m.b31 + 270*m.b40*m.b31 + 710*m.b33*m.b32 + 100*m.b34*m.b32 + 980*
                          m.b35*m.b32 + 910*m.b36*m.b32 + 860*m.b37*m.b32 + 300*m.b38*m.b32 + 550*m.b39*m.b32 + 200*
                          m.b40*m.b32 + 400*m.b34*m.b33 + 70*m.b35*m.b33 + 760*m.b36*m.b33 + 530*m.b37*m.b33 + 910*m.b38
                          *m.b33 + 750*m.b39*m.b33 + 330*m.b40*m.b33 + 720*m.b35*m.b34 + 340*m.b36*m.b34 + 320*m.b37*
                          m.b34 + 70*m.b38*m.b34 + 870*m.b39*m.b34 + 640*m.b40*m.b34 + 70*m.b36*m.b35 + 740*m.b37*m.b35
                           + 540*m.b38*m.b35 + 580*m.b39*m.b35 + 970*m.b40*m.b35 + 890*m.b37*m.b36 + 120*m.b38*m.b36 + 
                          830*m.b39*m.b36 + 790*m.b40*m.b36 + 390*m.b38*m.b37 + 70*m.b39*m.b37 + 890*m.b40*m.b37 + 890*
                          m.b39*m.b38 + 980*m.b40*m.b38 + 270*m.b40*m.b39 >= 67751)

m.c3994 = Constraint(expr=750*m.b22*m.b3 + 260*m.b41*m.b3 + 20*m.b42*m.b3 + 940*m.b43*m.b3 + 760*m.b44*m.b3 + 550*m.b45*
                          m.b3 + 800*m.b46*m.b3 + 580*m.b47*m.b3 + 340*m.b48*m.b3 + 200*m.b49*m.b3 + 880*m.b50*m.b3 + 
                          600*m.b51*m.b3 + 170*m.b52*m.b3 + 850*m.b53*m.b3 + 710*m.b54*m.b3 + 970*m.b55*m.b3 + 830*m.b56
                          *m.b3 + 990*m.b57*m.b3 + 640*m.b58*m.b3 + 680*m.b41*m.b22 + 410*m.b42*m.b22 + 630*m.b43*m.b22
                           + 670*m.b44*m.b22 + 310*m.b45*m.b22 + 210*m.b46*m.b22 + 710*m.b47*m.b22 + 880*m.b48*m.b22 + 
                          530*m.b49*m.b22 + 500*m.b50*m.b22 + 630*m.b51*m.b22 + 920*m.b52*m.b22 + 290*m.b53*m.b22 + 180*
                          m.b54*m.b22 + 860*m.b55*m.b22 + 570*m.b56*m.b22 + 730*m.b57*m.b22 + 180*m.b58*m.b22 + 80*m.b42
                          *m.b41 + 40*m.b43*m.b41 + 340*m.b44*m.b41 + 620*m.b45*m.b41 + 550*m.b46*m.b41 + 490*m.b47*
                          m.b41 + 60*m.b48*m.b41 + 360*m.b49*m.b41 + 670*m.b50*m.b41 + 450*m.b51*m.b41 + 930*m.b52*m.b41
                           + 930*m.b53*m.b41 + 630*m.b54*m.b41 + 80*m.b55*m.b41 + 520*m.b56*m.b41 + 540*m.b57*m.b41 + 
                          640*m.b58*m.b41 + 240*m.b43*m.b42 + 140*m.b44*m.b42 + 40*m.b45*m.b42 + 190*m.b46*m.b42 + 710*
                          m.b47*m.b42 + 280*m.b48*m.b42 + 130*m.b49*m.b42 + 450*m.b50*m.b42 + 520*m.b51*m.b42 + 790*
                          m.b52*m.b42 + 110*m.b53*m.b42 + 400*m.b54*m.b42 + 120*m.b55*m.b42 + 570*m.b56*m.b42 + 480*
                          m.b57*m.b42 + 170*m.b58*m.b42 + 430*m.b44*m.b43 + 620*m.b45*m.b43 + 240*m.b46*m.b43 + 450*
                          m.b47*m.b43 + 210*m.b48*m.b43 + 600*m.b49*m.b43 + 120*m.b50*m.b43 + 660*m.b51*m.b43 + 530*
                          m.b52*m.b43 + 50*m.b53*m.b43 + 810*m.b54*m.b43 + 610*m.b55*m.b43 + 100*m.b56*m.b43 + 880*m.b57
                          *m.b43 + 770*m.b58*m.b43 + 340*m.b45*m.b44 + 20*m.b46*m.b44 + 820*m.b47*m.b44 + 530*m.b48*
                          m.b44 + 260*m.b49*m.b44 + 620*m.b50*m.b44 + 180*m.b51*m.b44 + 710*m.b52*m.b44 + 140*m.b53*
                          m.b44 + 970*m.b54*m.b44 + 820*m.b55*m.b44 + 540*m.b56*m.b44 + 90*m.b57*m.b44 + 920*m.b58*m.b44
                           + 550*m.b46*m.b45 + 780*m.b47*m.b45 + 870*m.b48*m.b45 + 690*m.b49*m.b45 + 20*m.b50*m.b45 + 
                          320*m.b51*m.b45 + 420*m.b52*m.b45 + 140*m.b53*m.b45 + 450*m.b54*m.b45 + 600*m.b55*m.b45 + 670*
                          m.b56*m.b45 + 20*m.b57*m.b45 + 420*m.b58*m.b45 + 810*m.b47*m.b46 + 640*m.b48*m.b46 + 820*m.b49
                          *m.b46 + 580*m.b50*m.b46 + 980*m.b51*m.b46 + 360*m.b52*m.b46 + 920*m.b53*m.b46 + 30*m.b54*
                          m.b46 + 620*m.b55*m.b46 + 540*m.b56*m.b46 + 210*m.b57*m.b46 + 850*m.b58*m.b46 + 690*m.b48*
                          m.b47 + 700*m.b49*m.b47 + 200*m.b50*m.b47 + 750*m.b51*m.b47 + 800*m.b52*m.b47 + 120*m.b53*
                          m.b47 + 820*m.b54*m.b47 + 100*m.b55*m.b47 + 990*m.b56*m.b47 + 40*m.b57*m.b47 + 130*m.b58*m.b47
                           + 840*m.b49*m.b48 + 980*m.b50*m.b48 + 270*m.b51*m.b48 + 810*m.b52*m.b48 + 590*m.b53*m.b48 + 
                          470*m.b54*m.b48 + 830*m.b55*m.b48 + 530*m.b56*m.b48 + 800*m.b57*m.b48 + 350*m.b50*m.b49 + 900*
                          m.b51*m.b49 + 980*m.b52*m.b49 + 710*m.b53*m.b49 + 830*m.b54*m.b49 + 540*m.b55*m.b49 + 860*
                          m.b56*m.b49 + 890*m.b57*m.b49 + 270*m.b58*m.b49 + 710*m.b51*m.b50 + 100*m.b52*m.b50 + 980*
                          m.b53*m.b50 + 910*m.b54*m.b50 + 860*m.b55*m.b50 + 300*m.b56*m.b50 + 550*m.b57*m.b50 + 200*
                          m.b58*m.b50 + 400*m.b52*m.b51 + 70*m.b53*m.b51 + 760*m.b54*m.b51 + 530*m.b55*m.b51 + 910*m.b56
                          *m.b51 + 750*m.b57*m.b51 + 330*m.b58*m.b51 + 720*m.b53*m.b52 + 340*m.b54*m.b52 + 320*m.b55*
                          m.b52 + 70*m.b56*m.b52 + 870*m.b57*m.b52 + 640*m.b58*m.b52 + 70*m.b54*m.b53 + 740*m.b55*m.b53
                           + 540*m.b56*m.b53 + 580*m.b57*m.b53 + 970*m.b58*m.b53 + 890*m.b55*m.b54 + 120*m.b56*m.b54 + 
                          830*m.b57*m.b54 + 790*m.b58*m.b54 + 390*m.b56*m.b55 + 70*m.b57*m.b55 + 890*m.b58*m.b55 + 890*
                          m.b57*m.b56 + 980*m.b58*m.b56 + 270*m.b58*m.b57 >= 67751)

m.c3995 = Constraint(expr=750*m.b23*m.b4 + 390*m.b41*m.b4 + 20*m.b59*m.b4 + 940*m.b60*m.b4 + 760*m.b61*m.b4 + 550*m.b62*
                          m.b4 + 800*m.b63*m.b4 + 580*m.b64*m.b4 + 340*m.b65*m.b4 + 200*m.b66*m.b4 + 880*m.b67*m.b4 + 
                          600*m.b68*m.b4 + 170*m.b69*m.b4 + 850*m.b70*m.b4 + 710*m.b71*m.b4 + 970*m.b72*m.b4 + 830*m.b73
                          *m.b4 + 990*m.b74*m.b4 + 640*m.b75*m.b4 + 970*m.b41*m.b23 + 410*m.b59*m.b23 + 630*m.b60*m.b23
                           + 670*m.b61*m.b23 + 310*m.b62*m.b23 + 210*m.b63*m.b23 + 710*m.b64*m.b23 + 880*m.b65*m.b23 + 
                          530*m.b66*m.b23 + 500*m.b67*m.b23 + 630*m.b68*m.b23 + 920*m.b69*m.b23 + 290*m.b70*m.b23 + 180*
                          m.b71*m.b23 + 860*m.b72*m.b23 + 570*m.b73*m.b23 + 730*m.b74*m.b23 + 180*m.b75*m.b23 + 590*
                          m.b59*m.b41 + 390*m.b60*m.b41 + 30*m.b61*m.b41 + 190*m.b62*m.b41 + 80*m.b63*m.b41 + 880*m.b64*
                          m.b41 + 430*m.b65*m.b41 + 570*m.b66*m.b41 + 230*m.b67*m.b41 + 940*m.b68*m.b41 + 210*m.b69*
                          m.b41 + 720*m.b70*m.b41 + 140*m.b71*m.b41 + 140*m.b72*m.b41 + 870*m.b73*m.b41 + 330*m.b74*
                          m.b41 + 460*m.b75*m.b41 + 240*m.b60*m.b59 + 140*m.b61*m.b59 + 40*m.b62*m.b59 + 190*m.b63*m.b59
                           + 710*m.b64*m.b59 + 280*m.b65*m.b59 + 130*m.b66*m.b59 + 450*m.b67*m.b59 + 520*m.b68*m.b59 + 
                          790*m.b69*m.b59 + 110*m.b70*m.b59 + 400*m.b71*m.b59 + 120*m.b72*m.b59 + 570*m.b73*m.b59 + 480*
                          m.b74*m.b59 + 170*m.b75*m.b59 + 430*m.b61*m.b60 + 620*m.b62*m.b60 + 240*m.b63*m.b60 + 450*
                          m.b64*m.b60 + 210*m.b65*m.b60 + 600*m.b66*m.b60 + 120*m.b67*m.b60 + 660*m.b68*m.b60 + 530*
                          m.b69*m.b60 + 50*m.b70*m.b60 + 810*m.b71*m.b60 + 610*m.b72*m.b60 + 100*m.b73*m.b60 + 880*m.b74
                          *m.b60 + 770*m.b75*m.b60 + 340*m.b62*m.b61 + 20*m.b63*m.b61 + 820*m.b64*m.b61 + 530*m.b65*
                          m.b61 + 260*m.b66*m.b61 + 620*m.b67*m.b61 + 180*m.b68*m.b61 + 710*m.b69*m.b61 + 140*m.b70*
                          m.b61 + 970*m.b71*m.b61 + 820*m.b72*m.b61 + 540*m.b73*m.b61 + 90*m.b74*m.b61 + 920*m.b75*m.b61
                           + 550*m.b63*m.b62 + 780*m.b64*m.b62 + 870*m.b65*m.b62 + 690*m.b66*m.b62 + 20*m.b67*m.b62 + 
                          320*m.b68*m.b62 + 420*m.b69*m.b62 + 140*m.b70*m.b62 + 450*m.b71*m.b62 + 600*m.b72*m.b62 + 670*
                          m.b73*m.b62 + 20*m.b74*m.b62 + 420*m.b75*m.b62 + 810*m.b64*m.b63 + 640*m.b65*m.b63 + 820*m.b66
                          *m.b63 + 580*m.b67*m.b63 + 980*m.b68*m.b63 + 360*m.b69*m.b63 + 920*m.b70*m.b63 + 30*m.b71*
                          m.b63 + 620*m.b72*m.b63 + 540*m.b73*m.b63 + 210*m.b74*m.b63 + 850*m.b75*m.b63 + 690*m.b65*
                          m.b64 + 700*m.b66*m.b64 + 200*m.b67*m.b64 + 750*m.b68*m.b64 + 800*m.b69*m.b64 + 120*m.b70*
                          m.b64 + 820*m.b71*m.b64 + 100*m.b72*m.b64 + 990*m.b73*m.b64 + 40*m.b74*m.b64 + 130*m.b75*m.b64
                           + 840*m.b66*m.b65 + 980*m.b67*m.b65 + 270*m.b68*m.b65 + 810*m.b69*m.b65 + 590*m.b70*m.b65 + 
                          470*m.b71*m.b65 + 830*m.b72*m.b65 + 530*m.b73*m.b65 + 800*m.b74*m.b65 + 350*m.b67*m.b66 + 900*
                          m.b68*m.b66 + 980*m.b69*m.b66 + 710*m.b70*m.b66 + 830*m.b71*m.b66 + 540*m.b72*m.b66 + 860*
                          m.b73*m.b66 + 890*m.b74*m.b66 + 270*m.b75*m.b66 + 710*m.b68*m.b67 + 100*m.b69*m.b67 + 980*
                          m.b70*m.b67 + 910*m.b71*m.b67 + 860*m.b72*m.b67 + 300*m.b73*m.b67 + 550*m.b74*m.b67 + 200*
                          m.b75*m.b67 + 400*m.b69*m.b68 + 70*m.b70*m.b68 + 760*m.b71*m.b68 + 530*m.b72*m.b68 + 910*m.b73
                          *m.b68 + 750*m.b74*m.b68 + 330*m.b75*m.b68 + 720*m.b70*m.b69 + 340*m.b71*m.b69 + 320*m.b72*
                          m.b69 + 70*m.b73*m.b69 + 870*m.b74*m.b69 + 640*m.b75*m.b69 + 70*m.b71*m.b70 + 740*m.b72*m.b70
                           + 540*m.b73*m.b70 + 580*m.b74*m.b70 + 970*m.b75*m.b70 + 890*m.b72*m.b71 + 120*m.b73*m.b71 + 
                          830*m.b74*m.b71 + 790*m.b75*m.b71 + 390*m.b73*m.b72 + 70*m.b74*m.b72 + 890*m.b75*m.b72 + 890*
                          m.b74*m.b73 + 980*m.b75*m.b73 + 270*m.b75*m.b74 >= 67751)

m.c3996 = Constraint(expr=750*m.b24*m.b5 + 390*m.b42*m.b5 + 260*m.b59*m.b5 + 940*m.b76*m.b5 + 760*m.b77*m.b5 + 550*m.b78
                          *m.b5 + 800*m.b79*m.b5 + 580*m.b80*m.b5 + 340*m.b81*m.b5 + 200*m.b82*m.b5 + 880*m.b83*m.b5 + 
                          600*m.b84*m.b5 + 170*m.b85*m.b5 + 850*m.b86*m.b5 + 710*m.b87*m.b5 + 970*m.b88*m.b5 + 830*m.b89
                          *m.b5 + 990*m.b90*m.b5 + 640*m.b91*m.b5 + 970*m.b42*m.b24 + 680*m.b59*m.b24 + 630*m.b76*m.b24
                           + 670*m.b77*m.b24 + 310*m.b78*m.b24 + 210*m.b79*m.b24 + 710*m.b80*m.b24 + 880*m.b81*m.b24 + 
                          530*m.b82*m.b24 + 500*m.b83*m.b24 + 630*m.b84*m.b24 + 920*m.b85*m.b24 + 290*m.b86*m.b24 + 180*
                          m.b87*m.b24 + 860*m.b88*m.b24 + 570*m.b89*m.b24 + 730*m.b90*m.b24 + 180*m.b91*m.b24 + 150*
                          m.b59*m.b42 + 390*m.b76*m.b42 + 30*m.b77*m.b42 + 190*m.b78*m.b42 + 80*m.b79*m.b42 + 880*m.b80*
                          m.b42 + 430*m.b81*m.b42 + 570*m.b82*m.b42 + 230*m.b83*m.b42 + 940*m.b84*m.b42 + 210*m.b85*
                          m.b42 + 720*m.b86*m.b42 + 140*m.b87*m.b42 + 140*m.b88*m.b42 + 870*m.b89*m.b42 + 330*m.b90*
                          m.b42 + 460*m.b91*m.b42 + 40*m.b76*m.b59 + 340*m.b77*m.b59 + 620*m.b78*m.b59 + 550*m.b79*m.b59
                           + 490*m.b80*m.b59 + 60*m.b81*m.b59 + 360*m.b82*m.b59 + 670*m.b83*m.b59 + 450*m.b84*m.b59 + 
                          930*m.b85*m.b59 + 930*m.b86*m.b59 + 630*m.b87*m.b59 + 80*m.b88*m.b59 + 520*m.b89*m.b59 + 540*
                          m.b90*m.b59 + 640*m.b91*m.b59 + 430*m.b77*m.b76 + 620*m.b78*m.b76 + 240*m.b79*m.b76 + 450*
                          m.b80*m.b76 + 210*m.b81*m.b76 + 600*m.b82*m.b76 + 120*m.b83*m.b76 + 660*m.b84*m.b76 + 530*
                          m.b85*m.b76 + 50*m.b86*m.b76 + 810*m.b87*m.b76 + 610*m.b88*m.b76 + 100*m.b89*m.b76 + 880*m.b90
                          *m.b76 + 770*m.b91*m.b76 + 340*m.b78*m.b77 + 20*m.b79*m.b77 + 820*m.b80*m.b77 + 530*m.b81*
                          m.b77 + 260*m.b82*m.b77 + 620*m.b83*m.b77 + 180*m.b84*m.b77 + 710*m.b85*m.b77 + 140*m.b86*
                          m.b77 + 970*m.b87*m.b77 + 820*m.b88*m.b77 + 540*m.b89*m.b77 + 90*m.b90*m.b77 + 920*m.b91*m.b77
                           + 550*m.b79*m.b78 + 780*m.b80*m.b78 + 870*m.b81*m.b78 + 690*m.b82*m.b78 + 20*m.b83*m.b78 + 
                          320*m.b84*m.b78 + 420*m.b85*m.b78 + 140*m.b86*m.b78 + 450*m.b87*m.b78 + 600*m.b88*m.b78 + 670*
                          m.b89*m.b78 + 20*m.b90*m.b78 + 420*m.b91*m.b78 + 810*m.b80*m.b79 + 640*m.b81*m.b79 + 820*m.b82
                          *m.b79 + 580*m.b83*m.b79 + 980*m.b84*m.b79 + 360*m.b85*m.b79 + 920*m.b86*m.b79 + 30*m.b87*
                          m.b79 + 620*m.b88*m.b79 + 540*m.b89*m.b79 + 210*m.b90*m.b79 + 850*m.b91*m.b79 + 690*m.b81*
                          m.b80 + 700*m.b82*m.b80 + 200*m.b83*m.b80 + 750*m.b84*m.b80 + 800*m.b85*m.b80 + 120*m.b86*
                          m.b80 + 820*m.b87*m.b80 + 100*m.b88*m.b80 + 990*m.b89*m.b80 + 40*m.b90*m.b80 + 130*m.b91*m.b80
                           + 840*m.b82*m.b81 + 980*m.b83*m.b81 + 270*m.b84*m.b81 + 810*m.b85*m.b81 + 590*m.b86*m.b81 + 
                          470*m.b87*m.b81 + 830*m.b88*m.b81 + 530*m.b89*m.b81 + 800*m.b90*m.b81 + 350*m.b83*m.b82 + 900*
                          m.b84*m.b82 + 980*m.b85*m.b82 + 710*m.b86*m.b82 + 830*m.b87*m.b82 + 540*m.b88*m.b82 + 860*
                          m.b89*m.b82 + 890*m.b90*m.b82 + 270*m.b91*m.b82 + 710*m.b84*m.b83 + 100*m.b85*m.b83 + 980*
                          m.b86*m.b83 + 910*m.b87*m.b83 + 860*m.b88*m.b83 + 300*m.b89*m.b83 + 550*m.b90*m.b83 + 200*
                          m.b91*m.b83 + 400*m.b85*m.b84 + 70*m.b86*m.b84 + 760*m.b87*m.b84 + 530*m.b88*m.b84 + 910*m.b89
                          *m.b84 + 750*m.b90*m.b84 + 330*m.b91*m.b84 + 720*m.b86*m.b85 + 340*m.b87*m.b85 + 320*m.b88*
                          m.b85 + 70*m.b89*m.b85 + 870*m.b90*m.b85 + 640*m.b91*m.b85 + 70*m.b87*m.b86 + 740*m.b88*m.b86
                           + 540*m.b89*m.b86 + 580*m.b90*m.b86 + 970*m.b91*m.b86 + 890*m.b88*m.b87 + 120*m.b89*m.b87 + 
                          830*m.b90*m.b87 + 790*m.b91*m.b87 + 390*m.b89*m.b88 + 70*m.b90*m.b88 + 890*m.b91*m.b88 + 890*
                          m.b90*m.b89 + 980*m.b91*m.b89 + 270*m.b91*m.b90 >= 67751)

m.c3997 = Constraint(expr=750*m.b25*m.b6 + 390*m.b43*m.b6 + 260*m.b60*m.b6 + 20*m.b76*m.b6 + 760*m.b92*m.b6 + 550*m.b93*
                          m.b6 + 800*m.b94*m.b6 + 580*m.b95*m.b6 + 340*m.b96*m.b6 + 200*m.b97*m.b6 + 880*m.b98*m.b6 + 
                          600*m.b99*m.b6 + 170*m.b100*m.b6 + 850*m.b101*m.b6 + 710*m.b102*m.b6 + 970*m.b103*m.b6 + 830*
                          m.b104*m.b6 + 990*m.b105*m.b6 + 640*m.b106*m.b6 + 970*m.b43*m.b25 + 680*m.b60*m.b25 + 410*
                          m.b76*m.b25 + 670*m.b92*m.b25 + 310*m.b93*m.b25 + 210*m.b94*m.b25 + 710*m.b95*m.b25 + 880*
                          m.b96*m.b25 + 530*m.b97*m.b25 + 500*m.b98*m.b25 + 630*m.b99*m.b25 + 920*m.b100*m.b25 + 290*
                          m.b101*m.b25 + 180*m.b102*m.b25 + 860*m.b103*m.b25 + 570*m.b104*m.b25 + 730*m.b105*m.b25 + 180
                          *m.b106*m.b25 + 150*m.b60*m.b43 + 590*m.b76*m.b43 + 30*m.b92*m.b43 + 190*m.b93*m.b43 + 80*
                          m.b94*m.b43 + 880*m.b95*m.b43 + 430*m.b96*m.b43 + 570*m.b97*m.b43 + 230*m.b98*m.b43 + 940*
                          m.b99*m.b43 + 210*m.b100*m.b43 + 720*m.b101*m.b43 + 140*m.b102*m.b43 + 140*m.b103*m.b43 + 870*
                          m.b104*m.b43 + 330*m.b105*m.b43 + 460*m.b106*m.b43 + 80*m.b76*m.b60 + 340*m.b92*m.b60 + 620*
                          m.b93*m.b60 + 550*m.b94*m.b60 + 490*m.b95*m.b60 + 60*m.b96*m.b60 + 360*m.b97*m.b60 + 670*m.b98
                          *m.b60 + 450*m.b99*m.b60 + 930*m.b100*m.b60 + 930*m.b101*m.b60 + 630*m.b102*m.b60 + 80*m.b103*
                          m.b60 + 520*m.b104*m.b60 + 540*m.b105*m.b60 + 640*m.b106*m.b60 + 140*m.b92*m.b76 + 40*m.b93*
                          m.b76 + 190*m.b94*m.b76 + 710*m.b95*m.b76 + 280*m.b96*m.b76 + 130*m.b97*m.b76 + 450*m.b98*
                          m.b76 + 520*m.b99*m.b76 + 790*m.b100*m.b76 + 110*m.b101*m.b76 + 400*m.b102*m.b76 + 120*m.b103*
                          m.b76 + 570*m.b104*m.b76 + 480*m.b105*m.b76 + 170*m.b106*m.b76 + 340*m.b93*m.b92 + 20*m.b94*
                          m.b92 + 820*m.b95*m.b92 + 530*m.b96*m.b92 + 260*m.b97*m.b92 + 620*m.b98*m.b92 + 180*m.b99*
                          m.b92 + 710*m.b100*m.b92 + 140*m.b101*m.b92 + 970*m.b102*m.b92 + 820*m.b103*m.b92 + 540*m.b104
                          *m.b92 + 90*m.b105*m.b92 + 920*m.b106*m.b92 + 550*m.b94*m.b93 + 780*m.b95*m.b93 + 870*m.b96*
                          m.b93 + 690*m.b97*m.b93 + 20*m.b98*m.b93 + 320*m.b99*m.b93 + 420*m.b100*m.b93 + 140*m.b101*
                          m.b93 + 450*m.b102*m.b93 + 600*m.b103*m.b93 + 670*m.b104*m.b93 + 20*m.b105*m.b93 + 420*m.b106*
                          m.b93 + 810*m.b95*m.b94 + 640*m.b96*m.b94 + 820*m.b97*m.b94 + 580*m.b98*m.b94 + 980*m.b99*
                          m.b94 + 360*m.b100*m.b94 + 920*m.b101*m.b94 + 30*m.b102*m.b94 + 620*m.b103*m.b94 + 540*m.b104*
                          m.b94 + 210*m.b105*m.b94 + 850*m.b106*m.b94 + 690*m.b96*m.b95 + 700*m.b97*m.b95 + 200*m.b98*
                          m.b95 + 750*m.b99*m.b95 + 800*m.b100*m.b95 + 120*m.b101*m.b95 + 820*m.b102*m.b95 + 100*m.b103*
                          m.b95 + 990*m.b104*m.b95 + 40*m.b105*m.b95 + 130*m.b106*m.b95 + 840*m.b97*m.b96 + 980*m.b98*
                          m.b96 + 270*m.b99*m.b96 + 810*m.b100*m.b96 + 590*m.b101*m.b96 + 470*m.b102*m.b96 + 830*m.b103*
                          m.b96 + 530*m.b104*m.b96 + 800*m.b105*m.b96 + 350*m.b98*m.b97 + 900*m.b99*m.b97 + 980*m.b100*
                          m.b97 + 710*m.b101*m.b97 + 830*m.b102*m.b97 + 540*m.b103*m.b97 + 860*m.b104*m.b97 + 890*m.b105
                          *m.b97 + 270*m.b106*m.b97 + 710*m.b99*m.b98 + 100*m.b100*m.b98 + 980*m.b101*m.b98 + 910*m.b102
                          *m.b98 + 860*m.b103*m.b98 + 300*m.b104*m.b98 + 550*m.b105*m.b98 + 200*m.b106*m.b98 + 400*
                          m.b100*m.b99 + 70*m.b101*m.b99 + 760*m.b102*m.b99 + 530*m.b103*m.b99 + 910*m.b104*m.b99 + 750*
                          m.b105*m.b99 + 330*m.b106*m.b99 + 720*m.b101*m.b100 + 340*m.b102*m.b100 + 320*m.b103*m.b100 + 
                          70*m.b104*m.b100 + 870*m.b105*m.b100 + 640*m.b106*m.b100 + 70*m.b102*m.b101 + 740*m.b103*
                          m.b101 + 540*m.b104*m.b101 + 580*m.b105*m.b101 + 970*m.b106*m.b101 + 890*m.b103*m.b102 + 120*
                          m.b104*m.b102 + 830*m.b105*m.b102 + 790*m.b106*m.b102 + 390*m.b104*m.b103 + 70*m.b105*m.b103
                           + 890*m.b106*m.b103 + 890*m.b105*m.b104 + 980*m.b106*m.b104 + 270*m.b106*m.b105 >= 67751)

m.c3998 = Constraint(expr=750*m.b26*m.b7 + 390*m.b44*m.b7 + 260*m.b61*m.b7 + 20*m.b77*m.b7 + 940*m.b92*m.b7 + 550*m.b107
                          *m.b7 + 800*m.b108*m.b7 + 580*m.b109*m.b7 + 340*m.b110*m.b7 + 200*m.b111*m.b7 + 880*m.b112*
                          m.b7 + 600*m.b113*m.b7 + 170*m.b114*m.b7 + 850*m.b115*m.b7 + 710*m.b116*m.b7 + 970*m.b117*m.b7
                           + 830*m.b118*m.b7 + 990*m.b119*m.b7 + 640*m.b120*m.b7 + 970*m.b44*m.b26 + 680*m.b61*m.b26 + 
                          410*m.b77*m.b26 + 630*m.b92*m.b26 + 310*m.b107*m.b26 + 210*m.b108*m.b26 + 710*m.b109*m.b26 + 
                          880*m.b110*m.b26 + 530*m.b111*m.b26 + 500*m.b112*m.b26 + 630*m.b113*m.b26 + 920*m.b114*m.b26
                           + 290*m.b115*m.b26 + 180*m.b116*m.b26 + 860*m.b117*m.b26 + 570*m.b118*m.b26 + 730*m.b119*
                          m.b26 + 180*m.b120*m.b26 + 150*m.b61*m.b44 + 590*m.b77*m.b44 + 390*m.b92*m.b44 + 190*m.b107*
                          m.b44 + 80*m.b108*m.b44 + 880*m.b109*m.b44 + 430*m.b110*m.b44 + 570*m.b111*m.b44 + 230*m.b112*
                          m.b44 + 940*m.b113*m.b44 + 210*m.b114*m.b44 + 720*m.b115*m.b44 + 140*m.b116*m.b44 + 140*m.b117
                          *m.b44 + 870*m.b118*m.b44 + 330*m.b119*m.b44 + 460*m.b120*m.b44 + 80*m.b77*m.b61 + 40*m.b92*
                          m.b61 + 620*m.b107*m.b61 + 550*m.b108*m.b61 + 490*m.b109*m.b61 + 60*m.b110*m.b61 + 360*m.b111*
                          m.b61 + 670*m.b112*m.b61 + 450*m.b113*m.b61 + 930*m.b114*m.b61 + 930*m.b115*m.b61 + 630*m.b116
                          *m.b61 + 80*m.b117*m.b61 + 520*m.b118*m.b61 + 540*m.b119*m.b61 + 640*m.b120*m.b61 + 240*m.b92*
                          m.b77 + 40*m.b107*m.b77 + 190*m.b108*m.b77 + 710*m.b109*m.b77 + 280*m.b110*m.b77 + 130*m.b111*
                          m.b77 + 450*m.b112*m.b77 + 520*m.b113*m.b77 + 790*m.b114*m.b77 + 110*m.b115*m.b77 + 400*m.b116
                          *m.b77 + 120*m.b117*m.b77 + 570*m.b118*m.b77 + 480*m.b119*m.b77 + 170*m.b120*m.b77 + 620*
                          m.b107*m.b92 + 240*m.b108*m.b92 + 450*m.b109*m.b92 + 210*m.b110*m.b92 + 600*m.b111*m.b92 + 120
                          *m.b112*m.b92 + 660*m.b113*m.b92 + 530*m.b114*m.b92 + 50*m.b115*m.b92 + 810*m.b116*m.b92 + 610
                          *m.b117*m.b92 + 100*m.b118*m.b92 + 880*m.b119*m.b92 + 770*m.b120*m.b92 + 550*m.b108*m.b107 + 
                          780*m.b109*m.b107 + 870*m.b110*m.b107 + 690*m.b111*m.b107 + 20*m.b112*m.b107 + 320*m.b113*
                          m.b107 + 420*m.b114*m.b107 + 140*m.b115*m.b107 + 450*m.b116*m.b107 + 600*m.b117*m.b107 + 670*
                          m.b118*m.b107 + 20*m.b119*m.b107 + 420*m.b120*m.b107 + 810*m.b109*m.b108 + 640*m.b110*m.b108
                           + 820*m.b111*m.b108 + 580*m.b112*m.b108 + 980*m.b113*m.b108 + 360*m.b114*m.b108 + 920*m.b115*
                          m.b108 + 30*m.b116*m.b108 + 620*m.b117*m.b108 + 540*m.b118*m.b108 + 210*m.b119*m.b108 + 850*
                          m.b120*m.b108 + 690*m.b110*m.b109 + 700*m.b111*m.b109 + 200*m.b112*m.b109 + 750*m.b113*m.b109
                           + 800*m.b114*m.b109 + 120*m.b115*m.b109 + 820*m.b116*m.b109 + 100*m.b117*m.b109 + 990*m.b118*
                          m.b109 + 40*m.b119*m.b109 + 130*m.b120*m.b109 + 840*m.b111*m.b110 + 980*m.b112*m.b110 + 270*
                          m.b113*m.b110 + 810*m.b114*m.b110 + 590*m.b115*m.b110 + 470*m.b116*m.b110 + 830*m.b117*m.b110
                           + 530*m.b118*m.b110 + 800*m.b119*m.b110 + 350*m.b112*m.b111 + 900*m.b113*m.b111 + 980*m.b114*
                          m.b111 + 710*m.b115*m.b111 + 830*m.b116*m.b111 + 540*m.b117*m.b111 + 860*m.b118*m.b111 + 890*
                          m.b119*m.b111 + 270*m.b120*m.b111 + 710*m.b113*m.b112 + 100*m.b114*m.b112 + 980*m.b115*m.b112
                           + 910*m.b116*m.b112 + 860*m.b117*m.b112 + 300*m.b118*m.b112 + 550*m.b119*m.b112 + 200*m.b120*
                          m.b112 + 400*m.b114*m.b113 + 70*m.b115*m.b113 + 760*m.b116*m.b113 + 530*m.b117*m.b113 + 910*
                          m.b118*m.b113 + 750*m.b119*m.b113 + 330*m.b120*m.b113 + 720*m.b115*m.b114 + 340*m.b116*m.b114
                           + 320*m.b117*m.b114 + 70*m.b118*m.b114 + 870*m.b119*m.b114 + 640*m.b120*m.b114 + 70*m.b116*
                          m.b115 + 740*m.b117*m.b115 + 540*m.b118*m.b115 + 580*m.b119*m.b115 + 970*m.b120*m.b115 + 890*
                          m.b117*m.b116 + 120*m.b118*m.b116 + 830*m.b119*m.b116 + 790*m.b120*m.b116 + 390*m.b118*m.b117
                           + 70*m.b119*m.b117 + 890*m.b120*m.b117 + 890*m.b119*m.b118 + 980*m.b120*m.b118 + 270*m.b120*
                          m.b119 >= 67751)

m.c3999 = Constraint(expr=750*m.b27*m.b8 + 390*m.b45*m.b8 + 260*m.b62*m.b8 + 20*m.b78*m.b8 + 940*m.b93*m.b8 + 760*m.b107
                          *m.b8 + 800*m.b121*m.b8 + 580*m.b122*m.b8 + 340*m.b123*m.b8 + 200*m.b124*m.b8 + 880*m.b125*
                          m.b8 + 600*m.b126*m.b8 + 170*m.b127*m.b8 + 850*m.b128*m.b8 + 710*m.b129*m.b8 + 970*m.b130*m.b8
                           + 830*m.b131*m.b8 + 990*m.b132*m.b8 + 640*m.b133*m.b8 + 970*m.b45*m.b27 + 680*m.b62*m.b27 + 
                          410*m.b78*m.b27 + 630*m.b93*m.b27 + 670*m.b107*m.b27 + 210*m.b121*m.b27 + 710*m.b122*m.b27 + 
                          880*m.b123*m.b27 + 530*m.b124*m.b27 + 500*m.b125*m.b27 + 630*m.b126*m.b27 + 920*m.b127*m.b27
                           + 290*m.b128*m.b27 + 180*m.b129*m.b27 + 860*m.b130*m.b27 + 570*m.b131*m.b27 + 730*m.b132*
                          m.b27 + 180*m.b133*m.b27 + 150*m.b62*m.b45 + 590*m.b78*m.b45 + 390*m.b93*m.b45 + 30*m.b107*
                          m.b45 + 80*m.b121*m.b45 + 880*m.b122*m.b45 + 430*m.b123*m.b45 + 570*m.b124*m.b45 + 230*m.b125*
                          m.b45 + 940*m.b126*m.b45 + 210*m.b127*m.b45 + 720*m.b128*m.b45 + 140*m.b129*m.b45 + 140*m.b130
                          *m.b45 + 870*m.b131*m.b45 + 330*m.b132*m.b45 + 460*m.b133*m.b45 + 80*m.b78*m.b62 + 40*m.b93*
                          m.b62 + 340*m.b107*m.b62 + 550*m.b121*m.b62 + 490*m.b122*m.b62 + 60*m.b123*m.b62 + 360*m.b124*
                          m.b62 + 670*m.b125*m.b62 + 450*m.b126*m.b62 + 930*m.b127*m.b62 + 930*m.b128*m.b62 + 630*m.b129
                          *m.b62 + 80*m.b130*m.b62 + 520*m.b131*m.b62 + 540*m.b132*m.b62 + 640*m.b133*m.b62 + 240*m.b93*
                          m.b78 + 140*m.b107*m.b78 + 190*m.b121*m.b78 + 710*m.b122*m.b78 + 280*m.b123*m.b78 + 130*m.b124
                          *m.b78 + 450*m.b125*m.b78 + 520*m.b126*m.b78 + 790*m.b127*m.b78 + 110*m.b128*m.b78 + 400*
                          m.b129*m.b78 + 120*m.b130*m.b78 + 570*m.b131*m.b78 + 480*m.b132*m.b78 + 170*m.b133*m.b78 + 430
                          *m.b107*m.b93 + 240*m.b121*m.b93 + 450*m.b122*m.b93 + 210*m.b123*m.b93 + 600*m.b124*m.b93 + 
                          120*m.b125*m.b93 + 660*m.b126*m.b93 + 530*m.b127*m.b93 + 50*m.b128*m.b93 + 810*m.b129*m.b93 + 
                          610*m.b130*m.b93 + 100*m.b131*m.b93 + 880*m.b132*m.b93 + 770*m.b133*m.b93 + 20*m.b121*m.b107
                           + 820*m.b122*m.b107 + 530*m.b123*m.b107 + 260*m.b124*m.b107 + 620*m.b125*m.b107 + 180*m.b126*
                          m.b107 + 710*m.b127*m.b107 + 140*m.b128*m.b107 + 970*m.b129*m.b107 + 820*m.b130*m.b107 + 540*
                          m.b131*m.b107 + 90*m.b132*m.b107 + 920*m.b133*m.b107 + 810*m.b122*m.b121 + 640*m.b123*m.b121
                           + 820*m.b124*m.b121 + 580*m.b125*m.b121 + 980*m.b126*m.b121 + 360*m.b127*m.b121 + 920*m.b128*
                          m.b121 + 30*m.b129*m.b121 + 620*m.b130*m.b121 + 540*m.b131*m.b121 + 210*m.b132*m.b121 + 850*
                          m.b133*m.b121 + 690*m.b123*m.b122 + 700*m.b124*m.b122 + 200*m.b125*m.b122 + 750*m.b126*m.b122
                           + 800*m.b127*m.b122 + 120*m.b128*m.b122 + 820*m.b129*m.b122 + 100*m.b130*m.b122 + 990*m.b131*
                          m.b122 + 40*m.b132*m.b122 + 130*m.b133*m.b122 + 840*m.b124*m.b123 + 980*m.b125*m.b123 + 270*
                          m.b126*m.b123 + 810*m.b127*m.b123 + 590*m.b128*m.b123 + 470*m.b129*m.b123 + 830*m.b130*m.b123
                           + 530*m.b131*m.b123 + 800*m.b132*m.b123 + 350*m.b125*m.b124 + 900*m.b126*m.b124 + 980*m.b127*
                          m.b124 + 710*m.b128*m.b124 + 830*m.b129*m.b124 + 540*m.b130*m.b124 + 860*m.b131*m.b124 + 890*
                          m.b132*m.b124 + 270*m.b133*m.b124 + 710*m.b126*m.b125 + 100*m.b127*m.b125 + 980*m.b128*m.b125
                           + 910*m.b129*m.b125 + 860*m.b130*m.b125 + 300*m.b131*m.b125 + 550*m.b132*m.b125 + 200*m.b133*
                          m.b125 + 400*m.b127*m.b126 + 70*m.b128*m.b126 + 760*m.b129*m.b126 + 530*m.b130*m.b126 + 910*
                          m.b131*m.b126 + 750*m.b132*m.b126 + 330*m.b133*m.b126 + 720*m.b128*m.b127 + 340*m.b129*m.b127
                           + 320*m.b130*m.b127 + 70*m.b131*m.b127 + 870*m.b132*m.b127 + 640*m.b133*m.b127 + 70*m.b129*
                          m.b128 + 740*m.b130*m.b128 + 540*m.b131*m.b128 + 580*m.b132*m.b128 + 970*m.b133*m.b128 + 890*
                          m.b130*m.b129 + 120*m.b131*m.b129 + 830*m.b132*m.b129 + 790*m.b133*m.b129 + 390*m.b131*m.b130
                           + 70*m.b132*m.b130 + 890*m.b133*m.b130 + 890*m.b132*m.b131 + 980*m.b133*m.b131 + 270*m.b133*
                          m.b132 >= 67751)

m.c4000 = Constraint(expr=750*m.b28*m.b9 + 390*m.b46*m.b9 + 260*m.b63*m.b9 + 20*m.b79*m.b9 + 940*m.b94*m.b9 + 760*m.b108
                          *m.b9 + 550*m.b121*m.b9 + 580*m.b134*m.b9 + 340*m.b135*m.b9 + 200*m.b136*m.b9 + 880*m.b137*
                          m.b9 + 600*m.b138*m.b9 + 170*m.b139*m.b9 + 850*m.b140*m.b9 + 710*m.b141*m.b9 + 970*m.b142*m.b9
                           + 830*m.b143*m.b9 + 990*m.b144*m.b9 + 640*m.b145*m.b9 + 970*m.b46*m.b28 + 680*m.b63*m.b28 + 
                          410*m.b79*m.b28 + 630*m.b94*m.b28 + 670*m.b108*m.b28 + 310*m.b121*m.b28 + 710*m.b134*m.b28 + 
                          880*m.b135*m.b28 + 530*m.b136*m.b28 + 500*m.b137*m.b28 + 630*m.b138*m.b28 + 920*m.b139*m.b28
                           + 290*m.b140*m.b28 + 180*m.b141*m.b28 + 860*m.b142*m.b28 + 570*m.b143*m.b28 + 730*m.b144*
                          m.b28 + 180*m.b145*m.b28 + 150*m.b63*m.b46 + 590*m.b79*m.b46 + 390*m.b94*m.b46 + 30*m.b108*
                          m.b46 + 190*m.b121*m.b46 + 880*m.b134*m.b46 + 430*m.b135*m.b46 + 570*m.b136*m.b46 + 230*m.b137
                          *m.b46 + 940*m.b138*m.b46 + 210*m.b139*m.b46 + 720*m.b140*m.b46 + 140*m.b141*m.b46 + 140*
                          m.b142*m.b46 + 870*m.b143*m.b46 + 330*m.b144*m.b46 + 460*m.b145*m.b46 + 80*m.b79*m.b63 + 40*
                          m.b94*m.b63 + 340*m.b108*m.b63 + 620*m.b121*m.b63 + 490*m.b134*m.b63 + 60*m.b135*m.b63 + 360*
                          m.b136*m.b63 + 670*m.b137*m.b63 + 450*m.b138*m.b63 + 930*m.b139*m.b63 + 930*m.b140*m.b63 + 630
                          *m.b141*m.b63 + 80*m.b142*m.b63 + 520*m.b143*m.b63 + 540*m.b144*m.b63 + 640*m.b145*m.b63 + 240
                          *m.b94*m.b79 + 140*m.b108*m.b79 + 40*m.b121*m.b79 + 710*m.b134*m.b79 + 280*m.b135*m.b79 + 130*
                          m.b136*m.b79 + 450*m.b137*m.b79 + 520*m.b138*m.b79 + 790*m.b139*m.b79 + 110*m.b140*m.b79 + 400
                          *m.b141*m.b79 + 120*m.b142*m.b79 + 570*m.b143*m.b79 + 480*m.b144*m.b79 + 170*m.b145*m.b79 + 
                          430*m.b108*m.b94 + 620*m.b121*m.b94 + 450*m.b134*m.b94 + 210*m.b135*m.b94 + 600*m.b136*m.b94
                           + 120*m.b137*m.b94 + 660*m.b138*m.b94 + 530*m.b139*m.b94 + 50*m.b140*m.b94 + 810*m.b141*m.b94
                           + 610*m.b142*m.b94 + 100*m.b143*m.b94 + 880*m.b144*m.b94 + 770*m.b145*m.b94 + 340*m.b121*
                          m.b108 + 820*m.b134*m.b108 + 530*m.b135*m.b108 + 260*m.b136*m.b108 + 620*m.b137*m.b108 + 180*
                          m.b138*m.b108 + 710*m.b139*m.b108 + 140*m.b140*m.b108 + 970*m.b141*m.b108 + 820*m.b142*m.b108
                           + 540*m.b143*m.b108 + 90*m.b144*m.b108 + 920*m.b145*m.b108 + 780*m.b134*m.b121 + 870*m.b135*
                          m.b121 + 690*m.b136*m.b121 + 20*m.b137*m.b121 + 320*m.b138*m.b121 + 420*m.b139*m.b121 + 140*
                          m.b140*m.b121 + 450*m.b141*m.b121 + 600*m.b142*m.b121 + 670*m.b143*m.b121 + 20*m.b144*m.b121
                           + 420*m.b145*m.b121 + 690*m.b135*m.b134 + 700*m.b136*m.b134 + 200*m.b137*m.b134 + 750*m.b138*
                          m.b134 + 800*m.b139*m.b134 + 120*m.b140*m.b134 + 820*m.b141*m.b134 + 100*m.b142*m.b134 + 990*
                          m.b143*m.b134 + 40*m.b144*m.b134 + 130*m.b145*m.b134 + 840*m.b136*m.b135 + 980*m.b137*m.b135
                           + 270*m.b138*m.b135 + 810*m.b139*m.b135 + 590*m.b140*m.b135 + 470*m.b141*m.b135 + 830*m.b142*
                          m.b135 + 530*m.b143*m.b135 + 800*m.b144*m.b135 + 350*m.b137*m.b136 + 900*m.b138*m.b136 + 980*
                          m.b139*m.b136 + 710*m.b140*m.b136 + 830*m.b141*m.b136 + 540*m.b142*m.b136 + 860*m.b143*m.b136
                           + 890*m.b144*m.b136 + 270*m.b145*m.b136 + 710*m.b138*m.b137 + 100*m.b139*m.b137 + 980*m.b140*
                          m.b137 + 910*m.b141*m.b137 + 860*m.b142*m.b137 + 300*m.b143*m.b137 + 550*m.b144*m.b137 + 200*
                          m.b145*m.b137 + 400*m.b139*m.b138 + 70*m.b140*m.b138 + 760*m.b141*m.b138 + 530*m.b142*m.b138
                           + 910*m.b143*m.b138 + 750*m.b144*m.b138 + 330*m.b145*m.b138 + 720*m.b140*m.b139 + 340*m.b141*
                          m.b139 + 320*m.b142*m.b139 + 70*m.b143*m.b139 + 870*m.b144*m.b139 + 640*m.b145*m.b139 + 70*
                          m.b141*m.b140 + 740*m.b142*m.b140 + 540*m.b143*m.b140 + 580*m.b144*m.b140 + 970*m.b145*m.b140
                           + 890*m.b142*m.b141 + 120*m.b143*m.b141 + 830*m.b144*m.b141 + 790*m.b145*m.b141 + 390*m.b143*
                          m.b142 + 70*m.b144*m.b142 + 890*m.b145*m.b142 + 890*m.b144*m.b143 + 980*m.b145*m.b143 + 270*
                          m.b145*m.b144 >= 67751)

m.c4001 = Constraint(expr=750*m.b29*m.b10 + 390*m.b47*m.b10 + 260*m.b64*m.b10 + 20*m.b80*m.b10 + 940*m.b95*m.b10 + 760*
                          m.b109*m.b10 + 550*m.b122*m.b10 + 800*m.b134*m.b10 + 340*m.b146*m.b10 + 200*m.b147*m.b10 + 880
                          *m.b148*m.b10 + 600*m.b149*m.b10 + 170*m.b150*m.b10 + 850*m.b151*m.b10 + 710*m.b152*m.b10 + 
                          970*m.b153*m.b10 + 830*m.b154*m.b10 + 990*m.b155*m.b10 + 640*m.b156*m.b10 + 970*m.b47*m.b29 + 
                          680*m.b64*m.b29 + 410*m.b80*m.b29 + 630*m.b95*m.b29 + 670*m.b109*m.b29 + 310*m.b122*m.b29 + 
                          210*m.b134*m.b29 + 880*m.b146*m.b29 + 530*m.b147*m.b29 + 500*m.b148*m.b29 + 630*m.b149*m.b29
                           + 920*m.b150*m.b29 + 290*m.b151*m.b29 + 180*m.b152*m.b29 + 860*m.b153*m.b29 + 570*m.b154*
                          m.b29 + 730*m.b155*m.b29 + 180*m.b156*m.b29 + 150*m.b64*m.b47 + 590*m.b80*m.b47 + 390*m.b95*
                          m.b47 + 30*m.b109*m.b47 + 190*m.b122*m.b47 + 80*m.b134*m.b47 + 430*m.b146*m.b47 + 570*m.b147*
                          m.b47 + 230*m.b148*m.b47 + 940*m.b149*m.b47 + 210*m.b150*m.b47 + 720*m.b151*m.b47 + 140*m.b152
                          *m.b47 + 140*m.b153*m.b47 + 870*m.b154*m.b47 + 330*m.b155*m.b47 + 460*m.b156*m.b47 + 80*m.b80*
                          m.b64 + 40*m.b95*m.b64 + 340*m.b109*m.b64 + 620*m.b122*m.b64 + 550*m.b134*m.b64 + 60*m.b146*
                          m.b64 + 360*m.b147*m.b64 + 670*m.b148*m.b64 + 450*m.b149*m.b64 + 930*m.b150*m.b64 + 930*m.b151
                          *m.b64 + 630*m.b152*m.b64 + 80*m.b153*m.b64 + 520*m.b154*m.b64 + 540*m.b155*m.b64 + 640*m.b156
                          *m.b64 + 240*m.b95*m.b80 + 140*m.b109*m.b80 + 40*m.b122*m.b80 + 190*m.b134*m.b80 + 280*m.b146*
                          m.b80 + 130*m.b147*m.b80 + 450*m.b148*m.b80 + 520*m.b149*m.b80 + 790*m.b150*m.b80 + 110*m.b151
                          *m.b80 + 400*m.b152*m.b80 + 120*m.b153*m.b80 + 570*m.b154*m.b80 + 480*m.b155*m.b80 + 170*
                          m.b156*m.b80 + 430*m.b109*m.b95 + 620*m.b122*m.b95 + 240*m.b134*m.b95 + 210*m.b146*m.b95 + 600
                          *m.b147*m.b95 + 120*m.b148*m.b95 + 660*m.b149*m.b95 + 530*m.b150*m.b95 + 50*m.b151*m.b95 + 810
                          *m.b152*m.b95 + 610*m.b153*m.b95 + 100*m.b154*m.b95 + 880*m.b155*m.b95 + 770*m.b156*m.b95 + 
                          340*m.b122*m.b109 + 20*m.b134*m.b109 + 530*m.b146*m.b109 + 260*m.b147*m.b109 + 620*m.b148*
                          m.b109 + 180*m.b149*m.b109 + 710*m.b150*m.b109 + 140*m.b151*m.b109 + 970*m.b152*m.b109 + 820*
                          m.b153*m.b109 + 540*m.b154*m.b109 + 90*m.b155*m.b109 + 920*m.b156*m.b109 + 550*m.b134*m.b122
                           + 870*m.b146*m.b122 + 690*m.b147*m.b122 + 20*m.b148*m.b122 + 320*m.b149*m.b122 + 420*m.b150*
                          m.b122 + 140*m.b151*m.b122 + 450*m.b152*m.b122 + 600*m.b153*m.b122 + 670*m.b154*m.b122 + 20*
                          m.b155*m.b122 + 420*m.b156*m.b122 + 640*m.b146*m.b134 + 820*m.b147*m.b134 + 580*m.b148*m.b134
                           + 980*m.b149*m.b134 + 360*m.b150*m.b134 + 920*m.b151*m.b134 + 30*m.b152*m.b134 + 620*m.b153*
                          m.b134 + 540*m.b154*m.b134 + 210*m.b155*m.b134 + 850*m.b156*m.b134 + 840*m.b147*m.b146 + 980*
                          m.b148*m.b146 + 270*m.b149*m.b146 + 810*m.b150*m.b146 + 590*m.b151*m.b146 + 470*m.b152*m.b146
                           + 830*m.b153*m.b146 + 530*m.b154*m.b146 + 800*m.b155*m.b146 + 350*m.b148*m.b147 + 900*m.b149*
                          m.b147 + 980*m.b150*m.b147 + 710*m.b151*m.b147 + 830*m.b152*m.b147 + 540*m.b153*m.b147 + 860*
                          m.b154*m.b147 + 890*m.b155*m.b147 + 270*m.b156*m.b147 + 710*m.b149*m.b148 + 100*m.b150*m.b148
                           + 980*m.b151*m.b148 + 910*m.b152*m.b148 + 860*m.b153*m.b148 + 300*m.b154*m.b148 + 550*m.b155*
                          m.b148 + 200*m.b156*m.b148 + 400*m.b150*m.b149 + 70*m.b151*m.b149 + 760*m.b152*m.b149 + 530*
                          m.b153*m.b149 + 910*m.b154*m.b149 + 750*m.b155*m.b149 + 330*m.b156*m.b149 + 720*m.b151*m.b150
                           + 340*m.b152*m.b150 + 320*m.b153*m.b150 + 70*m.b154*m.b150 + 870*m.b155*m.b150 + 640*m.b156*
                          m.b150 + 70*m.b152*m.b151 + 740*m.b153*m.b151 + 540*m.b154*m.b151 + 580*m.b155*m.b151 + 970*
                          m.b156*m.b151 + 890*m.b153*m.b152 + 120*m.b154*m.b152 + 830*m.b155*m.b152 + 790*m.b156*m.b152
                           + 390*m.b154*m.b153 + 70*m.b155*m.b153 + 890*m.b156*m.b153 + 890*m.b155*m.b154 + 980*m.b156*
                          m.b154 + 270*m.b156*m.b155 >= 67751)

m.c4002 = Constraint(expr=750*m.b30*m.b11 + 390*m.b48*m.b11 + 260*m.b65*m.b11 + 20*m.b81*m.b11 + 940*m.b96*m.b11 + 760*
                          m.b110*m.b11 + 550*m.b123*m.b11 + 800*m.b135*m.b11 + 580*m.b146*m.b11 + 200*m.b157*m.b11 + 880
                          *m.b158*m.b11 + 600*m.b159*m.b11 + 170*m.b160*m.b11 + 850*m.b161*m.b11 + 710*m.b162*m.b11 + 
                          970*m.b163*m.b11 + 830*m.b164*m.b11 + 990*m.b165*m.b11 + 640*m.b211*m.b11 + 970*m.b48*m.b30 + 
                          680*m.b65*m.b30 + 410*m.b81*m.b30 + 630*m.b96*m.b30 + 670*m.b110*m.b30 + 310*m.b123*m.b30 + 
                          210*m.b135*m.b30 + 710*m.b146*m.b30 + 530*m.b157*m.b30 + 500*m.b158*m.b30 + 630*m.b159*m.b30
                           + 920*m.b160*m.b30 + 290*m.b161*m.b30 + 180*m.b162*m.b30 + 860*m.b163*m.b30 + 570*m.b164*
                          m.b30 + 730*m.b165*m.b30 + 180*m.b211*m.b30 + 150*m.b65*m.b48 + 590*m.b81*m.b48 + 390*m.b96*
                          m.b48 + 30*m.b110*m.b48 + 190*m.b123*m.b48 + 80*m.b135*m.b48 + 880*m.b146*m.b48 + 570*m.b157*
                          m.b48 + 230*m.b158*m.b48 + 940*m.b159*m.b48 + 210*m.b160*m.b48 + 720*m.b161*m.b48 + 140*m.b162
                          *m.b48 + 140*m.b163*m.b48 + 870*m.b164*m.b48 + 330*m.b165*m.b48 + 460*m.b211*m.b48 + 80*m.b81*
                          m.b65 + 40*m.b96*m.b65 + 340*m.b110*m.b65 + 620*m.b123*m.b65 + 550*m.b135*m.b65 + 490*m.b146*
                          m.b65 + 360*m.b157*m.b65 + 670*m.b158*m.b65 + 450*m.b159*m.b65 + 930*m.b160*m.b65 + 930*m.b161
                          *m.b65 + 630*m.b162*m.b65 + 80*m.b163*m.b65 + 520*m.b164*m.b65 + 540*m.b165*m.b65 + 640*m.b211
                          *m.b65 + 240*m.b96*m.b81 + 140*m.b110*m.b81 + 40*m.b123*m.b81 + 190*m.b135*m.b81 + 710*m.b146*
                          m.b81 + 130*m.b157*m.b81 + 450*m.b158*m.b81 + 520*m.b159*m.b81 + 790*m.b160*m.b81 + 110*m.b161
                          *m.b81 + 400*m.b162*m.b81 + 120*m.b163*m.b81 + 570*m.b164*m.b81 + 480*m.b165*m.b81 + 170*
                          m.b211*m.b81 + 430*m.b110*m.b96 + 620*m.b123*m.b96 + 240*m.b135*m.b96 + 450*m.b146*m.b96 + 600
                          *m.b157*m.b96 + 120*m.b158*m.b96 + 660*m.b159*m.b96 + 530*m.b160*m.b96 + 50*m.b161*m.b96 + 810
                          *m.b162*m.b96 + 610*m.b163*m.b96 + 100*m.b164*m.b96 + 880*m.b165*m.b96 + 770*m.b211*m.b96 + 
                          340*m.b123*m.b110 + 20*m.b135*m.b110 + 820*m.b146*m.b110 + 260*m.b157*m.b110 + 620*m.b158*
                          m.b110 + 180*m.b159*m.b110 + 710*m.b160*m.b110 + 140*m.b161*m.b110 + 970*m.b162*m.b110 + 820*
                          m.b163*m.b110 + 540*m.b164*m.b110 + 90*m.b165*m.b110 + 920*m.b211*m.b110 + 550*m.b135*m.b123
                           + 780*m.b146*m.b123 + 690*m.b157*m.b123 + 20*m.b158*m.b123 + 320*m.b159*m.b123 + 420*m.b160*
                          m.b123 + 140*m.b161*m.b123 + 450*m.b162*m.b123 + 600*m.b163*m.b123 + 670*m.b164*m.b123 + 20*
                          m.b165*m.b123 + 420*m.b211*m.b123 + 810*m.b146*m.b135 + 820*m.b157*m.b135 + 580*m.b158*m.b135
                           + 980*m.b159*m.b135 + 360*m.b160*m.b135 + 920*m.b161*m.b135 + 30*m.b162*m.b135 + 620*m.b163*
                          m.b135 + 540*m.b164*m.b135 + 210*m.b165*m.b135 + 850*m.b211*m.b135 + 700*m.b157*m.b146 + 200*
                          m.b158*m.b146 + 750*m.b159*m.b146 + 800*m.b160*m.b146 + 120*m.b161*m.b146 + 820*m.b162*m.b146
                           + 100*m.b163*m.b146 + 990*m.b164*m.b146 + 40*m.b165*m.b146 + 130*m.b211*m.b146 + 350*m.b158*
                          m.b157 + 900*m.b159*m.b157 + 980*m.b160*m.b157 + 710*m.b161*m.b157 + 830*m.b162*m.b157 + 540*
                          m.b163*m.b157 + 860*m.b164*m.b157 + 890*m.b165*m.b157 + 270*m.b211*m.b157 + 710*m.b159*m.b158
                           + 100*m.b160*m.b158 + 980*m.b161*m.b158 + 910*m.b162*m.b158 + 860*m.b163*m.b158 + 300*m.b164*
                          m.b158 + 550*m.b165*m.b158 + 200*m.b211*m.b158 + 400*m.b160*m.b159 + 70*m.b161*m.b159 + 760*
                          m.b162*m.b159 + 530*m.b163*m.b159 + 910*m.b164*m.b159 + 750*m.b165*m.b159 + 330*m.b211*m.b159
                           + 720*m.b161*m.b160 + 340*m.b162*m.b160 + 320*m.b163*m.b160 + 70*m.b164*m.b160 + 870*m.b165*
                          m.b160 + 640*m.b211*m.b160 + 70*m.b162*m.b161 + 740*m.b163*m.b161 + 540*m.b164*m.b161 + 580*
                          m.b165*m.b161 + 970*m.b211*m.b161 + 890*m.b163*m.b162 + 120*m.b164*m.b162 + 830*m.b165*m.b162
                           + 790*m.b211*m.b162 + 390*m.b164*m.b163 + 70*m.b165*m.b163 + 890*m.b211*m.b163 + 890*m.b165*
                          m.b164 + 980*m.b211*m.b164 + 270*m.b211*m.b165 >= 67751)

m.c4003 = Constraint(expr=750*m.b31*m.b12 + 390*m.b49*m.b12 + 260*m.b66*m.b12 + 20*m.b82*m.b12 + 940*m.b97*m.b12 + 760*
                          m.b111*m.b12 + 550*m.b124*m.b12 + 800*m.b136*m.b12 + 580*m.b147*m.b12 + 340*m.b157*m.b12 + 880
                          *m.b166*m.b12 + 600*m.b167*m.b12 + 170*m.b168*m.b12 + 850*m.b169*m.b12 + 710*m.b170*m.b12 + 
                          970*m.b171*m.b12 + 830*m.b172*m.b12 + 990*m.b173*m.b12 + 640*m.b174*m.b12 + 970*m.b49*m.b31 + 
                          680*m.b66*m.b31 + 410*m.b82*m.b31 + 630*m.b97*m.b31 + 670*m.b111*m.b31 + 310*m.b124*m.b31 + 
                          210*m.b136*m.b31 + 710*m.b147*m.b31 + 880*m.b157*m.b31 + 500*m.b166*m.b31 + 630*m.b167*m.b31
                           + 920*m.b168*m.b31 + 290*m.b169*m.b31 + 180*m.b170*m.b31 + 860*m.b171*m.b31 + 570*m.b172*
                          m.b31 + 730*m.b173*m.b31 + 180*m.b174*m.b31 + 150*m.b66*m.b49 + 590*m.b82*m.b49 + 390*m.b97*
                          m.b49 + 30*m.b111*m.b49 + 190*m.b124*m.b49 + 80*m.b136*m.b49 + 880*m.b147*m.b49 + 430*m.b157*
                          m.b49 + 230*m.b166*m.b49 + 940*m.b167*m.b49 + 210*m.b168*m.b49 + 720*m.b169*m.b49 + 140*m.b170
                          *m.b49 + 140*m.b171*m.b49 + 870*m.b172*m.b49 + 330*m.b173*m.b49 + 460*m.b174*m.b49 + 80*m.b82*
                          m.b66 + 40*m.b97*m.b66 + 340*m.b111*m.b66 + 620*m.b124*m.b66 + 550*m.b136*m.b66 + 490*m.b147*
                          m.b66 + 60*m.b157*m.b66 + 670*m.b166*m.b66 + 450*m.b167*m.b66 + 930*m.b168*m.b66 + 930*m.b169*
                          m.b66 + 630*m.b170*m.b66 + 80*m.b171*m.b66 + 520*m.b172*m.b66 + 540*m.b173*m.b66 + 640*m.b174*
                          m.b66 + 240*m.b97*m.b82 + 140*m.b111*m.b82 + 40*m.b124*m.b82 + 190*m.b136*m.b82 + 710*m.b147*
                          m.b82 + 280*m.b157*m.b82 + 450*m.b166*m.b82 + 520*m.b167*m.b82 + 790*m.b168*m.b82 + 110*m.b169
                          *m.b82 + 400*m.b170*m.b82 + 120*m.b171*m.b82 + 570*m.b172*m.b82 + 480*m.b173*m.b82 + 170*
                          m.b174*m.b82 + 430*m.b111*m.b97 + 620*m.b124*m.b97 + 240*m.b136*m.b97 + 450*m.b147*m.b97 + 210
                          *m.b157*m.b97 + 120*m.b166*m.b97 + 660*m.b167*m.b97 + 530*m.b168*m.b97 + 50*m.b169*m.b97 + 810
                          *m.b170*m.b97 + 610*m.b171*m.b97 + 100*m.b172*m.b97 + 880*m.b173*m.b97 + 770*m.b174*m.b97 + 
                          340*m.b124*m.b111 + 20*m.b136*m.b111 + 820*m.b147*m.b111 + 530*m.b157*m.b111 + 620*m.b166*
                          m.b111 + 180*m.b167*m.b111 + 710*m.b168*m.b111 + 140*m.b169*m.b111 + 970*m.b170*m.b111 + 820*
                          m.b171*m.b111 + 540*m.b172*m.b111 + 90*m.b173*m.b111 + 920*m.b174*m.b111 + 550*m.b136*m.b124
                           + 780*m.b147*m.b124 + 870*m.b157*m.b124 + 20*m.b166*m.b124 + 320*m.b167*m.b124 + 420*m.b168*
                          m.b124 + 140*m.b169*m.b124 + 450*m.b170*m.b124 + 600*m.b171*m.b124 + 670*m.b172*m.b124 + 20*
                          m.b173*m.b124 + 420*m.b174*m.b124 + 810*m.b147*m.b136 + 640*m.b157*m.b136 + 580*m.b166*m.b136
                           + 980*m.b167*m.b136 + 360*m.b168*m.b136 + 920*m.b169*m.b136 + 30*m.b170*m.b136 + 620*m.b171*
                          m.b136 + 540*m.b172*m.b136 + 210*m.b173*m.b136 + 850*m.b174*m.b136 + 690*m.b157*m.b147 + 200*
                          m.b166*m.b147 + 750*m.b167*m.b147 + 800*m.b168*m.b147 + 120*m.b169*m.b147 + 820*m.b170*m.b147
                           + 100*m.b171*m.b147 + 990*m.b172*m.b147 + 40*m.b173*m.b147 + 130*m.b174*m.b147 + 980*m.b166*
                          m.b157 + 270*m.b167*m.b157 + 810*m.b168*m.b157 + 590*m.b169*m.b157 + 470*m.b170*m.b157 + 830*
                          m.b171*m.b157 + 530*m.b172*m.b157 + 800*m.b173*m.b157 + 710*m.b167*m.b166 + 100*m.b168*m.b166
                           + 980*m.b169*m.b166 + 910*m.b170*m.b166 + 860*m.b171*m.b166 + 300*m.b172*m.b166 + 550*m.b173*
                          m.b166 + 200*m.b174*m.b166 + 400*m.b168*m.b167 + 70*m.b169*m.b167 + 760*m.b170*m.b167 + 530*
                          m.b171*m.b167 + 910*m.b172*m.b167 + 750*m.b173*m.b167 + 330*m.b174*m.b167 + 720*m.b169*m.b168
                           + 340*m.b170*m.b168 + 320*m.b171*m.b168 + 70*m.b172*m.b168 + 870*m.b173*m.b168 + 640*m.b174*
                          m.b168 + 70*m.b170*m.b169 + 740*m.b171*m.b169 + 540*m.b172*m.b169 + 580*m.b173*m.b169 + 970*
                          m.b174*m.b169 + 890*m.b171*m.b170 + 120*m.b172*m.b170 + 830*m.b173*m.b170 + 790*m.b174*m.b170
                           + 390*m.b172*m.b171 + 70*m.b173*m.b171 + 890*m.b174*m.b171 + 890*m.b173*m.b172 + 980*m.b174*
                          m.b172 + 270*m.b174*m.b173 >= 67751)

m.c4004 = Constraint(expr=750*m.b32*m.b13 + 390*m.b50*m.b13 + 260*m.b67*m.b13 + 20*m.b83*m.b13 + 940*m.b98*m.b13 + 760*
                          m.b112*m.b13 + 550*m.b125*m.b13 + 800*m.b137*m.b13 + 580*m.b148*m.b13 + 340*m.b158*m.b13 + 200
                          *m.b166*m.b13 + 600*m.b175*m.b13 + 170*m.b176*m.b13 + 850*m.b177*m.b13 + 710*m.b178*m.b13 + 
                          970*m.b179*m.b13 + 830*m.b180*m.b13 + 990*m.b181*m.b13 + 640*m.b182*m.b13 + 970*m.b50*m.b32 + 
                          680*m.b67*m.b32 + 410*m.b83*m.b32 + 630*m.b98*m.b32 + 670*m.b112*m.b32 + 310*m.b125*m.b32 + 
                          210*m.b137*m.b32 + 710*m.b148*m.b32 + 880*m.b158*m.b32 + 530*m.b166*m.b32 + 630*m.b175*m.b32
                           + 920*m.b176*m.b32 + 290*m.b177*m.b32 + 180*m.b178*m.b32 + 860*m.b179*m.b32 + 570*m.b180*
                          m.b32 + 730*m.b181*m.b32 + 180*m.b182*m.b32 + 150*m.b67*m.b50 + 590*m.b83*m.b50 + 390*m.b98*
                          m.b50 + 30*m.b112*m.b50 + 190*m.b125*m.b50 + 80*m.b137*m.b50 + 880*m.b148*m.b50 + 430*m.b158*
                          m.b50 + 570*m.b166*m.b50 + 940*m.b175*m.b50 + 210*m.b176*m.b50 + 720*m.b177*m.b50 + 140*m.b178
                          *m.b50 + 140*m.b179*m.b50 + 870*m.b180*m.b50 + 330*m.b181*m.b50 + 460*m.b182*m.b50 + 80*m.b83*
                          m.b67 + 40*m.b98*m.b67 + 340*m.b112*m.b67 + 620*m.b125*m.b67 + 550*m.b137*m.b67 + 490*m.b148*
                          m.b67 + 60*m.b158*m.b67 + 360*m.b166*m.b67 + 450*m.b175*m.b67 + 930*m.b176*m.b67 + 930*m.b177*
                          m.b67 + 630*m.b178*m.b67 + 80*m.b179*m.b67 + 520*m.b180*m.b67 + 540*m.b181*m.b67 + 640*m.b182*
                          m.b67 + 240*m.b98*m.b83 + 140*m.b112*m.b83 + 40*m.b125*m.b83 + 190*m.b137*m.b83 + 710*m.b148*
                          m.b83 + 280*m.b158*m.b83 + 130*m.b166*m.b83 + 520*m.b175*m.b83 + 790*m.b176*m.b83 + 110*m.b177
                          *m.b83 + 400*m.b178*m.b83 + 120*m.b179*m.b83 + 570*m.b180*m.b83 + 480*m.b181*m.b83 + 170*
                          m.b182*m.b83 + 430*m.b112*m.b98 + 620*m.b125*m.b98 + 240*m.b137*m.b98 + 450*m.b148*m.b98 + 210
                          *m.b158*m.b98 + 600*m.b166*m.b98 + 660*m.b175*m.b98 + 530*m.b176*m.b98 + 50*m.b177*m.b98 + 810
                          *m.b178*m.b98 + 610*m.b179*m.b98 + 100*m.b180*m.b98 + 880*m.b181*m.b98 + 770*m.b182*m.b98 + 
                          340*m.b125*m.b112 + 20*m.b137*m.b112 + 820*m.b148*m.b112 + 530*m.b158*m.b112 + 260*m.b166*
                          m.b112 + 180*m.b175*m.b112 + 710*m.b176*m.b112 + 140*m.b177*m.b112 + 970*m.b178*m.b112 + 820*
                          m.b179*m.b112 + 540*m.b180*m.b112 + 90*m.b181*m.b112 + 920*m.b182*m.b112 + 550*m.b137*m.b125
                           + 780*m.b148*m.b125 + 870*m.b158*m.b125 + 690*m.b166*m.b125 + 320*m.b175*m.b125 + 420*m.b176*
                          m.b125 + 140*m.b177*m.b125 + 450*m.b178*m.b125 + 600*m.b179*m.b125 + 670*m.b180*m.b125 + 20*
                          m.b181*m.b125 + 420*m.b182*m.b125 + 810*m.b148*m.b137 + 640*m.b158*m.b137 + 820*m.b166*m.b137
                           + 980*m.b175*m.b137 + 360*m.b176*m.b137 + 920*m.b177*m.b137 + 30*m.b178*m.b137 + 620*m.b179*
                          m.b137 + 540*m.b180*m.b137 + 210*m.b181*m.b137 + 850*m.b182*m.b137 + 690*m.b158*m.b148 + 700*
                          m.b166*m.b148 + 750*m.b175*m.b148 + 800*m.b176*m.b148 + 120*m.b177*m.b148 + 820*m.b178*m.b148
                           + 100*m.b179*m.b148 + 990*m.b180*m.b148 + 40*m.b181*m.b148 + 130*m.b182*m.b148 + 840*m.b166*
                          m.b158 + 270*m.b175*m.b158 + 810*m.b176*m.b158 + 590*m.b177*m.b158 + 470*m.b178*m.b158 + 830*
                          m.b179*m.b158 + 530*m.b180*m.b158 + 800*m.b181*m.b158 + 900*m.b175*m.b166 + 980*m.b176*m.b166
                           + 710*m.b177*m.b166 + 830*m.b178*m.b166 + 540*m.b179*m.b166 + 860*m.b180*m.b166 + 890*m.b181*
                          m.b166 + 270*m.b182*m.b166 + 400*m.b176*m.b175 + 70*m.b177*m.b175 + 760*m.b178*m.b175 + 530*
                          m.b179*m.b175 + 910*m.b180*m.b175 + 750*m.b181*m.b175 + 330*m.b182*m.b175 + 720*m.b177*m.b176
                           + 340*m.b178*m.b176 + 320*m.b179*m.b176 + 70*m.b180*m.b176 + 870*m.b181*m.b176 + 640*m.b182*
                          m.b176 + 70*m.b178*m.b177 + 740*m.b179*m.b177 + 540*m.b180*m.b177 + 580*m.b181*m.b177 + 970*
                          m.b182*m.b177 + 890*m.b179*m.b178 + 120*m.b180*m.b178 + 830*m.b181*m.b178 + 790*m.b182*m.b178
                           + 390*m.b180*m.b179 + 70*m.b181*m.b179 + 890*m.b182*m.b179 + 890*m.b181*m.b180 + 980*m.b182*
                          m.b180 + 270*m.b182*m.b181 >= 67751)

m.c4005 = Constraint(expr=750*m.b33*m.b14 + 390*m.b51*m.b14 + 260*m.b68*m.b14 + 20*m.b84*m.b14 + 940*m.b99*m.b14 + 760*
                          m.b113*m.b14 + 550*m.b126*m.b14 + 800*m.b138*m.b14 + 580*m.b149*m.b14 + 340*m.b159*m.b14 + 200
                          *m.b167*m.b14 + 880*m.b175*m.b14 + 170*m.b183*m.b14 + 850*m.b184*m.b14 + 710*m.b185*m.b14 + 
                          970*m.b186*m.b14 + 830*m.b187*m.b14 + 990*m.b188*m.b14 + 640*m.b189*m.b14 + 970*m.b51*m.b33 + 
                          680*m.b68*m.b33 + 410*m.b84*m.b33 + 630*m.b99*m.b33 + 670*m.b113*m.b33 + 310*m.b126*m.b33 + 
                          210*m.b138*m.b33 + 710*m.b149*m.b33 + 880*m.b159*m.b33 + 530*m.b167*m.b33 + 500*m.b175*m.b33
                           + 920*m.b183*m.b33 + 290*m.b184*m.b33 + 180*m.b185*m.b33 + 860*m.b186*m.b33 + 570*m.b187*
                          m.b33 + 730*m.b188*m.b33 + 180*m.b189*m.b33 + 150*m.b68*m.b51 + 590*m.b84*m.b51 + 390*m.b99*
                          m.b51 + 30*m.b113*m.b51 + 190*m.b126*m.b51 + 80*m.b138*m.b51 + 880*m.b149*m.b51 + 430*m.b159*
                          m.b51 + 570*m.b167*m.b51 + 230*m.b175*m.b51 + 210*m.b183*m.b51 + 720*m.b184*m.b51 + 140*m.b185
                          *m.b51 + 140*m.b186*m.b51 + 870*m.b187*m.b51 + 330*m.b188*m.b51 + 460*m.b189*m.b51 + 80*m.b84*
                          m.b68 + 40*m.b99*m.b68 + 340*m.b113*m.b68 + 620*m.b126*m.b68 + 550*m.b138*m.b68 + 490*m.b149*
                          m.b68 + 60*m.b159*m.b68 + 360*m.b167*m.b68 + 670*m.b175*m.b68 + 930*m.b183*m.b68 + 930*m.b184*
                          m.b68 + 630*m.b185*m.b68 + 80*m.b186*m.b68 + 520*m.b187*m.b68 + 540*m.b188*m.b68 + 640*m.b189*
                          m.b68 + 240*m.b99*m.b84 + 140*m.b113*m.b84 + 40*m.b126*m.b84 + 190*m.b138*m.b84 + 710*m.b149*
                          m.b84 + 280*m.b159*m.b84 + 130*m.b167*m.b84 + 450*m.b175*m.b84 + 790*m.b183*m.b84 + 110*m.b184
                          *m.b84 + 400*m.b185*m.b84 + 120*m.b186*m.b84 + 570*m.b187*m.b84 + 480*m.b188*m.b84 + 170*
                          m.b189*m.b84 + 430*m.b113*m.b99 + 620*m.b126*m.b99 + 240*m.b138*m.b99 + 450*m.b149*m.b99 + 210
                          *m.b159*m.b99 + 600*m.b167*m.b99 + 120*m.b175*m.b99 + 530*m.b183*m.b99 + 50*m.b184*m.b99 + 810
                          *m.b185*m.b99 + 610*m.b186*m.b99 + 100*m.b187*m.b99 + 880*m.b188*m.b99 + 770*m.b189*m.b99 + 
                          340*m.b126*m.b113 + 20*m.b138*m.b113 + 820*m.b149*m.b113 + 530*m.b159*m.b113 + 260*m.b167*
                          m.b113 + 620*m.b175*m.b113 + 710*m.b183*m.b113 + 140*m.b184*m.b113 + 970*m.b185*m.b113 + 820*
                          m.b186*m.b113 + 540*m.b187*m.b113 + 90*m.b188*m.b113 + 920*m.b189*m.b113 + 550*m.b138*m.b126
                           + 780*m.b149*m.b126 + 870*m.b159*m.b126 + 690*m.b167*m.b126 + 20*m.b175*m.b126 + 420*m.b183*
                          m.b126 + 140*m.b184*m.b126 + 450*m.b185*m.b126 + 600*m.b186*m.b126 + 670*m.b187*m.b126 + 20*
                          m.b188*m.b126 + 420*m.b189*m.b126 + 810*m.b149*m.b138 + 640*m.b159*m.b138 + 820*m.b167*m.b138
                           + 580*m.b175*m.b138 + 360*m.b183*m.b138 + 920*m.b184*m.b138 + 30*m.b185*m.b138 + 620*m.b186*
                          m.b138 + 540*m.b187*m.b138 + 210*m.b188*m.b138 + 850*m.b189*m.b138 + 690*m.b159*m.b149 + 700*
                          m.b167*m.b149 + 200*m.b175*m.b149 + 800*m.b183*m.b149 + 120*m.b184*m.b149 + 820*m.b185*m.b149
                           + 100*m.b186*m.b149 + 990*m.b187*m.b149 + 40*m.b188*m.b149 + 130*m.b189*m.b149 + 840*m.b167*
                          m.b159 + 980*m.b175*m.b159 + 810*m.b183*m.b159 + 590*m.b184*m.b159 + 470*m.b185*m.b159 + 830*
                          m.b186*m.b159 + 530*m.b187*m.b159 + 800*m.b188*m.b159 + 350*m.b175*m.b167 + 980*m.b183*m.b167
                           + 710*m.b184*m.b167 + 830*m.b185*m.b167 + 540*m.b186*m.b167 + 860*m.b187*m.b167 + 890*m.b188*
                          m.b167 + 270*m.b189*m.b167 + 100*m.b183*m.b175 + 980*m.b184*m.b175 + 910*m.b185*m.b175 + 860*
                          m.b186*m.b175 + 300*m.b187*m.b175 + 550*m.b188*m.b175 + 200*m.b189*m.b175 + 720*m.b184*m.b183
                           + 340*m.b185*m.b183 + 320*m.b186*m.b183 + 70*m.b187*m.b183 + 870*m.b188*m.b183 + 640*m.b189*
                          m.b183 + 70*m.b185*m.b184 + 740*m.b186*m.b184 + 540*m.b187*m.b184 + 580*m.b188*m.b184 + 970*
                          m.b189*m.b184 + 890*m.b186*m.b185 + 120*m.b187*m.b185 + 830*m.b188*m.b185 + 790*m.b189*m.b185
                           + 390*m.b187*m.b186 + 70*m.b188*m.b186 + 890*m.b189*m.b186 + 890*m.b188*m.b187 + 980*m.b189*
                          m.b187 + 270*m.b189*m.b188 >= 67751)

m.c4006 = Constraint(expr=750*m.b34*m.b15 + 390*m.b52*m.b15 + 260*m.b69*m.b15 + 20*m.b85*m.b15 + 940*m.b100*m.b15 + 760*
                          m.b114*m.b15 + 550*m.b127*m.b15 + 800*m.b139*m.b15 + 580*m.b150*m.b15 + 340*m.b160*m.b15 + 200
                          *m.b168*m.b15 + 880*m.b176*m.b15 + 600*m.b183*m.b15 + 850*m.b190*m.b15 + 710*m.b191*m.b15 + 
                          970*m.b192*m.b15 + 830*m.b193*m.b15 + 990*m.b194*m.b15 + 640*m.b195*m.b15 + 970*m.b52*m.b34 + 
                          680*m.b69*m.b34 + 410*m.b85*m.b34 + 630*m.b100*m.b34 + 670*m.b114*m.b34 + 310*m.b127*m.b34 + 
                          210*m.b139*m.b34 + 710*m.b150*m.b34 + 880*m.b160*m.b34 + 530*m.b168*m.b34 + 500*m.b176*m.b34
                           + 630*m.b183*m.b34 + 290*m.b190*m.b34 + 180*m.b191*m.b34 + 860*m.b192*m.b34 + 570*m.b193*
                          m.b34 + 730*m.b194*m.b34 + 180*m.b195*m.b34 + 150*m.b69*m.b52 + 590*m.b85*m.b52 + 390*m.b100*
                          m.b52 + 30*m.b114*m.b52 + 190*m.b127*m.b52 + 80*m.b139*m.b52 + 880*m.b150*m.b52 + 430*m.b160*
                          m.b52 + 570*m.b168*m.b52 + 230*m.b176*m.b52 + 940*m.b183*m.b52 + 720*m.b190*m.b52 + 140*m.b191
                          *m.b52 + 140*m.b192*m.b52 + 870*m.b193*m.b52 + 330*m.b194*m.b52 + 460*m.b195*m.b52 + 80*m.b85*
                          m.b69 + 40*m.b100*m.b69 + 340*m.b114*m.b69 + 620*m.b127*m.b69 + 550*m.b139*m.b69 + 490*m.b150*
                          m.b69 + 60*m.b160*m.b69 + 360*m.b168*m.b69 + 670*m.b176*m.b69 + 450*m.b183*m.b69 + 930*m.b190*
                          m.b69 + 630*m.b191*m.b69 + 80*m.b192*m.b69 + 520*m.b193*m.b69 + 540*m.b194*m.b69 + 640*m.b195*
                          m.b69 + 240*m.b100*m.b85 + 140*m.b114*m.b85 + 40*m.b127*m.b85 + 190*m.b139*m.b85 + 710*m.b150*
                          m.b85 + 280*m.b160*m.b85 + 130*m.b168*m.b85 + 450*m.b176*m.b85 + 520*m.b183*m.b85 + 110*m.b190
                          *m.b85 + 400*m.b191*m.b85 + 120*m.b192*m.b85 + 570*m.b193*m.b85 + 480*m.b194*m.b85 + 170*
                          m.b195*m.b85 + 430*m.b114*m.b100 + 620*m.b127*m.b100 + 240*m.b139*m.b100 + 450*m.b150*m.b100
                           + 210*m.b160*m.b100 + 600*m.b168*m.b100 + 120*m.b176*m.b100 + 660*m.b183*m.b100 + 50*m.b190*
                          m.b100 + 810*m.b191*m.b100 + 610*m.b192*m.b100 + 100*m.b193*m.b100 + 880*m.b194*m.b100 + 770*
                          m.b195*m.b100 + 340*m.b127*m.b114 + 20*m.b139*m.b114 + 820*m.b150*m.b114 + 530*m.b160*m.b114
                           + 260*m.b168*m.b114 + 620*m.b176*m.b114 + 180*m.b183*m.b114 + 140*m.b190*m.b114 + 970*m.b191*
                          m.b114 + 820*m.b192*m.b114 + 540*m.b193*m.b114 + 90*m.b194*m.b114 + 920*m.b195*m.b114 + 550*
                          m.b139*m.b127 + 780*m.b150*m.b127 + 870*m.b160*m.b127 + 690*m.b168*m.b127 + 20*m.b176*m.b127
                           + 320*m.b183*m.b127 + 140*m.b190*m.b127 + 450*m.b191*m.b127 + 600*m.b192*m.b127 + 670*m.b193*
                          m.b127 + 20*m.b194*m.b127 + 420*m.b195*m.b127 + 810*m.b150*m.b139 + 640*m.b160*m.b139 + 820*
                          m.b168*m.b139 + 580*m.b176*m.b139 + 980*m.b183*m.b139 + 920*m.b190*m.b139 + 30*m.b191*m.b139
                           + 620*m.b192*m.b139 + 540*m.b193*m.b139 + 210*m.b194*m.b139 + 850*m.b195*m.b139 + 690*m.b160*
                          m.b150 + 700*m.b168*m.b150 + 200*m.b176*m.b150 + 750*m.b183*m.b150 + 120*m.b190*m.b150 + 820*
                          m.b191*m.b150 + 100*m.b192*m.b150 + 990*m.b193*m.b150 + 40*m.b194*m.b150 + 130*m.b195*m.b150
                           + 840*m.b168*m.b160 + 980*m.b176*m.b160 + 270*m.b183*m.b160 + 590*m.b190*m.b160 + 470*m.b191*
                          m.b160 + 830*m.b192*m.b160 + 530*m.b193*m.b160 + 800*m.b194*m.b160 + 350*m.b176*m.b168 + 900*
                          m.b183*m.b168 + 710*m.b190*m.b168 + 830*m.b191*m.b168 + 540*m.b192*m.b168 + 860*m.b193*m.b168
                           + 890*m.b194*m.b168 + 270*m.b195*m.b168 + 710*m.b183*m.b176 + 980*m.b190*m.b176 + 910*m.b191*
                          m.b176 + 860*m.b192*m.b176 + 300*m.b193*m.b176 + 550*m.b194*m.b176 + 200*m.b195*m.b176 + 70*
                          m.b190*m.b183 + 760*m.b191*m.b183 + 530*m.b192*m.b183 + 910*m.b193*m.b183 + 750*m.b194*m.b183
                           + 330*m.b195*m.b183 + 70*m.b191*m.b190 + 740*m.b192*m.b190 + 540*m.b193*m.b190 + 580*m.b194*
                          m.b190 + 970*m.b195*m.b190 + 890*m.b192*m.b191 + 120*m.b193*m.b191 + 830*m.b194*m.b191 + 790*
                          m.b195*m.b191 + 390*m.b193*m.b192 + 70*m.b194*m.b192 + 890*m.b195*m.b192 + 890*m.b194*m.b193
                           + 980*m.b195*m.b193 + 270*m.b195*m.b194 >= 67751)

m.c4007 = Constraint(expr=750*m.b35*m.b16 + 390*m.b53*m.b16 + 260*m.b70*m.b16 + 20*m.b86*m.b16 + 940*m.b101*m.b16 + 760*
                          m.b115*m.b16 + 550*m.b128*m.b16 + 800*m.b140*m.b16 + 580*m.b151*m.b16 + 340*m.b161*m.b16 + 200
                          *m.b169*m.b16 + 880*m.b177*m.b16 + 600*m.b184*m.b16 + 170*m.b190*m.b16 + 710*m.b196*m.b16 + 
                          970*m.b197*m.b16 + 830*m.b198*m.b16 + 990*m.b199*m.b16 + 640*m.b200*m.b16 + 970*m.b53*m.b35 + 
                          680*m.b70*m.b35 + 410*m.b86*m.b35 + 630*m.b101*m.b35 + 670*m.b115*m.b35 + 310*m.b128*m.b35 + 
                          210*m.b140*m.b35 + 710*m.b151*m.b35 + 880*m.b161*m.b35 + 530*m.b169*m.b35 + 500*m.b177*m.b35
                           + 630*m.b184*m.b35 + 920*m.b190*m.b35 + 180*m.b196*m.b35 + 860*m.b197*m.b35 + 570*m.b198*
                          m.b35 + 730*m.b199*m.b35 + 180*m.b200*m.b35 + 150*m.b70*m.b53 + 590*m.b86*m.b53 + 390*m.b101*
                          m.b53 + 30*m.b115*m.b53 + 190*m.b128*m.b53 + 80*m.b140*m.b53 + 880*m.b151*m.b53 + 430*m.b161*
                          m.b53 + 570*m.b169*m.b53 + 230*m.b177*m.b53 + 940*m.b184*m.b53 + 210*m.b190*m.b53 + 140*m.b196
                          *m.b53 + 140*m.b197*m.b53 + 870*m.b198*m.b53 + 330*m.b199*m.b53 + 460*m.b200*m.b53 + 80*m.b86*
                          m.b70 + 40*m.b101*m.b70 + 340*m.b115*m.b70 + 620*m.b128*m.b70 + 550*m.b140*m.b70 + 490*m.b151*
                          m.b70 + 60*m.b161*m.b70 + 360*m.b169*m.b70 + 670*m.b177*m.b70 + 450*m.b184*m.b70 + 930*m.b190*
                          m.b70 + 630*m.b196*m.b70 + 80*m.b197*m.b70 + 520*m.b198*m.b70 + 540*m.b199*m.b70 + 640*m.b200*
                          m.b70 + 240*m.b101*m.b86 + 140*m.b115*m.b86 + 40*m.b128*m.b86 + 190*m.b140*m.b86 + 710*m.b151*
                          m.b86 + 280*m.b161*m.b86 + 130*m.b169*m.b86 + 450*m.b177*m.b86 + 520*m.b184*m.b86 + 790*m.b190
                          *m.b86 + 400*m.b196*m.b86 + 120*m.b197*m.b86 + 570*m.b198*m.b86 + 480*m.b199*m.b86 + 170*
                          m.b200*m.b86 + 430*m.b115*m.b101 + 620*m.b128*m.b101 + 240*m.b140*m.b101 + 450*m.b151*m.b101
                           + 210*m.b161*m.b101 + 600*m.b169*m.b101 + 120*m.b177*m.b101 + 660*m.b184*m.b101 + 530*m.b190*
                          m.b101 + 810*m.b196*m.b101 + 610*m.b197*m.b101 + 100*m.b198*m.b101 + 880*m.b199*m.b101 + 770*
                          m.b200*m.b101 + 340*m.b128*m.b115 + 20*m.b140*m.b115 + 820*m.b151*m.b115 + 530*m.b161*m.b115
                           + 260*m.b169*m.b115 + 620*m.b177*m.b115 + 180*m.b184*m.b115 + 710*m.b190*m.b115 + 970*m.b196*
                          m.b115 + 820*m.b197*m.b115 + 540*m.b198*m.b115 + 90*m.b199*m.b115 + 920*m.b200*m.b115 + 550*
                          m.b140*m.b128 + 780*m.b151*m.b128 + 870*m.b161*m.b128 + 690*m.b169*m.b128 + 20*m.b177*m.b128
                           + 320*m.b184*m.b128 + 420*m.b190*m.b128 + 450*m.b196*m.b128 + 600*m.b197*m.b128 + 670*m.b198*
                          m.b128 + 20*m.b199*m.b128 + 420*m.b200*m.b128 + 810*m.b151*m.b140 + 640*m.b161*m.b140 + 820*
                          m.b169*m.b140 + 580*m.b177*m.b140 + 980*m.b184*m.b140 + 360*m.b190*m.b140 + 30*m.b196*m.b140
                           + 620*m.b197*m.b140 + 540*m.b198*m.b140 + 210*m.b199*m.b140 + 850*m.b200*m.b140 + 690*m.b161*
                          m.b151 + 700*m.b169*m.b151 + 200*m.b177*m.b151 + 750*m.b184*m.b151 + 800*m.b190*m.b151 + 820*
                          m.b196*m.b151 + 100*m.b197*m.b151 + 990*m.b198*m.b151 + 40*m.b199*m.b151 + 130*m.b200*m.b151
                           + 840*m.b169*m.b161 + 980*m.b177*m.b161 + 270*m.b184*m.b161 + 810*m.b190*m.b161 + 470*m.b196*
                          m.b161 + 830*m.b197*m.b161 + 530*m.b198*m.b161 + 800*m.b199*m.b161 + 350*m.b177*m.b169 + 900*
                          m.b184*m.b169 + 980*m.b190*m.b169 + 830*m.b196*m.b169 + 540*m.b197*m.b169 + 860*m.b198*m.b169
                           + 890*m.b199*m.b169 + 270*m.b200*m.b169 + 710*m.b184*m.b177 + 100*m.b190*m.b177 + 910*m.b196*
                          m.b177 + 860*m.b197*m.b177 + 300*m.b198*m.b177 + 550*m.b199*m.b177 + 200*m.b200*m.b177 + 400*
                          m.b190*m.b184 + 760*m.b196*m.b184 + 530*m.b197*m.b184 + 910*m.b198*m.b184 + 750*m.b199*m.b184
                           + 330*m.b200*m.b184 + 340*m.b196*m.b190 + 320*m.b197*m.b190 + 70*m.b198*m.b190 + 870*m.b199*
                          m.b190 + 640*m.b200*m.b190 + 890*m.b197*m.b196 + 120*m.b198*m.b196 + 830*m.b199*m.b196 + 790*
                          m.b200*m.b196 + 390*m.b198*m.b197 + 70*m.b199*m.b197 + 890*m.b200*m.b197 + 890*m.b199*m.b198
                           + 980*m.b200*m.b198 + 270*m.b200*m.b199 >= 67751)

m.c4008 = Constraint(expr=750*m.b36*m.b17 + 390*m.b54*m.b17 + 260*m.b71*m.b17 + 20*m.b87*m.b17 + 940*m.b102*m.b17 + 760*
                          m.b116*m.b17 + 550*m.b129*m.b17 + 800*m.b141*m.b17 + 580*m.b152*m.b17 + 340*m.b162*m.b17 + 200
                          *m.b170*m.b17 + 880*m.b178*m.b17 + 600*m.b185*m.b17 + 170*m.b191*m.b17 + 850*m.b196*m.b17 + 
                          970*m.b201*m.b17 + 830*m.b202*m.b17 + 990*m.b203*m.b17 + 640*m.b204*m.b17 + 970*m.b54*m.b36 + 
                          680*m.b71*m.b36 + 410*m.b87*m.b36 + 630*m.b102*m.b36 + 670*m.b116*m.b36 + 310*m.b129*m.b36 + 
                          210*m.b141*m.b36 + 710*m.b152*m.b36 + 880*m.b162*m.b36 + 530*m.b170*m.b36 + 500*m.b178*m.b36
                           + 630*m.b185*m.b36 + 920*m.b191*m.b36 + 290*m.b196*m.b36 + 860*m.b201*m.b36 + 570*m.b202*
                          m.b36 + 730*m.b203*m.b36 + 180*m.b204*m.b36 + 150*m.b71*m.b54 + 590*m.b87*m.b54 + 390*m.b102*
                          m.b54 + 30*m.b116*m.b54 + 190*m.b129*m.b54 + 80*m.b141*m.b54 + 880*m.b152*m.b54 + 430*m.b162*
                          m.b54 + 570*m.b170*m.b54 + 230*m.b178*m.b54 + 940*m.b185*m.b54 + 210*m.b191*m.b54 + 720*m.b196
                          *m.b54 + 140*m.b201*m.b54 + 870*m.b202*m.b54 + 330*m.b203*m.b54 + 460*m.b204*m.b54 + 80*m.b87*
                          m.b71 + 40*m.b102*m.b71 + 340*m.b116*m.b71 + 620*m.b129*m.b71 + 550*m.b141*m.b71 + 490*m.b152*
                          m.b71 + 60*m.b162*m.b71 + 360*m.b170*m.b71 + 670*m.b178*m.b71 + 450*m.b185*m.b71 + 930*m.b191*
                          m.b71 + 930*m.b196*m.b71 + 80*m.b201*m.b71 + 520*m.b202*m.b71 + 540*m.b203*m.b71 + 640*m.b204*
                          m.b71 + 240*m.b102*m.b87 + 140*m.b116*m.b87 + 40*m.b129*m.b87 + 190*m.b141*m.b87 + 710*m.b152*
                          m.b87 + 280*m.b162*m.b87 + 130*m.b170*m.b87 + 450*m.b178*m.b87 + 520*m.b185*m.b87 + 790*m.b191
                          *m.b87 + 110*m.b196*m.b87 + 120*m.b201*m.b87 + 570*m.b202*m.b87 + 480*m.b203*m.b87 + 170*
                          m.b204*m.b87 + 430*m.b116*m.b102 + 620*m.b129*m.b102 + 240*m.b141*m.b102 + 450*m.b152*m.b102
                           + 210*m.b162*m.b102 + 600*m.b170*m.b102 + 120*m.b178*m.b102 + 660*m.b185*m.b102 + 530*m.b191*
                          m.b102 + 50*m.b196*m.b102 + 610*m.b201*m.b102 + 100*m.b202*m.b102 + 880*m.b203*m.b102 + 770*
                          m.b204*m.b102 + 340*m.b129*m.b116 + 20*m.b141*m.b116 + 820*m.b152*m.b116 + 530*m.b162*m.b116
                           + 260*m.b170*m.b116 + 620*m.b178*m.b116 + 180*m.b185*m.b116 + 710*m.b191*m.b116 + 140*m.b196*
                          m.b116 + 820*m.b201*m.b116 + 540*m.b202*m.b116 + 90*m.b203*m.b116 + 920*m.b204*m.b116 + 550*
                          m.b141*m.b129 + 780*m.b152*m.b129 + 870*m.b162*m.b129 + 690*m.b170*m.b129 + 20*m.b178*m.b129
                           + 320*m.b185*m.b129 + 420*m.b191*m.b129 + 140*m.b196*m.b129 + 600*m.b201*m.b129 + 670*m.b202*
                          m.b129 + 20*m.b203*m.b129 + 420*m.b204*m.b129 + 810*m.b152*m.b141 + 640*m.b162*m.b141 + 820*
                          m.b170*m.b141 + 580*m.b178*m.b141 + 980*m.b185*m.b141 + 360*m.b191*m.b141 + 920*m.b196*m.b141
                           + 620*m.b201*m.b141 + 540*m.b202*m.b141 + 210*m.b203*m.b141 + 850*m.b204*m.b141 + 690*m.b162*
                          m.b152 + 700*m.b170*m.b152 + 200*m.b178*m.b152 + 750*m.b185*m.b152 + 800*m.b191*m.b152 + 120*
                          m.b196*m.b152 + 100*m.b201*m.b152 + 990*m.b202*m.b152 + 40*m.b203*m.b152 + 130*m.b204*m.b152
                           + 840*m.b170*m.b162 + 980*m.b178*m.b162 + 270*m.b185*m.b162 + 810*m.b191*m.b162 + 590*m.b196*
                          m.b162 + 830*m.b201*m.b162 + 530*m.b202*m.b162 + 800*m.b203*m.b162 + 350*m.b178*m.b170 + 900*
                          m.b185*m.b170 + 980*m.b191*m.b170 + 710*m.b196*m.b170 + 540*m.b201*m.b170 + 860*m.b202*m.b170
                           + 890*m.b203*m.b170 + 270*m.b204*m.b170 + 710*m.b185*m.b178 + 100*m.b191*m.b178 + 980*m.b196*
                          m.b178 + 860*m.b201*m.b178 + 300*m.b202*m.b178 + 550*m.b203*m.b178 + 200*m.b204*m.b178 + 400*
                          m.b191*m.b185 + 70*m.b196*m.b185 + 530*m.b201*m.b185 + 910*m.b202*m.b185 + 750*m.b203*m.b185
                           + 330*m.b204*m.b185 + 720*m.b196*m.b191 + 320*m.b201*m.b191 + 70*m.b202*m.b191 + 870*m.b203*
                          m.b191 + 640*m.b204*m.b191 + 740*m.b201*m.b196 + 540*m.b202*m.b196 + 580*m.b203*m.b196 + 970*
                          m.b204*m.b196 + 390*m.b202*m.b201 + 70*m.b203*m.b201 + 890*m.b204*m.b201 + 890*m.b203*m.b202
                           + 980*m.b204*m.b202 + 270*m.b204*m.b203 >= 67751)

m.c4009 = Constraint(expr=750*m.b37*m.b18 + 390*m.b55*m.b18 + 260*m.b72*m.b18 + 20*m.b88*m.b18 + 940*m.b103*m.b18 + 760*
                          m.b117*m.b18 + 550*m.b130*m.b18 + 800*m.b142*m.b18 + 580*m.b153*m.b18 + 340*m.b163*m.b18 + 200
                          *m.b171*m.b18 + 880*m.b179*m.b18 + 600*m.b186*m.b18 + 170*m.b192*m.b18 + 850*m.b197*m.b18 + 
                          710*m.b201*m.b18 + 830*m.b205*m.b18 + 990*m.b206*m.b18 + 640*m.b207*m.b18 + 970*m.b55*m.b37 + 
                          680*m.b72*m.b37 + 410*m.b88*m.b37 + 630*m.b103*m.b37 + 670*m.b117*m.b37 + 310*m.b130*m.b37 + 
                          210*m.b142*m.b37 + 710*m.b153*m.b37 + 880*m.b163*m.b37 + 530*m.b171*m.b37 + 500*m.b179*m.b37
                           + 630*m.b186*m.b37 + 920*m.b192*m.b37 + 290*m.b197*m.b37 + 180*m.b201*m.b37 + 570*m.b205*
                          m.b37 + 730*m.b206*m.b37 + 180*m.b207*m.b37 + 150*m.b72*m.b55 + 590*m.b88*m.b55 + 390*m.b103*
                          m.b55 + 30*m.b117*m.b55 + 190*m.b130*m.b55 + 80*m.b142*m.b55 + 880*m.b153*m.b55 + 430*m.b163*
                          m.b55 + 570*m.b171*m.b55 + 230*m.b179*m.b55 + 940*m.b186*m.b55 + 210*m.b192*m.b55 + 720*m.b197
                          *m.b55 + 140*m.b201*m.b55 + 870*m.b205*m.b55 + 330*m.b206*m.b55 + 460*m.b207*m.b55 + 80*m.b88*
                          m.b72 + 40*m.b103*m.b72 + 340*m.b117*m.b72 + 620*m.b130*m.b72 + 550*m.b142*m.b72 + 490*m.b153*
                          m.b72 + 60*m.b163*m.b72 + 360*m.b171*m.b72 + 670*m.b179*m.b72 + 450*m.b186*m.b72 + 930*m.b192*
                          m.b72 + 930*m.b197*m.b72 + 630*m.b201*m.b72 + 520*m.b205*m.b72 + 540*m.b206*m.b72 + 640*m.b207
                          *m.b72 + 240*m.b103*m.b88 + 140*m.b117*m.b88 + 40*m.b130*m.b88 + 190*m.b142*m.b88 + 710*m.b153
                          *m.b88 + 280*m.b163*m.b88 + 130*m.b171*m.b88 + 450*m.b179*m.b88 + 520*m.b186*m.b88 + 790*
                          m.b192*m.b88 + 110*m.b197*m.b88 + 400*m.b201*m.b88 + 570*m.b205*m.b88 + 480*m.b206*m.b88 + 170
                          *m.b207*m.b88 + 430*m.b117*m.b103 + 620*m.b130*m.b103 + 240*m.b142*m.b103 + 450*m.b153*m.b103
                           + 210*m.b163*m.b103 + 600*m.b171*m.b103 + 120*m.b179*m.b103 + 660*m.b186*m.b103 + 530*m.b192*
                          m.b103 + 50*m.b197*m.b103 + 810*m.b201*m.b103 + 100*m.b205*m.b103 + 880*m.b206*m.b103 + 770*
                          m.b207*m.b103 + 340*m.b130*m.b117 + 20*m.b142*m.b117 + 820*m.b153*m.b117 + 530*m.b163*m.b117
                           + 260*m.b171*m.b117 + 620*m.b179*m.b117 + 180*m.b186*m.b117 + 710*m.b192*m.b117 + 140*m.b197*
                          m.b117 + 970*m.b201*m.b117 + 540*m.b205*m.b117 + 90*m.b206*m.b117 + 920*m.b207*m.b117 + 550*
                          m.b142*m.b130 + 780*m.b153*m.b130 + 870*m.b163*m.b130 + 690*m.b171*m.b130 + 20*m.b179*m.b130
                           + 320*m.b186*m.b130 + 420*m.b192*m.b130 + 140*m.b197*m.b130 + 450*m.b201*m.b130 + 670*m.b205*
                          m.b130 + 20*m.b206*m.b130 + 420*m.b207*m.b130 + 810*m.b153*m.b142 + 640*m.b163*m.b142 + 820*
                          m.b171*m.b142 + 580*m.b179*m.b142 + 980*m.b186*m.b142 + 360*m.b192*m.b142 + 920*m.b197*m.b142
                           + 30*m.b201*m.b142 + 540*m.b205*m.b142 + 210*m.b206*m.b142 + 850*m.b207*m.b142 + 690*m.b163*
                          m.b153 + 700*m.b171*m.b153 + 200*m.b179*m.b153 + 750*m.b186*m.b153 + 800*m.b192*m.b153 + 120*
                          m.b197*m.b153 + 820*m.b201*m.b153 + 990*m.b205*m.b153 + 40*m.b206*m.b153 + 130*m.b207*m.b153
                           + 840*m.b171*m.b163 + 980*m.b179*m.b163 + 270*m.b186*m.b163 + 810*m.b192*m.b163 + 590*m.b197*
                          m.b163 + 470*m.b201*m.b163 + 530*m.b205*m.b163 + 800*m.b206*m.b163 + 350*m.b179*m.b171 + 900*
                          m.b186*m.b171 + 980*m.b192*m.b171 + 710*m.b197*m.b171 + 830*m.b201*m.b171 + 860*m.b205*m.b171
                           + 890*m.b206*m.b171 + 270*m.b207*m.b171 + 710*m.b186*m.b179 + 100*m.b192*m.b179 + 980*m.b197*
                          m.b179 + 910*m.b201*m.b179 + 300*m.b205*m.b179 + 550*m.b206*m.b179 + 200*m.b207*m.b179 + 400*
                          m.b192*m.b186 + 70*m.b197*m.b186 + 760*m.b201*m.b186 + 910*m.b205*m.b186 + 750*m.b206*m.b186
                           + 330*m.b207*m.b186 + 720*m.b197*m.b192 + 340*m.b201*m.b192 + 70*m.b205*m.b192 + 870*m.b206*
                          m.b192 + 640*m.b207*m.b192 + 70*m.b201*m.b197 + 540*m.b205*m.b197 + 580*m.b206*m.b197 + 970*
                          m.b207*m.b197 + 120*m.b205*m.b201 + 830*m.b206*m.b201 + 790*m.b207*m.b201 + 890*m.b206*m.b205
                           + 980*m.b207*m.b205 + 270*m.b207*m.b206 >= 67751)

m.c4010 = Constraint(expr=750*m.b38*m.b19 + 390*m.b56*m.b19 + 260*m.b73*m.b19 + 20*m.b89*m.b19 + 940*m.b104*m.b19 + 760*
                          m.b118*m.b19 + 550*m.b131*m.b19 + 800*m.b143*m.b19 + 580*m.b154*m.b19 + 340*m.b164*m.b19 + 200
                          *m.b172*m.b19 + 880*m.b180*m.b19 + 600*m.b187*m.b19 + 170*m.b193*m.b19 + 850*m.b198*m.b19 + 
                          710*m.b202*m.b19 + 970*m.b205*m.b19 + 990*m.b208*m.b19 + 640*m.b209*m.b19 + 970*m.b56*m.b38 + 
                          680*m.b73*m.b38 + 410*m.b89*m.b38 + 630*m.b104*m.b38 + 670*m.b118*m.b38 + 310*m.b131*m.b38 + 
                          210*m.b143*m.b38 + 710*m.b154*m.b38 + 880*m.b164*m.b38 + 530*m.b172*m.b38 + 500*m.b180*m.b38
                           + 630*m.b187*m.b38 + 920*m.b193*m.b38 + 290*m.b198*m.b38 + 180*m.b202*m.b38 + 860*m.b205*
                          m.b38 + 730*m.b208*m.b38 + 180*m.b209*m.b38 + 150*m.b73*m.b56 + 590*m.b89*m.b56 + 390*m.b104*
                          m.b56 + 30*m.b118*m.b56 + 190*m.b131*m.b56 + 80*m.b143*m.b56 + 880*m.b154*m.b56 + 430*m.b164*
                          m.b56 + 570*m.b172*m.b56 + 230*m.b180*m.b56 + 940*m.b187*m.b56 + 210*m.b193*m.b56 + 720*m.b198
                          *m.b56 + 140*m.b202*m.b56 + 140*m.b205*m.b56 + 330*m.b208*m.b56 + 460*m.b209*m.b56 + 80*m.b89*
                          m.b73 + 40*m.b104*m.b73 + 340*m.b118*m.b73 + 620*m.b131*m.b73 + 550*m.b143*m.b73 + 490*m.b154*
                          m.b73 + 60*m.b164*m.b73 + 360*m.b172*m.b73 + 670*m.b180*m.b73 + 450*m.b187*m.b73 + 930*m.b193*
                          m.b73 + 930*m.b198*m.b73 + 630*m.b202*m.b73 + 80*m.b205*m.b73 + 540*m.b208*m.b73 + 640*m.b209*
                          m.b73 + 240*m.b104*m.b89 + 140*m.b118*m.b89 + 40*m.b131*m.b89 + 190*m.b143*m.b89 + 710*m.b154*
                          m.b89 + 280*m.b164*m.b89 + 130*m.b172*m.b89 + 450*m.b180*m.b89 + 520*m.b187*m.b89 + 790*m.b193
                          *m.b89 + 110*m.b198*m.b89 + 400*m.b202*m.b89 + 120*m.b205*m.b89 + 480*m.b208*m.b89 + 170*
                          m.b209*m.b89 + 430*m.b118*m.b104 + 620*m.b131*m.b104 + 240*m.b143*m.b104 + 450*m.b154*m.b104
                           + 210*m.b164*m.b104 + 600*m.b172*m.b104 + 120*m.b180*m.b104 + 660*m.b187*m.b104 + 530*m.b193*
                          m.b104 + 50*m.b198*m.b104 + 810*m.b202*m.b104 + 610*m.b205*m.b104 + 880*m.b208*m.b104 + 770*
                          m.b209*m.b104 + 340*m.b131*m.b118 + 20*m.b143*m.b118 + 820*m.b154*m.b118 + 530*m.b164*m.b118
                           + 260*m.b172*m.b118 + 620*m.b180*m.b118 + 180*m.b187*m.b118 + 710*m.b193*m.b118 + 140*m.b198*
                          m.b118 + 970*m.b202*m.b118 + 820*m.b205*m.b118 + 90*m.b208*m.b118 + 920*m.b209*m.b118 + 550*
                          m.b143*m.b131 + 780*m.b154*m.b131 + 870*m.b164*m.b131 + 690*m.b172*m.b131 + 20*m.b180*m.b131
                           + 320*m.b187*m.b131 + 420*m.b193*m.b131 + 140*m.b198*m.b131 + 450*m.b202*m.b131 + 600*m.b205*
                          m.b131 + 20*m.b208*m.b131 + 420*m.b209*m.b131 + 810*m.b154*m.b143 + 640*m.b164*m.b143 + 820*
                          m.b172*m.b143 + 580*m.b180*m.b143 + 980*m.b187*m.b143 + 360*m.b193*m.b143 + 920*m.b198*m.b143
                           + 30*m.b202*m.b143 + 620*m.b205*m.b143 + 210*m.b208*m.b143 + 850*m.b209*m.b143 + 690*m.b164*
                          m.b154 + 700*m.b172*m.b154 + 200*m.b180*m.b154 + 750*m.b187*m.b154 + 800*m.b193*m.b154 + 120*
                          m.b198*m.b154 + 820*m.b202*m.b154 + 100*m.b205*m.b154 + 40*m.b208*m.b154 + 130*m.b209*m.b154
                           + 840*m.b172*m.b164 + 980*m.b180*m.b164 + 270*m.b187*m.b164 + 810*m.b193*m.b164 + 590*m.b198*
                          m.b164 + 470*m.b202*m.b164 + 830*m.b205*m.b164 + 800*m.b208*m.b164 + 350*m.b180*m.b172 + 900*
                          m.b187*m.b172 + 980*m.b193*m.b172 + 710*m.b198*m.b172 + 830*m.b202*m.b172 + 540*m.b205*m.b172
                           + 890*m.b208*m.b172 + 270*m.b209*m.b172 + 710*m.b187*m.b180 + 100*m.b193*m.b180 + 980*m.b198*
                          m.b180 + 910*m.b202*m.b180 + 860*m.b205*m.b180 + 550*m.b208*m.b180 + 200*m.b209*m.b180 + 400*
                          m.b193*m.b187 + 70*m.b198*m.b187 + 760*m.b202*m.b187 + 530*m.b205*m.b187 + 750*m.b208*m.b187
                           + 330*m.b209*m.b187 + 720*m.b198*m.b193 + 340*m.b202*m.b193 + 320*m.b205*m.b193 + 870*m.b208*
                          m.b193 + 640*m.b209*m.b193 + 70*m.b202*m.b198 + 740*m.b205*m.b198 + 580*m.b208*m.b198 + 970*
                          m.b209*m.b198 + 890*m.b205*m.b202 + 830*m.b208*m.b202 + 790*m.b209*m.b202 + 70*m.b208*m.b205
                           + 890*m.b209*m.b205 + 270*m.b209*m.b208 >= 67751)

m.c4011 = Constraint(expr=750*m.b39*m.b20 + 390*m.b57*m.b20 + 260*m.b74*m.b20 + 20*m.b90*m.b20 + 940*m.b105*m.b20 + 760*
                          m.b119*m.b20 + 550*m.b132*m.b20 + 800*m.b144*m.b20 + 580*m.b155*m.b20 + 340*m.b165*m.b20 + 200
                          *m.b173*m.b20 + 880*m.b181*m.b20 + 600*m.b188*m.b20 + 170*m.b194*m.b20 + 850*m.b199*m.b20 + 
                          710*m.b203*m.b20 + 970*m.b206*m.b20 + 830*m.b208*m.b20 + 640*m.b210*m.b20 + 970*m.b57*m.b39 + 
                          680*m.b74*m.b39 + 410*m.b90*m.b39 + 630*m.b105*m.b39 + 670*m.b119*m.b39 + 310*m.b132*m.b39 + 
                          210*m.b144*m.b39 + 710*m.b155*m.b39 + 880*m.b165*m.b39 + 530*m.b173*m.b39 + 500*m.b181*m.b39
                           + 630*m.b188*m.b39 + 920*m.b194*m.b39 + 290*m.b199*m.b39 + 180*m.b203*m.b39 + 860*m.b206*
                          m.b39 + 570*m.b208*m.b39 + 180*m.b210*m.b39 + 150*m.b74*m.b57 + 590*m.b90*m.b57 + 390*m.b105*
                          m.b57 + 30*m.b119*m.b57 + 190*m.b132*m.b57 + 80*m.b144*m.b57 + 880*m.b155*m.b57 + 430*m.b165*
                          m.b57 + 570*m.b173*m.b57 + 230*m.b181*m.b57 + 940*m.b188*m.b57 + 210*m.b194*m.b57 + 720*m.b199
                          *m.b57 + 140*m.b203*m.b57 + 140*m.b206*m.b57 + 870*m.b208*m.b57 + 460*m.b210*m.b57 + 80*m.b90*
                          m.b74 + 40*m.b105*m.b74 + 340*m.b119*m.b74 + 620*m.b132*m.b74 + 550*m.b144*m.b74 + 490*m.b155*
                          m.b74 + 60*m.b165*m.b74 + 360*m.b173*m.b74 + 670*m.b181*m.b74 + 450*m.b188*m.b74 + 930*m.b194*
                          m.b74 + 930*m.b199*m.b74 + 630*m.b203*m.b74 + 80*m.b206*m.b74 + 520*m.b208*m.b74 + 640*m.b210*
                          m.b74 + 240*m.b105*m.b90 + 140*m.b119*m.b90 + 40*m.b132*m.b90 + 190*m.b144*m.b90 + 710*m.b155*
                          m.b90 + 280*m.b165*m.b90 + 130*m.b173*m.b90 + 450*m.b181*m.b90 + 520*m.b188*m.b90 + 790*m.b194
                          *m.b90 + 110*m.b199*m.b90 + 400*m.b203*m.b90 + 120*m.b206*m.b90 + 570*m.b208*m.b90 + 170*
                          m.b210*m.b90 + 430*m.b119*m.b105 + 620*m.b132*m.b105 + 240*m.b144*m.b105 + 450*m.b155*m.b105
                           + 210*m.b165*m.b105 + 600*m.b173*m.b105 + 120*m.b181*m.b105 + 660*m.b188*m.b105 + 530*m.b194*
                          m.b105 + 50*m.b199*m.b105 + 810*m.b203*m.b105 + 610*m.b206*m.b105 + 100*m.b208*m.b105 + 770*
                          m.b210*m.b105 + 340*m.b132*m.b119 + 20*m.b144*m.b119 + 820*m.b155*m.b119 + 530*m.b165*m.b119
                           + 260*m.b173*m.b119 + 620*m.b181*m.b119 + 180*m.b188*m.b119 + 710*m.b194*m.b119 + 140*m.b199*
                          m.b119 + 970*m.b203*m.b119 + 820*m.b206*m.b119 + 540*m.b208*m.b119 + 920*m.b210*m.b119 + 550*
                          m.b144*m.b132 + 780*m.b155*m.b132 + 870*m.b165*m.b132 + 690*m.b173*m.b132 + 20*m.b181*m.b132
                           + 320*m.b188*m.b132 + 420*m.b194*m.b132 + 140*m.b199*m.b132 + 450*m.b203*m.b132 + 600*m.b206*
                          m.b132 + 670*m.b208*m.b132 + 420*m.b210*m.b132 + 810*m.b155*m.b144 + 640*m.b165*m.b144 + 820*
                          m.b173*m.b144 + 580*m.b181*m.b144 + 980*m.b188*m.b144 + 360*m.b194*m.b144 + 920*m.b199*m.b144
                           + 30*m.b203*m.b144 + 620*m.b206*m.b144 + 540*m.b208*m.b144 + 850*m.b210*m.b144 + 690*m.b165*
                          m.b155 + 700*m.b173*m.b155 + 200*m.b181*m.b155 + 750*m.b188*m.b155 + 800*m.b194*m.b155 + 120*
                          m.b199*m.b155 + 820*m.b203*m.b155 + 100*m.b206*m.b155 + 990*m.b208*m.b155 + 130*m.b210*m.b155
                           + 840*m.b173*m.b165 + 980*m.b181*m.b165 + 270*m.b188*m.b165 + 810*m.b194*m.b165 + 590*m.b199*
                          m.b165 + 470*m.b203*m.b165 + 830*m.b206*m.b165 + 530*m.b208*m.b165 + 350*m.b181*m.b173 + 900*
                          m.b188*m.b173 + 980*m.b194*m.b173 + 710*m.b199*m.b173 + 830*m.b203*m.b173 + 540*m.b206*m.b173
                           + 860*m.b208*m.b173 + 270*m.b210*m.b173 + 710*m.b188*m.b181 + 100*m.b194*m.b181 + 980*m.b199*
                          m.b181 + 910*m.b203*m.b181 + 860*m.b206*m.b181 + 300*m.b208*m.b181 + 200*m.b210*m.b181 + 400*
                          m.b194*m.b188 + 70*m.b199*m.b188 + 760*m.b203*m.b188 + 530*m.b206*m.b188 + 910*m.b208*m.b188
                           + 330*m.b210*m.b188 + 720*m.b199*m.b194 + 340*m.b203*m.b194 + 320*m.b206*m.b194 + 70*m.b208*
                          m.b194 + 640*m.b210*m.b194 + 70*m.b203*m.b199 + 740*m.b206*m.b199 + 540*m.b208*m.b199 + 970*
                          m.b210*m.b199 + 890*m.b206*m.b203 + 120*m.b208*m.b203 + 790*m.b210*m.b203 + 390*m.b208*m.b206
                           + 890*m.b210*m.b206 + 980*m.b210*m.b208 >= 67751)

m.c4012 = Constraint(expr=750*m.b40*m.b21 + 390*m.b58*m.b21 + 260*m.b75*m.b21 + 20*m.b91*m.b21 + 940*m.b106*m.b21 + 760*
                          m.b120*m.b21 + 550*m.b133*m.b21 + 800*m.b145*m.b21 + 580*m.b156*m.b21 + 200*m.b174*m.b21 + 880
                          *m.b182*m.b21 + 600*m.b189*m.b21 + 170*m.b195*m.b21 + 850*m.b200*m.b21 + 710*m.b204*m.b21 + 
                          970*m.b207*m.b21 + 830*m.b209*m.b21 + 990*m.b210*m.b21 + 340*m.b211*m.b21 + 970*m.b58*m.b40 + 
                          680*m.b75*m.b40 + 410*m.b91*m.b40 + 630*m.b106*m.b40 + 670*m.b120*m.b40 + 310*m.b133*m.b40 + 
                          210*m.b145*m.b40 + 710*m.b156*m.b40 + 530*m.b174*m.b40 + 500*m.b182*m.b40 + 630*m.b189*m.b40
                           + 920*m.b195*m.b40 + 290*m.b200*m.b40 + 180*m.b204*m.b40 + 860*m.b207*m.b40 + 570*m.b209*
                          m.b40 + 730*m.b210*m.b40 + 880*m.b211*m.b40 + 150*m.b75*m.b58 + 590*m.b91*m.b58 + 390*m.b106*
                          m.b58 + 30*m.b120*m.b58 + 190*m.b133*m.b58 + 80*m.b145*m.b58 + 880*m.b156*m.b58 + 570*m.b174*
                          m.b58 + 230*m.b182*m.b58 + 940*m.b189*m.b58 + 210*m.b195*m.b58 + 720*m.b200*m.b58 + 140*m.b204
                          *m.b58 + 140*m.b207*m.b58 + 870*m.b209*m.b58 + 330*m.b210*m.b58 + 430*m.b211*m.b58 + 80*m.b91*
                          m.b75 + 40*m.b106*m.b75 + 340*m.b120*m.b75 + 620*m.b133*m.b75 + 550*m.b145*m.b75 + 490*m.b156*
                          m.b75 + 360*m.b174*m.b75 + 670*m.b182*m.b75 + 450*m.b189*m.b75 + 930*m.b195*m.b75 + 930*m.b200
                          *m.b75 + 630*m.b204*m.b75 + 80*m.b207*m.b75 + 520*m.b209*m.b75 + 540*m.b210*m.b75 + 60*m.b211*
                          m.b75 + 240*m.b106*m.b91 + 140*m.b120*m.b91 + 40*m.b133*m.b91 + 190*m.b145*m.b91 + 710*m.b156*
                          m.b91 + 130*m.b174*m.b91 + 450*m.b182*m.b91 + 520*m.b189*m.b91 + 790*m.b195*m.b91 + 110*m.b200
                          *m.b91 + 400*m.b204*m.b91 + 120*m.b207*m.b91 + 570*m.b209*m.b91 + 480*m.b210*m.b91 + 280*
                          m.b211*m.b91 + 430*m.b120*m.b106 + 620*m.b133*m.b106 + 240*m.b145*m.b106 + 450*m.b156*m.b106
                           + 600*m.b174*m.b106 + 120*m.b182*m.b106 + 660*m.b189*m.b106 + 530*m.b195*m.b106 + 50*m.b200*
                          m.b106 + 810*m.b204*m.b106 + 610*m.b207*m.b106 + 100*m.b209*m.b106 + 880*m.b210*m.b106 + 210*
                          m.b211*m.b106 + 340*m.b133*m.b120 + 20*m.b145*m.b120 + 820*m.b156*m.b120 + 260*m.b174*m.b120
                           + 620*m.b182*m.b120 + 180*m.b189*m.b120 + 710*m.b195*m.b120 + 140*m.b200*m.b120 + 970*m.b204*
                          m.b120 + 820*m.b207*m.b120 + 540*m.b209*m.b120 + 90*m.b210*m.b120 + 530*m.b211*m.b120 + 550*
                          m.b145*m.b133 + 780*m.b156*m.b133 + 690*m.b174*m.b133 + 20*m.b182*m.b133 + 320*m.b189*m.b133
                           + 420*m.b195*m.b133 + 140*m.b200*m.b133 + 450*m.b204*m.b133 + 600*m.b207*m.b133 + 670*m.b209*
                          m.b133 + 20*m.b210*m.b133 + 870*m.b211*m.b133 + 810*m.b156*m.b145 + 820*m.b174*m.b145 + 580*
                          m.b182*m.b145 + 980*m.b189*m.b145 + 360*m.b195*m.b145 + 920*m.b200*m.b145 + 30*m.b204*m.b145
                           + 620*m.b207*m.b145 + 540*m.b209*m.b145 + 210*m.b210*m.b145 + 640*m.b211*m.b145 + 700*m.b174*
                          m.b156 + 200*m.b182*m.b156 + 750*m.b189*m.b156 + 800*m.b195*m.b156 + 120*m.b200*m.b156 + 820*
                          m.b204*m.b156 + 100*m.b207*m.b156 + 990*m.b209*m.b156 + 40*m.b210*m.b156 + 690*m.b211*m.b156
                           + 350*m.b182*m.b174 + 900*m.b189*m.b174 + 980*m.b195*m.b174 + 710*m.b200*m.b174 + 830*m.b204*
                          m.b174 + 540*m.b207*m.b174 + 860*m.b209*m.b174 + 890*m.b210*m.b174 + 840*m.b211*m.b174 + 710*
                          m.b189*m.b182 + 100*m.b195*m.b182 + 980*m.b200*m.b182 + 910*m.b204*m.b182 + 860*m.b207*m.b182
                           + 300*m.b209*m.b182 + 550*m.b210*m.b182 + 980*m.b211*m.b182 + 400*m.b195*m.b189 + 70*m.b200*
                          m.b189 + 760*m.b204*m.b189 + 530*m.b207*m.b189 + 910*m.b209*m.b189 + 750*m.b210*m.b189 + 270*
                          m.b211*m.b189 + 720*m.b200*m.b195 + 340*m.b204*m.b195 + 320*m.b207*m.b195 + 70*m.b209*m.b195
                           + 870*m.b210*m.b195 + 810*m.b211*m.b195 + 70*m.b204*m.b200 + 740*m.b207*m.b200 + 540*m.b209*
                          m.b200 + 580*m.b210*m.b200 + 590*m.b211*m.b200 + 890*m.b207*m.b204 + 120*m.b209*m.b204 + 830*
                          m.b210*m.b204 + 470*m.b211*m.b204 + 390*m.b209*m.b207 + 70*m.b210*m.b207 + 830*m.b211*m.b207
                           + 890*m.b210*m.b209 + 530*m.b211*m.b209 + 800*m.b211*m.b210 >= 67751)
