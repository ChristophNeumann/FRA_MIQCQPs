#  MINLP written by GAMS Convert at 01/04/19 10:30:23
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        944      160      144      640        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        362      261      101        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       3913     2409     1504        0
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
m.x73 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x74 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x75 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x76 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x77 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x78 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x79 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x80 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x81 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x82 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x83 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x84 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x85 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x86 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x87 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x88 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x89 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x90 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x91 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x92 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x93 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x94 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x95 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x96 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x97 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x98 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x99 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x100 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x101 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x102 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x103 = Var(within=Reals,bounds=(0.1,1),initialize=0.1)
m.x104 = Var(within=Reals,bounds=(0.1,1),initialize=0.1)
m.x105 = Var(within=Reals,bounds=(0.1,1),initialize=0.1)
m.x106 = Var(within=Reals,bounds=(0.1,1),initialize=0.1)
m.x107 = Var(within=Reals,bounds=(0.1,0.9),initialize=0.1)
m.x108 = Var(within=Reals,bounds=(0.1,0.9),initialize=0.1)
m.x109 = Var(within=Reals,bounds=(0.1,0.9),initialize=0.1)
m.x110 = Var(within=Reals,bounds=(0.1,0.9),initialize=0.1)
m.x111 = Var(within=Reals,bounds=(0,0.9),initialize=0)
m.x112 = Var(within=Reals,bounds=(0,0.9),initialize=0)
m.x113 = Var(within=Reals,bounds=(0,0.9),initialize=0)
m.x114 = Var(within=Reals,bounds=(0,0.9),initialize=0)
m.x115 = Var(within=Reals,bounds=(0,0.8),initialize=0)
m.x116 = Var(within=Reals,bounds=(0,0.8),initialize=0)
m.x117 = Var(within=Reals,bounds=(0,0.8),initialize=0)
m.x118 = Var(within=Reals,bounds=(0,0.8),initialize=0)
m.x119 = Var(within=Reals,bounds=(0.2,1),initialize=0.2)
m.x120 = Var(within=Reals,bounds=(0.2,1),initialize=0.2)
m.x121 = Var(within=Reals,bounds=(0.2,1),initialize=0.2)
m.x122 = Var(within=Reals,bounds=(0.2,1),initialize=0.2)
m.x123 = Var(within=Reals,bounds=(0.2,1),initialize=0.2)
m.x124 = Var(within=Reals,bounds=(0.2,1),initialize=0.2)
m.x125 = Var(within=Reals,bounds=(0.2,1),initialize=0.2)
m.x126 = Var(within=Reals,bounds=(0.2,1),initialize=0.2)
m.x127 = Var(within=Reals,bounds=(0,0.9),initialize=0)
m.x128 = Var(within=Reals,bounds=(0,0.9),initialize=0)
m.x129 = Var(within=Reals,bounds=(0,0.9),initialize=0)
m.x130 = Var(within=Reals,bounds=(0,0.9),initialize=0)
m.x131 = Var(within=Reals,bounds=(0.2,1),initialize=0.2)
m.x132 = Var(within=Reals,bounds=(0.2,1),initialize=0.2)
m.x133 = Var(within=Reals,bounds=(0.2,1),initialize=0.2)
m.x134 = Var(within=Reals,bounds=(0.2,1),initialize=0.2)
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
m.b212 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b213 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b214 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b215 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b216 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b217 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b218 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b219 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b220 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b221 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b222 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b223 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b224 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b225 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b226 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b227 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b228 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b229 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b230 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b231 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b232 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b233 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b234 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b235 = Var(within=Binary,bounds=(0,1),initialize=0)
m.x236 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x237 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x238 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x239 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x240 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x241 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x242 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x243 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x244 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x245 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x246 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x247 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x248 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x249 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x250 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x251 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x252 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x253 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x254 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x255 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x256 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x257 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x258 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x259 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x260 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x261 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x262 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x263 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x264 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x265 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x266 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x267 = Var(within=Reals,bounds=(0.1,1),initialize=0.1)
m.x268 = Var(within=Reals,bounds=(0.1,1),initialize=0.1)
m.x269 = Var(within=Reals,bounds=(0.1,1),initialize=0.1)
m.x270 = Var(within=Reals,bounds=(0.1,1),initialize=0.1)
m.x271 = Var(within=Reals,bounds=(0.1,1),initialize=0.1)
m.x272 = Var(within=Reals,bounds=(0.1,1),initialize=0.1)
m.x273 = Var(within=Reals,bounds=(0.1,1),initialize=0.1)
m.x274 = Var(within=Reals,bounds=(0.1,1),initialize=0.1)
m.x275 = Var(within=Reals,bounds=(0.1,1),initialize=0.1)
m.x276 = Var(within=Reals,bounds=(0.1,1),initialize=0.1)
m.x277 = Var(within=Reals,bounds=(0.1,1),initialize=0.1)
m.x278 = Var(within=Reals,bounds=(0.1,1),initialize=0.1)
m.x279 = Var(within=Reals,bounds=(0.1,0.9),initialize=0.1)
m.x280 = Var(within=Reals,bounds=(0.1,0.9),initialize=0.1)
m.x281 = Var(within=Reals,bounds=(0.1,0.9),initialize=0.1)
m.x282 = Var(within=Reals,bounds=(0.1,0.9),initialize=0.1)
m.x283 = Var(within=Reals,bounds=(0.1,0.9),initialize=0.1)
m.x284 = Var(within=Reals,bounds=(0.1,0.9),initialize=0.1)
m.x285 = Var(within=Reals,bounds=(0.1,0.9),initialize=0.1)
m.x286 = Var(within=Reals,bounds=(0.1,0.9),initialize=0.1)
m.x287 = Var(within=Reals,bounds=(0.1,0.9),initialize=0.1)
m.x288 = Var(within=Reals,bounds=(0.1,0.9),initialize=0.1)
m.x289 = Var(within=Reals,bounds=(0.1,0.9),initialize=0.1)
m.x290 = Var(within=Reals,bounds=(0.1,0.9),initialize=0.1)
m.x291 = Var(within=Reals,bounds=(0,0.9),initialize=0)
m.x292 = Var(within=Reals,bounds=(0,0.9),initialize=0)
m.x293 = Var(within=Reals,bounds=(0,0.9),initialize=0)
m.x294 = Var(within=Reals,bounds=(0,0.9),initialize=0)
m.x295 = Var(within=Reals,bounds=(0,0.9),initialize=0)
m.x296 = Var(within=Reals,bounds=(0,0.9),initialize=0)
m.x297 = Var(within=Reals,bounds=(0,0.9),initialize=0)
m.x298 = Var(within=Reals,bounds=(0,0.9),initialize=0)
m.x299 = Var(within=Reals,bounds=(0,0.9),initialize=0)
m.x300 = Var(within=Reals,bounds=(0,0.9),initialize=0)
m.x301 = Var(within=Reals,bounds=(0,0.9),initialize=0)
m.x302 = Var(within=Reals,bounds=(0,0.9),initialize=0)
m.x303 = Var(within=Reals,bounds=(0,0.8),initialize=0)
m.x304 = Var(within=Reals,bounds=(0,0.8),initialize=0)
m.x305 = Var(within=Reals,bounds=(0,0.8),initialize=0)
m.x306 = Var(within=Reals,bounds=(0,0.8),initialize=0)
m.x307 = Var(within=Reals,bounds=(0,0.8),initialize=0)
m.x308 = Var(within=Reals,bounds=(0,0.8),initialize=0)
m.x309 = Var(within=Reals,bounds=(0,0.8),initialize=0)
m.x310 = Var(within=Reals,bounds=(0,0.8),initialize=0)
m.x311 = Var(within=Reals,bounds=(0,0.8),initialize=0)
m.x312 = Var(within=Reals,bounds=(0,0.8),initialize=0)
m.x313 = Var(within=Reals,bounds=(0,0.8),initialize=0)
m.x314 = Var(within=Reals,bounds=(0,0.8),initialize=0)
m.x315 = Var(within=Reals,bounds=(0.2,1),initialize=0.2)
m.x316 = Var(within=Reals,bounds=(0.2,1),initialize=0.2)
m.x317 = Var(within=Reals,bounds=(0.2,1),initialize=0.2)
m.x318 = Var(within=Reals,bounds=(0.2,1),initialize=0.2)
m.x319 = Var(within=Reals,bounds=(0.2,1),initialize=0.2)
m.x320 = Var(within=Reals,bounds=(0.2,1),initialize=0.2)
m.x321 = Var(within=Reals,bounds=(0.2,1),initialize=0.2)
m.x322 = Var(within=Reals,bounds=(0.2,1),initialize=0.2)
m.x323 = Var(within=Reals,bounds=(0.2,1),initialize=0.2)
m.x324 = Var(within=Reals,bounds=(0.2,1),initialize=0.2)
m.x325 = Var(within=Reals,bounds=(0.2,1),initialize=0.2)
m.x326 = Var(within=Reals,bounds=(0.2,1),initialize=0.2)
m.x327 = Var(within=Reals,bounds=(0.2,1),initialize=0.2)
m.x328 = Var(within=Reals,bounds=(0.2,1),initialize=0.2)
m.x329 = Var(within=Reals,bounds=(0.2,1),initialize=0.2)
m.x330 = Var(within=Reals,bounds=(0.2,1),initialize=0.2)
m.x331 = Var(within=Reals,bounds=(0.2,1),initialize=0.2)
m.x332 = Var(within=Reals,bounds=(0.2,1),initialize=0.2)
m.x333 = Var(within=Reals,bounds=(0.2,1),initialize=0.2)
m.x334 = Var(within=Reals,bounds=(0.2,1),initialize=0.2)
m.x335 = Var(within=Reals,bounds=(0.2,1),initialize=0.2)
m.x336 = Var(within=Reals,bounds=(0.2,1),initialize=0.2)
m.x337 = Var(within=Reals,bounds=(0.2,1),initialize=0.2)
m.x338 = Var(within=Reals,bounds=(0.2,1),initialize=0.2)
m.x339 = Var(within=Reals,bounds=(0,0.9),initialize=0)
m.x340 = Var(within=Reals,bounds=(0,0.9),initialize=0)
m.x341 = Var(within=Reals,bounds=(0,0.9),initialize=0)
m.x342 = Var(within=Reals,bounds=(0,0.9),initialize=0)
m.x343 = Var(within=Reals,bounds=(0,0.9),initialize=0)
m.x344 = Var(within=Reals,bounds=(0,0.9),initialize=0)
m.x345 = Var(within=Reals,bounds=(0,0.9),initialize=0)
m.x346 = Var(within=Reals,bounds=(0,0.9),initialize=0)
m.x347 = Var(within=Reals,bounds=(0,0.9),initialize=0)
m.x348 = Var(within=Reals,bounds=(0,0.9),initialize=0)
m.x349 = Var(within=Reals,bounds=(0,0.9),initialize=0)
m.x350 = Var(within=Reals,bounds=(0,0.9),initialize=0)
m.x351 = Var(within=Reals,bounds=(0.2,1),initialize=0.2)
m.x352 = Var(within=Reals,bounds=(0.2,1),initialize=0.2)
m.x353 = Var(within=Reals,bounds=(0.2,1),initialize=0.2)
m.x354 = Var(within=Reals,bounds=(0.2,1),initialize=0.2)
m.x355 = Var(within=Reals,bounds=(0.2,1),initialize=0.2)
m.x356 = Var(within=Reals,bounds=(0.2,1),initialize=0.2)
m.x357 = Var(within=Reals,bounds=(0.2,1),initialize=0.2)
m.x358 = Var(within=Reals,bounds=(0.2,1),initialize=0.2)
m.x359 = Var(within=Reals,bounds=(0.2,1),initialize=0.2)
m.x360 = Var(within=Reals,bounds=(0.2,1),initialize=0.2)
m.x361 = Var(within=Reals,bounds=(0.2,1),initialize=0.2)
m.x362 = Var(within=Reals,bounds=(0.2,1),initialize=0.2)

m.obj = Objective(expr= - 0.43*m.x2 - 0.43*m.x3 - 0.43*m.x4 - 0.43*m.x5 - 0.9*m.x6 - 0.9*m.x7 - 0.9*m.x8 - 0.9*m.x9
                        - 0.44*m.x10 - 0.44*m.x11 - 0.44*m.x12 - 0.44*m.x13 - 1.5*m.x14 - 1.5*m.x15 - 1.5*m.x16
                        - 1.5*m.x17 - 1.12*m.x18 - 1.12*m.x19 - 1.12*m.x20 - 1.12*m.x21 - 1.2*m.x22 - 1.2*m.x23
                        - 1.2*m.x24 - 1.2*m.x25 - 1.32*m.x26 - 1.32*m.x27 - 1.32*m.x28 - 1.32*m.x29 - 0.93*m.x30
                        - 0.93*m.x31 - 0.93*m.x32 - 0.93*m.x33 - 0.49*m.x34 - 0.49*m.x35 - 0.49*m.x36 - 0.49*m.x37
                        - 0.24*m.x38 - 0.24*m.x39 - 0.24*m.x40 - 0.24*m.x41 + 1.44*m.x42 + 1.44*m.x43 + 1.44*m.x44
                        + 3.68*m.x45 + 3.68*m.x46 + 3.68*m.x47 - 0.49*m.x48 - 0.49*m.x49 - 0.49*m.x50 - 0.49*m.x51
                        - 0.68*m.x52 - 0.68*m.x53 - 0.68*m.x54 - 0.68*m.x55 - 0.37*m.x56 - 0.37*m.x57 - 0.37*m.x58
                        - 0.37*m.x59 + 2.36*m.x60 + 2.36*m.x61 + 2.36*m.x62 + 3.29*m.x63 + 3.29*m.x64 + 3.29*m.x65
                        - 0.1*m.x66 - 0.1*m.x67 - 0.1*m.x68 - 0.1*m.x69 - 0.34*m.x70 - 0.34*m.x71 - 0.34*m.x72
                        - 0.34*m.x73 - 0.14*m.x74 - 0.14*m.x75 - 0.14*m.x76 - 0.14*m.x77 + 2.29*m.x78 + 2.29*m.x79
                        + 2.29*m.x80 + 3.71*m.x81 + 3.71*m.x82 + 3.71*m.x83 - 0.72*m.x84 - 0.72*m.x85 - 0.72*m.x86
                        - 0.72*m.x87 - 0.89*m.x88 - 0.89*m.x89 - 0.89*m.x90 - 0.89*m.x91 - 0.7*m.x92 - 0.7*m.x93
                        - 0.7*m.x94 - 0.7*m.x95 + 2.37*m.x96 + 2.37*m.x97 + 2.37*m.x98 + 2.37*m.x99 + 3.7*m.x100
                        + 3.7*m.x101 + 3.7*m.x102 - 0.92*m.b135 - 0.92*m.b136 - 0.92*m.b137 - 0.92*m.b138 - 0.18*m.b139
                        - 0.18*m.b140 - 0.18*m.b141 - 0.18*m.b142 - 0.98*m.b143 - 0.98*m.b144 - 0.98*m.b145
                        - 0.98*m.b146 - 0.26*m.b147 - 0.26*m.b148 - 0.26*m.b149 - 0.26*m.b150 - 0.71*m.b151
                        - 0.71*m.b152 - 0.71*m.b153 - 0.71*m.b154 - 0.12*m.b155 - 0.12*m.b156 - 0.12*m.b157
                        - 0.12*m.b158 - 0.32*m.b159 - 0.32*m.b160 - 0.32*m.b161 - 0.32*m.b162 - 0.03*m.b163
                        - 0.03*m.b164 - 0.03*m.b165 - 0.03*m.b166 - 0.73*m.b167 - 0.73*m.b168 - 0.73*m.b169
                        - 0.73*m.b170 - 0.58*m.b171 - 0.58*m.b172 - 0.58*m.b173 - 0.58*m.b174 - 0.46*m.b175
                        - 0.46*m.b176 - 0.46*m.b177 - 0.55*m.b178 - 0.55*m.b179 - 0.55*m.b180 - 0.23*m.b181
                        - 0.23*m.b182 - 0.23*m.b183 - 0.23*m.b184 - 0.62*m.b185 - 0.62*m.b186 - 0.62*m.b187
                        - 0.62*m.b188 - 0.4*m.b189 - 0.4*m.b190 - 0.4*m.b191 - 0.4*m.b192 - 0.99*m.b193 - 0.99*m.b194
                        - 0.99*m.b195 - 0.89*m.b196 - 0.89*m.b197 - 0.89*m.b198 - 0.8*m.b199 - 0.8*m.b200 - 0.8*m.b201
                        - 0.8*m.b202 - 0.26*m.b203 - 0.26*m.b204 - 0.26*m.b205 - 0.26*m.b206 - 0.68*m.b207 - 0.68*m.b208
                        - 0.68*m.b209 - 0.68*m.b210 - 0.72*m.b211 - 0.72*m.b212 - 0.72*m.b213 - 0.65*m.b214
                        - 0.65*m.b215 - 0.65*m.b216 - 0.78*m.b217 - 0.78*m.b218 - 0.78*m.b219 - 0.78*m.b220 - 0.9*m.b221
                        - 0.9*m.b222 - 0.9*m.b223 - 0.9*m.b224 - 0.33*m.b225 - 0.33*m.b226 - 0.33*m.b227 - 0.33*m.b228
                        - 0.2*m.b229 - 0.2*m.b230 - 0.2*m.b231 - 0.2*m.b232 - 0.74*m.b233 - 0.74*m.b234 - 0.74*m.b235
                       , sense=maximize)

