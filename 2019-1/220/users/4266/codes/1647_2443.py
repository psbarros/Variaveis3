# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import*

r = float(input("Digite o raio: "))
a = float (input("Digite a altura: "))
opcao = int(input("Digite a opcao 1 para volume de ar ou 2 para volume de combustivel: "))


v = (4*pi*(r**3))/3
v2 = (pi*(a**2)*(3*r - a))/3

if(opcao == 1):
	print(round(v2, 4))
	
else:
	vt = v - v2
	print(round(vt, 4))

