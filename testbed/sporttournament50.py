#  MINLP written by GAMS Convert at 01/04/19 10:34:49
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          1        0        0        1        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#       1226        1     1225        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#       1226        1     1225        0


from pyomo.environ import *

model = m = ConcreteModel()


m.b1 = Var(within=Binary,bounds=(0,1),initialize=0)
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
m.b236 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b237 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b238 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b239 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b240 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b241 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b242 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b243 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b244 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b245 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b246 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b247 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b248 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b249 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b250 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b251 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b252 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b253 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b254 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b255 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b256 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b257 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b258 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b259 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b260 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b261 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b262 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b263 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b264 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b265 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b266 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b267 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b268 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b269 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b270 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b271 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b272 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b273 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b274 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b275 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b276 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b277 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b278 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b279 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b280 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b281 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b282 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b283 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b284 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b285 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b286 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b287 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b288 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b289 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b290 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b291 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b292 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b293 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b294 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b295 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b296 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b297 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b298 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b299 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b300 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b301 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b302 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b303 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b304 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b305 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b306 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b307 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b308 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b309 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b310 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b311 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b312 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b313 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b314 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b315 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b316 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b317 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b318 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b319 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b320 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b321 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b322 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b323 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b324 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b325 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b326 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b327 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b328 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b329 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b330 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b331 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b332 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b333 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b334 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b335 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b336 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b337 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b338 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b339 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b340 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b341 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b342 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b343 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b344 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b345 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b346 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b347 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b348 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b349 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b350 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b351 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b352 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b353 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b354 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b355 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b356 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b357 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b358 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b359 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b360 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b361 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b362 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b363 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b364 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b365 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b366 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b367 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b368 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b369 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b370 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b371 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b372 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b373 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b374 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b375 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b376 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b377 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b378 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b379 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b380 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b381 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b382 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b383 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b384 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b385 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b386 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b387 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b388 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b389 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b390 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b391 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b392 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b393 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b394 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b395 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b396 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b397 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b398 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b399 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b400 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b401 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b402 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b403 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b404 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b405 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b406 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b407 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b408 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b409 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b410 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b411 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b412 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b413 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b414 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b415 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b416 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b417 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b418 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b419 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b420 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b421 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b422 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b423 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b424 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b425 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b426 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b427 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b428 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b429 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b430 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b431 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b432 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b433 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b434 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b435 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b436 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b437 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b438 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b439 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b440 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b441 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b442 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b443 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b444 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b445 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b446 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b447 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b448 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b449 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b450 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b451 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b452 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b453 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b454 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b455 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b456 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b457 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b458 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b459 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b460 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b461 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b462 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b463 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b464 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b465 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b466 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b467 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b468 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b469 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b470 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b471 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b472 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b473 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b474 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b475 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b476 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b477 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b478 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b479 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b480 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b481 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b482 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b483 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b484 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b485 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b486 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b487 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b488 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b489 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b490 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b491 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b492 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b493 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b494 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b495 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b496 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b497 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b498 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b499 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b500 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b501 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b502 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b503 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b504 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b505 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b506 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b507 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b508 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b509 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b510 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b511 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b512 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b513 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b514 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b515 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b516 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b517 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b518 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b519 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b520 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b521 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b522 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b523 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b524 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b525 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b526 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b527 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b528 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b529 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b530 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b531 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b532 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b533 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b534 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b535 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b536 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b537 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b538 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b539 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b540 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b541 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b542 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b543 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b544 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b545 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b546 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b547 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b548 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b549 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b550 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b551 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b552 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b553 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b554 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b555 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b556 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b557 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b558 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b559 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b560 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b561 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b562 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b563 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b564 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b565 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b566 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b567 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b568 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b569 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b570 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b571 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b572 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b573 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b574 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b575 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b576 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b577 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b578 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b579 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b580 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b581 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b582 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b583 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b584 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b585 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b586 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b587 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b588 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b589 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b590 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b591 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b592 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b593 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b594 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b595 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b596 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b597 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b598 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b599 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b600 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b601 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b602 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b603 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b604 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b605 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b606 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b607 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b608 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b609 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b610 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b611 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b612 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b613 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b614 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b615 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b616 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b617 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b618 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b619 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b620 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b621 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b622 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b623 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b624 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b625 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b626 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b627 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b628 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b629 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b630 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b631 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b632 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b633 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b634 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b635 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b636 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b637 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b638 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b639 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b640 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b641 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b642 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b643 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b644 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b645 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b646 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b647 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b648 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b649 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b650 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b651 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b652 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b653 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b654 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b655 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b656 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b657 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b658 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b659 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b660 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b661 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b662 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b663 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b664 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b665 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b666 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b667 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b668 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b669 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b670 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b671 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b672 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b673 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b674 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b675 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b676 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b677 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b678 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b679 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b680 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b681 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b682 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b683 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b684 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b685 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b686 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b687 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b688 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b689 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b690 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b691 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b692 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b693 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b694 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b695 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b696 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b697 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b698 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b699 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b700 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b701 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b702 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b703 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b704 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b705 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b706 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b707 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b708 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b709 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b710 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b711 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b712 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b713 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b714 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b715 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b716 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b717 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b718 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b719 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b720 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b721 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b722 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b723 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b724 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b725 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b726 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b727 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b728 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b729 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b730 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b731 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b732 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b733 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b734 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b735 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b736 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b737 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b738 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b739 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b740 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b741 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b742 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b743 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b744 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b745 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b746 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b747 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b748 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b749 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b750 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b751 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b752 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b753 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b754 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b755 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b756 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b757 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b758 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b759 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b760 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b761 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b762 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b763 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b764 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b765 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b766 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b767 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b768 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b769 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b770 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b771 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b772 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b773 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b774 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b775 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b776 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b777 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b778 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b779 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b780 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b781 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b782 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b783 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b784 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b785 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b786 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b787 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b788 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b789 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b790 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b791 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b792 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b793 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b794 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b795 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b796 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b797 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b798 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b799 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b800 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b801 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b802 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b803 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b804 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b805 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b806 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b807 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b808 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b809 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b810 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b811 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b812 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b813 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b814 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b815 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b816 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b817 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b818 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b819 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b820 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b821 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b822 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b823 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b824 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b825 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b826 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b827 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b828 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b829 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b830 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b831 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b832 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b833 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b834 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b835 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b836 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b837 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b838 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b839 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b840 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b841 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b842 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b843 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b844 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b845 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b846 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b847 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b848 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b849 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b850 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b851 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b852 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b853 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b854 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b855 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b856 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b857 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b858 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b859 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b860 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b861 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b862 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b863 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b864 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b865 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b866 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b867 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b868 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b869 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b870 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b871 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b872 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b873 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b874 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b875 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b876 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b877 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b878 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b879 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b880 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b881 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b882 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b883 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b884 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b885 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b886 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b887 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b888 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b889 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b890 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b891 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b892 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b893 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b894 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b895 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b896 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b897 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b898 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b899 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b900 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b901 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b902 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b903 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b904 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b905 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b906 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b907 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b908 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b909 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b910 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b911 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b912 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b913 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b914 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b915 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b916 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b917 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b918 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b919 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b920 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b921 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b922 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b923 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b924 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b925 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b926 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b927 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b928 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b929 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b930 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b931 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b932 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b933 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b934 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b935 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b936 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b937 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b938 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b939 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b940 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b941 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b942 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b943 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b944 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b945 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b946 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b947 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b948 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b949 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b950 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b951 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b952 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b953 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b954 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b955 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b956 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b957 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b958 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b959 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b960 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b961 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b962 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b963 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b964 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b965 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b966 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b967 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b968 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b969 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b970 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b971 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b972 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b973 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b974 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b975 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b976 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b977 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b978 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b979 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b980 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b981 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b982 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b983 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b984 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b985 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b986 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b987 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b988 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b989 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b990 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b991 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b992 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b993 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b994 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b995 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b996 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b997 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b998 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b999 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1000 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1001 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1002 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1003 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1004 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1005 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1006 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1007 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1008 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1009 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1010 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1011 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1012 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1013 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1014 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1015 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1016 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1017 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1018 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1019 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1020 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1021 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1022 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1023 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1024 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1025 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1026 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1027 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1028 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1029 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1030 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1031 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1032 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1033 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1034 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1035 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1036 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1037 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1038 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1039 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1040 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1041 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1042 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1043 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1044 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1045 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1046 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1047 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1048 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1049 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1050 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1051 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1052 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1053 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1054 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1055 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1056 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1057 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1058 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1059 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1060 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1061 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1062 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1063 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1064 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1065 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1066 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1067 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1068 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1069 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1070 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1071 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1072 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1073 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1074 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1075 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1076 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1077 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1078 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1079 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1080 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1081 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1082 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1083 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1084 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1085 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1086 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1087 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1088 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1089 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1090 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1091 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1092 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1093 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1094 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1095 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1096 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1097 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1098 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1099 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1100 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1101 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1102 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1103 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1104 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1105 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1106 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1107 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1108 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1109 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1110 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1111 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1112 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1113 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1114 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1115 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1116 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1117 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1118 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1119 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1120 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1121 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1122 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1123 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1124 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1125 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1126 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1127 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1128 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1129 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1130 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1131 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1132 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1133 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1134 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1135 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1136 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1137 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1138 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1139 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1140 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1141 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1142 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1143 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1144 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1145 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1146 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1147 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1148 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1149 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1150 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1151 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1152 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1153 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1154 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1155 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1156 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1157 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1158 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1159 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1160 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1161 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1162 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1163 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1164 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1165 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1166 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1167 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1168 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1169 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1170 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1171 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1172 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1173 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1174 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1175 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1176 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1177 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1178 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1179 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1180 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1181 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1182 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1183 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1184 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1185 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1186 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1187 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1188 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1189 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1190 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1191 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1192 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1193 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1194 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1195 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1196 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1197 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1198 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1199 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1200 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1201 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1202 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1203 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1204 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1205 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1206 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1207 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1208 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1209 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1210 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1211 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1212 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1213 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1214 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1215 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1216 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1217 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1218 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1219 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1220 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1221 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1222 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1223 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1224 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b1225 = Var(within=Binary,bounds=(0,1),initialize=0)
m.x1226 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=m.x1226, sense=maximize)

