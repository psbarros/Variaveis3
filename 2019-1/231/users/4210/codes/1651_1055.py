from math import*
v0 = float(input("Insira a velocidade: "))
x = radians(float(input("Insira um angulo em graus: ")))
D = float(input("Insira a distancia: "))
g = 9.8
R = ((v0**2)*sin(2*x))/g


if (D-0.1< R < D+0.1):
	mensagem = "sim"
else:
	mensagem = "nao"

print(mensagem)