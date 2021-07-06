from math import*
t1 = radians(float(input("Latitute t1: ")))
g1 = radians(float(input("Longitude g1: ")))
t2 = radians(float(input("Latitude t2: ")))
g2 = radians(float(input("Longitude g2: ")))

r = 6371.01

d = float(r*acos(sin(t1)*sin(t2)+cos(t1)*cos(t2)*cos(g1-g2)))

print(round(d,2))
