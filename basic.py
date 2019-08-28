#import math
import time
deltaT = 0.01

sStart = 100

g = 9.80665

t = 0
s = sStart
v = 0

while t < 50.0:
	s = s + v * deltaT
 	v = v - g * deltaT
 	t += deltaT
 	print("t = " + format(t, ".3f"), " s = " + format(s, ".3f"), " v = " + format(v, ".3f"), " g = " + format(g, ".3f"))
 # time.sleep(deltaT)