m.c2 = Constraint(expr=   m.x2 + m.x6 + m.x10 + m.x236 == 1.2)

m.c3 = Constraint(expr=   m.x14 + m.x18 + m.x22 + m.x26 + m.x237 == 0.7)

m.c4 = Constraint(expr= - m.x14 + m.x30 + m.x34 + m.x38 - m.x48 - m.x66 - m.x84 + m.x238 == 1)

m.c5 = Constraint(expr= - m.x2 - m.x18 - m.x30 + m.x48 + m.x52 + m.x56 - m.x70 - m.x88 + m.x239 == 0.8)

m.c6 = Constraint(expr= - m.x6 - m.x22 - m.x34 - m.x52 + m.x66 + m.x70 + m.x74 - m.x92 + m.x240 == 0.2)

m.c7 = Constraint(expr= - m.x10 - m.x26 - m.x38 - m.x56 - m.x74 + m.x84 + m.x88 + m.x92 + m.x96 + m.x241 == 0.5)

m.c8 = Constraint(expr= - m.x96 + m.x242 == -0.1)

m.c9 = Constraint(expr=   m.x3 + m.x7 + m.x11 - m.x236 + m.x243 == 0.2)

m.c10 = Constraint(expr=   m.x4 + m.x8 + m.x12 - m.x243 + m.x244 == 0.7)

m.c11 = Constraint(expr=   m.x5 + m.x9 + m.x13 - m.x244 + m.x245 == 0.5)

m.c12 = Constraint(expr=   m.x15 + m.x19 + m.x23 + m.x27 - m.x237 + m.x246 == 0.6)

m.c13 = Constraint(expr=   m.x16 + m.x20 + m.x24 + m.x28 - m.x246 + m.x247 == 0.6)

m.c14 = Constraint(expr=   m.x17 + m.x21 + m.x25 + m.x29 - m.x247 + m.x248 == 0.5)

m.c15 = Constraint(expr= - m.x15 + m.x31 + m.x35 + m.x39 + m.x42 + m.x45 - m.x49 - m.x67 - m.x85 - m.x238 + m.x249 == 0)

m.c16 = Constraint(expr= - m.x16 + m.x32 + m.x36 + m.x40 + m.x43 + m.x46 - m.x50 - m.x68 - m.x86 - m.x249 + m.x250 == 0)

m.c17 = Constraint(expr= - m.x17 + m.x33 + m.x37 + m.x41 + m.x44 + m.x47 - m.x51 - m.x69 - m.x87 - m.x250 + m.x251 == 0)

m.c18 = Constraint(expr= - m.x3 - m.x19 - m.x31 + m.x49 + m.x53 + m.x57 + m.x60 + m.x63 - m.x71 - m.x89 - m.x239
                         + m.x252 == 0)

m.c19 = Constraint(expr= - m.x4 - m.x20 - m.x32 + m.x50 + m.x54 + m.x58 + m.x61 + m.x64 - m.x72 - m.x90 - m.x252
                         + m.x253 == 0)

m.c20 = Constraint(expr= - m.x5 - m.x21 - m.x33 + m.x51 + m.x55 + m.x59 + m.x62 + m.x65 - m.x73 - m.x91 - m.x253
                         + m.x254 == 0)

m.c21 = Constraint(expr= - m.x7 - m.x23 - m.x35 - m.x53 + m.x67 + m.x71 + m.x75 + m.x78 + m.x81 - m.x93 - m.x240
                         + m.x255 == 0)

m.c22 = Constraint(expr= - m.x8 - m.x24 - m.x36 - m.x54 + m.x68 + m.x72 + m.x76 + m.x79 + m.x82 - m.x94 - m.x255
                         + m.x256 == 0)

m.c23 = Constraint(expr= - m.x9 - m.x25 - m.x37 - m.x55 + m.x69 + m.x73 + m.x77 + m.x80 + m.x83 - m.x95 - m.x256
                         + m.x257 == 0)

m.c24 = Constraint(expr= - m.x11 - m.x27 - m.x39 - m.x57 - m.x75 + m.x85 + m.x89 + m.x93 + m.x97 + m.x100 - m.x241
                         + m.x258 == 0)

m.c25 = Constraint(expr= - m.x12 - m.x28 - m.x40 - m.x58 - m.x76 + m.x86 + m.x90 + m.x94 + m.x98 + m.x101 - m.x258
                         + m.x259 == 0)

m.c26 = Constraint(expr= - m.x13 - m.x29 - m.x41 - m.x59 - m.x77 + m.x87 + m.x91 + m.x95 + m.x99 + m.x102 - m.x259
                         + m.x260 == 0)

m.c27 = Constraint(expr= - m.x42 - m.x60 - m.x78 - m.x97 - m.x242 + m.x261 == -0.19)

m.c28 = Constraint(expr= - m.x43 - m.x61 - m.x79 - m.x98 - m.x261 + m.x262 == -0.18)

m.c29 = Constraint(expr= - m.x44 - m.x62 - m.x80 - m.x99 - m.x262 + m.x263 == -0.63)

m.c30 = Constraint(expr= - m.x45 - m.x63 - m.x81 - m.x100 + m.x264 == -0.63)

m.c31 = Constraint(expr= - m.x46 - m.x64 - m.x82 - m.x101 - m.x264 + m.x265 == -0.37)

m.c32 = Constraint(expr= - m.x47 - m.x65 - m.x83 - m.x102 - m.x265 + m.x266 == -0.78)

m.c33 = Constraint(expr=   m.x2 - m.b135 <= 0)

m.c34 = Constraint(expr=   m.x3 - m.b136 <= 0)

m.c35 = Constraint(expr=   m.x4 - m.b137 <= 0)

m.c36 = Constraint(expr=   m.x5 - m.b138 <= 0)

m.c37 = Constraint(expr=   m.x6 - m.b139 <= 0)

m.c38 = Constraint(expr=   m.x7 - m.b140 <= 0)

m.c39 = Constraint(expr=   m.x8 - m.b141 <= 0)

m.c40 = Constraint(expr=   m.x9 - m.b142 <= 0)

m.c41 = Constraint(expr=   m.x10 - m.b143 <= 0)

m.c42 = Constraint(expr=   m.x11 - m.b144 <= 0)

m.c43 = Constraint(expr=   m.x12 - m.b145 <= 0)

m.c44 = Constraint(expr=   m.x13 - m.b146 <= 0)

m.c45 = Constraint(expr=   m.x14 - m.b147 <= 0)

m.c46 = Constraint(expr=   m.x15 - m.b148 <= 0)

m.c47 = Constraint(expr=   m.x16 - m.b149 <= 0)

m.c48 = Constraint(expr=   m.x17 - m.b150 <= 0)

m.c49 = Constraint(expr=   m.x18 - m.b151 <= 0)

m.c50 = Constraint(expr=   m.x19 - m.b152 <= 0)

m.c51 = Constraint(expr=   m.x20 - m.b153 <= 0)

m.c52 = Constraint(expr=   m.x21 - m.b154 <= 0)

m.c53 = Constraint(expr=   m.x22 - m.b155 <= 0)

m.c54 = Constraint(expr=   m.x23 - m.b156 <= 0)

m.c55 = Constraint(expr=   m.x24 - m.b157 <= 0)

m.c56 = Constraint(expr=   m.x25 - m.b158 <= 0)

m.c57 = Constraint(expr=   m.x26 - m.b159 <= 0)

m.c58 = Constraint(expr=   m.x27 - m.b160 <= 0)

m.c59 = Constraint(expr=   m.x28 - m.b161 <= 0)

m.c60 = Constraint(expr=   m.x29 - m.b162 <= 0)

m.c61 = Constraint(expr=   m.x30 - m.b163 <= 0)

m.c62 = Constraint(expr=   m.x31 - m.b164 <= 0)

m.c63 = Constraint(expr=   m.x32 - m.b165 <= 0)

m.c64 = Constraint(expr=   m.x33 - m.b166 <= 0)

m.c65 = Constraint(expr=   m.x34 - m.b167 <= 0)

m.c66 = Constraint(expr=   m.x35 - m.b168 <= 0)

m.c67 = Constraint(expr=   m.x36 - m.b169 <= 0)

m.c68 = Constraint(expr=   m.x37 - m.b170 <= 0)

m.c69 = Constraint(expr=   m.x38 - m.b171 <= 0)

m.c70 = Constraint(expr=   m.x39 - m.b172 <= 0)

m.c71 = Constraint(expr=   m.x40 - m.b173 <= 0)

m.c72 = Constraint(expr=   m.x41 - m.b174 <= 0)

m.c73 = Constraint(expr=   m.x42 - m.b175 <= 0)

m.c74 = Constraint(expr=   m.x43 - m.b176 <= 0)

m.c75 = Constraint(expr=   m.x44 - m.b177 <= 0)

m.c76 = Constraint(expr=   m.x45 - m.b178 <= 0)

m.c77 = Constraint(expr=   m.x46 - m.b179 <= 0)

m.c78 = Constraint(expr=   m.x47 - m.b180 <= 0)

m.c79 = Constraint(expr=   m.x48 - m.b181 <= 0)

m.c80 = Constraint(expr=   m.x49 - m.b182 <= 0)

m.c81 = Constraint(expr=   m.x50 - m.b183 <= 0)

m.c82 = Constraint(expr=   m.x51 - m.b184 <= 0)

m.c83 = Constraint(expr=   m.x52 - m.b185 <= 0)

m.c84 = Constraint(expr=   m.x53 - m.b186 <= 0)

m.c85 = Constraint(expr=   m.x54 - m.b187 <= 0)

m.c86 = Constraint(expr=   m.x55 - m.b188 <= 0)

m.c87 = Constraint(expr=   m.x56 - m.b189 <= 0)

m.c88 = Constraint(expr=   m.x57 - m.b190 <= 0)

m.c89 = Constraint(expr=   m.x58 - m.b191 <= 0)

m.c90 = Constraint(expr=   m.x59 - m.b192 <= 0)

m.c91 = Constraint(expr=   m.x60 - m.b193 <= 0)

m.c92 = Constraint(expr=   m.x61 - m.b194 <= 0)

m.c93 = Constraint(expr=   m.x62 - m.b195 <= 0)

m.c94 = Constraint(expr=   m.x63 - m.b196 <= 0)

m.c95 = Constraint(expr=   m.x64 - m.b197 <= 0)

m.c96 = Constraint(expr=   m.x65 - m.b198 <= 0)

m.c97 = Constraint(expr=   m.x66 - m.b199 <= 0)

m.c98 = Constraint(expr=   m.x67 - m.b200 <= 0)

m.c99 = Constraint(expr=   m.x68 - m.b201 <= 0)

m.c100 = Constraint(expr=   m.x69 - m.b202 <= 0)

m.c101 = Constraint(expr=   m.x70 - m.b203 <= 0)

m.c102 = Constraint(expr=   m.x71 - m.b204 <= 0)

m.c103 = Constraint(expr=   m.x72 - m.b205 <= 0)

m.c104 = Constraint(expr=   m.x73 - m.b206 <= 0)

m.c105 = Constraint(expr=   m.x74 - m.b207 <= 0)

m.c106 = Constraint(expr=   m.x75 - m.b208 <= 0)

m.c107 = Constraint(expr=   m.x76 - m.b209 <= 0)

m.c108 = Constraint(expr=   m.x77 - m.b210 <= 0)

m.c109 = Constraint(expr=   m.x78 - m.b211 <= 0)

m.c110 = Constraint(expr=   m.x79 - m.b212 <= 0)

m.c111 = Constraint(expr=   m.x80 - m.b213 <= 0)

m.c112 = Constraint(expr=   m.x81 - m.b214 <= 0)

m.c113 = Constraint(expr=   m.x82 - m.b215 <= 0)

m.c114 = Constraint(expr=   m.x83 - m.b216 <= 0)

m.c115 = Constraint(expr=   m.x84 - m.b217 <= 0)

m.c116 = Constraint(expr=   m.x85 - m.b218 <= 0)

m.c117 = Constraint(expr=   m.x86 - m.b219 <= 0)

m.c118 = Constraint(expr=   m.x87 - m.b220 <= 0)

m.c119 = Constraint(expr=   m.x88 - m.b221 <= 0)

m.c120 = Constraint(expr=   m.x89 - m.b222 <= 0)

m.c121 = Constraint(expr=   m.x90 - m.b223 <= 0)

m.c122 = Constraint(expr=   m.x91 - m.b224 <= 0)

m.c123 = Constraint(expr=   m.x92 - m.b225 <= 0)

m.c124 = Constraint(expr=   m.x93 - m.b226 <= 0)

m.c125 = Constraint(expr=   m.x94 - m.b227 <= 0)

m.c126 = Constraint(expr=   m.x95 - m.b228 <= 0)

m.c127 = Constraint(expr=   m.x96 - m.b229 <= 0)

m.c128 = Constraint(expr=   m.x97 - m.b230 <= 0)

m.c129 = Constraint(expr=   m.x98 - m.b231 <= 0)

m.c130 = Constraint(expr=   m.x99 - m.b232 <= 0)

m.c131 = Constraint(expr=   m.x100 - m.b233 <= 0)

m.c132 = Constraint(expr=   m.x101 - m.b234 <= 0)

m.c133 = Constraint(expr=   m.x102 - m.b235 <= 0)

m.c134 = Constraint(expr=   0.6*m.b175 - m.x267 <= -0.1)

m.c135 = Constraint(expr=   0.6*m.b176 - m.x268 <= -0.1)

m.c136 = Constraint(expr=   0.6*m.b177 - m.x269 <= -0.1)

m.c137 = Constraint(expr=   0.4*m.b178 - m.x267 <= -0.1)

m.c138 = Constraint(expr=   0.4*m.b179 - m.x268 <= -0.1)

m.c139 = Constraint(expr=   0.4*m.b180 - m.x269 <= -0.1)

m.c140 = Constraint(expr=   0.6*m.b193 - m.x270 <= -0.1)

m.c141 = Constraint(expr=   0.6*m.b194 - m.x271 <= -0.1)

m.c142 = Constraint(expr=   0.6*m.b195 - m.x272 <= -0.1)

m.c143 = Constraint(expr=   0.4*m.b196 - m.x270 <= -0.1)

m.c144 = Constraint(expr=   0.4*m.b197 - m.x271 <= -0.1)

m.c145 = Constraint(expr=   0.4*m.b198 - m.x272 <= -0.1)

m.c146 = Constraint(expr=   0.6*m.b211 - m.x273 <= -0.1)

m.c147 = Constraint(expr=   0.6*m.b212 - m.x274 <= -0.1)

m.c148 = Constraint(expr=   0.6*m.b213 - m.x275 <= -0.1)

m.c149 = Constraint(expr=   0.4*m.b214 - m.x273 <= -0.1)

m.c150 = Constraint(expr=   0.4*m.b215 - m.x274 <= -0.1)

m.c151 = Constraint(expr=   0.4*m.b216 - m.x275 <= -0.1)

m.c152 = Constraint(expr=   0.6*m.b230 - m.x276 <= -0.1)

m.c153 = Constraint(expr=   0.6*m.b231 - m.x277 <= -0.1)

m.c154 = Constraint(expr=   0.6*m.b232 - m.x278 <= -0.1)

m.c155 = Constraint(expr=   0.4*m.b233 - m.x276 <= -0.1)

m.c156 = Constraint(expr=   0.4*m.b234 - m.x277 <= -0.1)

m.c157 = Constraint(expr=   0.4*m.b235 - m.x278 <= -0.1)

m.c158 = Constraint(expr=   0.2*m.b175 - m.x279 <= -0.1)

