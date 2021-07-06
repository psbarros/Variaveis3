# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo.

a = float(input())
b = float(input())
c = float(input())
d = float(input())

print("Intervalo 1: " + str(a) + " , " + str(b))
print("Intervalo 2: " + str(c) + " , " + str(d))

if(b > a and d > c):
	if( (a <= c and c <= b) or (a <= d and d <= b) or (c <= a and a <= d)):
		print("Ha intersecao")
	else:
		print("Nao ha intersecao")
else:
	print("Entradas invalidas")
