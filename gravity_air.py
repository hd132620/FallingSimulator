__author__ = 'USER'

import math
import time

# F = -mg + kv^2

deltaX = 0.001

# 중력가속도 g0
g0 = 9.80665
# 공기밀도
row = 1.224978
# 항력계수
Cd = 0.5
# 면적
A = 10

# 공기저항계수 Fd
Fd = 0.5 * row * Cd * A
##
# 질량 m
m = 40

t = 0
#떨어트리는 높이
s = 40
v = 0
a = 0

while t < 120:
    if(s<0):
        break
    s = s + v * deltaX
    v = v + a * deltaX
    a = -g0 + (Fd/m) * v**2
    t += deltaX
    print("t = " + format(t, ".3f"), " s = " + format(s, ".3f"), " v = " + format(v, ".3f"), " a = " + format(a, ".3f"))
    #time.sleep(deltaX)
