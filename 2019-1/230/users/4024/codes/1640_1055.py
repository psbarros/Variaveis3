# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
v = float(input("qual a velocidade inicial?"))
a = float(input("qual o angulo?"))
d = float(input("qual a distancia?"))

from math import*
g = 9.8
R = (((v**2) * sin(radians(2*a))) / g)

if (abs(d - R)<= 0.1) :
	mensagem = "sim"
else:
	mensagem = "nao"
	
print(mensagem)