m.c159 = Constraint(expr=   0.2*m.b176 - m.x280 <= -0.1)

m.c160 = Constraint(expr=   0.2*m.b177 - m.x281 <= -0.1)

m.c161 = Constraint(expr=   0.2*m.b178 - m.x279 <= -0.1)

m.c162 = Constraint(expr=   0.2*m.b179 - m.x280 <= -0.1)

m.c163 = Constraint(expr=   0.2*m.b180 - m.x281 <= -0.1)

m.c164 = Constraint(expr=   0.2*m.b193 - m.x282 <= -0.1)

m.c165 = Constraint(expr=   0.2*m.b194 - m.x283 <= -0.1)

m.c166 = Constraint(expr=   0.2*m.b195 - m.x284 <= -0.1)

m.c167 = Constraint(expr=   0.2*m.b196 - m.x282 <= -0.1)

m.c168 = Constraint(expr=   0.2*m.b197 - m.x283 <= -0.1)

m.c169 = Constraint(expr=   0.2*m.b198 - m.x284 <= -0.1)

m.c170 = Constraint(expr=   0.2*m.b211 - m.x285 <= -0.1)

m.c171 = Constraint(expr=   0.2*m.b212 - m.x286 <= -0.1)

m.c172 = Constraint(expr=   0.2*m.b213 - m.x287 <= -0.1)

m.c173 = Constraint(expr=   0.2*m.b214 - m.x285 <= -0.1)

m.c174 = Constraint(expr=   0.2*m.b215 - m.x286 <= -0.1)

m.c175 = Constraint(expr=   0.2*m.b216 - m.x287 <= -0.1)

m.c176 = Constraint(expr=   0.2*m.b230 - m.x288 <= -0.1)

m.c177 = Constraint(expr=   0.2*m.b231 - m.x289 <= -0.1)

m.c178 = Constraint(expr=   0.2*m.b232 - m.x290 <= -0.1)

m.c179 = Constraint(expr=   0.2*m.b233 - m.x288 <= -0.1)

m.c180 = Constraint(expr=   0.2*m.b234 - m.x289 <= -0.1)

m.c181 = Constraint(expr=   0.2*m.b235 - m.x290 <= -0.1)

m.c182 = Constraint(expr=   0.6*m.b175 - m.x291 <= 0)

m.c183 = Constraint(expr=   0.6*m.b176 - m.x292 <= 0)

m.c184 = Constraint(expr=   0.6*m.b177 - m.x293 <= 0)

m.c185 = Constraint(expr=   0.4*m.b178 - m.x291 <= 0)

m.c186 = Constraint(expr=   0.4*m.b179 - m.x292 <= 0)

m.c187 = Constraint(expr=   0.4*m.b180 - m.x293 <= 0)

m.c188 = Constraint(expr=   0.6*m.b193 - m.x294 <= 0)

m.c189 = Constraint(expr=   0.6*m.b194 - m.x295 <= 0)

m.c190 = Constraint(expr=   0.6*m.b195 - m.x296 <= 0)

m.c191 = Constraint(expr=   0.4*m.b196 - m.x294 <= 0)

m.c192 = Constraint(expr=   0.4*m.b197 - m.x295 <= 0)

m.c193 = Constraint(expr=   0.4*m.b198 - m.x296 <= 0)

m.c194 = Constraint(expr=   0.6*m.b211 - m.x297 <= 0)

m.c195 = Constraint(expr=   0.6*m.b212 - m.x298 <= 0)

m.c196 = Constraint(expr=   0.6*m.b213 - m.x299 <= 0)

m.c197 = Constraint(expr=   0.4*m.b214 - m.x297 <= 0)

m.c198 = Constraint(expr=   0.4*m.b215 - m.x298 <= 0)

m.c199 = Constraint(expr=   0.4*m.b216 - m.x299 <= 0)

m.c200 = Constraint(expr=   0.6*m.b230 - m.x300 <= 0)

m.c201 = Constraint(expr=   0.6*m.b231 - m.x301 <= 0)

m.c202 = Constraint(expr=   0.6*m.b232 - m.x302 <= 0)

m.c203 = Constraint(expr=   0.4*m.b233 - m.x300 <= 0)

m.c204 = Constraint(expr=   0.4*m.b234 - m.x301 <= 0)

m.c205 = Constraint(expr=   0.4*m.b235 - m.x302 <= 0)

m.c206 = Constraint(expr=   0.2*m.b175 - m.x303 <= 0)

m.c207 = Constraint(expr=   0.2*m.b176 - m.x304 <= 0)

m.c208 = Constraint(expr=   0.2*m.b177 - m.x305 <= 0)

m.c209 = Constraint(expr=   0.2*m.b178 - m.x303 <= 0)

m.c210 = Constraint(expr=   0.2*m.b179 - m.x304 <= 0)

m.c211 = Constraint(expr=   0.2*m.b180 - m.x305 <= 0)

m.c212 = Constraint(expr=   0.2*m.b193 - m.x306 <= 0)

m.c213 = Constraint(expr=   0.2*m.b194 - m.x307 <= 0)

m.c214 = Constraint(expr=   0.2*m.b195 - m.x308 <= 0)

m.c215 = Constraint(expr=   0.2*m.b196 - m.x306 <= 0)

m.c216 = Constraint(expr=   0.2*m.b197 - m.x307 <= 0)

m.c217 = Constraint(expr=   0.2*m.b198 - m.x308 <= 0)

m.c218 = Constraint(expr=   0.2*m.b211 - m.x309 <= 0)

m.c219 = Constraint(expr=   0.2*m.b212 - m.x310 <= 0)

m.c220 = Constraint(expr=   0.2*m.b213 - m.x311 <= 0)

m.c221 = Constraint(expr=   0.2*m.b214 - m.x309 <= 0)

m.c222 = Constraint(expr=   0.2*m.b215 - m.x310 <= 0)

m.c223 = Constraint(expr=   0.2*m.b216 - m.x311 <= 0)

m.c224 = Constraint(expr=   0.2*m.b230 - m.x312 <= 0)

m.c225 = Constraint(expr=   0.2*m.b231 - m.x313 <= 0)

m.c226 = Constraint(expr=   0.2*m.b232 - m.x314 <= 0)

m.c227 = Constraint(expr=   0.2*m.b233 - m.x312 <= 0)

m.c228 = Constraint(expr=   0.2*m.b234 - m.x313 <= 0)

m.c229 = Constraint(expr=   0.2*m.b235 - m.x314 <= 0)

m.c230 = Constraint(expr=   0.6*m.b175 - m.x315 <= -0.2)

m.c231 = Constraint(expr=   0.6*m.b176 - m.x316 <= -0.2)

m.c232 = Constraint(expr=   0.6*m.b177 - m.x317 <= -0.2)

m.c233 = Constraint(expr=   0.4*m.b178 - m.x315 <= -0.2)

m.c234 = Constraint(expr=   0.4*m.b179 - m.x316 <= -0.2)

m.c235 = Constraint(expr=   0.4*m.b180 - m.x317 <= -0.2)

m.c236 = Constraint(expr=   0.6*m.b193 - m.x318 <= -0.2)

m.c237 = Constraint(expr=   0.6*m.b194 - m.x319 <= -0.2)

m.c238 = Constraint(expr=   0.6*m.b195 - m.x320 <= -0.2)

m.c239 = Constraint(expr=   0.4*m.b196 - m.x318 <= -0.2)

m.c240 = Constraint(expr=   0.4*m.b197 - m.x319 <= -0.2)

m.c241 = Constraint(expr=   0.4*m.b198 - m.x320 <= -0.2)

m.c242 = Constraint(expr=   0.6*m.b211 - m.x321 <= -0.2)

m.c243 = Constraint(expr=   0.6*m.b212 - m.x322 <= -0.2)

m.c244 = Constraint(expr=   0.6*m.b213 - m.x323 <= -0.2)

m.c245 = Constraint(expr=   0.4*m.b214 - m.x321 <= -0.2)

m.c246 = Constraint(expr=   0.4*m.b215 - m.x322 <= -0.2)

m.c247 = Constraint(expr=   0.4*m.b216 - m.x323 <= -0.2)

m.c248 = Constraint(expr=   0.6*m.b230 - m.x324 <= -0.2)

m.c249 = Constraint(expr=   0.6*m.b231 - m.x325 <= -0.2)

m.c250 = Constraint(expr=   0.6*m.b232 - m.x326 <= -0.2)

m.c251 = Constraint(expr=   0.4*m.b233 - m.x324 <= -0.2)

m.c252 = Constraint(expr=   0.4*m.b234 - m.x325 <= -0.2)

m.c253 = Constraint(expr=   0.4*m.b235 - m.x326 <= -0.2)

m.c254 = Constraint(expr=   0.2*m.b175 - m.x327 <= -0.2)

m.c255 = Constraint(expr=   0.2*m.b176 - m.x328 <= -0.2)

m.c256 = Constraint(expr=   0.2*m.b177 - m.x329 <= -0.2)

m.c257 = Constraint(expr=   0.2*m.b178 - m.x327 <= -0.2)

m.c258 = Constraint(expr=   0.2*m.b179 - m.x328 <= -0.2)

m.c259 = Constraint(expr=   0.2*m.b180 - m.x329 <= -0.2)

m.c260 = Constraint(expr=   0.2*m.b193 - m.x330 <= -0.2)

m.c261 = Constraint(expr=   0.2*m.b194 - m.x331 <= -0.2)

m.c262 = Constraint(expr=   0.2*m.b195 - m.x332 <= -0.2)

m.c263 = Constraint(expr=   0.2*m.b196 - m.x330 <= -0.2)

m.c264 = Constraint(expr=   0.2*m.b197 - m.x331 <= -0.2)

m.c265 = Constraint(expr=   0.2*m.b198 - m.x332 <= -0.2)

m.c266 = Constraint(expr=   0.2*m.b211 - m.x333 <= -0.2)

m.c267 = Constraint(expr=   0.2*m.b212 - m.x334 <= -0.2)

m.c268 = Constraint(expr=   0.2*m.b213 - m.x335 <= -0.2)

m.c269 = Constraint(expr=   0.2*m.b214 - m.x333 <= -0.2)

m.c270 = Constraint(expr=   0.2*m.b215 - m.x334 <= -0.2)

m.c271 = Constraint(expr=   0.2*m.b216 - m.x335 <= -0.2)

m.c272 = Constraint(expr=   0.2*m.b230 - m.x336 <= -0.2)

m.c273 = Constraint(expr=   0.2*m.b231 - m.x337 <= -0.2)

m.c274 = Constraint(expr=   0.2*m.b232 - m.x338 <= -0.2)

m.c275 = Constraint(expr=   0.2*m.b233 - m.x336 <= -0.2)

m.c276 = Constraint(expr=   0.2*m.b234 - m.x337 <= -0.2)

m.c277 = Constraint(expr=   0.2*m.b235 - m.x338 <= -0.2)

m.c278 = Constraint(expr=   0.6*m.b175 - m.x339 <= 0)

m.c279 = Constraint(expr=   0.6*m.b176 - m.x340 <= 0)

m.c280 = Constraint(expr=   0.6*m.b177 - m.x341 <= 0)

m.c281 = Constraint(expr=   0.4*m.b178 - m.x339 <= 0)

m.c282 = Constraint(expr=   0.4*m.b179 - m.x340 <= 0)

m.c283 = Constraint(expr=   0.4*m.b180 - m.x341 <= 0)

m.c284 = Constraint(expr=   0.6*m.b193 - m.x342 <= 0)

m.c285 = Constraint(expr=   0.6*m.b194 - m.x343 <= 0)

m.c286 = Constraint(expr=   0.6*m.b195 - m.x344 <= 0)

m.c287 = Constraint(expr=   0.4*m.b196 - m.x342 <= 0)

m.c288 = Constraint(expr=   0.4*m.b197 - m.x343 <= 0)

m.c289 = Constraint(expr=   0.4*m.b198 - m.x344 <= 0)

m.c290 = Constraint(expr=   0.6*m.b211 - m.x345 <= 0)

m.c291 = Constraint(expr=   0.6*m.b212 - m.x346 <= 0)

m.c292 = Constraint(expr=   0.6*m.b213 - m.x347 <= 0)

m.c293 = Constraint(expr=   0.4*m.b214 - m.x345 <= 0)

m.c294 = Constraint(expr=   0.4*m.b215 - m.x346 <= 0)

m.c295 = Constraint(expr=   0.4*m.b216 - m.x347 <= 0)

m.c296 = Constraint(expr=   0.6*m.b230 - m.x348 <= 0)

m.c297 = Constraint(expr=   0.6*m.b231 - m.x349 <= 0)

m.c298 = Constraint(expr=   0.6*m.b232 - m.x350 <= 0)

m.c299 = Constraint(expr=   0.4*m.b233 - m.x348 <= 0)

m.c300 = Constraint(expr=   0.4*m.b234 - m.x349 <= 0)

m.c301 = Constraint(expr=   0.4*m.b235 - m.x350 <= 0)

m.c302 = Constraint(expr=   0.2*m.b175 - m.x351 <= -0.2)

m.c303 = Constraint(expr=   0.2*m.b176 - m.x352 <= -0.2)

m.c304 = Constraint(expr=   0.2*m.b177 - m.x353 <= -0.2)

m.c305 = Constraint(expr=   0.2*m.b178 - m.x351 <= -0.2)

m.c306 = Constraint(expr=   0.2*m.b179 - m.x352 <= -0.2)

m.c307 = Constraint(expr=   0.2*m.b180 - m.x353 <= -0.2)

m.c308 = Constraint(expr=   0.2*m.b193 - m.x354 <= -0.2)

m.c309 = Constraint(expr=   0.2*m.b194 - m.x355 <= -0.2)

m.c310 = Constraint(expr=   0.2*m.b195 - m.x356 <= -0.2)

m.c311 = Constraint(expr=   0.2*m.b196 - m.x354 <= -0.2)

m.c312 = Constraint(expr=   0.2*m.b197 - m.x355 <= -0.2)

m.c313 = Constraint(expr=   0.2*m.b198 - m.x356 <= -0.2)

m.c314 = Constraint(expr=   0.2*m.b211 - m.x357 <= -0.2)

m.c315 = Constraint(expr=   0.2*m.b212 - m.x358 <= -0.2)

m.c316 = Constraint(expr=   0.2*m.b213 - m.x359 <= -0.2)

m.c317 = Constraint(expr=   0.2*m.b214 - m.x357 <= -0.2)

m.c318 = Constraint(expr=   0.2*m.b215 - m.x358 <= -0.2)

m.c319 = Constraint(expr=   0.2*m.b216 - m.x359 <= -0.2)

m.c320 = Constraint(expr=   0.2*m.b230 - m.x360 <= -0.2)

m.c321 = Constraint(expr=   0.2*m.b231 - m.x361 <= -0.2)

m.c322 = Constraint(expr=   0.2*m.b232 - m.x362 <= -0.2)

m.c323 = Constraint(expr=   0.2*m.b233 - m.x360 <= -0.2)

m.c324 = Constraint(expr=   0.2*m.b234 - m.x361 <= -0.2)

m.c325 = Constraint(expr=   0.2*m.b235 - m.x362 <= -0.2)

m.c326 = Constraint(expr= - 0.2*m.b178 - m.x267 >= -1)

m.c327 = Constraint(expr= - 0.2*m.b179 - m.x268 >= -1)

m.c328 = Constraint(expr= - 0.2*m.b180 - m.x269 >= -1)

m.c329 = Constraint(expr= - 0.2*m.b196 - m.x270 >= -1)

m.c330 = Constraint(expr= - 0.2*m.b197 - m.x271 >= -1)

m.c331 = Constraint(expr= - 0.2*m.b198 - m.x272 >= -1)

m.c332 = Constraint(expr= - 0.2*m.b214 - m.x273 >= -1)

m.c333 = Constraint(expr= - 0.2*m.b215 - m.x274 >= -1)

m.c334 = Constraint(expr= - 0.2*m.b216 - m.x275 >= -1)

m.c335 = Constraint(expr= - 0.2*m.b233 - m.x276 >= -1)

m.c336 = Constraint(expr= - 0.2*m.b234 - m.x277 >= -1)

m.c337 = Constraint(expr= - 0.2*m.b235 - m.x278 >= -1)

m.c338 = Constraint(expr= - 0.3*m.b175 - m.x279 >= -0.9)

m.c339 = Constraint(expr= - 0.3*m.b176 - m.x280 >= -0.9)

m.c340 = Constraint(expr= - 0.3*m.b177 - m.x281 >= -0.9)

