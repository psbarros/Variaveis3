from math import *
H = float(input("altura total do tanque: "))
h = float(input("nivel de combustivel no tanque: "))
r = float(input("raio: "))
if (H>0 and h>0 and r>0 and H>h and H>2*r):
        if(h>=(H-r)):
            v = (2*(pi/3)*(r**2)*(2*r) + pi*(r**2)*(H-(2*r))) - (pi/3)*(r**2)*(H-2*r)
            vt = round((v * 1000),3)
            print("Entradas: ", H, ", ", h, ", ", r)
            print("Volume: ", vt, "litros")
        elif(h<(H-r)):
            v = (pi/3)*(r**2)*(2*r) + pi*(r**2)*(h-r)
            vt = round((v * 1000),3)
            print("Entradas: ", H, ", ", h, ", ", r)
            print("Volume: ", vt, "litros")
        elif(h<=r):
            v = (pi/3)*((r-h)**2)*(3*r-(r-h))
            vt = round((v * 1000),3)
            print("Entradas: ", H, ", ", h, ", ", r)
            print("Volume: ", vt, "litros")
else:
   print("Entradas: ", H, ", ", h, ", ", r)
   print("Entradas invalidas")
