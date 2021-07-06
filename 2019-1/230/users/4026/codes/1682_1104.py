# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo.
a= float(input("Entrada a:"))
b= float(input("Entrada b:"))
c= float(input("Entrada c:"))
d= float(input("Entrada d:"))
print("Intervalo 1:", a, ",", b)
print("Intervalo 2:", c, ",", d)
if		(a < b) and (c < d):
		if		((c >= a) and (b >= c) or (d >= a) and (d <= b)):
				print("Ha intersecao")
		else:
				print("Nao ha intersecao")
else:
		print("Entradas invalidas")