m.c341 = Constraint(expr= - 0.1*m.b178 - m.x279 >= -0.9)

m.c342 = Constraint(expr= - 0.1*m.b179 - m.x280 >= -0.9)

m.c343 = Constraint(expr= - 0.1*m.b180 - m.x281 >= -0.9)

m.c344 = Constraint(expr= - 0.3*m.b193 - m.x282 >= -0.9)

m.c345 = Constraint(expr= - 0.3*m.b194 - m.x283 >= -0.9)

m.c346 = Constraint(expr= - 0.3*m.b195 - m.x284 >= -0.9)

m.c347 = Constraint(expr= - 0.1*m.b196 - m.x282 >= -0.9)

m.c348 = Constraint(expr= - 0.1*m.b197 - m.x283 >= -0.9)

m.c349 = Constraint(expr= - 0.1*m.b198 - m.x284 >= -0.9)

m.c350 = Constraint(expr= - 0.3*m.b211 - m.x285 >= -0.9)

m.c351 = Constraint(expr= - 0.3*m.b212 - m.x286 >= -0.9)

m.c352 = Constraint(expr= - 0.3*m.b213 - m.x287 >= -0.9)

m.c353 = Constraint(expr= - 0.1*m.b214 - m.x285 >= -0.9)

m.c354 = Constraint(expr= - 0.1*m.b215 - m.x286 >= -0.9)

m.c355 = Constraint(expr= - 0.1*m.b216 - m.x287 >= -0.9)

m.c356 = Constraint(expr= - 0.3*m.b230 - m.x288 >= -0.9)

m.c357 = Constraint(expr= - 0.3*m.b231 - m.x289 >= -0.9)

m.c358 = Constraint(expr= - 0.3*m.b232 - m.x290 >= -0.9)

m.c359 = Constraint(expr= - 0.1*m.b233 - m.x288 >= -0.9)

m.c360 = Constraint(expr= - 0.1*m.b234 - m.x289 >= -0.9)

m.c361 = Constraint(expr= - 0.1*m.b235 - m.x290 >= -0.9)

m.c362 = Constraint(expr= - 0.2*m.b178 - m.x291 >= -0.9)

m.c363 = Constraint(expr= - 0.2*m.b179 - m.x292 >= -0.9)

m.c364 = Constraint(expr= - 0.2*m.b180 - m.x293 >= -0.9)

m.c365 = Constraint(expr= - 0.2*m.b196 - m.x294 >= -0.9)

m.c366 = Constraint(expr= - 0.2*m.b197 - m.x295 >= -0.9)

m.c367 = Constraint(expr= - 0.2*m.b198 - m.x296 >= -0.9)

m.c368 = Constraint(expr= - 0.2*m.b214 - m.x297 >= -0.9)

m.c369 = Constraint(expr= - 0.2*m.b215 - m.x298 >= -0.9)

m.c370 = Constraint(expr= - 0.2*m.b216 - m.x299 >= -0.9)

m.c371 = Constraint(expr= - 0.2*m.b233 - m.x300 >= -0.9)

m.c372 = Constraint(expr= - 0.2*m.b234 - m.x301 >= -0.9)

m.c373 = Constraint(expr= - 0.2*m.b235 - m.x302 >= -0.9)

m.c374 = Constraint(expr= - 0.3*m.b175 - m.x303 >= -0.8)

m.c375 = Constraint(expr= - 0.3*m.b176 - m.x304 >= -0.8)

m.c376 = Constraint(expr= - 0.3*m.b177 - m.x305 >= -0.8)

m.c377 = Constraint(expr= - 0.1*m.b178 - m.x303 >= -0.8)

m.c378 = Constraint(expr= - 0.1*m.b179 - m.x304 >= -0.8)

m.c379 = Constraint(expr= - 0.1*m.b180 - m.x305 >= -0.8)

m.c380 = Constraint(expr= - 0.3*m.b193 - m.x306 >= -0.8)

m.c381 = Constraint(expr= - 0.3*m.b194 - m.x307 >= -0.8)

m.c382 = Constraint(expr= - 0.3*m.b195 - m.x308 >= -0.8)

m.c383 = Constraint(expr= - 0.1*m.b196 - m.x306 >= -0.8)

m.c384 = Constraint(expr= - 0.1*m.b197 - m.x307 >= -0.8)

m.c385 = Constraint(expr= - 0.1*m.b198 - m.x308 >= -0.8)

m.c386 = Constraint(expr= - 0.3*m.b211 - m.x309 >= -0.8)

m.c387 = Constraint(expr= - 0.3*m.b212 - m.x310 >= -0.8)

m.c388 = Constraint(expr= - 0.3*m.b213 - m.x311 >= -0.8)

m.c389 = Constraint(expr= - 0.1*m.b214 - m.x309 >= -0.8)

m.c390 = Constraint(expr= - 0.1*m.b215 - m.x310 >= -0.8)

m.c391 = Constraint(expr= - 0.1*m.b216 - m.x311 >= -0.8)

m.c392 = Constraint(expr= - 0.3*m.b230 - m.x312 >= -0.8)

m.c393 = Constraint(expr= - 0.3*m.b231 - m.x313 >= -0.8)

m.c394 = Constraint(expr= - 0.3*m.b232 - m.x314 >= -0.8)

m.c395 = Constraint(expr= - 0.1*m.b233 - m.x312 >= -0.8)

m.c396 = Constraint(expr= - 0.1*m.b234 - m.x313 >= -0.8)

m.c397 = Constraint(expr= - 0.1*m.b235 - m.x314 >= -0.8)

m.c398 = Constraint(expr= - 0.1*m.b178 - m.x315 >= -1)

m.c399 = Constraint(expr= - 0.1*m.b179 - m.x316 >= -1)

m.c400 = Constraint(expr= - 0.1*m.b180 - m.x317 >= -1)

m.c401 = Constraint(expr= - 0.1*m.b196 - m.x318 >= -1)

m.c402 = Constraint(expr= - 0.1*m.b197 - m.x319 >= -1)

m.c403 = Constraint(expr= - 0.1*m.b198 - m.x320 >= -1)

m.c404 = Constraint(expr= - 0.1*m.b214 - m.x321 >= -1)

m.c405 = Constraint(expr= - 0.1*m.b215 - m.x322 >= -1)

m.c406 = Constraint(expr= - 0.1*m.b216 - m.x323 >= -1)

m.c407 = Constraint(expr= - 0.1*m.b233 - m.x324 >= -1)

m.c408 = Constraint(expr= - 0.1*m.b234 - m.x325 >= -1)

m.c409 = Constraint(expr= - 0.1*m.b235 - m.x326 >= -1)

m.c410 = Constraint(expr= - 0.3*m.b175 - m.x327 >= -1)

m.c411 = Constraint(expr= - 0.3*m.b176 - m.x328 >= -1)

m.c412 = Constraint(expr= - 0.3*m.b177 - m.x329 >= -1)

m.c413 = Constraint(expr= - 0.1*m.b178 - m.x327 >= -1)

m.c414 = Constraint(expr= - 0.1*m.b179 - m.x328 >= -1)

m.c415 = Constraint(expr= - 0.1*m.b180 - m.x329 >= -1)

m.c416 = Constraint(expr= - 0.3*m.b193 - m.x330 >= -1)

m.c417 = Constraint(expr= - 0.3*m.b194 - m.x331 >= -1)

m.c418 = Constraint(expr= - 0.3*m.b195 - m.x332 >= -1)

m.c419 = Constraint(expr= - 0.1*m.b196 - m.x330 >= -1)

m.c420 = Constraint(expr= - 0.1*m.b197 - m.x331 >= -1)

m.c421 = Constraint(expr= - 0.1*m.b198 - m.x332 >= -1)

m.c422 = Constraint(expr= - 0.3*m.b211 - m.x333 >= -1)

m.c423 = Constraint(expr= - 0.3*m.b212 - m.x334 >= -1)

m.c424 = Constraint(expr= - 0.3*m.b213 - m.x335 >= -1)

m.c425 = Constraint(expr= - 0.1*m.b214 - m.x333 >= -1)

m.c426 = Constraint(expr= - 0.1*m.b215 - m.x334 >= -1)

m.c427 = Constraint(expr= - 0.1*m.b216 - m.x335 >= -1)

m.c428 = Constraint(expr= - 0.3*m.b230 - m.x336 >= -1)

m.c429 = Constraint(expr= - 0.3*m.b231 - m.x337 >= -1)

m.c430 = Constraint(expr= - 0.3*m.b232 - m.x338 >= -1)

m.c431 = Constraint(expr= - 0.1*m.b233 - m.x336 >= -1)

m.c432 = Constraint(expr= - 0.1*m.b234 - m.x337 >= -1)

m.c433 = Constraint(expr= - 0.1*m.b235 - m.x338 >= -1)

m.c434 = Constraint(expr= - 0.2*m.b178 - m.x339 >= -0.9)

m.c435 = Constraint(expr= - 0.2*m.b179 - m.x340 >= -0.9)

m.c436 = Constraint(expr= - 0.2*m.b180 - m.x341 >= -0.9)

m.c437 = Constraint(expr= - 0.2*m.b196 - m.x342 >= -0.9)

m.c438 = Constraint(expr= - 0.2*m.b197 - m.x343 >= -0.9)

m.c439 = Constraint(expr= - 0.2*m.b198 - m.x344 >= -0.9)

m.c440 = Constraint(expr= - 0.2*m.b214 - m.x345 >= -0.9)

m.c441 = Constraint(expr= - 0.2*m.b215 - m.x346 >= -0.9)

m.c442 = Constraint(expr= - 0.2*m.b216 - m.x347 >= -0.9)

m.c443 = Constraint(expr= - 0.2*m.b233 - m.x348 >= -0.9)

m.c444 = Constraint(expr= - 0.2*m.b234 - m.x349 >= -0.9)

m.c445 = Constraint(expr= - 0.2*m.b235 - m.x350 >= -0.9)

m.c446 = Constraint(expr= - 0.3*m.b175 - m.x351 >= -1)

m.c447 = Constraint(expr= - 0.3*m.b176 - m.x352 >= -1)

m.c448 = Constraint(expr= - 0.3*m.b177 - m.x353 >= -1)

m.c449 = Constraint(expr= - 0.1*m.b178 - m.x351 >= -1)

m.c450 = Constraint(expr= - 0.1*m.b179 - m.x352 >= -1)

m.c451 = Constraint(expr= - 0.1*m.b180 - m.x353 >= -1)

m.c452 = Constraint(expr= - 0.3*m.b193 - m.x354 >= -1)

m.c453 = Constraint(expr= - 0.3*m.b194 - m.x355 >= -1)

m.c454 = Constraint(expr= - 0.3*m.b195 - m.x356 >= -1)

m.c455 = Constraint(expr= - 0.1*m.b196 - m.x354 >= -1)

m.c456 = Constraint(expr= - 0.1*m.b197 - m.x355 >= -1)

m.c457 = Constraint(expr= - 0.1*m.b198 - m.x356 >= -1)

m.c458 = Constraint(expr= - 0.3*m.b211 - m.x357 >= -1)

m.c459 = Constraint(expr= - 0.3*m.b212 - m.x358 >= -1)

m.c460 = Constraint(expr= - 0.3*m.b213 - m.x359 >= -1)

m.c461 = Constraint(expr= - 0.1*m.b214 - m.x357 >= -1)

m.c462 = Constraint(expr= - 0.1*m.b215 - m.x358 >= -1)

m.c463 = Constraint(expr= - 0.1*m.b216 - m.x359 >= -1)

m.c464 = Constraint(expr= - 0.3*m.b230 - m.x360 >= -1)

m.c465 = Constraint(expr= - 0.3*m.b231 - m.x361 >= -1)

m.c466 = Constraint(expr= - 0.3*m.b232 - m.x362 >= -1)

m.c467 = Constraint(expr= - 0.1*m.b233 - m.x360 >= -1)

m.c468 = Constraint(expr= - 0.1*m.b234 - m.x361 >= -1)

m.c469 = Constraint(expr= - 0.1*m.b235 - m.x362 >= -1)

m.c470 = Constraint(expr=   m.b147 + m.b163 <= 1)

m.c471 = Constraint(expr=   m.b148 + m.b164 <= 1)

m.c472 = Constraint(expr=   m.b149 + m.b165 <= 1)

m.c473 = Constraint(expr=   m.b150 + m.b166 <= 1)

m.c474 = Constraint(expr=   m.b147 + m.b167 <= 1)

m.c475 = Constraint(expr=   m.b148 + m.b168 <= 1)

m.c476 = Constraint(expr=   m.b149 + m.b169 <= 1)

m.c477 = Constraint(expr=   m.b150 + m.b170 <= 1)

m.c478 = Constraint(expr=   m.b147 + m.b171 <= 1)

m.c479 = Constraint(expr=   m.b148 + m.b172 <= 1)

m.c480 = Constraint(expr=   m.b149 + m.b173 <= 1)

m.c481 = Constraint(expr=   m.b150 + m.b174 <= 1)

m.c482 = Constraint(expr=   m.b148 + m.b175 <= 1)

m.c483 = Constraint(expr=   m.b149 + m.b176 <= 1)

m.c484 = Constraint(expr=   m.b150 + m.b177 <= 1)

m.c485 = Constraint(expr=   m.b148 + m.b178 <= 1)

m.c486 = Constraint(expr=   m.b149 + m.b179 <= 1)

m.c487 = Constraint(expr=   m.b150 + m.b180 <= 1)

m.c488 = Constraint(expr=   m.b163 + m.b181 <= 1)

m.c489 = Constraint(expr=   m.b164 + m.b182 <= 1)

m.c490 = Constraint(expr=   m.b165 + m.b183 <= 1)

m.c491 = Constraint(expr=   m.b166 + m.b184 <= 1)

m.c492 = Constraint(expr=   m.b167 + m.b181 <= 1)

m.c493 = Constraint(expr=   m.b168 + m.b182 <= 1)

m.c494 = Constraint(expr=   m.b169 + m.b183 <= 1)

m.c495 = Constraint(expr=   m.b170 + m.b184 <= 1)

m.c496 = Constraint(expr=   m.b171 + m.b181 <= 1)

m.c497 = Constraint(expr=   m.b172 + m.b182 <= 1)

m.c498 = Constraint(expr=   m.b173 + m.b183 <= 1)

m.c499 = Constraint(expr=   m.b174 + m.b184 <= 1)

m.c500 = Constraint(expr=   m.b175 + m.b182 <= 1)

m.c501 = Constraint(expr=   m.b176 + m.b183 <= 1)

m.c502 = Constraint(expr=   m.b177 + m.b184 <= 1)

m.c503 = Constraint(expr=   m.b178 + m.b182 <= 1)

m.c504 = Constraint(expr=   m.b179 + m.b183 <= 1)

m.c505 = Constraint(expr=   m.b180 + m.b184 <= 1)

m.c506 = Constraint(expr=   m.b163 + m.b199 <= 1)

m.c507 = Constraint(expr=   m.b164 + m.b200 <= 1)

m.c508 = Constraint(expr=   m.b165 + m.b201 <= 1)

m.c509 = Constraint(expr=   m.b166 + m.b202 <= 1)

m.c510 = Constraint(expr=   m.b167 + m.b199 <= 1)

m.c511 = Constraint(expr=   m.b168 + m.b200 <= 1)

m.c512 = Constraint(expr=   m.b169 + m.b201 <= 1)

m.c513 = Constraint(expr=   m.b170 + m.b202 <= 1)

m.c514 = Constraint(expr=   m.b171 + m.b199 <= 1)

m.c515 = Constraint(expr=   m.b172 + m.b200 <= 1)

m.c516 = Constraint(expr=   m.b173 + m.b201 <= 1)

m.c517 = Constraint(expr=   m.b174 + m.b202 <= 1)

m.c518 = Constraint(expr=   m.b175 + m.b200 <= 1)

m.c519 = Constraint(expr=   m.b176 + m.b201 <= 1)

m.c520 = Constraint(expr=   m.b177 + m.b202 <= 1)

m.c521 = Constraint(expr=   m.b178 + m.b200 <= 1)

m.c522 = Constraint(expr=   m.b179 + m.b201 <= 1)

m.c523 = Constraint(expr=   m.b180 + m.b202 <= 1)

m.c524 = Constraint(expr=   m.b163 + m.b217 <= 1)

m.c525 = Constraint(expr=   m.b164 + m.b218 <= 1)

m.c526 = Constraint(expr=   m.b165 + m.b219 <= 1)

m.c527 = Constraint(expr=   m.b166 + m.b220 <= 1)

