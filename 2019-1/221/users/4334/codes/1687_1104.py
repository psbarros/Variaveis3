# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo.
a=float(input("digite um numero: "))
b=float(input("digite um numero maior que o anterior inserido: "))
c=float(input("digite um numero: "))
d=float(input("digite um numero maior que o anterior inserido: "))

if (b<a or d<c):
	print("Intervalo 1:" , a, ",", b)
	print("Intervalo 2:" , c, ",", d)
	print("Entradas invalidas")
elif (c<=a<=d) or (c<=b<=d):
	print("Intervalo 1:" , a, ",", b)
	print("Intervalo 2:" , c, ",", d)
	print("Ha intersecao")
elif (a<=c<=b) or (a<=d<=b):
	print("Intervalo 1:" , a, ",", b)
	print("Intervalo 2:" , c, ",", d)
	print("Ha intersecao")
else:
	print("Intervalo 1:" , a, ",", b)
	print("Intervalo 2:" , c, ",", d)
	print("Nao ha intersecao")
	
	