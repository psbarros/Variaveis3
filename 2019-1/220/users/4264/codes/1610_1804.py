from math import *
Xa=float(input("Xa:"))
Ya=float(input("Ya:"))
Xb=float(input("Xb:"))
Yb=float(input("Yb:"))
A=(Xb-Xa)**2
B=(Yb-Ya)**2
C=A+B
dAB=sqrt(C)
print(round(dAB, 3))
