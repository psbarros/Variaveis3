# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
a = float(input ("Lado 1: "))
b = float(input ("Lado 2: "))
c = float(input ("Lado 3: "))

print("Entradas:", a, ",", b, ",", c)

if ( a > 0 and  b > 0 and c > 0 ):
	if ( (a + b > c) and (a + c > b) and (b + c > a) ):
		if ( (a == b) and (a == c) and (b == c) ):
			print("Tipo de triangulo: equilatero")
		if ( (a == c) or (a == b) or (b == c) ):
			print("Tipo de triangulo: isosceles")
		if ( a != b and a != c and b != c):
			print("Tipo de triangulo: escaleno")

	else:
		print("Tipo de triangulo: invalido")
else:
	print("Tipo de triangulo: invalido")
