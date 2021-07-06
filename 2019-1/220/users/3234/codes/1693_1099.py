# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
from math import *

# Leitura dos lados do triangulo a, b, and c
a = float(input ("Lado 1: "))
b = float(input ("Lado 2: "))
c = float(input ("Lado 3: "))

print("Entradas:", a, ",", b, ",", c)
if (a,b,c > 0):
	if (a + b > c and b + c > a and a + c > b):
		if(a==b and  b==c and c==a):
			print("Tipo de triangulo: equilatero")
		elif (a == b or b == c or c == a):
			print("Tipo de triangulo: isosceles")
		elif (a != b or b != c or c != a):
			print("Tipo de triangulo: escaleno")
	else:
		print("Tipo de triangulo: invalido")
else:
		print("Tipo de triangulo: invalido")
