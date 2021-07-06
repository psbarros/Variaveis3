# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
v=float(input("velocidade inicial:"))
a=float(input("angulo:"))
import math
b=float(math.radians(2*a))
D=float(input("distancia:"))
g=(9.8)
import math
sen=float(math.sin(b))

R=float((v**2*(sen))/g)

x=abs(D - R)

if(x<0.1):
	print("sim")
else:
	print("nao")