m.c528 = Constraint(expr=   m.b167 + m.b217 <= 1)

m.c529 = Constraint(expr=   m.b168 + m.b218 <= 1)

m.c530 = Constraint(expr=   m.b169 + m.b219 <= 1)

m.c531 = Constraint(expr=   m.b170 + m.b220 <= 1)

m.c532 = Constraint(expr=   m.b171 + m.b217 <= 1)

m.c533 = Constraint(expr=   m.b172 + m.b218 <= 1)

m.c534 = Constraint(expr=   m.b173 + m.b219 <= 1)

m.c535 = Constraint(expr=   m.b174 + m.b220 <= 1)

m.c536 = Constraint(expr=   m.b175 + m.b218 <= 1)

m.c537 = Constraint(expr=   m.b176 + m.b219 <= 1)

m.c538 = Constraint(expr=   m.b177 + m.b220 <= 1)

m.c539 = Constraint(expr=   m.b178 + m.b218 <= 1)

m.c540 = Constraint(expr=   m.b179 + m.b219 <= 1)

m.c541 = Constraint(expr=   m.b180 + m.b220 <= 1)

m.c542 = Constraint(expr=   m.b135 + m.b181 <= 1)

m.c543 = Constraint(expr=   m.b136 + m.b182 <= 1)

m.c544 = Constraint(expr=   m.b137 + m.b183 <= 1)

m.c545 = Constraint(expr=   m.b138 + m.b184 <= 1)

m.c546 = Constraint(expr=   m.b135 + m.b185 <= 1)

m.c547 = Constraint(expr=   m.b136 + m.b186 <= 1)

m.c548 = Constraint(expr=   m.b137 + m.b187 <= 1)

m.c549 = Constraint(expr=   m.b138 + m.b188 <= 1)

m.c550 = Constraint(expr=   m.b135 + m.b189 <= 1)

m.c551 = Constraint(expr=   m.b136 + m.b190 <= 1)

m.c552 = Constraint(expr=   m.b137 + m.b191 <= 1)

m.c553 = Constraint(expr=   m.b138 + m.b192 <= 1)

m.c554 = Constraint(expr=   m.b136 + m.b193 <= 1)

m.c555 = Constraint(expr=   m.b137 + m.b194 <= 1)

m.c556 = Constraint(expr=   m.b138 + m.b195 <= 1)

m.c557 = Constraint(expr=   m.b136 + m.b196 <= 1)

m.c558 = Constraint(expr=   m.b137 + m.b197 <= 1)

m.c559 = Constraint(expr=   m.b138 + m.b198 <= 1)

m.c560 = Constraint(expr=   m.b151 + m.b181 <= 1)

m.c561 = Constraint(expr=   m.b152 + m.b182 <= 1)

m.c562 = Constraint(expr=   m.b153 + m.b183 <= 1)

m.c563 = Constraint(expr=   m.b154 + m.b184 <= 1)

m.c564 = Constraint(expr=   m.b151 + m.b185 <= 1)

m.c565 = Constraint(expr=   m.b152 + m.b186 <= 1)

m.c566 = Constraint(expr=   m.b153 + m.b187 <= 1)

m.c567 = Constraint(expr=   m.b154 + m.b188 <= 1)

m.c568 = Constraint(expr=   m.b151 + m.b189 <= 1)

m.c569 = Constraint(expr=   m.b152 + m.b190 <= 1)

m.c570 = Constraint(expr=   m.b153 + m.b191 <= 1)

m.c571 = Constraint(expr=   m.b154 + m.b192 <= 1)

m.c572 = Constraint(expr=   m.b152 + m.b193 <= 1)

m.c573 = Constraint(expr=   m.b153 + m.b194 <= 1)

m.c574 = Constraint(expr=   m.b154 + m.b195 <= 1)

m.c575 = Constraint(expr=   m.b152 + m.b196 <= 1)

m.c576 = Constraint(expr=   m.b153 + m.b197 <= 1)

m.c577 = Constraint(expr=   m.b154 + m.b198 <= 1)

m.c578 = Constraint(expr=   m.b163 + m.b181 <= 1)

m.c579 = Constraint(expr=   m.b164 + m.b182 <= 1)

m.c580 = Constraint(expr=   m.b165 + m.b183 <= 1)

m.c581 = Constraint(expr=   m.b166 + m.b184 <= 1)

m.c582 = Constraint(expr=   m.b163 + m.b185 <= 1)

m.c583 = Constraint(expr=   m.b164 + m.b186 <= 1)

m.c584 = Constraint(expr=   m.b165 + m.b187 <= 1)

m.c585 = Constraint(expr=   m.b166 + m.b188 <= 1)

m.c586 = Constraint(expr=   m.b163 + m.b189 <= 1)

m.c587 = Constraint(expr=   m.b164 + m.b190 <= 1)

m.c588 = Constraint(expr=   m.b165 + m.b191 <= 1)

m.c589 = Constraint(expr=   m.b166 + m.b192 <= 1)

m.c590 = Constraint(expr=   m.b164 + m.b193 <= 1)

m.c591 = Constraint(expr=   m.b165 + m.b194 <= 1)

m.c592 = Constraint(expr=   m.b166 + m.b195 <= 1)

m.c593 = Constraint(expr=   m.b164 + m.b196 <= 1)

m.c594 = Constraint(expr=   m.b165 + m.b197 <= 1)

m.c595 = Constraint(expr=   m.b166 + m.b198 <= 1)

m.c596 = Constraint(expr=   m.b181 + m.b203 <= 1)

m.c597 = Constraint(expr=   m.b182 + m.b204 <= 1)

m.c598 = Constraint(expr=   m.b183 + m.b205 <= 1)

m.c599 = Constraint(expr=   m.b184 + m.b206 <= 1)

m.c600 = Constraint(expr=   m.b185 + m.b203 <= 1)

m.c601 = Constraint(expr=   m.b186 + m.b204 <= 1)

m.c602 = Constraint(expr=   m.b187 + m.b205 <= 1)

m.c603 = Constraint(expr=   m.b188 + m.b206 <= 1)

m.c604 = Constraint(expr=   m.b189 + m.b203 <= 1)

m.c605 = Constraint(expr=   m.b190 + m.b204 <= 1)

m.c606 = Constraint(expr=   m.b191 + m.b205 <= 1)

m.c607 = Constraint(expr=   m.b192 + m.b206 <= 1)

m.c608 = Constraint(expr=   m.b193 + m.b204 <= 1)

m.c609 = Constraint(expr=   m.b194 + m.b205 <= 1)

m.c610 = Constraint(expr=   m.b195 + m.b206 <= 1)

m.c611 = Constraint(expr=   m.b196 + m.b204 <= 1)

m.c612 = Constraint(expr=   m.b197 + m.b205 <= 1)

m.c613 = Constraint(expr=   m.b198 + m.b206 <= 1)

m.c614 = Constraint(expr=   m.b181 + m.b221 <= 1)

m.c615 = Constraint(expr=   m.b182 + m.b222 <= 1)

m.c616 = Constraint(expr=   m.b183 + m.b223 <= 1)

m.c617 = Constraint(expr=   m.b184 + m.b224 <= 1)

m.c618 = Constraint(expr=   m.b185 + m.b221 <= 1)

m.c619 = Constraint(expr=   m.b186 + m.b222 <= 1)

m.c620 = Constraint(expr=   m.b187 + m.b223 <= 1)

m.c621 = Constraint(expr=   m.b188 + m.b224 <= 1)

m.c622 = Constraint(expr=   m.b189 + m.b221 <= 1)

m.c623 = Constraint(expr=   m.b190 + m.b222 <= 1)

m.c624 = Constraint(expr=   m.b191 + m.b223 <= 1)

m.c625 = Constraint(expr=   m.b192 + m.b224 <= 1)

m.c626 = Constraint(expr=   m.b193 + m.b222 <= 1)

m.c627 = Constraint(expr=   m.b194 + m.b223 <= 1)

m.c628 = Constraint(expr=   m.b195 + m.b224 <= 1)

m.c629 = Constraint(expr=   m.b196 + m.b222 <= 1)

m.c630 = Constraint(expr=   m.b197 + m.b223 <= 1)

m.c631 = Constraint(expr=   m.b198 + m.b224 <= 1)

m.c632 = Constraint(expr=   m.b139 + m.b199 <= 1)

m.c633 = Constraint(expr=   m.b140 + m.b200 <= 1)

m.c634 = Constraint(expr=   m.b141 + m.b201 <= 1)

m.c635 = Constraint(expr=   m.b142 + m.b202 <= 1)

m.c636 = Constraint(expr=   m.b139 + m.b203 <= 1)

m.c637 = Constraint(expr=   m.b140 + m.b204 <= 1)

m.c638 = Constraint(expr=   m.b141 + m.b205 <= 1)

m.c639 = Constraint(expr=   m.b142 + m.b206 <= 1)

m.c640 = Constraint(expr=   m.b139 + m.b207 <= 1)

m.c641 = Constraint(expr=   m.b140 + m.b208 <= 1)

m.c642 = Constraint(expr=   m.b141 + m.b209 <= 1)

m.c643 = Constraint(expr=   m.b142 + m.b210 <= 1)

m.c644 = Constraint(expr=   m.b140 + m.b211 <= 1)

m.c645 = Constraint(expr=   m.b141 + m.b212 <= 1)

m.c646 = Constraint(expr=   m.b142 + m.b213 <= 1)

m.c647 = Constraint(expr=   m.b140 + m.b214 <= 1)

m.c648 = Constraint(expr=   m.b141 + m.b215 <= 1)

m.c649 = Constraint(expr=   m.b142 + m.b216 <= 1)

m.c650 = Constraint(expr=   m.b155 + m.b199 <= 1)

m.c651 = Constraint(expr=   m.b156 + m.b200 <= 1)

m.c652 = Constraint(expr=   m.b157 + m.b201 <= 1)

m.c653 = Constraint(expr=   m.b158 + m.b202 <= 1)

m.c654 = Constraint(expr=   m.b155 + m.b203 <= 1)

m.c655 = Constraint(expr=   m.b156 + m.b204 <= 1)

m.c656 = Constraint(expr=   m.b157 + m.b205 <= 1)

m.c657 = Constraint(expr=   m.b158 + m.b206 <= 1)

m.c658 = Constraint(expr=   m.b155 + m.b207 <= 1)

m.c659 = Constraint(expr=   m.b156 + m.b208 <= 1)

m.c660 = Constraint(expr=   m.b157 + m.b209 <= 1)

m.c661 = Constraint(expr=   m.b158 + m.b210 <= 1)

m.c662 = Constraint(expr=   m.b156 + m.b211 <= 1)

m.c663 = Constraint(expr=   m.b157 + m.b212 <= 1)

m.c664 = Constraint(expr=   m.b158 + m.b213 <= 1)

m.c665 = Constraint(expr=   m.b156 + m.b214 <= 1)

m.c666 = Constraint(expr=   m.b157 + m.b215 <= 1)

m.c667 = Constraint(expr=   m.b158 + m.b216 <= 1)

m.c668 = Constraint(expr=   m.b167 + m.b199 <= 1)

m.c669 = Constraint(expr=   m.b168 + m.b200 <= 1)

m.c670 = Constraint(expr=   m.b169 + m.b201 <= 1)

m.c671 = Constraint(expr=   m.b170 + m.b202 <= 1)

m.c672 = Constraint(expr=   m.b167 + m.b203 <= 1)

m.c673 = Constraint(expr=   m.b168 + m.b204 <= 1)

m.c674 = Constraint(expr=   m.b169 + m.b205 <= 1)

m.c675 = Constraint(expr=   m.b170 + m.b206 <= 1)

m.c676 = Constraint(expr=   m.b167 + m.b207 <= 1)

m.c677 = Constraint(expr=   m.b168 + m.b208 <= 1)

m.c678 = Constraint(expr=   m.b169 + m.b209 <= 1)

m.c679 = Constraint(expr=   m.b170 + m.b210 <= 1)

m.c680 = Constraint(expr=   m.b168 + m.b211 <= 1)

m.c681 = Constraint(expr=   m.b169 + m.b212 <= 1)

m.c682 = Constraint(expr=   m.b170 + m.b213 <= 1)

m.c683 = Constraint(expr=   m.b168 + m.b214 <= 1)

m.c684 = Constraint(expr=   m.b169 + m.b215 <= 1)

m.c685 = Constraint(expr=   m.b170 + m.b216 <= 1)

m.c686 = Constraint(expr=   m.b185 + m.b199 <= 1)

m.c687 = Constraint(expr=   m.b186 + m.b200 <= 1)

m.c688 = Constraint(expr=   m.b187 + m.b201 <= 1)

m.c689 = Constraint(expr=   m.b188 + m.b202 <= 1)

m.c690 = Constraint(expr=   m.b185 + m.b203 <= 1)

m.c691 = Constraint(expr=   m.b186 + m.b204 <= 1)

m.c692 = Constraint(expr=   m.b187 + m.b205 <= 1)

m.c693 = Constraint(expr=   m.b188 + m.b206 <= 1)

m.c694 = Constraint(expr=   m.b185 + m.b207 <= 1)

m.c695 = Constraint(expr=   m.b186 + m.b208 <= 1)

m.c696 = Constraint(expr=   m.b187 + m.b209 <= 1)

m.c697 = Constraint(expr=   m.b188 + m.b210 <= 1)

m.c698 = Constraint(expr=   m.b186 + m.b211 <= 1)

m.c699 = Constraint(expr=   m.b187 + m.b212 <= 1)

m.c700 = Constraint(expr=   m.b188 + m.b213 <= 1)

m.c701 = Constraint(expr=   m.b186 + m.b214 <= 1)

m.c702 = Constraint(expr=   m.b187 + m.b215 <= 1)

m.c703 = Constraint(expr=   m.b188 + m.b216 <= 1)

m.c704 = Constraint(expr=   m.b199 + m.b225 <= 1)

m.c705 = Constraint(expr=   m.b200 + m.b226 <= 1)

m.c706 = Constraint(expr=   m.b201 + m.b227 <= 1)

m.c707 = Constraint(expr=   m.b202 + m.b228 <= 1)

m.c708 = Constraint(expr=   m.b203 + m.b225 <= 1)

m.c709 = Constraint(expr=   m.b204 + m.b226 <= 1)

m.c710 = Constraint(expr=   m.b205 + m.b227 <= 1)

m.c711 = Constraint(expr=   m.b206 + m.b228 <= 1)

m.c712 = Constraint(expr=   m.b207 + m.b225 <= 1)

m.c713 = Constraint(expr=   m.b208 + m.b226 <= 1)

m.c714 = Constraint(expr=   m.b209 + m.b227 <= 1)

m.c715 = Constraint(expr=   m.b210 + m.b228 <= 1)

m.c716 = Constraint(expr=   m.b211 + m.b226 <= 1)

m.c717 = Constraint(expr=   m.b212 + m.b227 <= 1)

m.c718 = Constraint(expr=   m.b213 + m.b228 <= 1)

m.c719 = Constraint(expr=   m.b214 + m.b226 <= 1)

m.c720 = Constraint(expr=   m.b215 + m.b227 <= 1)

m.c721 = Constraint(expr=   m.b216 + m.b228 <= 1)

m.c722 = Constraint(expr=   m.b143 + m.b217 <= 1)

m.c723 = Constraint(expr=   m.b144 + m.b218 <= 1)

m.c724 = Constraint(expr=   m.b145 + m.b219 <= 1)

m.c725 = Constraint(expr=   m.b146 + m.b220 <= 1)

m.c726 = Constraint(expr=   m.b143 + m.b221 <= 1)

m.c727 = Constraint(expr=   m.b144 + m.b222 <= 1)

m.c728 = Constraint(expr=   m.b145 + m.b223 <= 1)

m.c729 = Constraint(expr=   m.b146 + m.b224 <= 1)

m.c730 = Constraint(expr=   m.b143 + m.b225 <= 1)

m.c731 = Constraint(expr=   m.b144 + m.b226 <= 1)

m.c732 = Constraint(expr=   m.b145 + m.b227 <= 1)

m.c733 = Constraint(expr=   m.b146 + m.b228 <= 1)

m.c734 = Constraint(expr=   m.b143 + m.b229 <= 1)

m.c735 = Constraint(expr=   m.b144 + m.b230 <= 1)

m.c736 = Constraint(expr=   m.b145 + m.b231 <= 1)

m.c737 = Constraint(expr=   m.b146 + m.b232 <= 1)

m.c738 = Constraint(expr=   m.b144 + m.b233 <= 1)

