he = float(input("Numero de horas extras: "))
hf = float(input("Numero de horas faltou: "))

h = (he-(1/4*hf))

print(he, "extras", "e", hf, "de falta")

if(h<=400):
	print("R$", round(100.00,2))
else:
	print("R$", round(500.00,2))


	
	