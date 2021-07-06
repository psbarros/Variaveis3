a = float(input("Digite o coeficiente a: "))
b = float(input("Digite o coeficiente b: "))
c = float(input("Digite o coeficiente c: "))
d = float(input("Digite o coeficiente d: "))
e = float(input("Digite o coeficiente e: "))
f = float(input("Digite o coeficiente f: "))

n1 = ((c*e) - (b*f))
n2 = ((a*e) - (b*d))  
n3 = ((a*f) - (c*d))
n4 = ((a*e) - (b*d))

if ((n2 != 0) and (n4 != 0)): 
	x = n1 / n2
	y = n3 / n4
	print(x)
	print(y)
else:
	print("Nao tem solucao")