m.c739 = Constraint(expr=   m.b145 + m.b234 <= 1)

m.c740 = Constraint(expr=   m.b146 + m.b235 <= 1)

m.c741 = Constraint(expr=   m.b159 + m.b217 <= 1)

m.c742 = Constraint(expr=   m.b160 + m.b218 <= 1)

m.c743 = Constraint(expr=   m.b161 + m.b219 <= 1)

m.c744 = Constraint(expr=   m.b162 + m.b220 <= 1)

m.c745 = Constraint(expr=   m.b159 + m.b221 <= 1)

m.c746 = Constraint(expr=   m.b160 + m.b222 <= 1)

m.c747 = Constraint(expr=   m.b161 + m.b223 <= 1)

m.c748 = Constraint(expr=   m.b162 + m.b224 <= 1)

m.c749 = Constraint(expr=   m.b159 + m.b225 <= 1)

m.c750 = Constraint(expr=   m.b160 + m.b226 <= 1)

m.c751 = Constraint(expr=   m.b161 + m.b227 <= 1)

m.c752 = Constraint(expr=   m.b162 + m.b228 <= 1)

m.c753 = Constraint(expr=   m.b159 + m.b229 <= 1)

m.c754 = Constraint(expr=   m.b160 + m.b230 <= 1)

m.c755 = Constraint(expr=   m.b161 + m.b231 <= 1)

m.c756 = Constraint(expr=   m.b162 + m.b232 <= 1)

m.c757 = Constraint(expr=   m.b160 + m.b233 <= 1)

m.c758 = Constraint(expr=   m.b161 + m.b234 <= 1)

m.c759 = Constraint(expr=   m.b162 + m.b235 <= 1)

m.c760 = Constraint(expr=   m.b171 + m.b217 <= 1)

m.c761 = Constraint(expr=   m.b172 + m.b218 <= 1)

m.c762 = Constraint(expr=   m.b173 + m.b219 <= 1)

m.c763 = Constraint(expr=   m.b174 + m.b220 <= 1)

m.c764 = Constraint(expr=   m.b171 + m.b221 <= 1)

m.c765 = Constraint(expr=   m.b172 + m.b222 <= 1)

m.c766 = Constraint(expr=   m.b173 + m.b223 <= 1)

m.c767 = Constraint(expr=   m.b174 + m.b224 <= 1)

m.c768 = Constraint(expr=   m.b171 + m.b225 <= 1)

m.c769 = Constraint(expr=   m.b172 + m.b226 <= 1)

m.c770 = Constraint(expr=   m.b173 + m.b227 <= 1)

m.c771 = Constraint(expr=   m.b174 + m.b228 <= 1)

m.c772 = Constraint(expr=   m.b171 + m.b229 <= 1)

m.c773 = Constraint(expr=   m.b172 + m.b230 <= 1)

m.c774 = Constraint(expr=   m.b173 + m.b231 <= 1)

m.c775 = Constraint(expr=   m.b174 + m.b232 <= 1)

m.c776 = Constraint(expr=   m.b172 + m.b233 <= 1)

m.c777 = Constraint(expr=   m.b173 + m.b234 <= 1)

m.c778 = Constraint(expr=   m.b174 + m.b235 <= 1)

m.c779 = Constraint(expr=   m.b189 + m.b217 <= 1)

m.c780 = Constraint(expr=   m.b190 + m.b218 <= 1)

m.c781 = Constraint(expr=   m.b191 + m.b219 <= 1)

m.c782 = Constraint(expr=   m.b192 + m.b220 <= 1)

m.c783 = Constraint(expr=   m.b189 + m.b221 <= 1)

m.c784 = Constraint(expr=   m.b190 + m.b222 <= 1)

m.c785 = Constraint(expr=   m.b191 + m.b223 <= 1)

m.c786 = Constraint(expr=   m.b192 + m.b224 <= 1)

m.c787 = Constraint(expr=   m.b189 + m.b225 <= 1)

m.c788 = Constraint(expr=   m.b190 + m.b226 <= 1)

m.c789 = Constraint(expr=   m.b191 + m.b227 <= 1)

m.c790 = Constraint(expr=   m.b192 + m.b228 <= 1)

m.c791 = Constraint(expr=   m.b189 + m.b229 <= 1)

m.c792 = Constraint(expr=   m.b190 + m.b230 <= 1)

m.c793 = Constraint(expr=   m.b191 + m.b231 <= 1)

m.c794 = Constraint(expr=   m.b192 + m.b232 <= 1)

m.c795 = Constraint(expr=   m.b190 + m.b233 <= 1)

m.c796 = Constraint(expr=   m.b191 + m.b234 <= 1)

m.c797 = Constraint(expr=   m.b192 + m.b235 <= 1)

m.c798 = Constraint(expr=   m.b207 + m.b217 <= 1)

m.c799 = Constraint(expr=   m.b208 + m.b218 <= 1)

m.c800 = Constraint(expr=   m.b209 + m.b219 <= 1)

m.c801 = Constraint(expr=   m.b210 + m.b220 <= 1)

m.c802 = Constraint(expr=   m.b207 + m.b221 <= 1)

m.c803 = Constraint(expr=   m.b208 + m.b222 <= 1)

m.c804 = Constraint(expr=   m.b209 + m.b223 <= 1)

m.c805 = Constraint(expr=   m.b210 + m.b224 <= 1)

m.c806 = Constraint(expr=   m.b207 + m.b225 <= 1)

m.c807 = Constraint(expr=   m.b208 + m.b226 <= 1)

m.c808 = Constraint(expr=   m.b209 + m.b227 <= 1)

m.c809 = Constraint(expr=   m.b210 + m.b228 <= 1)

m.c810 = Constraint(expr=   m.b207 + m.b229 <= 1)

m.c811 = Constraint(expr=   m.b208 + m.b230 <= 1)

m.c812 = Constraint(expr=   m.b209 + m.b231 <= 1)

m.c813 = Constraint(expr=   m.b210 + m.b232 <= 1)

m.c814 = Constraint(expr=   m.b208 + m.b233 <= 1)

m.c815 = Constraint(expr=   m.b209 + m.b234 <= 1)

m.c816 = Constraint(expr=   m.b210 + m.b235 <= 1)

m.c817 = Constraint(expr=m.x267*m.x238 - 0.9*m.x14 + 0.4*m.x30 + 0.4*m.x34 + 0.4*m.x38 - 0.4*m.x48 - 0.1*m.x66 - m.x84
                          == 0.4)

m.c818 = Constraint(expr=m.x270*m.x239 - 0.1*m.x2 - 0.9*m.x18 - 0.4*m.x30 + 0.4*m.x48 + 0.4*m.x52 + 0.4*m.x56
                          - 0.1*m.x70 - m.x88 == 0.32)

m.c819 = Constraint(expr=m.x273*m.x240 - 0.1*m.x6 - 0.9*m.x22 - 0.4*m.x34 - 0.4*m.x52 + 0.1*m.x66 + 0.1*m.x70
                          + 0.1*m.x74 - m.x92 == 0.02)

m.c820 = Constraint(expr=m.x276*m.x241 - 0.1*m.x10 - 0.9*m.x26 - 0.4*m.x38 - 0.4*m.x56 - 0.1*m.x74 + m.x84 + m.x88
                          + m.x92 + m.x96 == 0.5)

m.c821 = Constraint(expr=m.x279*m.x238 - 0.8*m.x14 + 0.2*m.x30 + 0.2*m.x34 + 0.2*m.x38 - 0.1*m.x48 - 0.9*m.x66
                          - 0.6*m.x84 == 0.2)

m.c822 = Constraint(expr=m.x282*m.x239 - 0.2*m.x2 - 0.8*m.x18 - 0.2*m.x30 + 0.1*m.x48 + 0.1*m.x52 + 0.1*m.x56
                          - 0.9*m.x70 - 0.6*m.x88 == 0.08)

m.c823 = Constraint(expr=m.x285*m.x240 - 0.2*m.x6 - 0.8*m.x22 - 0.2*m.x34 - 0.1*m.x52 + 0.9*m.x66 + 0.9*m.x70
                          + 0.9*m.x74 - 0.6*m.x92 == 0.18)

m.c824 = Constraint(expr=m.x288*m.x241 - 0.2*m.x10 - 0.8*m.x26 - 0.2*m.x38 - 0.1*m.x56 - 0.9*m.x74 + 0.6*m.x84
                          + 0.6*m.x88 + 0.6*m.x92 + 0.6*m.x96 == 0.3)

m.c825 = Constraint(expr=m.x291*m.x238 - 0.8*m.x14 + 0.3*m.x30 + 0.3*m.x34 + 0.3*m.x38 - 0.3*m.x48 - 0.9*m.x84 == 0.3)

m.c826 = Constraint(expr=m.x294*m.x239 - 0.8*m.x18 - 0.3*m.x30 + 0.3*m.x48 + 0.3*m.x52 + 0.3*m.x56 - 0.9*m.x88 == 0.24)

m.c827 = Constraint(expr=m.x297*m.x240 - 0.8*m.x22 - 0.3*m.x34 - 0.3*m.x52 - 0.9*m.x92 == 0)

m.c828 = Constraint(expr=m.x300*m.x241 - 0.8*m.x26 - 0.3*m.x38 - 0.3*m.x56 + 0.9*m.x84 + 0.9*m.x88 + 0.9*m.x92
                          + 0.9*m.x96 == 0.45)

m.c829 = Constraint(expr=m.x303*m.x238 - 0.7*m.x14 + 0.1*m.x30 + 0.1*m.x34 + 0.1*m.x38 - 0.8*m.x66 - 0.5*m.x84 == 0.1)

m.c830 = Constraint(expr=m.x306*m.x239 - 0.1*m.x2 - 0.7*m.x18 - 0.1*m.x30 - 0.8*m.x70 - 0.5*m.x88 == 0)

m.c831 = Constraint(expr=m.x309*m.x240 - 0.1*m.x6 - 0.7*m.x22 - 0.1*m.x34 + 0.8*m.x66 + 0.8*m.x70 + 0.8*m.x74
                          - 0.5*m.x92 == 0.16)

m.c832 = Constraint(expr=m.x312*m.x241 - 0.1*m.x10 - 0.7*m.x26 - 0.1*m.x38 - 0.8*m.x74 + 0.5*m.x84 + 0.5*m.x88
                          + 0.5*m.x92 + 0.5*m.x96 == 0.25)

m.c833 = Constraint(expr=m.x315*m.x238 - m.x14 + 0.5*m.x30 + 0.5*m.x34 + 0.5*m.x38 - 0.5*m.x48 - 0.2*m.x66 - m.x84
                          == 0.5)

m.c834 = Constraint(expr=m.x318*m.x239 - 0.2*m.x2 - m.x18 - 0.5*m.x30 + 0.5*m.x48 + 0.5*m.x52 + 0.5*m.x56 - 0.2*m.x70
                          - m.x88 == 0.4)

m.c835 = Constraint(expr=m.x321*m.x240 - 0.2*m.x6 - m.x22 - 0.5*m.x34 - 0.5*m.x52 + 0.2*m.x66 + 0.2*m.x70 + 0.2*m.x74
                          - m.x92 == 0.04)

m.c836 = Constraint(expr=m.x324*m.x241 - 0.2*m.x10 - m.x26 - 0.5*m.x38 - 0.5*m.x56 - 0.2*m.x74 + m.x84 + m.x88 + m.x92
                          + m.x96 == 0.5)

m.c837 = Constraint(expr=m.x327*m.x238 - 0.9*m.x14 + 0.3*m.x30 + 0.3*m.x34 + 0.3*m.x38 - 0.2*m.x48 - m.x66 - 0.7*m.x84
                          == 0.3)

m.c838 = Constraint(expr=m.x330*m.x239 - 0.3*m.x2 - 0.9*m.x18 - 0.3*m.x30 + 0.2*m.x48 + 0.2*m.x52 + 0.2*m.x56 - m.x70
                          - 0.7*m.x88 == 0.16)

m.c839 = Constraint(expr=m.x333*m.x240 - 0.3*m.x6 - 0.9*m.x22 - 0.3*m.x34 - 0.2*m.x52 + m.x66 + m.x70 + m.x74
                          - 0.7*m.x92 == 0.2)

m.c840 = Constraint(expr=m.x336*m.x241 - 0.3*m.x10 - 0.9*m.x26 - 0.3*m.x38 - 0.2*m.x56 - m.x74 + 0.7*m.x84 + 0.7*m.x88
                          + 0.7*m.x92 + 0.7*m.x96 == 0.35)

m.c841 = Constraint(expr=m.x339*m.x238 - 0.8*m.x14 + 0.3*m.x30 + 0.3*m.x34 + 0.3*m.x38 - 0.3*m.x48 - 0.9*m.x84 == 0.3)

m.c842 = Constraint(expr=m.x342*m.x239 - 0.8*m.x18 - 0.3*m.x30 + 0.3*m.x48 + 0.3*m.x52 + 0.3*m.x56 - 0.9*m.x88 == 0.24)

m.c843 = Constraint(expr=m.x345*m.x240 - 0.8*m.x22 - 0.3*m.x34 - 0.3*m.x52 - 0.9*m.x92 == 0)

m.c844 = Constraint(expr=m.x348*m.x241 - 0.8*m.x26 - 0.3*m.x38 - 0.3*m.x56 + 0.9*m.x84 + 0.9*m.x88 + 0.9*m.x92
                          + 0.9*m.x96 == 0.45)

m.c845 = Constraint(expr=m.x351*m.x238 - 0.9*m.x14 + 0.3*m.x30 + 0.3*m.x34 + 0.3*m.x38 - 0.2*m.x48 - m.x66 - 0.7*m.x84
                          == 0.3)

m.c846 = Constraint(expr=m.x354*m.x239 - 0.3*m.x2 - 0.9*m.x18 - 0.3*m.x30 + 0.2*m.x48 + 0.2*m.x52 + 0.2*m.x56 - m.x70
                          - 0.7*m.x88 == 0.16)

m.c847 = Constraint(expr=m.x357*m.x240 - 0.3*m.x6 - 0.9*m.x22 - 0.3*m.x34 - 0.2*m.x52 + m.x66 + m.x70 + m.x74
                          - 0.7*m.x92 == 0.2)

m.c848 = Constraint(expr=m.x360*m.x241 - 0.3*m.x10 - 0.9*m.x26 - 0.3*m.x38 - 0.2*m.x56 - m.x74 + 0.7*m.x84 + 0.7*m.x88
                          + 0.7*m.x92 + 0.7*m.x96 == 0.35)

m.c849 = Constraint(expr=m.x267*m.x31 + m.x267*m.x35 + m.x267*m.x39 + m.x267*m.x42 + m.x267*m.x45 - m.x270*m.x49 - 
                         m.x273*m.x67 - m.x276*m.x85 - m.x267*m.x238 + m.x268*m.x249 - 0.9*m.x15 == 0)

m.c850 = Constraint(expr=m.x268*m.x32 + m.x268*m.x36 + m.x268*m.x40 + m.x268*m.x43 + m.x268*m.x46 - m.x271*m.x50 - 
                         m.x274*m.x68 - m.x277*m.x86 - m.x268*m.x249 + m.x269*m.x250 - 0.9*m.x16 == 0)

m.c851 = Constraint(expr=m.x269*m.x33 + m.x269*m.x37 + m.x269*m.x41 + m.x269*m.x44 + m.x269*m.x47 - m.x272*m.x51 - 
                         m.x275*m.x69 - m.x278*m.x87 + m.x251*m.x103 - m.x269*m.x250 - 0.9*m.x17 == 0)

m.c852 = Constraint(expr=m.x270*m.x49 - m.x267*m.x31 + m.x270*m.x53 + m.x270*m.x57 + m.x270*m.x60 + m.x270*m.x63 - 
                         m.x273*m.x71 - m.x276*m.x89 - m.x270*m.x239 + m.x271*m.x252 - 0.1*m.x3 - 0.9*m.x19 == 0)

m.c853 = Constraint(expr=m.x271*m.x50 - m.x268*m.x32 + m.x271*m.x54 + m.x271*m.x58 + m.x271*m.x61 + m.x271*m.x64 - 
                         m.x274*m.x72 - m.x277*m.x90 - m.x271*m.x252 + m.x272*m.x253 - 0.1*m.x4 - 0.9*m.x20 == 0)

m.c854 = Constraint(expr=m.x272*m.x51 - m.x269*m.x33 + m.x272*m.x55 + m.x272*m.x59 + m.x272*m.x62 + m.x272*m.x65 - 
                         m.x275*m.x73 - m.x278*m.x91 + m.x254*m.x104 - m.x272*m.x253 - 0.1*m.x5 - 0.9*m.x21 == 0)

