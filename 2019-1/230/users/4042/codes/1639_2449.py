a = float(input("1. Digite o coeficiente a: "))
b = float(input("2. Digite o coeficiente b: "))
c = float(input("3. Digite o coeficiente c: "))
d = float(input("4. Digite o coeficiente d: "))
e = float(input("6. Digite o coeficiente e: "))
f = float(input("7. Digite o coeficiente f: "))

if((a * e - b * d) != 0):
	x = (c * e - b * f)/(a * e - b * d)
	print(x)
	y = (a * f - c * d)/(a * e - b * d)
	print(y)
else:
	print("Nao tem solucao")