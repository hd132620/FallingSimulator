__author__ = 'USER'

import math
import time
import util
import matplotlib.pyplot as plt

deltaT = 0.01

g = 9.80665
theta = 55
launch_velocity = 142
launch_theta = math.pi/180 * theta

t = 0

s = util.coordinate(0, 0, "s")
v = util.coordinate(launch_velocity * math.cos(launch_theta), launch_velocity * math.sin(launch_theta), "v")
a = util.coordinate(0, -g, "a")

sXlist = [s.x]
sYlist = [s.y]

fig = plt.figure(figsize=(12, 9))
ax1 = fig.add_subplot(1, 1, 1)

#print(theta, launch_velocity)

while t < 1000:
    s.calculateD(v, deltaT)
    sXlist.append(s.x)
    sYlist.append(s.y)

    v.calculateD(a, deltaT)

    if s.y <= 0:
        break

    s.print()
    v.printWithAll()
    a.printWithAll()
    print("t = " + format(t,".2f"))
    print()

    t += deltaT
    #time.sleep(deltaT)
ax1.set(xlim=[0, s.x], ylim=[0, 800], xlabel='x', ylabel='y')
ax1.plot(sXlist, sYlist)
plt.show()
