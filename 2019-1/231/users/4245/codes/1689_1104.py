# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo.

a= float(input("Digite um valor para a: "))
b= float(input("Digite um valor para b: "))
c= float(input("Digite um valor para c: "))
d= float(input("Digite um valor para d: "))

if(b>a and d>c):
	if(a<c and c<b):
		print("Intervalo 1: ",a,", ",b)
		print("Intervalo 2: ",c,", ",d)
		print("Ha intersecao")
		
	elif(a<d and d<b):
		print("Intervalo 1: ",a,", ",b)
		print("Intervalo 2: ",c,", ",d)
		print("Ha intersecao")
	
	elif(c<a and a<d):
		print("Intervalo 1: ",a,", ",b)
		print("Intervalo 2: ",c,", ",d)
		print("Ha intersecao")
		
	elif(c<b and b<d):
		print("Intervalo 1: ",a,", ",b)
		print("Intervalo 2: ",c,", ",d)
		print("Ha intersecao")
	else:
		print("Intervalo 1: ",a,", ",b)
		print("Intervalo 2: ",c,", ",d)
		print("Nao ha intersecao")
else:
	print("Intervalo 1: ",a,", ",b)
	print("Intervalo 2: ",c,", ",d)
	print("Entradas invalidas")

