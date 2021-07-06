# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo.
a=float(input("ponto a:"))
b=float(input("ponto b:"))
c=float(input("ponto c:"))
d=float(input("ponto d:"))

print("Intervalo 1:", a,",",b)
print("Intervalo 2:", c,",",d)

if((b<=a)or(d<=c)):
	print("Entradas invalidas")
elif(((a<=c)and(c<=b))or((c<=a)and(a<=d))):
	print("Ha intersecao")
else:
	print("Nao ha intersecao")
	