m.c855 = Constraint(expr=(-m.x267*m.x35) - m.x270*m.x53 + m.x273*m.x67 + m.x273*m.x71 + m.x273*m.x75 + m.x273*m.x78 + 
                         m.x273*m.x81 - m.x276*m.x93 - m.x273*m.x240 + m.x274*m.x255 - 0.1*m.x7 - 0.9*m.x23 == 0)

m.c856 = Constraint(expr=(-m.x268*m.x36) - m.x271*m.x54 + m.x274*m.x68 + m.x274*m.x72 + m.x274*m.x76 + m.x274*m.x79 + 
                         m.x274*m.x82 - m.x277*m.x94 - m.x274*m.x255 + m.x275*m.x256 - 0.1*m.x8 - 0.9*m.x24 == 0)

m.c857 = Constraint(expr=(-m.x269*m.x37) - m.x272*m.x55 + m.x275*m.x69 + m.x275*m.x73 + m.x275*m.x77 + m.x275*m.x80 + 
                         m.x275*m.x83 - m.x278*m.x95 + m.x257*m.x105 - m.x275*m.x256 - 0.1*m.x9 - 0.9*m.x25 == 0)

m.c858 = Constraint(expr=(-m.x267*m.x39) - m.x270*m.x57 - m.x273*m.x75 + m.x276*m.x85 + m.x276*m.x89 + m.x276*m.x93 + 
                         m.x276*m.x97 + m.x276*m.x100 - m.x276*m.x241 + m.x277*m.x258 - 0.1*m.x11 - 0.9*m.x27 == 0)

m.c859 = Constraint(expr=(-m.x268*m.x40) - m.x271*m.x58 - m.x274*m.x76 + m.x277*m.x86 + m.x277*m.x90 + m.x277*m.x94 + 
                         m.x277*m.x98 + m.x277*m.x101 - m.x277*m.x258 + m.x278*m.x259 - 0.1*m.x12 - 0.9*m.x28 == 0)

m.c860 = Constraint(expr=(-m.x269*m.x41) - m.x272*m.x59 - m.x275*m.x77 + m.x278*m.x87 + m.x278*m.x91 + m.x278*m.x95 + 
                         m.x278*m.x99 + m.x278*m.x102 + m.x260*m.x106 - m.x278*m.x259 - 0.1*m.x13 - 0.9*m.x29 == 0)

m.c861 = Constraint(expr=m.x279*m.x31 + m.x279*m.x35 + m.x279*m.x39 + m.x279*m.x42 + m.x279*m.x45 - m.x282*m.x49 - 
                         m.x285*m.x67 - m.x288*m.x85 - m.x279*m.x238 + m.x280*m.x249 - 0.8*m.x15 == 0)

m.c862 = Constraint(expr=m.x280*m.x32 + m.x280*m.x36 + m.x280*m.x40 + m.x280*m.x43 + m.x280*m.x46 - m.x283*m.x50 - 
                         m.x286*m.x68 - m.x289*m.x86 - m.x280*m.x249 + m.x281*m.x250 - 0.8*m.x16 == 0)

m.c863 = Constraint(expr=m.x281*m.x33 + m.x281*m.x37 + m.x281*m.x41 + m.x281*m.x44 + m.x281*m.x47 - m.x284*m.x51 - 
                         m.x287*m.x69 - m.x290*m.x87 + m.x251*m.x107 - m.x281*m.x250 - 0.8*m.x17 == 0)

m.c864 = Constraint(expr=m.x282*m.x49 - m.x279*m.x31 + m.x282*m.x53 + m.x282*m.x57 + m.x282*m.x60 + m.x282*m.x63 - 
                         m.x285*m.x71 - m.x288*m.x89 - m.x282*m.x239 + m.x283*m.x252 - 0.2*m.x3 - 0.8*m.x19 == 0)

m.c865 = Constraint(expr=m.x283*m.x50 - m.x280*m.x32 + m.x283*m.x54 + m.x283*m.x58 + m.x283*m.x61 + m.x283*m.x64 - 
                         m.x286*m.x72 - m.x289*m.x90 - m.x283*m.x252 + m.x284*m.x253 - 0.2*m.x4 - 0.8*m.x20 == 0)

m.c866 = Constraint(expr=m.x284*m.x51 - m.x281*m.x33 + m.x284*m.x55 + m.x284*m.x59 + m.x284*m.x62 + m.x284*m.x65 - 
                         m.x287*m.x73 - m.x290*m.x91 + m.x254*m.x108 - m.x284*m.x253 - 0.2*m.x5 - 0.8*m.x21 == 0)

m.c867 = Constraint(expr=(-m.x279*m.x35) - m.x282*m.x53 + m.x285*m.x67 + m.x285*m.x71 + m.x285*m.x75 + m.x285*m.x78 + 
                         m.x285*m.x81 - m.x288*m.x93 - m.x285*m.x240 + m.x286*m.x255 - 0.2*m.x7 - 0.8*m.x23 == 0)

m.c868 = Constraint(expr=(-m.x280*m.x36) - m.x283*m.x54 + m.x286*m.x68 + m.x286*m.x72 + m.x286*m.x76 + m.x286*m.x79 + 
                         m.x286*m.x82 - m.x289*m.x94 - m.x286*m.x255 + m.x287*m.x256 - 0.2*m.x8 - 0.8*m.x24 == 0)

m.c869 = Constraint(expr=(-m.x281*m.x37) - m.x284*m.x55 + m.x287*m.x69 + m.x287*m.x73 + m.x287*m.x77 + m.x287*m.x80 + 
                         m.x287*m.x83 - m.x290*m.x95 + m.x257*m.x109 - m.x287*m.x256 - 0.2*m.x9 - 0.8*m.x25 == 0)

m.c870 = Constraint(expr=(-m.x279*m.x39) - m.x282*m.x57 - m.x285*m.x75 + m.x288*m.x85 + m.x288*m.x89 + m.x288*m.x93 + 
                         m.x288*m.x97 + m.x288*m.x100 - m.x288*m.x241 + m.x289*m.x258 - 0.2*m.x11 - 0.8*m.x27 == 0)

m.c871 = Constraint(expr=(-m.x280*m.x40) - m.x283*m.x58 - m.x286*m.x76 + m.x289*m.x86 + m.x289*m.x90 + m.x289*m.x94 + 
                         m.x289*m.x98 + m.x289*m.x101 - m.x289*m.x258 + m.x290*m.x259 - 0.2*m.x12 - 0.8*m.x28 == 0)

m.c872 = Constraint(expr=(-m.x281*m.x41) - m.x284*m.x59 - m.x287*m.x77 + m.x290*m.x87 + m.x290*m.x91 + m.x290*m.x95 + 
                         m.x290*m.x99 + m.x290*m.x102 + m.x260*m.x110 - m.x290*m.x259 - 0.2*m.x13 - 0.8*m.x29 == 0)

m.c873 = Constraint(expr=m.x291*m.x31 + m.x291*m.x35 + m.x291*m.x39 + m.x291*m.x42 + m.x291*m.x45 - m.x294*m.x49 - 
                         m.x297*m.x67 - m.x300*m.x85 - m.x291*m.x238 + m.x292*m.x249 - 0.8*m.x15 == 0)

m.c874 = Constraint(expr=m.x292*m.x32 + m.x292*m.x36 + m.x292*m.x40 + m.x292*m.x43 + m.x292*m.x46 - m.x295*m.x50 - 
                         m.x298*m.x68 - m.x301*m.x86 - m.x292*m.x249 + m.x293*m.x250 - 0.8*m.x16 == 0)

m.c875 = Constraint(expr=m.x293*m.x33 + m.x293*m.x37 + m.x293*m.x41 + m.x293*m.x44 + m.x293*m.x47 - m.x296*m.x51 - 
                         m.x299*m.x69 - m.x302*m.x87 + m.x251*m.x111 - m.x293*m.x250 - 0.8*m.x17 == 0)

m.c876 = Constraint(expr=m.x294*m.x49 - m.x291*m.x31 + m.x294*m.x53 + m.x294*m.x57 + m.x294*m.x60 + m.x294*m.x63 - 
                         m.x297*m.x71 - m.x300*m.x89 - m.x294*m.x239 + m.x295*m.x252 - 0.8*m.x19 == 0)

m.c877 = Constraint(expr=m.x295*m.x50 - m.x292*m.x32 + m.x295*m.x54 + m.x295*m.x58 + m.x295*m.x61 + m.x295*m.x64 - 
                         m.x298*m.x72 - m.x301*m.x90 - m.x295*m.x252 + m.x296*m.x253 - 0.8*m.x20 == 0)

m.c878 = Constraint(expr=m.x296*m.x51 - m.x293*m.x33 + m.x296*m.x55 + m.x296*m.x59 + m.x296*m.x62 + m.x296*m.x65 - 
                         m.x299*m.x73 - m.x302*m.x91 + m.x254*m.x112 - m.x296*m.x253 - 0.8*m.x21 == 0)

m.c879 = Constraint(expr=(-m.x291*m.x35) - m.x294*m.x53 + m.x297*m.x67 + m.x297*m.x71 + m.x297*m.x75 + m.x297*m.x78 + 
                         m.x297*m.x81 - m.x300*m.x93 - m.x297*m.x240 + m.x298*m.x255 - 0.8*m.x23 == 0)

m.c880 = Constraint(expr=(-m.x292*m.x36) - m.x295*m.x54 + m.x298*m.x68 + m.x298*m.x72 + m.x298*m.x76 + m.x298*m.x79 + 
                         m.x298*m.x82 - m.x301*m.x94 - m.x298*m.x255 + m.x299*m.x256 - 0.8*m.x24 == 0)

m.c881 = Constraint(expr=(-m.x293*m.x37) - m.x296*m.x55 + m.x299*m.x69 + m.x299*m.x73 + m.x299*m.x77 + m.x299*m.x80 + 
                         m.x299*m.x83 - m.x302*m.x95 + m.x257*m.x113 - m.x299*m.x256 - 0.8*m.x25 == 0)

m.c882 = Constraint(expr=(-m.x291*m.x39) - m.x294*m.x57 - m.x297*m.x75 + m.x300*m.x85 + m.x300*m.x89 + m.x300*m.x93 + 
                         m.x300*m.x97 + m.x300*m.x100 - m.x300*m.x241 + m.x301*m.x258 - 0.8*m.x27 == 0)

m.c883 = Constraint(expr=(-m.x292*m.x40) - m.x295*m.x58 - m.x298*m.x76 + m.x301*m.x86 + m.x301*m.x90 + m.x301*m.x94 + 
                         m.x301*m.x98 + m.x301*m.x101 - m.x301*m.x258 + m.x302*m.x259 - 0.8*m.x28 == 0)

m.c884 = Constraint(expr=(-m.x293*m.x41) - m.x296*m.x59 - m.x299*m.x77 + m.x302*m.x87 + m.x302*m.x91 + m.x302*m.x95 + 
                         m.x302*m.x99 + m.x302*m.x102 + m.x260*m.x114 - m.x302*m.x259 - 0.8*m.x29 == 0)

m.c885 = Constraint(expr=m.x303*m.x31 + m.x303*m.x35 + m.x303*m.x39 + m.x303*m.x42 + m.x303*m.x45 - m.x306*m.x49 - 
                         m.x309*m.x67 - m.x312*m.x85 - m.x303*m.x238 + m.x304*m.x249 - 0.7*m.x15 == 0)

m.c886 = Constraint(expr=m.x304*m.x32 + m.x304*m.x36 + m.x304*m.x40 + m.x304*m.x43 + m.x304*m.x46 - m.x307*m.x50 - 
                         m.x310*m.x68 - m.x313*m.x86 - m.x304*m.x249 + m.x305*m.x250 - 0.7*m.x16 == 0)

m.c887 = Constraint(expr=m.x305*m.x33 + m.x305*m.x37 + m.x305*m.x41 + m.x305*m.x44 + m.x305*m.x47 - m.x308*m.x51 - 
                         m.x311*m.x69 - m.x314*m.x87 + m.x251*m.x115 - m.x305*m.x250 - 0.7*m.x17 == 0)

m.c888 = Constraint(expr=m.x306*m.x49 - m.x303*m.x31 + m.x306*m.x53 + m.x306*m.x57 + m.x306*m.x60 + m.x306*m.x63 - 
                         m.x309*m.x71 - m.x312*m.x89 - m.x306*m.x239 + m.x307*m.x252 - 0.1*m.x3 - 0.7*m.x19 == 0)

m.c889 = Constraint(expr=m.x307*m.x50 - m.x304*m.x32 + m.x307*m.x54 + m.x307*m.x58 + m.x307*m.x61 + m.x307*m.x64 - 
                         m.x310*m.x72 - m.x313*m.x90 - m.x307*m.x252 + m.x308*m.x253 - 0.1*m.x4 - 0.7*m.x20 == 0)

m.c890 = Constraint(expr=m.x308*m.x51 - m.x305*m.x33 + m.x308*m.x55 + m.x308*m.x59 + m.x308*m.x62 + m.x308*m.x65 - 
                         m.x311*m.x73 - m.x314*m.x91 + m.x254*m.x116 - m.x308*m.x253 - 0.1*m.x5 - 0.7*m.x21 == 0)

m.c891 = Constraint(expr=(-m.x303*m.x35) - m.x306*m.x53 + m.x309*m.x67 + m.x309*m.x71 + m.x309*m.x75 + m.x309*m.x78 + 
                         m.x309*m.x81 - m.x312*m.x93 - m.x309*m.x240 + m.x310*m.x255 - 0.1*m.x7 - 0.7*m.x23 == 0)

m.c892 = Constraint(expr=(-m.x304*m.x36) - m.x307*m.x54 + m.x310*m.x68 + m.x310*m.x72 + m.x310*m.x76 + m.x310*m.x79 + 
                         m.x310*m.x82 - m.x313*m.x94 - m.x310*m.x255 + m.x311*m.x256 - 0.1*m.x8 - 0.7*m.x24 == 0)

m.c893 = Constraint(expr=(-m.x305*m.x37) - m.x308*m.x55 + m.x311*m.x69 + m.x311*m.x73 + m.x311*m.x77 + m.x311*m.x80 + 
                         m.x311*m.x83 - m.x314*m.x95 + m.x257*m.x117 - m.x311*m.x256 - 0.1*m.x9 - 0.7*m.x25 == 0)

m.c894 = Constraint(expr=(-m.x303*m.x39) - m.x306*m.x57 - m.x309*m.x75 + m.x312*m.x85 + m.x312*m.x89 + m.x312*m.x93 + 
                         m.x312*m.x97 + m.x312*m.x100 - m.x312*m.x241 + m.x313*m.x258 - 0.1*m.x11 - 0.7*m.x27 == 0)

m.c895 = Constraint(expr=(-m.x304*m.x40) - m.x307*m.x58 - m.x310*m.x76 + m.x313*m.x86 + m.x313*m.x90 + m.x313*m.x94 + 
                         m.x313*m.x98 + m.x313*m.x101 - m.x313*m.x258 + m.x314*m.x259 - 0.1*m.x12 - 0.7*m.x28 == 0)

m.c896 = Constraint(expr=(-m.x305*m.x41) - m.x308*m.x59 - m.x311*m.x77 + m.x314*m.x87 + m.x314*m.x91 + m.x314*m.x95 + 
                         m.x314*m.x99 + m.x314*m.x102 + m.x260*m.x118 - m.x314*m.x259 - 0.1*m.x13 - 0.7*m.x29 == 0)

m.c897 = Constraint(expr=m.x315*m.x31 + m.x315*m.x35 + m.x315*m.x39 + m.x315*m.x42 + m.x315*m.x45 - m.x318*m.x49 - 
                         m.x321*m.x67 - m.x324*m.x85 - m.x315*m.x238 + m.x316*m.x249 - m.x15 == 0)

m.c898 = Constraint(expr=m.x316*m.x32 + m.x316*m.x36 + m.x316*m.x40 + m.x316*m.x43 + m.x316*m.x46 - m.x319*m.x50 - 
                         m.x322*m.x68 - m.x325*m.x86 - m.x316*m.x249 + m.x317*m.x250 - m.x16 == 0)

m.c899 = Constraint(expr=m.x317*m.x33 + m.x317*m.x37 + m.x317*m.x41 + m.x317*m.x44 + m.x317*m.x47 - m.x320*m.x51 - 
                         m.x323*m.x69 - m.x326*m.x87 + m.x251*m.x119 - m.x317*m.x250 - m.x17 == 0)

