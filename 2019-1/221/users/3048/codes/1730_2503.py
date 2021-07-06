n = int(input("Numero de termos: "))
pi = 0
cont = 0
num = 1
while (cont < n):
	pi = pi + ((-1)**cont) * (4/num)
	num = num + 2
	cont = cont + 1
print(round(pi, 8))