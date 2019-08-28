__author__ = 'USER'

import math

class coordinate:
    def __init__(self, x=0, y=0, setting="none"):
        self.x = x
        self.y = y
        self.setting = setting

    def calculateD(self, dxdy, deltaT):
        self.x += dxdy.x * deltaT
        self.y += dxdy.y * deltaT

    def print(self):
        print(self.setting + " (" +format(self.x, ".3f") + ", " + format(self.y, ".3f") + ")", end=" ")

    def printAbs(self):
        print("|" + self.setting + "|=" + format(self.abs(), ".2f"), end=" ")

    def printTheta(self):
        print("θ=" + format(self.theta(), ".2f"), end=" ")

    def printWithAbs(self):
        self.print()
        self.printAbs()

    def printWithTheta(self):
        self.print()
        self.printTheta()

    def printWithAll(self):
        self.print()
        self.printAbs()
        self.printTheta()

    def abs(self):
        return math.sqrt(self.x**2 + self.y**2)

    def theta(self, printWith180 = True):
        if printWith180:
            return math.asin(self.y / self.abs()) * 180 / math.pi
        else:
            return math.asin(self.y / self.abs()) 
