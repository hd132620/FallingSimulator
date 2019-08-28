__author__ = 'USER'

import numpy as np
import matplotlib.pyplot as plt

# F = GMm / r^2
# a = GM / r^2

deltaT = 0.01       # △s

GM = 398600.4418    # km^3/s^2 중력상수x지구질량
EarthR = 6378       # km       지구반지름

t = 0                       # s        시간
tList = [t]

hStart = EarthR + 700       # km       지면과의 높이
h = hStart
hList = [h]
v = 0                       # km/s     속도
vList = [v]

a = 0                       # m/s^2    가속도
aList = [a]

# 그래프 초기화
fig = plt.figure(figsize=(18.5, 6))
axH = fig.add_subplot(1, 3, 1)
axV = fig.add_subplot(1, 3, 2)
axA = fig.add_subplot(1, 3, 3)

axH.grid()
axV.grid()
axA.grid()

while True:
    h += v * deltaT

    if h < EarthR:
        break

    hList.append(h - EarthR)

    v += a * deltaT
    vList.append(v)

    a = -GM / h**2
    aList.append(a*1000) # 중력상수의 단위는 km단위가 기준이므로 이를 표준단위인 m로 			    고치기 위해서 1000을 곱해준다

    t += deltaT
    tList.append(t)

    print("t = " + format(t, ".2f"), " h = " + format((h-EarthR), ".3f") + "km",
          " v = " + format(v, ".3f") + "km/s", " a = " + format(a*1000 , ".3f") + "m/s")

axH.set(xlim=[0, t], ylim=[0, hStart - EarthR], xlabel='t', ylabel='height(km)')
axV.set(xlim=[0, t], ylim=[v, 0], xlabel='t', ylabel='velocity(km/s)')
axA.set(xlim=[0, t], ylim=[-9.80665, -0], xlabel='t', ylabel='acceleration(m/s)')

axH.plot(tList, hList)
axV.plot(tList, vList)
axA.plot(tList, aList)

tList.clear()
vList.clear()
hList.clear()
aList.clear()

plt.show()
