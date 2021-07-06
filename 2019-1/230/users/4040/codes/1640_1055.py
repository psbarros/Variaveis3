#Insertable Data

from math import *

v0 = float(input("Inicial Velocity: "))
α = float(input("Inicial Angle: "))
D = float(input("Inicial Distance: "))

#Processing

thetar0 = radians(2*α)
g = 9.8
R = (g**-1)*((v0)**2)*sin(thetar0)
ImpactFactor = abs(D-R)

if (ImpactFactor < 0.1):
	print("sim")
else:
	print("nao")