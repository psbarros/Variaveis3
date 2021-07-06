#Data

from math import*

La1 = radians(float(input("Latitude of P1: ")))
Lo1 = radians(float(input("Longitude of P1: ")))
La2 = radians(float(input("Latitude of P2: ")))
Lo2 = radians(float(input("Longitude of P2: ")))

#Operation

Re = 6371.01
theta = (sin(La1)*sin(La2))+(cos(La1)*cos(La2)*cos(Lo1-Lo2))
d = Re*acos(theta)
print(round(d,2))