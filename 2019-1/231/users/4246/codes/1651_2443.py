# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import *

r = float(input())
x = float(input())
opcao = int(input())

vc = (pi*(x**2) * (3*r - x)) / 3

if( opcao == 1):
	print(round(vc, 4))
else: 
	ve = (4 *  pi * (r**3))/3
	volumeCombustivel = ve - vc
	
	print(round(volumeCombustivel, 4))