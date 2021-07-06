# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
from math import *
t1 = radians(float(input("Latitude de P1: ")))
t2 = radians(float(input("Longitude de p1:")))
t3 = radians(float(input("Latitude de p2:")))
t4 = radians(float(input("Longitude de p2:")))
R = 637101
d = R * acos( (sin(t1) * sin(t2)) + (cos(t1) * cos(t2) * cos( t3 - t4)) )
print(round(d,2))
