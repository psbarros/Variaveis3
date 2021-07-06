# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
a = float(input ("Lado 1: "))
b = float(input ("Lado 2: "))
c = float(input ("Lado 3: "))

print("Entradas:", a, ",", b, ",", c)

if((a == b) and (b ==c)):
	m = "equilatero"	
else:
	if((a == b)or(b == c)or(c == a)):
		m = "isosceles"
	else:
		m = "escaleno"
if(a<0 or b<0 or c<0)or((a >= b + c)or(b >= c + a)or(c >= a + b)):
	m = "invalido"
print("Tipo de triangulo: " , m)		