m.c900 = Constraint(expr=m.x318*m.x49 - m.x315*m.x31 + m.x318*m.x53 + m.x318*m.x57 + m.x318*m.x60 + m.x318*m.x63 - 
                         m.x321*m.x71 - m.x324*m.x89 - m.x318*m.x239 + m.x319*m.x252 - 0.2*m.x3 - m.x19 == 0)

m.c901 = Constraint(expr=m.x319*m.x50 - m.x316*m.x32 + m.x319*m.x54 + m.x319*m.x58 + m.x319*m.x61 + m.x319*m.x64 - 
                         m.x322*m.x72 - m.x325*m.x90 - m.x319*m.x252 + m.x320*m.x253 - 0.2*m.x4 - m.x20 == 0)

m.c902 = Constraint(expr=m.x320*m.x51 - m.x317*m.x33 + m.x320*m.x55 + m.x320*m.x59 + m.x320*m.x62 + m.x320*m.x65 - 
                         m.x323*m.x73 - m.x326*m.x91 + m.x254*m.x120 - m.x320*m.x253 - 0.2*m.x5 - m.x21 == 0)

m.c903 = Constraint(expr=(-m.x315*m.x35) - m.x318*m.x53 + m.x321*m.x67 + m.x321*m.x71 + m.x321*m.x75 + m.x321*m.x78 + 
                         m.x321*m.x81 - m.x324*m.x93 - m.x321*m.x240 + m.x322*m.x255 - 0.2*m.x7 - m.x23 == 0)

m.c904 = Constraint(expr=(-m.x316*m.x36) - m.x319*m.x54 + m.x322*m.x68 + m.x322*m.x72 + m.x322*m.x76 + m.x322*m.x79 + 
                         m.x322*m.x82 - m.x325*m.x94 - m.x322*m.x255 + m.x323*m.x256 - 0.2*m.x8 - m.x24 == 0)

m.c905 = Constraint(expr=(-m.x317*m.x37) - m.x320*m.x55 + m.x323*m.x69 + m.x323*m.x73 + m.x323*m.x77 + m.x323*m.x80 + 
                         m.x323*m.x83 - m.x326*m.x95 + m.x257*m.x121 - m.x323*m.x256 - 0.2*m.x9 - m.x25 == 0)

m.c906 = Constraint(expr=(-m.x315*m.x39) - m.x318*m.x57 - m.x321*m.x75 + m.x324*m.x85 + m.x324*m.x89 + m.x324*m.x93 + 
                         m.x324*m.x97 + m.x324*m.x100 - m.x324*m.x241 + m.x325*m.x258 - 0.2*m.x11 - m.x27 == 0)

m.c907 = Constraint(expr=(-m.x316*m.x40) - m.x319*m.x58 - m.x322*m.x76 + m.x325*m.x86 + m.x325*m.x90 + m.x325*m.x94 + 
                         m.x325*m.x98 + m.x325*m.x101 - m.x325*m.x258 + m.x326*m.x259 - 0.2*m.x12 - m.x28 == 0)

m.c908 = Constraint(expr=(-m.x317*m.x41) - m.x320*m.x59 - m.x323*m.x77 + m.x326*m.x87 + m.x326*m.x91 + m.x326*m.x95 + 
                         m.x326*m.x99 + m.x326*m.x102 + m.x260*m.x122 - m.x326*m.x259 - 0.2*m.x13 - m.x29 == 0)

m.c909 = Constraint(expr=m.x327*m.x31 + m.x327*m.x35 + m.x327*m.x39 + m.x327*m.x42 + m.x327*m.x45 - m.x330*m.x49 - 
                         m.x333*m.x67 - m.x336*m.x85 - m.x327*m.x238 + m.x328*m.x249 - 0.9*m.x15 == 0)

m.c910 = Constraint(expr=m.x328*m.x32 + m.x328*m.x36 + m.x328*m.x40 + m.x328*m.x43 + m.x328*m.x46 - m.x331*m.x50 - 
                         m.x334*m.x68 - m.x337*m.x86 - m.x328*m.x249 + m.x329*m.x250 - 0.9*m.x16 == 0)

m.c911 = Constraint(expr=m.x329*m.x33 + m.x329*m.x37 + m.x329*m.x41 + m.x329*m.x44 + m.x329*m.x47 - m.x332*m.x51 - 
                         m.x335*m.x69 - m.x338*m.x87 + m.x251*m.x123 - m.x329*m.x250 - 0.9*m.x17 == 0)

m.c912 = Constraint(expr=m.x330*m.x49 - m.x327*m.x31 + m.x330*m.x53 + m.x330*m.x57 + m.x330*m.x60 + m.x330*m.x63 - 
                         m.x333*m.x71 - m.x336*m.x89 - m.x330*m.x239 + m.x331*m.x252 - 0.3*m.x3 - 0.9*m.x19 == 0)

m.c913 = Constraint(expr=m.x331*m.x50 - m.x328*m.x32 + m.x331*m.x54 + m.x331*m.x58 + m.x331*m.x61 + m.x331*m.x64 - 
                         m.x334*m.x72 - m.x337*m.x90 - m.x331*m.x252 + m.x332*m.x253 - 0.3*m.x4 - 0.9*m.x20 == 0)

m.c914 = Constraint(expr=m.x332*m.x51 - m.x329*m.x33 + m.x332*m.x55 + m.x332*m.x59 + m.x332*m.x62 + m.x332*m.x65 - 
                         m.x335*m.x73 - m.x338*m.x91 + m.x254*m.x124 - m.x332*m.x253 - 0.3*m.x5 - 0.9*m.x21 == 0)

m.c915 = Constraint(expr=(-m.x327*m.x35) - m.x330*m.x53 + m.x333*m.x67 + m.x333*m.x71 + m.x333*m.x75 + m.x333*m.x78 + 
                         m.x333*m.x81 - m.x336*m.x93 - m.x333*m.x240 + m.x334*m.x255 - 0.3*m.x7 - 0.9*m.x23 == 0)

m.c916 = Constraint(expr=(-m.x328*m.x36) - m.x331*m.x54 + m.x334*m.x68 + m.x334*m.x72 + m.x334*m.x76 + m.x334*m.x79 + 
                         m.x334*m.x82 - m.x337*m.x94 - m.x334*m.x255 + m.x335*m.x256 - 0.3*m.x8 - 0.9*m.x24 == 0)

m.c917 = Constraint(expr=(-m.x329*m.x37) - m.x332*m.x55 + m.x335*m.x69 + m.x335*m.x73 + m.x335*m.x77 + m.x335*m.x80 + 
                         m.x335*m.x83 - m.x338*m.x95 + m.x257*m.x125 - m.x335*m.x256 - 0.3*m.x9 - 0.9*m.x25 == 0)

m.c918 = Constraint(expr=(-m.x327*m.x39) - m.x330*m.x57 - m.x333*m.x75 + m.x336*m.x85 + m.x336*m.x89 + m.x336*m.x93 + 
                         m.x336*m.x97 + m.x336*m.x100 - m.x336*m.x241 + m.x337*m.x258 - 0.3*m.x11 - 0.9*m.x27 == 0)

m.c919 = Constraint(expr=(-m.x328*m.x40) - m.x331*m.x58 - m.x334*m.x76 + m.x337*m.x86 + m.x337*m.x90 + m.x337*m.x94 + 
                         m.x337*m.x98 + m.x337*m.x101 - m.x337*m.x258 + m.x338*m.x259 - 0.3*m.x12 - 0.9*m.x28 == 0)

m.c920 = Constraint(expr=(-m.x329*m.x41) - m.x332*m.x59 - m.x335*m.x77 + m.x338*m.x87 + m.x338*m.x91 + m.x338*m.x95 + 
                         m.x338*m.x99 + m.x338*m.x102 + m.x260*m.x126 - m.x338*m.x259 - 0.3*m.x13 - 0.9*m.x29 == 0)

m.c921 = Constraint(expr=m.x339*m.x31 + m.x339*m.x35 + m.x339*m.x39 + m.x339*m.x42 + m.x339*m.x45 - m.x342*m.x49 - 
                         m.x345*m.x67 - m.x348*m.x85 - m.x339*m.x238 + m.x340*m.x249 - 0.8*m.x15 == 0)

m.c922 = Constraint(expr=m.x340*m.x32 + m.x340*m.x36 + m.x340*m.x40 + m.x340*m.x43 + m.x340*m.x46 - m.x343*m.x50 - 
                         m.x346*m.x68 - m.x349*m.x86 - m.x340*m.x249 + m.x341*m.x250 - 0.8*m.x16 == 0)

m.c923 = Constraint(expr=m.x341*m.x33 + m.x341*m.x37 + m.x341*m.x41 + m.x341*m.x44 + m.x341*m.x47 - m.x344*m.x51 - 
                         m.x347*m.x69 - m.x350*m.x87 + m.x251*m.x127 - m.x341*m.x250 - 0.8*m.x17 == 0)

m.c924 = Constraint(expr=m.x342*m.x49 - m.x339*m.x31 + m.x342*m.x53 + m.x342*m.x57 + m.x342*m.x60 + m.x342*m.x63 - 
                         m.x345*m.x71 - m.x348*m.x89 - m.x342*m.x239 + m.x343*m.x252 - 0.8*m.x19 == 0)

m.c925 = Constraint(expr=m.x343*m.x50 - m.x340*m.x32 + m.x343*m.x54 + m.x343*m.x58 + m.x343*m.x61 + m.x343*m.x64 - 
                         m.x346*m.x72 - m.x349*m.x90 - m.x343*m.x252 + m.x344*m.x253 - 0.8*m.x20 == 0)

m.c926 = Constraint(expr=m.x344*m.x51 - m.x341*m.x33 + m.x344*m.x55 + m.x344*m.x59 + m.x344*m.x62 + m.x344*m.x65 - 
                         m.x347*m.x73 - m.x350*m.x91 + m.x254*m.x128 - m.x344*m.x253 - 0.8*m.x21 == 0)

m.c927 = Constraint(expr=(-m.x339*m.x35) - m.x342*m.x53 + m.x345*m.x67 + m.x345*m.x71 + m.x345*m.x75 + m.x345*m.x78 + 
                         m.x345*m.x81 - m.x348*m.x93 - m.x345*m.x240 + m.x346*m.x255 - 0.8*m.x23 == 0)

m.c928 = Constraint(expr=(-m.x340*m.x36) - m.x343*m.x54 + m.x346*m.x68 + m.x346*m.x72 + m.x346*m.x76 + m.x346*m.x79 + 
                         m.x346*m.x82 - m.x349*m.x94 - m.x346*m.x255 + m.x347*m.x256 - 0.8*m.x24 == 0)

m.c929 = Constraint(expr=(-m.x341*m.x37) - m.x344*m.x55 + m.x347*m.x69 + m.x347*m.x73 + m.x347*m.x77 + m.x347*m.x80 + 
                         m.x347*m.x83 - m.x350*m.x95 + m.x257*m.x129 - m.x347*m.x256 - 0.8*m.x25 == 0)

m.c930 = Constraint(expr=(-m.x339*m.x39) - m.x342*m.x57 - m.x345*m.x75 + m.x348*m.x85 + m.x348*m.x89 + m.x348*m.x93 + 
                         m.x348*m.x97 + m.x348*m.x100 - m.x348*m.x241 + m.x349*m.x258 - 0.8*m.x27 == 0)

m.c931 = Constraint(expr=(-m.x340*m.x40) - m.x343*m.x58 - m.x346*m.x76 + m.x349*m.x86 + m.x349*m.x90 + m.x349*m.x94 + 
                         m.x349*m.x98 + m.x349*m.x101 - m.x349*m.x258 + m.x350*m.x259 - 0.8*m.x28 == 0)

m.c932 = Constraint(expr=(-m.x341*m.x41) - m.x344*m.x59 - m.x347*m.x77 + m.x350*m.x87 + m.x350*m.x91 + m.x350*m.x95 + 
                         m.x350*m.x99 + m.x350*m.x102 + m.x260*m.x130 - m.x350*m.x259 - 0.8*m.x29 == 0)

m.c933 = Constraint(expr=m.x351*m.x31 + m.x351*m.x35 + m.x351*m.x39 + m.x351*m.x42 + m.x351*m.x45 - m.x354*m.x49 - 
                         m.x357*m.x67 - m.x360*m.x85 - m.x351*m.x238 + m.x352*m.x249 - 0.9*m.x15 == 0)

m.c934 = Constraint(expr=m.x352*m.x32 + m.x352*m.x36 + m.x352*m.x40 + m.x352*m.x43 + m.x352*m.x46 - m.x355*m.x50 - 
                         m.x358*m.x68 - m.x361*m.x86 - m.x352*m.x249 + m.x353*m.x250 - 0.9*m.x16 == 0)

m.c935 = Constraint(expr=m.x353*m.x33 + m.x353*m.x37 + m.x353*m.x41 + m.x353*m.x44 + m.x353*m.x47 - m.x356*m.x51 - 
                         m.x359*m.x69 - m.x362*m.x87 + m.x251*m.x131 - m.x353*m.x250 - 0.9*m.x17 == 0)

m.c936 = Constraint(expr=m.x354*m.x49 - m.x351*m.x31 + m.x354*m.x53 + m.x354*m.x57 + m.x354*m.x60 + m.x354*m.x63 - 
                         m.x357*m.x71 - m.x360*m.x89 - m.x354*m.x239 + m.x355*m.x252 - 0.3*m.x3 - 0.9*m.x19 == 0)

m.c937 = Constraint(expr=m.x355*m.x50 - m.x352*m.x32 + m.x355*m.x54 + m.x355*m.x58 + m.x355*m.x61 + m.x355*m.x64 - 
                         m.x358*m.x72 - m.x361*m.x90 - m.x355*m.x252 + m.x356*m.x253 - 0.3*m.x4 - 0.9*m.x20 == 0)

m.c938 = Constraint(expr=m.x356*m.x51 - m.x353*m.x33 + m.x356*m.x55 + m.x356*m.x59 + m.x356*m.x62 + m.x356*m.x65 - 
                         m.x359*m.x73 - m.x362*m.x91 + m.x254*m.x132 - m.x356*m.x253 - 0.3*m.x5 - 0.9*m.x21 == 0)

m.c939 = Constraint(expr=(-m.x351*m.x35) - m.x354*m.x53 + m.x357*m.x67 + m.x357*m.x71 + m.x357*m.x75 + m.x357*m.x78 + 
                         m.x357*m.x81 - m.x360*m.x93 - m.x357*m.x240 + m.x358*m.x255 - 0.3*m.x7 - 0.9*m.x23 == 0)

m.c940 = Constraint(expr=(-m.x352*m.x36) - m.x355*m.x54 + m.x358*m.x68 + m.x358*m.x72 + m.x358*m.x76 + m.x358*m.x79 + 
                         m.x358*m.x82 - m.x361*m.x94 - m.x358*m.x255 + m.x359*m.x256 - 0.3*m.x8 - 0.9*m.x24 == 0)

m.c941 = Constraint(expr=(-m.x353*m.x37) - m.x356*m.x55 + m.x359*m.x69 + m.x359*m.x73 + m.x359*m.x77 + m.x359*m.x80 + 
                         m.x359*m.x83 - m.x362*m.x95 + m.x257*m.x133 - m.x359*m.x256 - 0.3*m.x9 - 0.9*m.x25 == 0)

m.c942 = Constraint(expr=(-m.x351*m.x39) - m.x354*m.x57 - m.x357*m.x75 + m.x360*m.x85 + m.x360*m.x89 + m.x360*m.x93 + 
                         m.x360*m.x97 + m.x360*m.x100 - m.x360*m.x241 + m.x361*m.x258 - 0.3*m.x11 - 0.9*m.x27 == 0)

m.c943 = Constraint(expr=(-m.x352*m.x40) - m.x355*m.x58 - m.x358*m.x76 + m.x361*m.x86 + m.x361*m.x90 + m.x361*m.x94 + 
                         m.x361*m.x98 + m.x361*m.x101 - m.x361*m.x258 + m.x362*m.x259 - 0.3*m.x12 - 0.9*m.x28 == 0)

m.c944 = Constraint(expr=(-m.x353*m.x41) - m.x356*m.x59 - m.x359*m.x77 + m.x362*m.x87 + m.x362*m.x91 + m.x362*m.x95 + 
                         m.x362*m.x99 + m.x362*m.x102 + m.x260*m.x134 - m.x362*m.x259 - 0.3*m.x13 - 0.9*m.x29 == 0)
