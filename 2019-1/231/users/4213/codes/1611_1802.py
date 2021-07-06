from math import*
a=int(input("Vida:"))
d1=int(input("Lado1:"))
d2=int(input("Lado2:"))
dano=(5*d1)**0.5+pi**(d2/3)
e=int(dano)
print(a-e)