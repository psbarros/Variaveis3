a = float(input("Coeficiente 1: "))
b = float(input("Coeficiente 2: "))
c = float(input("Coeficiente 3: "))
d = float(input("Coeficiente 4: "))
e = float(input("Coeficiente 5: "))
f = float(input("Coeficiente 6: "))

if a*e - b*d != 0:
	x = (c*e - b*f) / (a*e - b*d)
	y = (a*f - c*d) / (a*e - b*d)
	print(x)
	print(y)
else:
	print("Nao tem solucao")