m.c1 = Constraint(expr=2*m.b1*m.b49 - 2*m.b1 - 2*m.b49 - 2*m.b1*m.b744 + 2*m.b1*m.b745 + 2*m.b1*m.b753 + 2*m.b2*m.b554
                        - 2*m.b2 - 2*m.b554 - 2*m.b2*m.b665 + 2*m.b665 + 2*m.b2*m.b751 + 2*m.b2*m.b791 + 2*m.b3*m.b69 - 
                       2*m.b3 - 2*m.b69 + 2*m.b3*m.b106 - 2*m.b106 + 2*m.b3*m.b312 + 2*m.b312 - 2*m.b3*m.b390 + 4*m.b390
                        + 2*m.b4*m.b18 - 4*m.b4 - 2*m.b18 + 2*m.b4*m.b34 - 2*m.b34 + 2*m.b4*m.b385 - 2*m.b385 + 2*m.b4*
                       m.b783 + 2*m.b5*m.b126 - 2*m.b5 - 2*m.b126 - 2*m.b5*m.b428 + 2*m.b428 + 2*m.b5*m.b842 + 2*m.b5*
                       m.b843 + 2*m.b6*m.b106 - 2*m.b6 + 2*m.b6*m.b155 - 2*m.b155 - 2*m.b6*m.b477 + 2*m.b477 + 2*m.b6*
                       m.b858 + 2*m.b7*m.b126 - 2*m.b7 + 2*m.b7*m.b182 - 2*m.b182 - 2*m.b7*m.b522 + 2*m.b522 + 2*m.b7*
                       m.b871 + 2*m.b8*m.b155 - 2*m.b8 + 2*m.b8*m.b180 - 2*m.b180 + 2*m.b8*m.b209 - 2*m.b209 - 2*m.b8*
                       m.b573 + 2*m.b573 + 2*m.b9*m.b131 - 2*m.b9 - 2*m.b131 + 2*m.b9*m.b764 - 2*m.b9*m.b846 + 2*m.b9*
                       m.b847 + 2*m.b10*m.b153 - 2*m.b10 - 2*m.b153 + 2*m.b10*m.b182 + 2*m.b10*m.b239 - 2*m.b239 - 2*
                       m.b10*m.b627 + 2*m.b627 + 2*m.b11*m.b162 - 2*m.b11 - 2*m.b162 + 2*m.b11*m.b756 - 2*m.b11*m.b861
                        + 2*m.b11*m.b862 + 2*m.b12*m.b19 - 2*m.b12 - 4*m.b19 + 2*m.b12*m.b59 - 4*m.b59 + 2*m.b12*m.b814
                        - 2*m.b12*m.b945 + 2*m.b13*m.b154 - 2*m.b13 - 4*m.b154 + 2*m.b13*m.b209 + 2*m.b13*m.b276 - 2*
                       m.b276 - 2*m.b13*m.b688 + 2*m.b688 + 2*m.b14*m.b188 - 2*m.b14 - 2*m.b188 + 2*m.b14*m.b488 + 2*
                       m.b488 + 2*m.b14*m.b757 - 2*m.b14*m.b875 + 2*m.b15*m.b181 - 2*m.b15 - 4*m.b181 + 2*m.b15*m.b239
                        + 2*m.b15*m.b314 - 2*m.b314 - 2*m.b15*m.b933 + 2*m.b16*m.b216 - 2*m.b16 - 2*m.b216 + 2*m.b16*
                       m.b765 + 2*m.b16*m.b787 - 2*m.b16*m.b890 - 2*m.b17*m.b400 - 2*m.b17 + 2*m.b400 + 2*m.b17*m.b402
                        - 2*m.b402 + 2*m.b17*m.b645 - 4*m.b645 + 2*m.b17*m.b833 - 2*m.b18*m.b347 - 2*m.b347 + 2*m.b18*
                       m.b469 - 2*m.b469 + 2*m.b18*m.b677 - 4*m.b677 + 2*m.b19*m.b208 - 4*m.b208 + 2*m.b19*m.b276 + 2*
                       m.b19*m.b353 - 2*m.b353 + 2*m.b20*m.b248 - 2*m.b20 - 2*m.b248 - 2*m.b20*m.b438 + 2*m.b438 + 2*
                       m.b20*m.b773 + 2*m.b20*m.b774 + 2*m.b21*m.b364 - 2*m.b21 - 2*m.b364 - 2*m.b21*m.b441 + 2*m.b441
                        + 2*m.b21*m.b707 - 4*m.b707 + 2*m.b21*m.b710 + 2*m.b710 + 2*m.b22*m.b237 - 4*m.b22 - 4*m.b237 + 
                       2*m.b22*m.b314 + 2*m.b22*m.b391 - 2*m.b391 + 2*m.b22*m.b933 + 2*m.b23*m.b285 - 2*m.b23 - 2*m.b285
                        - 2*m.b23*m.b485 + 2*m.b485 + 2*m.b23*m.b764 + 2*m.b23*m.b788 + 2*m.b24*m.b322 - 2*m.b24 - 2*
                       m.b322 - 2*m.b24*m.b533 + 2*m.b533 + 2*m.b24*m.b756 + 2*m.b24*m.b804 + 2*m.b25*m.b192 - 2*m.b25
                        - 2*m.b192 - 2*m.b25*m.b597 + 4*m.b597 + 2*m.b25*m.b940 + 2*m.b25*m.b941 + 2*m.b26*m.b46 - 2*
                       m.b26 - 2*m.b46 + 2*m.b26*m.b557 - 4*m.b557 + 2*m.b27*m.b219 - 2*m.b27 - 4*m.b219 + 2*m.b27*
                       m.b329 - 2*m.b329 - 2*m.b27*m.b654 + 4*m.b654 + 2*m.b27*m.b953 + 2*m.b28*m.b251 - 2*m.b28 - 4*
                       m.b251 + 2*m.b28*m.b368 - 2*m.b368 - 2*m.b28*m.b716 + 2*m.b716 + 2*m.b28*m.b966 - 2*m.b29*m.b177
                        - 2*m.b29 - 2*m.b177 + 2*m.b29*m.b748 + 2*m.b29*m.b797 + 2*m.b29*m.b870 + 2*m.b30*m.b137 - 2*
                       m.b30 - 2*m.b137 + 2*m.b30*m.b289 - 4*m.b289 + 2*m.b30*m.b405 - 4*m.b405 - 2*m.b30*m.b980 + 2*
                       m.b31*m.b79 - 2*m.b31 - 4*m.b79 - 2*m.b31*m.b166 - 2*m.b166 + 2*m.b31*m.b289 + 2*m.b31*m.b1008 + 
                       2*m.b32*m.b81 - 2*m.b32 - 2*m.b81 + 2*m.b32*m.b982 - 2*m.b33*m.b149 - 2*m.b33 - 2*m.b149 + 2*
                       m.b33*m.b752 + 2*m.b33*m.b784 + 2*m.b33*m.b885 + 2*m.b34*m.b737 + 2*m.b34*m.b870 - 2*m.b34*m.b886
                        + 2*m.b35*m.b166 - 2*m.b35 + 2*m.b35*m.b330 - 4*m.b330 + 2*m.b35*m.b450 - 4*m.b450 - 2*m.b35*
                       m.b994 + 2*m.b36*m.b55 - 2*m.b36 - 2*m.b55 + 2*m.b36*m.b95 - 4*m.b95 - 2*m.b36*m.b137 + 2*m.b36*
                       m.b330 + 2*m.b37*m.b99 - 2*m.b37 - 2*m.b99 + 2*m.b37*m.b996 + 2*m.b38*m.b469 - 2*m.b38 + 2*m.b38*
                       m.b759 + 2*m.b38*m.b901 - 2*m.b38*m.b969 + 2*m.b39*m.b40 - 4*m.b39 - 2*m.b40 + 2*m.b39*m.b856 + 2
                       *m.b39*m.b885 + 2*m.b39*m.b886 + 2*m.b40*m.b58 - 2*m.b58 - 2*m.b40*m.b348 + 4*m.b348 + 2*m.b40*
                       m.b736 + 2*m.b41*m.b104 - 2*m.b41 - 2*m.b104 + 2*m.b41*m.b273 - 4*m.b273 + 2*m.b41*m.b744 - 2*
                       m.b41*m.b1055 + 2*m.b42*m.b73 - 2*m.b42 - 2*m.b73 + 2*m.b42*m.b359 - 2*m.b359 - 2*m.b42*m.b934 + 
                       2*m.b42*m.b935 + 2*m.b43*m.b642 - 2*m.b43 - 2*m.b642 + 2*m.b43*m.b846 - 2*m.b43*m.b961 + 2*m.b43*
                       m.b962 + 2*m.b44*m.b192 - 2*m.b44 + 2*m.b44*m.b369 - 4*m.b369 + 2*m.b44*m.b500 - 4*m.b500 - 2*
                       m.b44*m.b1007 + 2*m.b45*m.b65 - 2*m.b45 - 4*m.b65 + 2*m.b45*m.b115 - 4*m.b115 + 2*m.b45*m.b369 - 
                       2*m.b45*m.b966 + 2*m.b46*m.b47 - 2*m.b47 - 2*m.b46*m.b142 - 2*m.b142 + 2*m.b46*m.b298 - 4*m.b298
                        + 2*m.b47*m.b118 - 2*m.b118 + 2*m.b48*m.b49 - 4*m.b48 + 2*m.b48*m.b840 + 2*m.b48*m.b901 + 2*
                       m.b48*m.b902 + 2*m.b49*m.b68 - 2*m.b68 - 2*m.b49*m.b386 + 2*m.b386 + 2*m.b50*m.b104 - 2*m.b50 + 2
                       *m.b50*m.b150 - 2*m.b150 + 2*m.b50*m.b737 - 2*m.b50*m.b1024 + 2*m.b51*m.b396 - 2*m.b51 - 2*m.b396
                        - 2*m.b51*m.b947 + 2*m.b51*m.b948 + 2*m.b51*m.b949 + 2*m.b52*m.b830 - 2*m.b52 - 2*m.b52*m.b975
                        + 2*m.b52*m.b976 + 2*m.b52*m.b977 + 2*m.b53*m.b219 - 2*m.b53 + 2*m.b53*m.b406 - 4*m.b406 + 2*
                       m.b53*m.b544 - 4*m.b544 - 2*m.b53*m.b1019 + 2*m.b54*m.b79 - 2*m.b54 + 2*m.b54*m.b139 - 4*m.b139
                        + 2*m.b54*m.b406 - 2*m.b54*m.b953 + 2*m.b55*m.b659 - 4*m.b659 + 2*m.b55*m.b981 - 2*m.b55*m.b1020
                        + 2*m.b56*m.b57 - 2*m.b56 - 2*m.b57 - 2*m.b56*m.b117 - 2*m.b117 + 2*m.b56*m.b337 - 4*m.b337 + 2*
                       m.b56*m.b1021 + 2*m.b57*m.b143 - 4*m.b143 + 2*m.b58*m.b178 - 4*m.b178 - 2*m.b58*m.b1013 + 2*m.b58
                       *m.b1055 + 2*m.b59*m.b104 + 2*m.b59*m.b178 + 2*m.b59*m.b842 + 2*m.b60*m.b71 + 2*m.b60 + 2*m.b71
                        - 2*m.b60*m.b127 + 4*m.b127 - 2*m.b60*m.b578 - 2*m.b578 - 2*m.b60*m.b769 + 2*m.b61*m.b436 - 2*
                       m.b61 - 2*m.b436 - 2*m.b61*m.b958 + 2*m.b61*m.b959 + 2*m.b61*m.b960 + 2*m.b62*m.b533 - 2*m.b62 + 
                       2*m.b62*m.b817 - 2*m.b62*m.b991 + 2*m.b62*m.b992 + 2*m.b63*m.b251 - 2*m.b63 + 2*m.b63*m.b451 - 4*
                       m.b451 + 2*m.b63*m.b598 - 4*m.b598 - 2*m.b63*m.b1029 + 2*m.b64*m.b95 - 2*m.b64 + 2*m.b64*m.b168
                        - 4*m.b168 + 2*m.b64*m.b451 - 2*m.b64*m.b941 + 2*m.b65*m.b254 - 4*m.b254 + 2*m.b65*m.b967 + 2*
                       m.b65*m.b1009 + 2*m.b66*m.b67 - 2*m.b66 - 2*m.b67 - 2*m.b66*m.b98 - 2*m.b98 + 2*m.b66*m.b376 - 4*
                       m.b376 + 2*m.b66*m.b1030 + 2*m.b67*m.b171 - 4*m.b171 + 2*m.b68*m.b150 + 2*m.b68*m.b206 - 4*m.b206
                        - 2*m.b68*m.b1001 + 2*m.b69*m.b156 - 2*m.b156 + 2*m.b69*m.b814 - 2*m.b69*m.b1098 - 2*m.b70*
                       m.b157 + 2*m.b70 + 4*m.b157 - 2*m.b70*m.b760 + 2*m.b70*m.b762 - 2*m.b70*m.b827 - 2*m.b71*m.b771
                        - 2*m.b71*m.b1088 - 2*m.b71*m.b1089 + 2*m.b72*m.b245 - 2*m.b72 - 4*m.b245 + 2*m.b72*m.b483 - 2*
                       m.b483 - 2*m.b72*m.b973 + 2*m.b72*m.b974 + 2*m.b73*m.b731 + 2*m.b73*m.b860 - 2*m.b73*m.b937 + 2*
                       m.b74*m.b485 - 2*m.b74 + 2*m.b74*m.b802 - 2*m.b74*m.b1005 + 2*m.b74*m.b1006 + 2*m.b75*m.b76 - 2*
                       m.b75 - 2*m.b76 + 2*m.b75*m.b112 - 2*m.b112 + 2*m.b75*m.b325 - 4*m.b325 - 2*m.b75*m.b848 + 2*
                       m.b76*m.b133 - 2*m.b133 + 2*m.b76*m.b217 - 2*m.b217 - 2*m.b76*m.b1101 + 2*m.b77*m.b289 - 4*m.b77
                        + 2*m.b77*m.b501 - 2*m.b501 + 2*m.b77*m.b655 - 4*m.b655 + 2*m.b77*m.b1029 + 2*m.b78*m.b115 - 4*
                       m.b78 + 2*m.b78*m.b194 - 4*m.b194 + 2*m.b78*m.b501 + 2*m.b78*m.b941 + 2*m.b79*m.b954 + 2*m.b79*
                       m.b1020 - 2*m.b80*m.b81 - 2*m.b80 + 2*m.b80*m.b169 - 4*m.b169 + 2*m.b80*m.b197 - 4*m.b197 + 2*
                       m.b80*m.b1048 + 2*m.b81*m.b82 - 2*m.b82 + 2*m.b81*m.b728 - 2*m.b728 + 2*m.b82*m.b197 + 2*m.b83*
                       m.b850 - 2*m.b83 + 2*m.b83*m.b1093 + 2*m.b84*m.b85 - 2*m.b84 - 4*m.b85 - 2*m.b84*m.b562 + 2*
                       m.b562 + 2*m.b84*m.b782 + 2*m.b84*m.b930 + 2*m.b85*m.b419 - 2*m.b419 + 2*m.b85*m.b463 - 4*m.b463
                        + 2*m.b85*m.b743 + 2*m.b86*m.b88 + 2*m.b86 - 2*m.b88 - 2*m.b86*m.b184 + 4*m.b184 - 2*m.b86*
                       m.b754 - 2*m.b86*m.b844 - 2*m.b87*m.b785 + 2*m.b87 + 2*m.b87*m.b799 - 2*m.b87*m.b1074 - 2*m.b87*
                       m.b1075 + 2*m.b88*m.b771 + 2*m.b88*m.b1075 - 2*m.b88*m.b1108 + 2*m.b89*m.b282 - 4*m.b89 - 4*
                       m.b282 + 2*m.b89*m.b529 - 2*m.b529 + 2*m.b89*m.b973 + 2*m.b89*m.b990 + 2*m.b90*m.b321 - 2*m.b90
                        - 2*m.b321 + 2*m.b90*m.b529 - 2*m.b90*m.b923 + 2*m.b90*m.b949 + 2*m.b91*m.b161 - 2*m.b91 - 2*
                       m.b161 + 2*m.b91*m.b360 - 2*m.b360 + 2*m.b91*m.b438 - 2*m.b91*m.b1018 + 2*m.b92*m.b134 - 2*m.b92
                        - 4*m.b134 - 2*m.b92*m.b654 + 2*m.b92*m.b738 + 2*m.b92*m.b894 + 2*m.b93*m.b330 - 4*m.b93 + 2*
                       m.b93*m.b545 - 2*m.b545 + 2*m.b93*m.b717 - 4*m.b717 + 2*m.b93*m.b1019 + 2*m.b94*m.b139 - 4*m.b94
                        + 2*m.b94*m.b221 - 4*m.b221 + 2*m.b94*m.b545 + 2*m.b94*m.b953 + 2*m.b95*m.b942 + 2*m.b95*m.b1010
                        - 2*m.b96*m.b97 - 2*m.b96 + 2*m.b97 + 2*m.b96*m.b735 + 2*m.b96*m.b751 + 2*m.b96*m.b1010 + 2*
                       m.b97*m.b195 - 4*m.b195 - 2*m.b97*m.b1048 - 2*m.b97*m.b1111 + 2*m.b98*m.b195 + 2*m.b98*m.b225 - 4
                       *m.b225 + 2*m.b98*m.b1063 + 2*m.b99*m.b100 - 2*m.b100 + 2*m.b99*m.b668 - 2*m.b668 - 2*m.b99*
                       m.b1050 + 2*m.b100*m.b225 + 2*m.b101*m.b866 - 2*m.b101 + 2*m.b101*m.b1080 - 2*m.b102*m.b512 + 2*
                       m.b102 + 2*m.b512 - 2*m.b102*m.b782 + 2*m.b102*m.b916 - 2*m.b102*m.b1095 - 2*m.b103*m.b613 - 2*
                       m.b103 + 2*m.b613 + 2*m.b103*m.b795 + 2*m.b103*m.b943 + 2*m.b103*m.b1095 - 2*m.b104*m.b1042 + 2*
                       m.b105*m.b180 + 2*m.b105 - 2*m.b105*m.b686 - 2*m.b686 - 2*m.b105*m.b753 - 2*m.b105*m.b871 + 2*
                       m.b106*m.b630 - 2*m.b630 - 2*m.b106*m.b1072 + 2*m.b107*m.b109 + 2*m.b107 - 4*m.b109 - 2*m.b107*
                       m.b696 + 2*m.b696 - 2*m.b107*m.b750 - 2*m.b107*m.b859 - 2*m.b108*m.b694 + 4*m.b108 + 2*m.b694 - 2
                       *m.b108*m.b799 - 2*m.b108*m.b800 - 2*m.b108*m.b1059 + 2*m.b109*m.b430 - 4*m.b430 + 2*m.b109*
                       m.b785 + 2*m.b109*m.b1059 + 2*m.b110*m.b319 - 4*m.b110 - 4*m.b319 + 2*m.b110*m.b585 - 2*m.b585 + 
                       2*m.b110*m.b958 + 2*m.b110*m.b1004 + 2*m.b111*m.b397 - 4*m.b111 - 2*m.b397 + 2*m.b111*m.b831 + 2*
                       m.b111*m.b890 + 2*m.b111*m.b1018 + 2*m.b112*m.b163 - 2*m.b163 + 2*m.b112*m.b287 - 2*m.b287 - 2*
                       m.b112*m.b595 + 4*m.b595 + 2*m.b113*m.b369 - 2*m.b113 + 2*m.b113*m.b599 - 2*m.b599 - 2*m.b113*
                       m.b738 + 2*m.b113*m.b1007 + 2*m.b114*m.b168 - 4*m.b114 + 2*m.b114*m.b253 - 4*m.b253 + 2*m.b114*
                       m.b599 + 2*m.b114*m.b966 + 2*m.b115*m.b929 + 2*m.b115*m.b995 + 2*m.b116*m.b117 - 2*m.b116 + 2*
                       m.b116*m.b1066 - 2*m.b116*m.b1078 + 2*m.b116*m.b1079 + 2*m.b117*m.b223 - 4*m.b223 + 2*m.b117*
                       m.b262 - 2*m.b262 + 2*m.b118*m.b119 - 2*m.b119 + 2*m.b118*m.b606 - 2*m.b606 - 2*m.b118*m.b1066 + 
                       2*m.b119*m.b262 + 2*m.b120*m.b302 + 2*m.b120 + 2*m.b302 - 2*m.b120*m.b510 + 2*m.b510 - 2*m.b120*
                       m.b808 - 2*m.b120*m.b1119 + 2*m.b121*m.b123 - 2*m.b121 - 2*m.b123 + 2*m.b121*m.b381 - 4*m.b381 - 
                       2*m.b121*m.b611 + 2*m.b611 + 2*m.b121*m.b955 - 2*m.b122*m.b795 + 2*m.b122 + 2*m.b122*m.b899 - 2*
                       m.b122*m.b1081 - 2*m.b122*m.b1083 - 2*m.b123*m.b673 + 2*m.b673 + 2*m.b123*m.b809 + 2*m.b123*
                       m.b1083 + 2*m.b124*m.b153 + 2*m.b124 - 2*m.b124*m.b625 - 2*m.b625 - 2*m.b124*m.b749 - 2*m.b124*
                       m.b858 + 2*m.b125*m.b153 - 2*m.b125 + 2*m.b125*m.b311 - 4*m.b311 - 2*m.b125*m.b428 + 2*m.b125*
                       m.b1055 + 2*m.b126*m.b691 - 2*m.b691 - 2*m.b126*m.b1057 - 2*m.b127*m.b815 - 2*m.b127*m.b1044 - 2*
                       m.b127*m.b1045 + 2*m.b128*m.b800 - 4*m.b128 + 2*m.b128*m.b872 + 2*m.b128*m.b1045 + 2*m.b128*
                       m.b1108 + 2*m.b129*m.b214 - 4*m.b129 - 2*m.b214 + 2*m.b129*m.b358 - 4*m.b358 + 2*m.b129*m.b638 - 
                       2*m.b638 + 2*m.b129*m.b947 + 2*m.b130*m.b131 - 4*m.b130 + 2*m.b130*m.b437 - 4*m.b437 + 2*m.b130*
                       m.b875 + 2*m.b130*m.b1005 - 2*m.b131*m.b1123 + 2*m.b131*m.b1124 + 2*m.b132*m.b134 - 2*m.b132 + 2*
                       m.b132*m.b249 - 2*m.b249 - 2*m.b132*m.b652 + 4*m.b652 + 2*m.b132*m.b833 + 2*m.b133*m.b135 - 4*
                       m.b135 + 2*m.b133*m.b739 - 2*m.b133*m.b926 + 2*m.b134*m.b135 + 2*m.b134*m.b1062 + 2*m.b135*m.b543
                        + 2*m.b543 + 2*m.b135*m.b733 + 2*m.b136*m.b406 - 2*m.b136 + 2*m.b136*m.b657 - 2*m.b657 - 2*
                       m.b136*m.b733 + 2*m.b136*m.b994 + 2*m.b137*m.b138 - 4*m.b138 + 2*m.b137*m.b912 + 2*m.b138*m.b194
                        + 2*m.b138*m.b291 - 4*m.b291 + 2*m.b138*m.b657 + 2*m.b139*m.b915 + 2*m.b139*m.b981 + 2*m.b140*
                       m.b254 - 2*m.b140 + 2*m.b140*m.b551 + 2*m.b551 + 2*m.b140*m.b724 - 4*m.b724 - 2*m.b140*m.b1065 + 
                       2*m.b141*m.b142 - 4*m.b141 + 2*m.b141*m.b1050 + 2*m.b141*m.b1078 + 2*m.b141*m.b1092 + 2*m.b142*
                       m.b259 - 4*m.b259 + 2*m.b142*m.b299 - 2*m.b299 + 2*m.b143*m.b144 - 2*m.b144 + 2*m.b143*m.b555 - 4
                       *m.b555 + 2*m.b143*m.b1066 + 2*m.b144*m.b299 - 2*m.b145*m.b560 + 2*m.b145 + 2*m.b560 - 2*m.b145*
                       m.b794 + 2*m.b145*m.b852 - 2*m.b145*m.b1129 + 2*m.b146*m.b148 - 2*m.b146 - 2*m.b148 + 2*m.b146*
                       m.b418 - 4*m.b418 - 2*m.b146*m.b671 + 2*m.b671 + 2*m.b146*m.b968 - 2*m.b147*m.b809 + 2*m.b147 + 2
                       *m.b147*m.b881 - 2*m.b147*m.b1067 - 2*m.b147*m.b1069 + 2*m.b148*m.b822 + 2*m.b148*m.b1069 - 2*
                       m.b148*m.b1130 + 2*m.b149*m.b385 + 2*m.b149*m.b563 - 2*m.b563 + 2*m.b149*m.b1012 + 2*m.b150*
                       m.b152 - 2*m.b152 - 2*m.b150*m.b1071 + 2*m.b151*m.b154 + 2*m.b151 - 2*m.b151*m.b571 - 2*m.b571 - 
                       2*m.b151*m.b745 - 2*m.b151*m.b842 + 2*m.b152*m.b154 + 2*m.b152*m.b351 - 4*m.b351 - 2*m.b152*
                       m.b477 - 2*m.b153*m.b1135 + 2*m.b154*m.b1135 - 2*m.b155*m.b355 + 2*m.b355 + 2*m.b155*m.b770 + 2*
                       m.b156*m.b243 - 2*m.b243 + 2*m.b156*m.b353 - 2*m.b156*m.b523 - 2*m.b523 - 2*m.b157*m.b828 - 2*
                       m.b157*m.b1036 - 2*m.b157*m.b1037 + 2*m.b158*m.b815 - 4*m.b158 + 2*m.b158*m.b887 + 2*m.b158*
                       m.b1037 + 2*m.b158*m.b1100 + 2*m.b159*m.b246 - 4*m.b159 - 4*m.b246 + 2*m.b159*m.b395 - 4*m.b395
                        + 2*m.b159*m.b700 - 2*m.b700 + 2*m.b159*m.b934 + 2*m.b160*m.b162 - 4*m.b160 + 2*m.b160*m.b484 - 
                       4*m.b484 + 2*m.b160*m.b861 + 2*m.b160*m.b991 + 2*m.b161*m.b321 + 2*m.b161*m.b816 - 2*m.b161*
                       m.b1138 - 2*m.b162*m.b1137 + 2*m.b162*m.b1138 - 2*m.b163*m.b164 + 2*m.b164 + 2*m.b163*m.b734 + 2*
                       m.b163*m.b1077 + 2*m.b164*m.b499 + 2*m.b499 - 2*m.b164*m.b597 - 2*m.b164*m.b1141 + 2*m.b165*
                       m.b451 - 4*m.b165 + 2*m.b165*m.b719 - 2*m.b719 + 2*m.b165*m.b738 + 2*m.b165*m.b980 + 2*m.b166*
                       m.b167 - 4*m.b167 + 2*m.b166*m.b927 + 2*m.b167*m.b221 + 2*m.b167*m.b332 - 4*m.b332 + 2*m.b167*
                       m.b719 + 2*m.b168*m.b898 + 2*m.b168*m.b967 + 2*m.b169*m.b170 - 2*m.b170 + 2*m.b169*m.b1064 + 2*
                       m.b169*m.b1104 + 2*m.b170*m.b296 - 4*m.b296 + 2*m.b170*m.b338 - 2*m.b338 - 2*m.b170*m.b996 + 2*
                       m.b171*m.b172 - 2*m.b172 + 2*m.b171*m.b607 - 4*m.b607 + 2*m.b171*m.b1050 + 2*m.b172*m.b338 - 2*
                       m.b173*m.b611 + 2*m.b173 - 2*m.b173*m.b781 + 2*m.b173*m.b868 - 2*m.b173*m.b1144 + 2*m.b174*m.b176
                        - 2*m.b174 - 2*m.b176 + 2*m.b174*m.b461 - 4*m.b461 - 2*m.b174*m.b983 + 2*m.b174*m.b984 - 2*
                       m.b175*m.b822 + 2*m.b175 + 2*m.b175*m.b867 - 2*m.b175*m.b1051 - 2*m.b175*m.b1052 + 2*m.b176*
                       m.b837 + 2*m.b176*m.b1052 - 2*m.b176*m.b1145 + 2*m.b177*m.b616 - 2*m.b616 + 2*m.b177*m.b1022 + 2*
                       m.b177*m.b1146 + 2*m.b178*m.b179 - 2*m.b179 + 2*m.b178*m.b1085 + 2*m.b179*m.b181 + 2*m.b179*
                       m.b389 - 4*m.b389 - 2*m.b179*m.b522 - 2*m.b180*m.b238 - 2*m.b238 + 2*m.b180*m.b1042 + 2*m.b181*
                       m.b238 + 2*m.b181*m.b798 + 2*m.b182*m.b183 - 2*m.b183 - 2*m.b182*m.b316 + 2*m.b316 + 2*m.b183*
                       m.b577 - 4*m.b577 - 2*m.b183*m.b760 + 2*m.b183*m.b1136 - 2*m.b184*m.b845 - 2*m.b184*m.b1026 - 2*
                       m.b184*m.b1027 + 2*m.b185*m.b828 - 4*m.b185 + 2*m.b185*m.b903 + 2*m.b185*m.b1027 + 2*m.b185*
                       m.b1088 + 2*m.b186*m.b283 - 4*m.b186 - 4*m.b283 + 2*m.b186*m.b434 - 4*m.b434 + 2*m.b186*m.b732 + 
                       2*m.b186*m.b921 + 2*m.b187*m.b188 - 4*m.b187 + 2*m.b187*m.b531 - 4*m.b531 + 2*m.b187*m.b846 + 2*
                       m.b187*m.b975 + 2*m.b188*m.b361 - 2*m.b361 - 2*m.b188*m.b1150 + 2*m.b189*m.b324 - 4*m.b189 - 2*
                       m.b324 + 2*m.b189*m.b361 + 2*m.b189*m.b490 + 2*m.b490 + 2*m.b189*m.b801 - 2*m.b190*m.b191 - 2*
                       m.b190 + 2*m.b191 + 2*m.b190*m.b739 + 2*m.b190*m.b832 + 2*m.b190*m.b1090 + 2*m.b191*m.b449 + 2*
                       m.b449 - 2*m.b191*m.b654 - 2*m.b191*m.b1152 + 2*m.b192*m.b193 - 2*m.b193 - 2*m.b192*m.b1009 + 2*
                       m.b193*m.b253 + 2*m.b193*m.b371 - 4*m.b371 - 2*m.b193*m.b720 - 2*m.b720 + 2*m.b194*m.b880 + 2*
                       m.b194*m.b954 + 2*m.b195*m.b196 - 2*m.b196 + 2*m.b195*m.b258 - 2*m.b258 + 2*m.b196*m.b336 - 4*
                       m.b336 + 2*m.b196*m.b377 - 2*m.b377 - 2*m.b196*m.b982 + 2*m.b197*m.b198 - 2*m.b198 + 2*m.b197*
                       m.b669 - 4*m.b669 + 2*m.b198*m.b377 - 2*m.b199*m.b200 + 2*m.b199 + 2*m.b200 - 2*m.b199*m.b768 + 2
                       *m.b200*m.b201 - 2*m.b201 - 2*m.b200*m.b671 - 2*m.b200*m.b1154 + 2*m.b201*m.b462 - 4*m.b462 - 2*
                       m.b201*m.b807 + 2*m.b201*m.b881 + 2*m.b202*m.b204 - 2*m.b202 - 4*m.b204 + 2*m.b202*m.b511 - 4*
                       m.b511 - 2*m.b202*m.b997 + 2*m.b202*m.b998 - 2*m.b203*m.b837 + 2*m.b203 + 2*m.b203*m.b851 - 2*
                       m.b203*m.b1039 - 2*m.b203*m.b1041 + 2*m.b204*m.b462 + 2*m.b204*m.b853 + 2*m.b204*m.b1041 + 2*
                       m.b205*m.b676 - 2*m.b205 - 4*m.b676 - 2*m.b205*m.b931 + 2*m.b205*m.b1032 + 2*m.b205*m.b1155 + 2*
                       m.b206*m.b207 - 2*m.b207 + 2*m.b206*m.b1071 + 2*m.b206*m.b1097 + 2*m.b207*m.b208 + 2*m.b207*
                       m.b426 - 4*m.b426 - 2*m.b207*m.b573 + 2*m.b208*m.b275 - 2*m.b275 + 2*m.b208*m.b813 + 2*m.b209*
                       m.b212 - 2*m.b212 - 2*m.b209*m.b278 + 2*m.b278 + 2*m.b210*m.b212 - 2*m.b210 + 2*m.b210*m.b275 - 2
                       *m.b210*m.b691 + 2*m.b210*m.b1135 - 2*m.b211*m.b276 + 2*m.b211 - 2*m.b211*m.b429 - 2*m.b429 + 2*
                       m.b211*m.b631 - 4*m.b631 - 2*m.b211*m.b690 - 2*m.b690 + 2*m.b212*m.b631 - 2*m.b212*m.b754 + 2*
                       m.b213*m.b845 - 4*m.b213 + 2*m.b213*m.b919 + 2*m.b213*m.b1016 + 2*m.b213*m.b1074 + 2*m.b214*
                       m.b873 + 2*m.b214*m.b962 - 2*m.b214*m.b1018 + 2*m.b215*m.b216 - 4*m.b215 + 2*m.b215*m.b587 - 4*
                       m.b587 + 2*m.b215*m.b830 + 2*m.b215*m.b961 + 2*m.b216*m.b398 - 2*m.b398 - 2*m.b216*m.b532 + 2*
                       m.b532 - 2*m.b217*m.b218 + 2*m.b218 + 2*m.b217*m.b818 + 2*m.b217*m.b910 - 2*m.b218*m.b716 + 2*
                       m.b218*m.b913 - 2*m.b218*m.b1160 + 2*m.b219*m.b220 - 2*m.b220 + 2*m.b219*m.b659 + 2*m.b220*m.b291
                        + 2*m.b220*m.b409 - 4*m.b409 - 2*m.b220*m.b658 - 2*m.b658 + 2*m.b221*m.b292 - 2*m.b292 + 2*
                       m.b221*m.b942 + 2*m.b222*m.b550 + 2*m.b222 - 4*m.b550 - 2*m.b222*m.b741 - 2*m.b222*m.b995 - 2*
                       m.b222*m.b1104 + 2*m.b223*m.b224 - 4*m.b224 + 2*m.b223*m.b295 - 2*m.b295 + 2*m.b223*m.b1049 + 2*
                       m.b224*m.b375 - 4*m.b375 + 2*m.b224*m.b414 - 2*m.b414 + 2*m.b224*m.b982 + 2*m.b225*m.b226 - 2*
                       m.b226 + 2*m.b225*m.b729 - 4*m.b729 + 2*m.b226*m.b414 - 2*m.b227*m.b228 + 2*m.b227 + 2*m.b228 - 2
                       *m.b227*m.b780 + 2*m.b228*m.b229 - 2*m.b229 - 2*m.b228*m.b983 - 2*m.b228*m.b1162 - 2*m.b229*
                       m.b793 + 2*m.b229*m.b899 + 2*m.b229*m.b1145 + 2*m.b230*m.b232 - 4*m.b230 - 4*m.b232 + 2*m.b230*
                       m.b304 + 2*m.b304 + 2*m.b230*m.b561 - 4*m.b561 + 2*m.b230*m.b997 - 2*m.b231*m.b851 + 4*m.b231 - 2
                       *m.b231*m.b853 - 2*m.b231*m.b1031 - 2*m.b231*m.b1033 + 2*m.b232*m.b869 + 2*m.b232*m.b1033 + 2*
                       m.b232*m.b1145 + 2*m.b233*m.b234 - 2*m.b233 - 2*m.b234 - 2*m.b233*m.b759 + 2*m.b233*m.b795 + 2*
                       m.b233*m.b1033 - 2*m.b234*m.b917 + 2*m.b234*m.b1040 + 2*m.b234*m.b1163 + 2*m.b235*m.b236 - 4*
                       m.b235 - 2*m.b236 + 2*m.b235*m.b1056 + 2*m.b235*m.b1085 + 2*m.b235*m.b1106 + 2*m.b236*m.b237 + 2*
                       m.b236*m.b473 - 4*m.b473 - 2*m.b236*m.b627 + 2*m.b237*m.b313 - 2*m.b313 + 2*m.b237*m.b826 + 2*
                       m.b238*m.b240 - 2*m.b240 + 2*m.b238*m.b1136 - 2*m.b239*m.b241 + 2*m.b241 + 2*m.b239*m.b242 - 2*
                       m.b242 + 2*m.b240*m.b242 + 2*m.b240*m.b313 - 2*m.b240*m.b630 - 2*m.b241*m.b629 - 2*m.b629 + 2*
                       m.b241*m.b692 - 4*m.b692 - 2*m.b241*m.b1107 + 2*m.b242*m.b692 - 2*m.b242*m.b750 + 2*m.b243*m.b430
                        - 2*m.b243*m.b694 + 2*m.b243*m.b1057 + 2*m.b244*m.b245 + 2*m.b244 - 2*m.b244*m.b634 + 2*m.b634
                        - 2*m.b244*m.b958 - 2*m.b244*m.b1166 + 2*m.b245*m.b771 + 2*m.b245*m.b1167 + 2*m.b246*m.b888 + 2*
                       m.b246*m.b976 + 2*m.b246*m.b1018 + 2*m.b247*m.b248 - 4*m.b247 + 2*m.b247*m.b640 - 4*m.b640 + 2*
                       m.b247*m.b817 + 2*m.b247*m.b951 + 2*m.b248*m.b439 - 2*m.b439 - 2*m.b248*m.b588 + 2*m.b588 + 2*
                       m.b249*m.b401 - 2*m.b401 - 2*m.b249*m.b540 + 2*m.b540 + 2*m.b249*m.b925 - 2*m.b250*m.b895 + 2*
                       m.b250 + 2*m.b250*m.b928 - 2*m.b250*m.b980 - 2*m.b250*m.b1170 + 2*m.b251*m.b252 - 2*m.b252 + 2*
                       m.b251*m.b1009 + 2*m.b252*m.b332 + 2*m.b252*m.b453 - 4*m.b453 - 2*m.b252*m.b600 - 2*m.b600 + 2*
                       m.b253*m.b255 - 4*m.b255 + 2*m.b253*m.b929 + 2*m.b254*m.b257 - 4*m.b257 + 2*m.b254*m.b662 - 4*
                       m.b662 + 2*m.b255*m.b257 + 2*m.b255*m.b453 + 2*m.b255*m.b897 - 2*m.b256*m.b258 + 2*m.b256 + 2*
                       m.b256*m.b505 - 4*m.b505 - 2*m.b256*m.b665 - 2*m.b256*m.b981 + 2*m.b257*m.b258 + 2*m.b257*m.b741
                        + 2*m.b258*m.b413 - 4*m.b413 + 2*m.b259*m.b261 - 4*m.b261 + 2*m.b259*m.b335 - 2*m.b335 + 2*
                       m.b259*m.b1065 - 2*m.b260*m.b377 + 2*m.b260 + 2*m.b260*m.b457 - 4*m.b457 - 2*m.b260*m.b746 - 2*
                       m.b260*m.b758 + 2*m.b261*m.b413 + 2*m.b261*m.b457 + 2*m.b261*m.b996 + 2*m.b262*m.b263 - 2*m.b263
                        - 2*m.b262*m.b791 + 2*m.b263*m.b457 - 2*m.b264*m.b265 + 2*m.b264 + 2*m.b265 - 2*m.b264*m.b793 + 
                       2*m.b265*m.b266 - 2*m.b266 - 2*m.b265*m.b997 - 2*m.b265*m.b1171 - 2*m.b266*m.b780 + 2*m.b266*
                       m.b916 + 2*m.b266*m.b1130 + 2*m.b267*m.b268 - 4*m.b267 + 2*m.b268 + 2*m.b267*m.b269 - 4*m.b269 + 
                       2*m.b267*m.b612 - 4*m.b612 + 2*m.b267*m.b983 - 2*m.b268*m.b867 - 2*m.b268*m.b869 - 2*m.b268*
                       m.b1023 + 2*m.b269*m.b883 + 2*m.b269*m.b1023 + 2*m.b269*m.b1130 + 2*m.b270*m.b272 - 2*m.b270 - 2*
                       m.b272 + 2*m.b270*m.b675 - 4*m.b675 - 2*m.b270*m.b1052 + 2*m.b270*m.b1053 + 2*m.b271*m.b272 - 2*
                       m.b271 - 2*m.b271*m.b752 + 2*m.b271*m.b809 + 2*m.b271*m.b1023 + 2*m.b272*m.b565 - 2*m.b565 - 2*
                       m.b272*m.b900 + 2*m.b273*m.b350 - 4*m.b350 + 2*m.b273*m.b783 + 2*m.b273*m.b1034 + 2*m.b274*m.b971
                        - 4*m.b274 + 2*m.b274*m.b1042 + 2*m.b274*m.b1097 + 2*m.b274*m.b1114 + 2*m.b275*m.b277 - 2*m.b277
                        - 2*m.b275*m.b871 + 2*m.b276*m.b279 - 4*m.b279 + 2*m.b277*m.b279 - 2*m.b277*m.b576 - 2*m.b576 + 
                       2*m.b277*m.b1172 + 2*m.b278*m.b280 - 2*m.b280 - 2*m.b278*m.b575 - 2*m.b575 - 2*m.b278*m.b1099 + 2
                       *m.b279*m.b280 + 2*m.b279*m.b750 - 2*m.b280*m.b919 + 2*m.b280*m.b1044 + 2*m.b281*m.b282 + 2*
                       m.b281 - 2*m.b281*m.b580 + 2*m.b580 - 2*m.b281*m.b973 - 2*m.b281*m.b1174 + 2*m.b282*m.b584 + 2*
                       m.b584 + 2*m.b282*m.b785 + 2*m.b283*m.b904 + 2*m.b283*m.b992 + 2*m.b283*m.b1005 + 2*m.b284*m.b285
                        - 4*m.b284 + 2*m.b284*m.b702 - 4*m.b702 + 2*m.b284*m.b802 + 2*m.b284*m.b937 + 2*m.b285*m.b486 - 
                       2*m.b486 - 2*m.b285*m.b641 + 2*m.b641 + 2*m.b286*m.b363 - 2*m.b286 + 2*m.b363 + 2*m.b286*m.b486
                        - 2*m.b286*m.b644 + 2*m.b644 + 2*m.b286*m.b1124 + 2*m.b287*m.b443 - 2*m.b443 - 2*m.b287*m.b496
                        + 2*m.b496 + 2*m.b287*m.b909 - 2*m.b288*m.b878 + 2*m.b288 + 2*m.b288*m.b940 - 2*m.b288*m.b994 - 
                       2*m.b288*m.b1177 + 2*m.b289*m.b290 - 2*m.b290 + 2*m.b290*m.b371 + 2*m.b290*m.b503 - 4*m.b503 - 2*
                       m.b290*m.b546 - 2*m.b546 + 2*m.b291*m.b293 - 4*m.b293 + 2*m.b291*m.b915 + 2*m.b292*m.b409 + 2*
                       m.b292*m.b879 - 2*m.b292*m.b1161 + 2*m.b293*m.b503 + 2*m.b293*m.b914 + 2*m.b293*m.b1161 - 2*
                       m.b294*m.b295 + 2*m.b294 + 2*m.b294*m.b454 - 4*m.b454 - 2*m.b294*m.b603 + 2*m.b603 - 2*m.b294*
                       m.b967 + 2*m.b295*m.b456 - 4*m.b456 + 2*m.b295*m.b1161 + 2*m.b296*m.b298 + 2*m.b296*m.b374 - 2*
                       m.b374 + 2*m.b296*m.b1079 - 2*m.b297*m.b338 + 2*m.b297 + 2*m.b297*m.b508 - 4*m.b508 - 2*m.b297*
                       m.b740 - 2*m.b297*m.b767 + 2*m.b298*m.b456 + 2*m.b298*m.b508 + 2*m.b299*m.b300 - 2*m.b300 - 2*
                       m.b299*m.b778 + 2*m.b300*m.b508 - 2*m.b301*m.b807 + 2*m.b301 - 2*m.b301*m.b1011 - 2*m.b302*m.b673
                        - 2*m.b302*m.b850 - 2*m.b302*m.b851 + 2*m.b303*m.b673 - 2*m.b303 - 2*m.b303*m.b768 + 2*m.b303*
                       m.b930 + 2*m.b303*m.b1011 - 2*m.b304*m.b305 + 2*m.b305 - 2*m.b304*m.b881 - 2*m.b304*m.b883 + 2*
                       m.b305*m.b306 - 2*m.b306 - 2*m.b305*m.b1012 - 2*m.b305*m.b1179 + 2*m.b306*m.b307 - 2*m.b307 - 2*
                       m.b306*m.b748 + 2*m.b306*m.b822 + 2*m.b307*m.b618 - 2*m.b618 - 2*m.b307*m.b884 + 2*m.b307*m.b1068
                        - 2*m.b308*m.b737 + 4*m.b308 - 2*m.b308*m.b885 - 2*m.b308*m.b1164 - 2*m.b308*m.b1165 + 2*m.b309*
                       m.b388 + 2*m.b309 - 4*m.b388 - 2*m.b309*m.b839 - 2*m.b309*m.b918 - 2*m.b309*m.b1133 + 2*m.b310*
                       m.b473 - 2*m.b310 + 2*m.b310*m.b570 - 4*m.b570 + 2*m.b310*m.b886 - 2*m.b310*m.b1165 + 2*m.b311*
                       m.b957 + 2*m.b311*m.b1106 + 2*m.b311*m.b1121 - 2*m.b312*m.b798 - 2*m.b312*m.b1071 - 2*m.b312*
                       m.b1180 + 2*m.b313*m.b315 - 2*m.b315 - 2*m.b313*m.b858 + 2*m.b314*m.b317 - 4*m.b317 - 2*m.b314*
                       m.b988 + 2*m.b315*m.b317 - 2*m.b315*m.b1098 + 2*m.b315*m.b1180 + 2*m.b316*m.b318 - 2*m.b318 - 2*
                       m.b316*m.b1035 - 2*m.b316*m.b1087 + 2*m.b317*m.b318 + 2*m.b317*m.b754 - 2*m.b318*m.b903 + 2*
                       m.b318*m.b1036 + 2*m.b319*m.b527 + 2*m.b527 + 2*m.b319*m.b800 + 2*m.b319*m.b989 + 2*m.b320*m.b920
                        - 2*m.b320 + 2*m.b320*m.b991 + 2*m.b320*m.b1006 - 2*m.b320*m.b1046 + 2*m.b321*m.b322 - 2*m.b321*
                       m.b731 + 2*m.b322*m.b534 - 2*m.b534 - 2*m.b322*m.b703 + 2*m.b703 + 2*m.b323*m.b534 - 2*m.b323 - 2
                       *m.b323*m.b706 + 2*m.b706 + 2*m.b323*m.b938 + 2*m.b323*m.b1138 + 2*m.b324*m.b325 - 2*m.b324*
                       m.b440 - 2*m.b440 + 2*m.b324*m.b492 - 2*m.b492 + 2*m.b325*m.b327 - 2*m.b327 + 2*m.b325*m.b938 - 2
                       *m.b326*m.b446 - 2*m.b326 + 2*m.b446 + 2*m.b326*m.b492 + 2*m.b326*m.b832 + 2*m.b326*m.b892 + 2*
                       m.b327*m.b446 + 2*m.b327*m.b647 - 2*m.b647 - 2*m.b327*m.b1077 + 2*m.b328*m.b329 + 2*m.b328 - 2*
                       m.b328*m.b865 - 2*m.b328*m.b1007 - 2*m.b328*m.b1184 - 2*m.b329*m.b834 + 2*m.b329*m.b1185 + 2*
                       m.b330*m.b331 - 2*m.b331 + 2*m.b331*m.b409 + 2*m.b331*m.b548 - 4*m.b548 - 2*m.b331*m.b1186 + 2*
                       m.b332*m.b333 - 4*m.b333 + 2*m.b332*m.b898 + 2*m.b333*m.b411 + 2*m.b411 + 2*m.b333*m.b548 + 2*
                       m.b333*m.b1153 - 2*m.b334*m.b335 + 2*m.b334 + 2*m.b334*m.b410 - 4*m.b410 - 2*m.b334*m.b551 - 2*
                       m.b334*m.b954 + 2*m.b335*m.b507 - 4*m.b507 + 2*m.b335*m.b1153 + 2*m.b336*m.b337 + 2*m.b336*m.b412
                        - 2*m.b412 + 2*m.b336*m.b1092 + 2*m.b337*m.b507 + 2*m.b337*m.b556 - 4*m.b556 + 2*m.b338*m.b339
                        - 2*m.b339 + 2*m.b339*m.b556 - 2*m.b340*m.b342 + 2*m.b340 - 2*m.b342 - 2*m.b340*m.b820 + 2*
                       m.b341*m.b342 - 2*m.b341 + 2*m.b341*m.b768 + 2*m.b342*m.b344 - 4*m.b344 + 2*m.b342*m.b983 - 2*
                       m.b343*m.b613 + 2*m.b343 - 2*m.b343*m.b866 - 2*m.b343*m.b867 + 2*m.b343*m.b1080 + 2*m.b344*m.b613
                        + 2*m.b344*m.b780 + 2*m.b344*m.b943 + 2*m.b345*m.b346 + 2*m.b345 - 2*m.b346 - 2*m.b345*m.b998 - 
                       2*m.b345*m.b999 - 2*m.b345*m.b1187 + 2*m.b346*m.b347 - 2*m.b346*m.b742 + 2*m.b346*m.b837 + 2*
                       m.b347*m.b678 - 2*m.b678 + 2*m.b347*m.b1082 - 2*m.b348*m.b901 - 2*m.b348*m.b1156 - 2*m.b348*
                       m.b1158 + 2*m.b349*m.b425 + 2*m.b349 - 4*m.b425 - 2*m.b349*m.b824 - 2*m.b349*m.b932 - 2*m.b349*
                       m.b1121 + 2*m.b350*m.b518 - 4*m.b518 + 2*m.b350*m.b624 - 4*m.b624 + 2*m.b350*m.b902 + 2*m.b351*
                       m.b945 + 2*m.b351*m.b1114 + 2*m.b351*m.b1133 - 2*m.b352*m.b813 + 4*m.b352 - 2*m.b352*m.b814 - 2*
                       m.b352*m.b1056 - 2*m.b352*m.b1188 + 2*m.b353*m.b356 - 4*m.b356 - 2*m.b353*m.b972 + 2*m.b354*
                       m.b356 - 2*m.b354 - 2*m.b354*m.b1086 + 2*m.b354*m.b1172 + 2*m.b354*m.b1188 + 2*m.b355*m.b357 - 2*
                       m.b357 - 2*m.b355*m.b1043 - 2*m.b355*m.b1073 + 2*m.b356*m.b357 + 2*m.b356*m.b760 - 2*m.b357*
                       m.b887 + 2*m.b357*m.b1026 + 2*m.b358*m.b481 + 2*m.b481 + 2*m.b358*m.b815 + 2*m.b358*m.b1003 + 2*
                       m.b359*m.b360 + 2*m.b359*m.b975 - 2*m.b359*m.b1060 + 2*m.b360*m.b703 - 2*m.b360*m.b1191 + 2*
                       m.b361*m.b362 - 2*m.b362 - 2*m.b361*m.b802 + 2*m.b362*m.b924 - 2*m.b362*m.b1047 + 2*m.b362*
                       m.b1192 - 2*m.b363*m.b757 - 2*m.b363*m.b848 - 2*m.b363*m.b1176 - 2*m.b364*m.b403 + 2*m.b403 + 2*
                       m.b364*m.b818 + 2*m.b364*m.b979 + 2*m.b365*m.b403 - 2*m.b365 + 2*m.b365*m.b709 - 2*m.b709 - 2*
                       m.b365*m.b1090 + 2*m.b365*m.b1176 - 2*m.b366*m.b367 + 2*m.b366 + 2*m.b367 - 2*m.b366*m.b712 + 2*
                       m.b712 - 2*m.b366*m.b775 + 2*m.b366*m.b849 + 2*m.b367*m.b368 - 2*m.b367*m.b1019 - 2*m.b367*
                       m.b1194 - 2*m.b368*m.b819 + 2*m.b368*m.b1195 + 2*m.b369*m.b370 - 2*m.b370 + 2*m.b370*m.b453 + 2*
                       m.b370*m.b601 - 4*m.b601 - 2*m.b370*m.b1196 + 2*m.b371*m.b372 - 4*m.b372 + 2*m.b371*m.b880 + 2*
                       m.b372*m.b373 + 2*m.b373 + 2*m.b372*m.b601 + 2*m.b372*m.b1143 - 2*m.b373*m.b374 - 2*m.b373*m.b747
                        - 2*m.b373*m.b942 + 2*m.b374*m.b553 - 4*m.b553 + 2*m.b374*m.b1143 + 2*m.b375*m.b376 + 2*m.b375*
                       m.b455 - 2*m.b455 + 2*m.b375*m.b1104 + 2*m.b376*m.b553 + 2*m.b376*m.b608 - 4*m.b608 + 2*m.b377*
                       m.b378 - 2*m.b378 + 2*m.b378*m.b608 - 2*m.b379*m.b380 + 2*m.b379 - 2*m.b380 - 2*m.b379*m.b835 + 2
                       *m.b380*m.b381 + 2*m.b380*m.b671 + 2*m.b380*m.b1178 + 2*m.b381*m.b562 + 2*m.b381*m.b793 + 2*
                       m.b382*m.b383 + 2*m.b382 - 4*m.b383 - 2*m.b382*m.b743 - 2*m.b382*m.b984 - 2*m.b382*m.b1197 + 2*
                       m.b383*m.b384 - 2*m.b384 + 2*m.b383*m.b748 + 2*m.b383*m.b853 - 2*m.b384*m.b854 + 2*m.b384*m.b1054
                        + 2*m.b384*m.b1094 + 2*m.b385*m.b742 - 2*m.b385*m.b1132 + 2*m.b386*m.b681 - 4*m.b681 - 2*m.b386*
                       m.b1147 - 2*m.b386*m.b1149 + 2*m.b387*m.b472 + 2*m.b387 - 4*m.b472 - 2*m.b387*m.b810 - 2*m.b387*
                       m.b944 - 2*m.b387*m.b1114 + 2*m.b388*m.b570 + 2*m.b388*m.b685 - 4*m.b685 + 2*m.b388*m.b1165 + 2*
                       m.b389*m.b520 - 2*m.b520 + 2*m.b389*m.b1121 + 2*m.b389*m.b1148 - 2*m.b390*m.b826 - 2*m.b390*
                       m.b1042 - 2*m.b390*m.b1198 + 2*m.b391*m.b393 - 4*m.b393 - 2*m.b391*m.b987 + 2*m.b391*m.b988 + 2*
                       m.b392*m.b393 - 2*m.b392 - 2*m.b392*m.b1072 + 2*m.b392*m.b1180 + 2*m.b392*m.b1198 + 2*m.b393*
                       m.b394 - 2*m.b394 + 2*m.b393*m.b769 - 2*m.b394*m.b872 + 2*m.b394*m.b1015 + 2*m.b394*m.b1057 + 2*
                       m.b395*m.b435 + 2*m.b435 + 2*m.b395*m.b828 + 2*m.b395*m.b1017 + 2*m.b396*m.b397 + 2*m.b396*m.b961
                        - 2*m.b396*m.b1076 + 2*m.b397*m.b641 - 2*m.b397*m.b1201 + 2*m.b398*m.b399 - 2*m.b399 - 2*m.b398*
                       m.b817 + 2*m.b398*m.b1139 + 2*m.b399*m.b908 - 2*m.b399*m.b1061 + 2*m.b399*m.b1202 - 2*m.b400*
                       m.b765 + 2*m.b400*m.b1125 - 2*m.b400*m.b1169 + 2*m.b401*m.b803 + 2*m.b401*m.b1047 - 2*m.b401*
                       m.b1101 + 2*m.b402*m.b805 + 2*m.b402*m.b964 - 2*m.b402*m.b965 - 2*m.b403*m.b652 - 2*m.b403*
                       m.b1194 - 2*m.b404*m.b650 + 2*m.b404 + 2*m.b650 - 2*m.b404*m.b789 + 2*m.b404*m.b834 - 2*m.b404*
                       m.b1038 + 2*m.b405*m.b656 - 2*m.b656 + 2*m.b405*m.b819 + 2*m.b405*m.b1038 + 2*m.b406*m.b408 - 4*
                       m.b408 + 2*m.b407*m.b408 - 4*m.b407 + 2*m.b407*m.b656 + 2*m.b407*m.b659 + 2*m.b407*m.b896 + 2*
                       m.b408*m.b503 + 2*m.b408*m.b661 - 4*m.b661 + 2*m.b409*m.b410 + 2*m.b410*m.b661 + 2*m.b410*m.b1128
                        - 2*m.b411*m.b412 - 2*m.b411*m.b751 - 2*m.b411*m.b929 + 2*m.b412*m.b605 - 4*m.b605 + 2*m.b412*
                       m.b1128 + 2*m.b413*m.b506 - 2*m.b506 + 2*m.b413*m.b728 - 2*m.b414*m.b554 + 2*m.b414*m.b1204 - 2*
                       m.b415*m.b416 + 2*m.b415 - 2*m.b416 - 2*m.b415*m.b850 + 2*m.b416*m.b418 + 2*m.b416*m.b611 + 2*
                       m.b416*m.b1171 - 2*m.b417*m.b512 + 2*m.b417 + 2*m.b417*m.b610 - 4*m.b610 - 2*m.b417*m.b899 - 2*
                       m.b417*m.b1093 + 2*m.b418*m.b512 + 2*m.b418*m.b807 + 2*m.b419*m.b421 - 2*m.b421 - 2*m.b419*m.b837
                        + 2*m.b419*m.b1105 + 2*m.b420*m.b421 - 4*m.b420 + 2*m.b420*m.b752 + 2*m.b420*m.b869 + 2*m.b420*
                       m.b1000 + 2*m.b421*m.b422 - 2*m.b422 - 2*m.b421*m.b838 + 2*m.b422*m.b423 - 2*m.b423 - 2*m.b422*
                       m.b885 + 2*m.b422*m.b1053 + 2*m.b423*m.b986 - 2*m.b423*m.b1120 + 2*m.b423*m.b1146 + 2*m.b424*
                       m.b517 + 2*m.b424 - 4*m.b517 - 2*m.b424*m.b796 - 2*m.b424*m.b956 - 2*m.b424*m.b1106 + 2*m.b425*
                       m.b427 - 2*m.b427 + 2*m.b425*m.b624 + 2*m.b425*m.b1158 + 2*m.b426*m.b475 - 2*m.b475 + 2*m.b426*
                       m.b1133 + 2*m.b426*m.b1157 + 2*m.b427*m.b475 + 2*m.b427*m.b517 - 2*m.b427*m.b826 + 2*m.b428*
                       m.b687 - 4*m.b687 - 2*m.b428*m.b1207 + 2*m.b429*m.b430 + 2*m.b429*m.b431 - 2*m.b431 + 2*m.b429*
                       m.b630 + 2*m.b430*m.b432 - 4*m.b432 + 2*m.b431*m.b432 - 2*m.b431*m.b634 + 2*m.b431*m.b859 + 2*
                       m.b432*m.b433 - 4*m.b433 + 2*m.b432*m.b761 + 2*m.b433*m.b434 + 2*m.b433*m.b934 + 2*m.b433*m.b946
                        + 2*m.b434*m.b845 + 2*m.b434*m.b1109 - 2*m.b435*m.b585 - 2*m.b435*m.b905 - 2*m.b435*m.b1201 + 2*
                       m.b436*m.b437 - 2*m.b436*m.b528 + 2*m.b528 + 2*m.b436*m.b951 + 2*m.b437*m.b588 + 2*m.b437*m.b1201
                        - 2*m.b438*m.b906 - 2*m.b438*m.b1210 + 2*m.b439*m.b440 - 2*m.b439*m.b830 + 2*m.b439*m.b1125 + 2*
                       m.b440*m.b442 - 2*m.b442 + 2*m.b440*m.b1210 - 2*m.b441*m.b774 + 2*m.b441*m.b1139 - 2*m.b441*
                       m.b1159 - 2*m.b442*m.b787 + 2*m.b442*m.b891 + 2*m.b442*m.b1159 - 2*m.b443*m.b445 - 2*m.b445 + 2*
                       m.b443*m.b786 + 2*m.b443*m.b1061 + 2*m.b444*m.b646 - 2*m.b444 + 2*m.b646 + 2*m.b444*m.b789 + 2*
                       m.b444*m.b848 - 2*m.b444*m.b952 + 2*m.b445*m.b952 + 2*m.b445*m.b1090 + 2*m.b445*m.b1159 - 2*
                       m.b446*m.b595 - 2*m.b446*m.b1184 - 2*m.b447*m.b448 + 2*m.b447 - 2*m.b448 - 2*m.b447*m.b805 + 2*
                       m.b447*m.b819 - 2*m.b447*m.b1028 + 2*m.b448*m.b450 + 2*m.b448*m.b1029 + 2*m.b448*m.b1184 - 2*
                       m.b449*m.b718 - 2*m.b718 - 2*m.b449*m.b893 - 2*m.b449*m.b896 + 2*m.b450*m.b718 + 2*m.b450*m.b834
                        + 2*m.b451*m.b452 - 4*m.b452 + 2*m.b452*m.b548 + 2*m.b452*m.b723 - 4*m.b723 + 2*m.b452*m.b1196
                        + 2*m.b453*m.b454 + 2*m.b454*m.b723 + 2*m.b454*m.b1118 + 2*m.b455*m.b667 - 2*m.b667 - 2*m.b455*
                       m.b914 + 2*m.b455*m.b1118 + 2*m.b456*m.b552 - 2*m.b552 + 2*m.b456*m.b668 + 2*m.b457*m.b1212 - 2*
                       m.b458*m.b459 + 2*m.b458 - 2*m.b459 - 2*m.b458*m.b866 + 2*m.b459*m.b461 + 2*m.b459*m.b560 + 2*
                       m.b459*m.b1162 + 2*m.b460*m.b559 + 2*m.b460 - 2*m.b559 - 2*m.b460*m.b916 - 2*m.b460*m.b1080 - 2*
                       m.b460*m.b1081 + 2*m.b461*m.b820 + 2*m.b461*m.b1081 + 2*m.b462*m.b463 + 2*m.b462*m.b672 - 4*
                       m.b672 + 2*m.b463*m.b464 - 2*m.b464 + 2*m.b463*m.b1081 + 2*m.b464*m.b466 - 4*m.b466 - 2*m.b464*
                       m.b955 + 2*m.b464*m.b1012 + 2*m.b465*m.b467 - 2*m.b465 - 2*m.b467 - 2*m.b465*m.b822 + 2*m.b465*
                       m.b1095 + 2*m.b465*m.b1112 + 2*m.b466*m.b467 + 2*m.b466*m.b759 + 2*m.b466*m.b883 + 2*m.b467*
                       m.b468 - 2*m.b468 - 2*m.b467*m.b823 + 2*m.b468*m.b470 - 2*m.b470 - 2*m.b468*m.b870 + 2*m.b468*
                       m.b1070 + 2*m.b469*m.b796 - 2*m.b469*m.b970 + 2*m.b470*m.b970 - 2*m.b470*m.b1113 + 2*m.b470*
                       m.b1155 + 2*m.b471*m.b569 + 2*m.b471 - 4*m.b569 - 2*m.b471*m.b783 - 2*m.b471*m.b970 - 2*m.b471*
                       m.b1097 + 2*m.b472*m.b474 - 2*m.b474 + 2*m.b472*m.b685 + 2*m.b472*m.b1149 + 2*m.b473*m.b476 - 4*
                       m.b476 + 2*m.b473*m.b1148 + 2*m.b474*m.b476 + 2*m.b474*m.b569 - 2*m.b474*m.b813 + 2*m.b475*m.b688
                        - 2*m.b475*m.b1208 + 2*m.b476*m.b627 + 2*m.b476*m.b1208 - 2*m.b477*m.b574 - 2*m.b574 + 2*m.b477*
                       m.b626 - 4*m.b626 + 2*m.b478*m.b479 - 2*m.b478 - 2*m.b479 + 2*m.b478*m.b691 - 2*m.b478*m.b988 + 2
                       *m.b478*m.b1108 - 2*m.b479*m.b580 + 2*m.b479*m.b844 + 2*m.b479*m.b1200 - 2*m.b480*m.b579 + 2*
                       m.b480 - 2*m.b579 + 2*m.b480*m.b697 - 2*m.b697 - 2*m.b480*m.b919 - 2*m.b480*m.b1003 - 2*m.b481*
                       m.b638 - 2*m.b481*m.b922 - 2*m.b481*m.b1191 - 2*m.b482*m.b483 + 2*m.b482 - 2*m.b482*m.b874 + 2*
                       m.b482*m.b1191 - 2*m.b482*m.b1214 + 2*m.b483*m.b484 + 2*m.b483*m.b937 + 2*m.b484*m.b532 + 2*
                       m.b484*m.b1191 - 2*m.b485*m.b487 + 2*m.b487 - 2*m.b485*m.b923 + 2*m.b486*m.b489 - 4*m.b489 - 2*
                       m.b486*m.b846 + 2*m.b487*m.b489 - 2*m.b487*m.b804 - 2*m.b487*m.b1215 - 2*m.b488*m.b491 - 2*m.b491
                        - 2*m.b488*m.b801 - 2*m.b488*m.b803 + 2*m.b489*m.b491 + 2*m.b489*m.b1061 - 2*m.b490*m.b493 - 2*
                       m.b493 - 2*m.b490*m.b788 - 2*m.b490*m.b892 + 2*m.b491*m.b493 + 2*m.b491*m.b876 - 2*m.b492*m.b495
                        - 2*m.b495 + 2*m.b492*m.b772 + 2*m.b493*m.b495 + 2*m.b493*m.b1151 + 2*m.b494*m.b708 - 2*m.b494
                        + 2*m.b708 + 2*m.b494*m.b775 + 2*m.b494*m.b863 - 2*m.b494*m.b939 + 2*m.b495*m.b939 + 2*m.b495*
                       m.b1077 - 2*m.b496*m.b541 + 4*m.b541 + 2*m.b496*m.b1126 - 2*m.b496*m.b1177 - 2*m.b497*m.b498 + 4*
                       m.b497 - 2*m.b498 - 2*m.b497*m.b540 - 2*m.b497*m.b818 - 2*m.b497*m.b819 + 2*m.b498*m.b500 + 2*
                       m.b498*m.b1019 + 2*m.b498*m.b1177 - 2*m.b499*m.b910 - 2*m.b499*m.b912 - 2*m.b499*m.b1142 + 2*
                       m.b500*m.b849 + 2*m.b500*m.b1142 + 2*m.b501*m.b502 - 4*m.b502 - 2*m.b501*m.b1102 + 2*m.b502*
                       m.b504 - 2*m.b504 + 2*m.b502*m.b601 + 2*m.b502*m.b1186 + 2*m.b503*m.b505 + 2*m.b504*m.b505 + 2*
                       m.b504*m.b660 - 4*m.b660 - 2*m.b504*m.b735 + 2*m.b505*m.b1111 + 2*m.b506*m.b727 - 2*m.b727 - 2*
                       m.b506*m.b897 + 2*m.b506*m.b1111 + 2*m.b507*m.b604 - 4*m.b604 + 2*m.b507*m.b606 + 2*m.b508*
                       m.b1216 + 2*m.b509*m.b510 - 2*m.b509 + 2*m.b509*m.b511 + 2*m.b509*m.b1154 - 2*m.b509*m.b1218 - 2*
                       m.b510*m.b930 - 2*m.b510*m.b1067 + 2*m.b511*m.b835 + 2*m.b511*m.b1067 - 2*m.b512*m.b1206 + 2*
                       m.b513*m.b514 - 2*m.b513 - 2*m.b514 - 2*m.b513*m.b809 + 2*m.b513*m.b969 + 2*m.b513*m.b1083 + 2*
                       m.b514*m.b515 - 2*m.b515 + 2*m.b514*m.b823 - 2*m.b514*m.b1219 + 2*m.b515*m.b516 - 4*m.b516 - 2*
                       m.b515*m.b857 + 2*m.b515*m.b1084 + 2*m.b516*m.b956 + 2*m.b516*m.b1113 + 2*m.b516*m.b1163 + 2*
                       m.b517*m.b519 - 2*m.b519 + 2*m.b517*m.b1134 + 2*m.b518*m.b521 - 4*m.b521 + 2*m.b518*m.b971 + 2*
                       m.b518*m.b1157 + 2*m.b519*m.b521 + 2*m.b519*m.b622 - 4*m.b622 - 2*m.b519*m.b798 + 2*m.b520*m.b685
                        + 2*m.b520*m.b933 - 2*m.b520*m.b1199 + 2*m.b521*m.b573 + 2*m.b521*m.b1199 + 2*m.b522*m.b572 - 4*
                       m.b572 - 2*m.b522*m.b628 - 2*m.b628 + 2*m.b523*m.b524 - 2*m.b524 + 2*m.b523*m.b770 + 2*m.b523*
                       m.b1100 - 2*m.b524*m.b525 + 2*m.b525 + 2*m.b524*m.b827 + 2*m.b524*m.b1190 + 2*m.b525*m.b635 - 2*
                       m.b635 - 2*m.b525*m.b903 - 2*m.b525*m.b989 - 2*m.b526*m.b528 + 2*m.b526 + 2*m.b526*m.b698 - 4*
                       m.b698 - 2*m.b526*m.b860 - 2*m.b526*m.b1089 - 2*m.b527*m.b700 - 2*m.b527*m.b935 - 2*m.b527*
                       m.b1183 + 2*m.b528*m.b1183 - 2*m.b528*m.b1221 + 2*m.b529*m.b531 - 2*m.b529*m.b1109 + 2*m.b530*
                       m.b732 - 2*m.b530 + 2*m.b530*m.b950 + 2*m.b530*m.b1004 - 2*m.b530*m.b1150 + 2*m.b531*m.b1150 + 2*
                       m.b531*m.b1183 - 2*m.b532*m.b962 - 2*m.b532*m.b1215 - 2*m.b533*m.b936 - 2*m.b533*m.b993 + 2*
                       m.b534*m.b535 - 4*m.b535 - 2*m.b534*m.b861 + 2*m.b535*m.b537 - 2*m.b537 + 2*m.b535*m.b993 + 2*
                       m.b535*m.b1047 - 2*m.b536*m.b538 + 4*m.b536 - 2*m.b538 - 2*m.b536*m.b804 - 2*m.b536*m.b909 - 2*
                       m.b536*m.b1139 + 2*m.b537*m.b538 - 2*m.b537*m.b862 + 2*m.b537*m.b863 + 2*m.b538*m.b539 - 2*m.b539
                        + 2*m.b538*m.b1140 + 2*m.b539*m.b926 - 2*m.b539*m.b979 + 2*m.b539*m.b1062 + 2*m.b540*m.b1140 - 2
                       *m.b540*m.b1170 - 2*m.b541*m.b542 - 2*m.b542 - 2*m.b541*m.b832 - 2*m.b541*m.b834 + 2*m.b542*
                       m.b544 + 2*m.b542*m.b1007 + 2*m.b542*m.b1170 - 2*m.b543*m.b739 - 2*m.b543*m.b927 - 2*m.b543*
                       m.b1127 + 2*m.b544*m.b864 + 2*m.b544*m.b1127 + 2*m.b545*m.b547 - 4*m.b547 - 2*m.b545*m.b1110 + 2*
                       m.b546*m.b547 + 2*m.b546*m.b1127 + 2*m.b546*m.b1185 + 2*m.b547*m.b549 - 4*m.b549 + 2*m.b547*
                       m.b661 + 2*m.b548*m.b550 + 2*m.b549*m.b550 + 2*m.b549*m.b722 - 4*m.b722 + 2*m.b549*m.b735 + 2*
                       m.b550*m.b1103 - 2*m.b551*m.b740 - 2*m.b551*m.b792 + 2*m.b552*m.b792 - 2*m.b552*m.b879 + 2*m.b552
                       *m.b1103 + 2*m.b553*m.b555 + 2*m.b553*m.b666 - 4*m.b666 + 2*m.b554*m.b557 + 2*m.b554*m.b740 + 2*
                       m.b555*m.b557 + 2*m.b555*m.b792 + 2*m.b556*m.b558 - 2*m.b558 + 2*m.b556*m.b778 + 2*m.b557*m.b558
                        + 2*m.b559*m.b561 + 2*m.b559*m.b1144 - 2*m.b559*m.b1222 - 2*m.b560*m.b943 - 2*m.b560*m.b1051 + 2
                       *m.b561*m.b850 + 2*m.b561*m.b1051 - 2*m.b562*m.b882 - 2*m.b562*m.b1197 + 2*m.b563*m.b564 - 2*
                       m.b564 - 2*m.b563*m.b795 + 2*m.b563*m.b1069 + 2*m.b564*m.b566 - 2*m.b566 + 2*m.b564*m.b838 - 2*
                       m.b564*m.b1223 + 2*m.b565*m.b567 - 4*m.b567 - 2*m.b565*m.b1096 + 2*m.b565*m.b1164 + 2*m.b566*
                       m.b567 - 2*m.b566*m.b841 + 2*m.b566*m.b1096 + 2*m.b567*m.b944 + 2*m.b567*m.b1120 + 2*m.b568*
                       m.b683 - 2*m.b568 - 4*m.b683 + 2*m.b568*m.b944 - 2*m.b568*m.b1106 + 2*m.b568*m.b1113 + 2*m.b569*
                       m.b571 + 2*m.b569*m.b1122 + 2*m.b570*m.b572 + 2*m.b570*m.b957 + 2*m.b571*m.b572 + 2*m.b571*m.b683
                        + 2*m.b572*m.b1189 - 2*m.b573*m.b689 - 2*m.b689 + 2*m.b574*m.b575 + 2*m.b574*m.b1043 + 2*m.b574*
                       m.b1208 + 2*m.b575*m.b689 + 2*m.b575*m.b1220 + 2*m.b576*m.b578 + 2*m.b576*m.b843 + 2*m.b576*
                       m.b1107 + 2*m.b577*m.b579 + 2*m.b577*m.b988 + 2*m.b577*m.b1088 + 2*m.b578*m.b579 + 2*m.b578*
                       m.b1220 + 2*m.b579*m.b1182 + 2*m.b580*m.b581 - 4*m.b581 - 2*m.b580*m.b887 + 2*m.b581*m.b583 - 4*
                       m.b583 + 2*m.b581*m.b637 + 2*m.b637 + 2*m.b581*m.b1182 + 2*m.b582*m.b636 + 2*m.b582 - 4*m.b636 - 
                       2*m.b582*m.b873 - 2*m.b582*m.b1075 - 2*m.b582*m.b1076 + 2*m.b583*m.b761 + 2*m.b583*m.b860 + 2*
                       m.b583*m.b1076 - 2*m.b584*m.b732 - 2*m.b584*m.b948 - 2*m.b584*m.b1175 + 2*m.b585*m.b587 + 2*
                       m.b585*m.b907 + 2*m.b586*m.b700 - 2*m.b586 + 2*m.b586*m.b936 + 2*m.b586*m.b990 - 2*m.b586*m.b1137
                        + 2*m.b587*m.b1137 + 2*m.b587*m.b1175 - 2*m.b588*m.b976 - 2*m.b588*m.b1211 + 2*m.b589*m.b591 - 4
                       *m.b589 - 2*m.b591 + 2*m.b589*m.b706 + 2*m.b589*m.b978 + 2*m.b589*m.b1192 - 2*m.b590*m.b592 + 2*
                       m.b590 - 2*m.b592 + 2*m.b590*m.b705 - 4*m.b705 - 2*m.b590*m.b925 - 2*m.b590*m.b1125 + 2*m.b591*
                       m.b592 - 2*m.b591*m.b847 + 2*m.b591*m.b848 + 2*m.b592*m.b593 - 2*m.b593 + 2*m.b592*m.b1126 + 2*
                       m.b593*m.b594 - 2*m.b594 + 2*m.b593*m.b712 - 2*m.b593*m.b964 - 2*m.b594*m.b790 + 2*m.b594*m.b911
                        + 2*m.b594*m.b1160 - 2*m.b595*m.b596 - 2*m.b596 - 2*m.b595*m.b849 + 2*m.b596*m.b598 + 2*m.b596*
                       m.b994 + 2*m.b596*m.b1160 - 2*m.b597*m.b734 - 2*m.b597*m.b1117 + 2*m.b598*m.b877 + 2*m.b598*
                       m.b1117 + 2*m.b599*m.b721 - 2*m.b721 - 2*m.b599*m.b1117 + 2*m.b600*m.b721 + 2*m.b600*m.b1117 + 2*
                       m.b600*m.b1195 + 2*m.b601*m.b602 - 2*m.b602 + 2*m.b602*m.b766 + 2*m.b602*m.b1091 - 2*m.b602*
                       m.b1224 - 2*m.b603*m.b746 + 2*m.b603*m.b777 - 2*m.b603*m.b779 + 2*m.b604*m.b779 + 2*m.b604*m.b879
                        + 2*m.b604*m.b1091 + 2*m.b605*m.b607 + 2*m.b605*m.b726 - 4*m.b726 + 2*m.b605*m.b728 + 2*m.b606*
                       m.b727 - 2*m.b606*m.b1217 + 2*m.b607*m.b779 + 2*m.b607*m.b1217 + 2*m.b608*m.b609 - 2*m.b609 + 2*
                       m.b608*m.b791 + 2*m.b609*m.b1217 + 2*m.b610*m.b612 + 2*m.b610*m.b1129 + 2*m.b610*m.b1222 - 2*
                       m.b611*m.b1039 + 2*m.b612*m.b866 + 2*m.b612*m.b1039 - 2*m.b613*m.b1187 + 2*m.b614*m.b968 - 2*
                       m.b614 + 2*m.b614*m.b1032 + 2*m.b614*m.b1197 - 2*m.b614*m.b1223 + 2*m.b615*m.b984 - 4*m.b615 + 2*
                       m.b615*m.b1040 + 2*m.b615*m.b1187 + 2*m.b615*m.b1223 + 2*m.b616*m.b617 - 4*m.b617 - 2*m.b616*
                       m.b782 + 2*m.b616*m.b1052 + 2*m.b617*m.b619 - 2*m.b619 + 2*m.b617*m.b854 + 2*m.b617*m.b1223 + 2*
                       m.b618*m.b620 - 4*m.b620 - 2*m.b618*m.b1084 + 2*m.b618*m.b1156 + 2*m.b619*m.b620 - 2*m.b619*
                       m.b825 + 2*m.b619*m.b1105 + 2*m.b620*m.b932 + 2*m.b620*m.b1131 + 2*m.b621*m.b623 - 2*m.b621 - 2*
                       m.b623 + 2*m.b621*m.b932 - 2*m.b621*m.b1097 + 2*m.b621*m.b1120 + 2*m.b622*m.b625 + 2*m.b622*
                       m.b985 + 2*m.b622*m.b1115 + 2*m.b623*m.b625 - 2*m.b623*m.b753 + 2*m.b623*m.b1013 + 2*m.b624*
                       m.b626 + 2*m.b624*m.b945 + 2*m.b625*m.b626 + 2*m.b626*m.b1181 - 2*m.b627*m.b987 + 2*m.b628*m.b629
                        + 2*m.b628*m.b1035 + 2*m.b628*m.b1199 + 2*m.b629*m.b987 + 2*m.b629*m.b1213 + 2*m.b630*m.b632 - 2
                       *m.b632 + 2*m.b631*m.b633 - 2*m.b633 + 2*m.b631*m.b1074 + 2*m.b632*m.b633 - 2*m.b632*m.b799 + 2*
                       m.b632*m.b1213 - 2*m.b633*m.b946 + 2*m.b633*m.b1174 + 2*m.b634*m.b636 - 2*m.b634*m.b872 + 2*
                       m.b635*m.b699 + 2*m.b699 + 2*m.b635*m.b1190 - 2*m.b635*m.b1221 + 2*m.b636*m.b1174 + 2*m.b636*
                       m.b1221 - 2*m.b637*m.b888 - 2*m.b637*m.b1059 - 2*m.b637*m.b1060 + 2*m.b638*m.b639 - 2*m.b639 + 2*
                       m.b638*m.b640 + 2*m.b639*m.b923 + 2*m.b639*m.b974 - 2*m.b639*m.b1123 + 2*m.b640*m.b1123 + 2*
                       m.b640*m.b1168 - 2*m.b641*m.b992 - 2*m.b641*m.b1203 + 2*m.b642*m.b801 + 2*m.b642*m.b906 - 2*
                       m.b642*m.b963 + 2*m.b643*m.b644 - 4*m.b643 + 2*m.b643*m.b645 + 2*m.b643*m.b963 + 2*m.b643*m.b1202
                        - 2*m.b644*m.b647 - 2*m.b644*m.b708 + 2*m.b645*m.b647 + 2*m.b645*m.b847 - 2*m.b646*m.b649 - 2*
                       m.b649 - 2*m.b646*m.b706 - 2*m.b646*m.b755 + 2*m.b647*m.b649 - 2*m.b648*m.b651 + 2*m.b648 - 2*
                       m.b651 - 2*m.b648*m.b805 - 2*m.b648*m.b891 + 2*m.b648*m.b892 + 2*m.b649*m.b650 + 2*m.b649*m.b651
                        - 2*m.b650*m.b1151 - 2*m.b650*m.b1152 + 2*m.b651*m.b894 + 2*m.b651*m.b1152 - 2*m.b652*m.b653 - 2
                       *m.b653 - 2*m.b652*m.b864 + 2*m.b653*m.b655 + 2*m.b653*m.b980 + 2*m.b653*m.b1152 - 2*m.b654*
                       m.b1110 + 2*m.b655*m.b893 + 2*m.b655*m.b1110 + 2*m.b656*m.b658 - 2*m.b656*m.b913 + 2*m.b657*
                       m.b660 - 2*m.b657*m.b1127 + 2*m.b658*m.b660 + 2*m.b658*m.b1110 + 2*m.b659*m.b662 + 2*m.b660*
                       m.b662 + 2*m.b661*m.b663 - 4*m.b663 + 2*m.b662*m.b663 + 2*m.b663*m.b664 - 2*m.b664 + 2*m.b663*
                       m.b777 + 2*m.b664*m.b666 - 2*m.b664*m.b981 + 2*m.b664*m.b1078 + 2*m.b665*m.b766 - 2*m.b665*m.b767
                        + 2*m.b666*m.b767 + 2*m.b666*m.b897 + 2*m.b667*m.b668 + 2*m.b667*m.b669 - 2*m.b667*m.b751 - 2*
                       m.b668*m.b730 + 2*m.b730 + 2*m.b669*m.b730 + 2*m.b669*m.b767 + 2*m.b670*m.b672 - 4*m.b670 + 2*
                       m.b670*m.b882 + 2*m.b670*m.b1119 + 2*m.b670*m.b1218 - 2*m.b671*m.b1031 + 2*m.b672*m.b768 + 2*
                       m.b672*m.b1031 - 2*m.b673*m.b1179 + 2*m.b674*m.b955 - 2*m.b674 + 2*m.b674*m.b1022 + 2*m.b674*
                       m.b1206 - 2*m.b674*m.b1219 + 2*m.b675*m.b998 + 2*m.b675*m.b1179 + 2*m.b675*m.b1219 + 2*m.b676*
                       m.b677 + 2*m.b676*m.b782 + 2*m.b676*m.b1041 + 2*m.b677*m.b679 - 2*m.b679 + 2*m.b677*m.b1219 + 2*
                       m.b678*m.b681 - 2*m.b678*m.b1070 + 2*m.b678*m.b1147 + 2*m.b679*m.b681 - 2*m.b679*m.b812 + 2*
                       m.b679*m.b1112 - 2*m.b680*m.b823 + 2*m.b680 - 2*m.b680*m.b824 + 2*m.b680*m.b917 - 2*m.b680*m.b918
                        + 2*m.b681*m.b918 + 2*m.b682*m.b684 - 2*m.b682 - 2*m.b684 + 2*m.b682*m.b918 - 2*m.b682*m.b1085
                        + 2*m.b682*m.b1131 + 2*m.b683*m.b686 + 2*m.b683*m.b1001 + 2*m.b684*m.b686 - 2*m.b684*m.b749 + 2*
                       m.b684*m.b1024 + 2*m.b685*m.b687 + 2*m.b686*m.b687 + 2*m.b687*m.b1173 - 2*m.b688*m.b971 - 2*
                       m.b688*m.b972 + 2*m.b689*m.b690 + 2*m.b689*m.b1189 + 2*m.b690*m.b972 + 2*m.b690*m.b1209 + 2*
                       m.b691*m.b693 - 4*m.b693 + 2*m.b692*m.b694 + 2*m.b692*m.b695 - 4*m.b695 + 2*m.b693*m.b695 + 2*
                       m.b693*m.b799 + 2*m.b693*m.b1209 - 2*m.b694*m.b1166 + 2*m.b695*m.b946 + 2*m.b695*m.b1166 + 2*
                       m.b696*m.b698 - 2*m.b696*m.b1015 - 2*m.b696*m.b1016 + 2*m.b697*m.b921 + 2*m.b697*m.b1200 - 2*
                       m.b697*m.b1214 + 2*m.b698*m.b1166 + 2*m.b698*m.b1214 - 2*m.b699*m.b904 - 2*m.b699*m.b1045 - 2*
                       m.b699*m.b1046 + 2*m.b700*m.b702 + 2*m.b701*m.b702 - 2*m.b701 - 2*m.b701*m.b962 + 2*m.b701*
                       m.b1046 + 2*m.b701*m.b1167 + 2*m.b702*m.b1116 - 2*m.b703*m.b1006 - 2*m.b703*m.b1193 + 2*m.b704*
                       m.b705 - 2*m.b704 - 2*m.b704*m.b757 + 2*m.b704*m.b977 + 2*m.b704*m.b1193 + 2*m.b705*m.b707 + 2*
                       m.b705*m.b1210 - 2*m.b706*m.b709 + 2*m.b707*m.b709 + 2*m.b707*m.b862 - 2*m.b708*m.b711 - 2*m.b711
                        - 2*m.b708*m.b763 + 2*m.b709*m.b711 - 2*m.b710*m.b713 - 2*m.b713 - 2*m.b710*m.b818 - 2*m.b710*
                       m.b876 + 2*m.b711*m.b713 + 2*m.b711*m.b1028 - 2*m.b712*m.b1140 - 2*m.b712*m.b1141 + 2*m.b713*
                       m.b714 + 2*m.b714 + 2*m.b713*m.b1141 - 2*m.b714*m.b715 - 2*m.b715 - 2*m.b714*m.b877 - 2*m.b714*
                       m.b965 + 2*m.b715*m.b716 + 2*m.b715*m.b717 + 2*m.b715*m.b1141 - 2*m.b716*m.b1102 + 2*m.b717*
                       m.b910 + 2*m.b717*m.b1102 + 2*m.b718*m.b720 + 2*m.b718*m.b1196 + 2*m.b719*m.b722 - 2*m.b719*
                       m.b1142 + 2*m.b720*m.b722 + 2*m.b720*m.b1102 + 2*m.b721*m.b723 - 2*m.b721*m.b1224 + 2*m.b722*
                       m.b1224 + 2*m.b723*m.b724 + 2*m.b724*m.b725 - 2*m.b725 + 2*m.b724*m.b1224 + 2*m.b725*m.b726 - 2*
                       m.b725*m.b995 + 2*m.b725*m.b1064 + 2*m.b726*m.b758 + 2*m.b726*m.b914 + 2*m.b727*m.b729 - 2*m.b727
                       *m.b747 - 2*m.b728*m.b1205 + 2*m.b729*m.b758 + 2*m.b729*m.b1205 - 2*m.b730*m.b1212 - 2*m.b730*
                       m.b1225 - 2*m.b731*m.b732 + 2*m.b731*m.b906 - 2*m.b733*m.b734 + 2*m.b733*m.b896 + 2*m.b734*m.b911
                        - 2*m.b735*m.b806 - 2*m.b736*m.b737 - 2*m.b736*m.b745 + 2*m.b736*m.b749 - 2*m.b738*m.b739 + 2*
                       m.b740*m.b741 - 2*m.b741*m.b758 + 2*m.b742*m.b743 - 2*m.b742*m.b931 - 2*m.b743*m.b1112 + 2*m.b744
                       *m.b855 - 2*m.b744*m.b1034 + 2*m.b745*m.b798 + 2*m.b746*m.b747 + 2*m.b746*m.b778 + 2*m.b747*
                       m.b806 - 2*m.b748*m.b917 + 2*m.b749*m.b813 + 2*m.b750*m.b872 - 2*m.b752*m.b900 + 2*m.b753*m.b826
                        + 2*m.b754*m.b887 - 2*m.b755*m.b756 + 2*m.b755*m.b757 + 2*m.b755*m.b964 - 2*m.b756*m.b938 - 2*
                       m.b759*m.b884 + 2*m.b760*m.b903 - 2*m.b761*m.b762 - 2*m.b761*m.b959 + 2*m.b762*m.b1089 - 2*m.b762
                       *m.b1100 - 2*m.b763*m.b764 + 2*m.b763*m.b765 + 2*m.b763*m.b979 - 2*m.b764*m.b924 - 2*m.b765*
                       m.b963 - 2*m.b766*m.b1010 - 2*m.b766*m.b1092 - 2*m.b769*m.b770 + 2*m.b769*m.b919 - 2*m.b770*
                       m.b1136 - 2*m.b771*m.b948 - 2*m.b772*m.b773 + 2*m.b772*m.b774 - 2*m.b772*m.b925 + 2*m.b773*m.b829
                        - 2*m.b773*m.b908 - 2*m.b774*m.b978 - 2*m.b775*m.b776 + 2*m.b775*m.b865 + 2*m.b776*m.b876 + 2*
                       m.b776*m.b925 - 2*m.b776*m.b926 - 2*m.b777*m.b1020 - 2*m.b777*m.b1079 - 2*m.b778*m.b779 + 2*
                       m.b780*m.b781 - 2*m.b783*m.b784 + 2*m.b784*m.b854 - 2*m.b784*m.b956 - 2*m.b785*m.b935 - 2*m.b786*
                       m.b787 + 2*m.b786*m.b788 - 2*m.b786*m.b909 + 2*m.b787*m.b816 - 2*m.b788*m.b993 - 2*m.b789*m.b790
                        + 2*m.b789*m.b878 + 2*m.b790*m.b891 + 2*m.b790*m.b909 - 2*m.b791*m.b792 + 2*m.b793*m.b794 - 2*
                       m.b796*m.b797 + 2*m.b796*m.b985 + 2*m.b797*m.b838 - 2*m.b797*m.b944 - 2*m.b800*m.b922 - 2*m.b801*
                       m.b802 + 2*m.b803*m.b804 - 2*m.b803*m.b892 + 2*m.b805*m.b895 + 2*m.b806*m.b1020 - 2*m.b806*
                       m.b1049 + 2*m.b807*m.b808 - 2*m.b810*m.b811 + 2*m.b810*m.b812 + 2*m.b810*m.b1001 + 2*m.b811*
                       m.b823 + 2*m.b811*m.b931 - 2*m.b811*m.b932 + 2*m.b812*m.b884 - 2*m.b812*m.b986 - 2*m.b814*m.b843
                        - 2*m.b815*m.b905 - 2*m.b816*m.b817 - 2*m.b816*m.b862 + 2*m.b820*m.b821 - 2*m.b820*m.b868 - 2*
                       m.b821*m.b1080 + 2*m.b824*m.b825 + 2*m.b824*m.b1013 + 2*m.b825*m.b900 - 2*m.b825*m.b1002 + 2*
                       m.b827*m.b1098 - 2*m.b827*m.b1220 - 2*m.b828*m.b889 - 2*m.b829*m.b830 + 2*m.b829*m.b831 - 2*
                       m.b829*m.b847 - 2*m.b831*m.b1116 - 2*m.b831*m.b1124 - 2*m.b832*m.b833 - 2*m.b833*m.b863 + 2*
                       m.b835*m.b836 - 2*m.b835*m.b852 - 2*m.b836*m.b1093 - 2*m.b838*m.b840 - 2*m.b839*m.b840 + 2*m.b839
                       *m.b841 + 2*m.b839*m.b1024 + 2*m.b840*m.b900 + 2*m.b841*m.b917 - 2*m.b841*m.b1014 - 2*m.b842*
                       m.b1172 - 2*m.b843*m.b1086 + 2*m.b844*m.b1086 - 2*m.b844*m.b1213 - 2*m.b845*m.b874 - 2*m.b849*
                       m.b940 + 2*m.b851*m.b852 - 2*m.b852*m.b1130 - 2*m.b853*m.b1094 - 2*m.b854*m.b856 - 2*m.b855*
                       m.b856 + 2*m.b855*m.b857 - 2*m.b855*m.b902 + 2*m.b856*m.b884 + 2*m.b857*m.b931 - 2*m.b857*m.b1025
                        + 2*m.b858*m.b1071 + 2*m.b859*m.b1072 - 2*m.b859*m.b1209 - 2*m.b860*m.b1004 + 2*m.b861*m.b950 - 
                       2*m.b863*m.b938 + 2*m.b864*m.b865 - 2*m.b864*m.b928 - 2*m.b865*m.b1062 + 2*m.b867*m.b868 - 2*
                       m.b868*m.b1145 - 2*m.b869*m.b1082 - 2*m.b870*m.b1034 + 2*m.b871*m.b1056 + 2*m.b873*m.b874 - 2*
                       m.b873*m.b990 + 2*m.b874*m.b1089 + 2*m.b875*m.b936 - 2*m.b875*m.b1192 - 2*m.b876*m.b924 + 2*
                       m.b877*m.b878 - 2*m.b877*m.b913 - 2*m.b878*m.b1077 - 2*m.b879*m.b880 - 2*m.b880*m.b1153 - 2*
                       m.b881*m.b882 + 2*m.b882*m.b1093 - 2*m.b883*m.b1068 - 2*m.b886*m.b1157 + 2*m.b888*m.b889 - 2*
                       m.b888*m.b974 + 2*m.b889*m.b1075 - 2*m.b889*m.b1109 + 2*m.b890*m.b923 - 2*m.b890*m.b1202 - 2*
                       m.b891*m.b908 - 2*m.b893*m.b894 + 2*m.b893*m.b895 - 2*m.b894*m.b952 - 2*m.b895*m.b1090 - 2*m.b896
                       *m.b966 - 2*m.b897*m.b898 - 2*m.b898*m.b1143 - 2*m.b899*m.b998 - 2*m.b901*m.b1054 - 2*m.b902*
                       m.b1148 + 2*m.b904*m.b905 - 2*m.b904*m.b960 + 2*m.b905*m.b1059 - 2*m.b906*m.b907 + 2*m.b907*
                       m.b960 - 2*m.b907*m.b1116 + 2*m.b908*m.b1169 - 2*m.b910*m.b911 - 2*m.b911*m.b939 + 2*m.b912*
                       m.b913 - 2*m.b912*m.b953 - 2*m.b914*m.b915 - 2*m.b915*m.b1128 - 2*m.b916*m.b984 - 2*m.b920*m.b921
                        + 2*m.b920*m.b922 - 2*m.b920*m.b949 - 2*m.b921*m.b1037 + 2*m.b922*m.b1045 + 2*m.b924*m.b1176 + 2
                       *m.b926*m.b1170 + 2*m.b927*m.b928 - 2*m.b927*m.b941 - 2*m.b928*m.b1195 - 2*m.b929*m.b1118 - 2*
                       m.b930*m.b968 - 2*m.b933*m.b957 - 2*m.b934*m.b1027 + 2*m.b935*m.b1037 - 2*m.b936*m.b937 + 2*
                       m.b939*m.b1177 - 2*m.b940*m.b1185 - 2*m.b942*m.b1111 - 2*m.b943*m.b955 - 2*m.b945*m.b1189 - 2*
                       m.b946*m.b1017 - 2*m.b947*m.b1016 + 2*m.b947*m.b1017 + 2*m.b948*m.b1027 - 2*m.b949*m.b951 - 2*
                       m.b950*m.b951 - 2*m.b950*m.b977 + 2*m.b952*m.b1184 - 2*m.b954*m.b1103 + 2*m.b956*m.b1115 - 2*
                       m.b957*m.b1181 + 2*m.b958*m.b1003 + 2*m.b959*m.b1016 - 2*m.b959*m.b1167 - 2*m.b960*m.b961 + 2*
                       m.b963*m.b1203 - 2*m.b964*m.b1047 + 2*m.b965*m.b1101 + 2*m.b965*m.b1194 - 2*m.b967*m.b1091 - 2*
                       m.b968*m.b1000 + 2*m.b969*m.b999 - 2*m.b969*m.b1146 + 2*m.b970*m.b1122 - 2*m.b971*m.b1173 + 2*
                       m.b972*m.b1173 + 2*m.b973*m.b989 - 2*m.b974*m.b975 - 2*m.b976*m.b1168 - 2*m.b977*m.b978 + 2*
                       m.b978*m.b1211 - 2*m.b979*m.b1061 - 2*m.b982*m.b1030 - 2*m.b985*m.b986 - 2*m.b985*m.b1085 + 2*
                       m.b986*m.b1134 + 2*m.b987*m.b1181 - 2*m.b989*m.b1182 - 2*m.b990*m.b991 - 2*m.b992*m.b1175 + 2*
                       m.b993*m.b1215 + 2*m.b995*m.b1008 - 2*m.b996*m.b1021 + 2*m.b997*m.b1011 + 2*m.b999*m.b1000 - 2*
                       m.b999*m.b1105 - 2*m.b1000*m.b1206 - 2*m.b1001*m.b1002 + 2*m.b1002*m.b1132 + 2*m.b1002*m.b1149 - 
                       2*m.b1003*m.b1190 - 2*m.b1004*m.b1005 - 2*m.b1006*m.b1183 - 2*m.b1008*m.b1009 - 2*m.b1008*m.b1010
                        - 2*m.b1011*m.b1178 - 2*m.b1012*m.b1096 - 2*m.b1013*m.b1014 + 2*m.b1014*m.b1147 + 2*m.b1014*
                       m.b1158 + 2*m.b1015*m.b1107 - 2*m.b1015*m.b1200 - 2*m.b1017*m.b1200 - 2*m.b1022*m.b1023 - 2*
                       m.b1022*m.b1084 - 2*m.b1024*m.b1025 + 2*m.b1025*m.b1156 + 2*m.b1025*m.b1165 + 2*m.b1026*m.b1099
                        - 2*m.b1026*m.b1190 + 2*m.b1028*m.b1151 - 2*m.b1028*m.b1160 - 2*m.b1029*m.b1038 + 2*m.b1031*
                       m.b1179 - 2*m.b1032*m.b1033 - 2*m.b1032*m.b1070 + 2*m.b1034*m.b1164 + 2*m.b1035*m.b1207 - 2*
                       m.b1035*m.b1220 + 2*m.b1036*m.b1087 - 2*m.b1036*m.b1182 + 2*m.b1038*m.b1194 + 2*m.b1039*m.b1187
                        - 2*m.b1040*m.b1041 - 2*m.b1040*m.b1053 + 2*m.b1043*m.b1198 - 2*m.b1043*m.b1213 + 2*m.b1044*
                       m.b1073 - 2*m.b1044*m.b1174 + 2*m.b1046*m.b1214 + 2*m.b1048*m.b1049 - 2*m.b1048*m.b1050 - 2*
                       m.b1049*m.b1118 + 2*m.b1051*m.b1197 - 2*m.b1053*m.b1054 + 2*m.b1054*m.b1132 - 2*m.b1055*m.b1056
                        - 2*m.b1057*m.b1058 + 2*m.b1058*m.b1188 + 2*m.b1058*m.b1207 - 2*m.b1058*m.b1209 + 2*m.b1060*
                       m.b1168 + 2*m.b1060*m.b1221 - 2*m.b1062*m.b1126 - 2*m.b1063*m.b1064 + 2*m.b1063*m.b1065 - 2*
                       m.b1063*m.b1066 - 2*m.b1064*m.b1103 - 2*m.b1065*m.b1128 + 2*m.b1067*m.b1206 - 2*m.b1068*m.b1069
                        + 2*m.b1068*m.b1070 + 2*m.b1072*m.b1073 - 2*m.b1073*m.b1074 + 2*m.b1076*m.b1175 - 2*m.b1078*
                       m.b1091 - 2*m.b1079*m.b1143 - 2*m.b1082*m.b1083 + 2*m.b1082*m.b1084 + 2*m.b1086*m.b1087 - 2*
                       m.b1087*m.b1088 - 2*m.b1092*m.b1153 - 2*m.b1094*m.b1095 + 2*m.b1094*m.b1096 + 2*m.b1098*m.b1099
                        - 2*m.b1099*m.b1100 + 2*m.b1101*m.b1169 - 2*m.b1104*m.b1161 - 2*m.b1105*m.b1163 - 2*m.b1107*
                       m.b1108 + 2*m.b1109*m.b1201 - 2*m.b1112*m.b1155 - 2*m.b1113*m.b1115 - 2*m.b1114*m.b1115 + 2*
                       m.b1116*m.b1193 - 2*m.b1120*m.b1122 - 2*m.b1121*m.b1122 + 2*m.b1123*m.b1203 - 2*m.b1124*m.b1125
                        - 2*m.b1126*m.b1176 - 2*m.b1131*m.b1132 - 2*m.b1131*m.b1134 - 2*m.b1133*m.b1134 - 2*m.b1135*
                       m.b1136 + 2*m.b1137*m.b1211 - 2*m.b1138*m.b1139 - 2*m.b1140*m.b1169 + 2*m.b1142*m.b1186 - 2*
                       m.b1146*m.b1147 - 2*m.b1148*m.b1149 + 2*m.b1150*m.b1215 - 2*m.b1151*m.b1159 - 2*m.b1155*m.b1156
                        - 2*m.b1157*m.b1158 - 2*m.b1163*m.b1164 - 2*m.b1167*m.b1168 - 2*m.b1172*m.b1173 - 2*m.b1180*
                       m.b1181 - 2*m.b1185*m.b1186 - 2*m.b1188*m.b1189 - 2*m.b1192*m.b1193 - 2*m.b1195*m.b1196 - 2*
                       m.b1198*m.b1199 - 2*m.b1202*m.b1203 - 2*m.b1204*m.b1205 + 2*m.b1205*m.b1225 - 2*m.b1207*m.b1208
                        - 2*m.b1210*m.b1211 - 2*m.b1216*m.b1217 + m.x1226 <= 0)
