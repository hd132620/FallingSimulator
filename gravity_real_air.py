__author__ = 'USER'

import math as m
import matplotlib.pyplot as plt

# F = -mg + kv^2

deltaT = 0.001

t = 0
tList = [t]

hStart = 3500
h = hStart
hList = [h]

vStart = 0
v = vStart
vList = [v]

aStart = 0
a = aStart
aList = [a]

## 고유 파라미터
# 중력가속도 g0
g0 = 9.80665
# 질량 m
m = 10

## 공기밀도 파라미터
# 표준대기압
p0 = 101.325 (1013.25hPa은 표준단위로 101325Pa이지만 여기서는 단위설정에 문제가 생겨 kPa단위로 해야 정상적으로 작동되었다.)
# 표준온도
T0 = 288.15
# 온도감율
L = 0.0065

# 온도
def tempOfAir(h):
    return T0 - (L * h)
T = tempOfAir(h)
# 이상기체상수
R = 8.31447
# 건조공기 몰질량
M = 0.0289644

# 대기압 (hm -> kPa)
def pressureOfAir(h):
    return p0 * (1 - L*h/T0)**((g0*M)/(R*L))
p = pressureOfAir(h)

# 공기밀도
def densityOfAir(h):
    return 1000 * (pressureOfAir(h) * M) / (R * tempOfAir(h))
row = densityOfAir(h)

## 공기저항 파라미터
# 항력계수
Cd = 0.3
# 면적
A = 3
# 공기저항계수 Fd
def getFdFromRow(row):
    return 0.5 * densityOfAir(h) * Cd * A

def getFdFromHeight(h):
    return 0.5 * densityOfAir(h) * Cd * A
Fd = getFdFromHeight(h)

#실구현부

fig = plt.figure(figsize=(18.5, 6))
axH = fig.add_subplot(1, 3, 1)
axV = fig.add_subplot(1, 3, 2)
axA = fig.add_subplot(1, 3, 3)

axH.grid()
axV.grid()
axA.grid()

while t < 300:
    h += v * deltaT
    if h < 0:
        break
    hList.append(h)

    v += a * deltaT
    vList.append(v)

    Fd = getFdFromHeight(h)
    a = -g0 + ((Fd/m) * v**2)
    aList.append(a)

    t += deltaT
    tList.append(t)
    print("t = " + format(t, ".3f"), " h = " + format(h, ".3f"), " v = " + format(v, ".3f"), " a = " + format(a, ".3f"), end="\n\n")

#index = aList.

axH.set(xlim=[0, t], ylim=[0, hStart], xlabel='t', ylabel='height')
axV.set(xlim=[0, t], ylim=[-250, 0], xlabel='t', ylabel='velocity')
axA.set(xlim=[0, t], ylim=[-9.805, 4], xlabel='t', ylabel='acceleration')

axH.plot(tList, hList)
axV.plot(tList, vList)
axA.plot(tList, aList)

plt.show()
