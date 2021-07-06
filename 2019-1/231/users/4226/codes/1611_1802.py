from math import *

LP = int(input("LP: "))
D1 = int(input("D 1-20: "))
D2 = int(input("D 1-20: "))

Dmg = ((sqrt(5*D1))+(pi**(D2/3)))

dmg = int(Dmg)

vida = (LP - dmg)
print(vida)