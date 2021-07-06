from math import *
pv=int(input("Pontos de vida iniciais: "))
D1=int(input("Dado 1: "))
D2=int(input("Dado 2: "))
dano= sqrt(5*D1) + pi**(D2/3)
dano=int(dano)
print(pv-dano)