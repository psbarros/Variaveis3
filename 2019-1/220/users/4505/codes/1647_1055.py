# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.

from math import*

v = float(input("Velocidade inicial: "))
a = radians(float(input("Angulo com o solo: ")))
D = float(input("Distancia entre passaro e porco: "))
g = 9.8
R = ((v ** 2) * sin(2 * a)) / g

if (abs(R - D) <= 0.1):
	print("sim")
else:
	print("nao")