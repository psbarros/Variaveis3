# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import*
r = float(input("raio: "))
x = float(input("Altura: "))
numero = input("opcao (1/2)?" )

ar = float((pi*x**2)*(3*r-x))/3
combustivel = float(((4*pi*r**3)/3)-ar)

if(numero == "1"):
	print(round(ar,4))
else:
	print(round(combustivel,4))