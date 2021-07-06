# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
import math
t1 = math.radians(float(input("Latitude de P1: ")))

Arquivo Editar Buscar Executar Ferramentas
Python 3
 main.py
Ajuda

d,2
1
# Teste seu codigo aos poucos.
2
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
3
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
4
import math
5
t1 = math.radians(float(input("Latitude de P1: ")))
6
g1 = math.radians(float(input("Longitude de P1: ")))
7
t2 = math.radians(float(input("Latitude de P2")))
8
g2 = math.radians(float(input("Longitude de P2")))
9
R = 6371.01 
10
d = R*math.acos(math.sin(t1)*math.sin(t2)+math.cos(t1)*math.cos(t2)*math.cos(g1-g2))
11
print(round(d,2))
g1 = math.radians(float(input("Longitude de P1: ")))
t2 = math.radians(float(input("Latitude de P2")))
g2 = math.radians(float(input("Longitude de P2")))
R = 6371.01 
d = R*math.acos(math.sin(t1)*math.sin(t2)+math.cos(t1)*math.cos(t2)*math.cos(g1-g2))
print(round(d,2))