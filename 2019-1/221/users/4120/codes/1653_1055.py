import math
v = float(input("digite a velocidade: "))
a = float(input("digite o angulo: "))
d = float(input("digite a distancia: "))
g = 9.8
b = math.radians(a)
R = ((v**2)*math.sin(2*b))/g
abs(d - R)
if(d - R <= 0.1 ):
	mensagem = "sim"
	print(mensagem)
else:
	mensagem = "nao"
	print(mensagem)
	
	