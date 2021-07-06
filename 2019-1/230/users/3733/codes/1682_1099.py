# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída

a = float(input ("valor de a: " ))
b = float(input("valor de b: "))
c=float(input("valor de c: "))

print("Entradas:", a, ",", b, ",", c)
if(a>0 and b>0 and c>0):
	if(a+b>c and a+c>b and c+b>a):
			if(a==b and b==c and a==c):
				print("Tipo de triangulo: equilatero")
			if(a==b or a==c or b==c):
				print("Tipo de triangulo: isosceles")
			if(a!=b and b!=c and c!=a):
				print ("Tipo de triangulo: escaleno")
	else:
		print("Tipo de triangulo: invalido")
else:
	print ("Tipo de triangulo: invalido")
	