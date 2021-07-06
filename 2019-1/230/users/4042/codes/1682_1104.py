a= float(input("Digite o valor de 'a' referente ao intervalo fechado [a,b]: "))
b= float(input("Digite o valor de 'b' referente ao intervalo fechado [a,b]: "))
c= float(input("Digite o valor de 'a' referente ao intervalo fechado [c,d]: "))
d= float(input("Digite o valor de 'd' referente ao intervalo fechado [c,d]: "))

print("Intervalo 1:", a, ",", b)
print("Intervalo 2:", c, ",", d)
 
if(a < b) and (c < d):
	if((c >= a) and (c <= b)) or ((d >= a) and (d <= b)):
		print("Ha intersecao")
	else:
		print("Nao ha intersecao")
else:
	print("Entradas invalidas")

