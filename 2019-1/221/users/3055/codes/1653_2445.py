temp_repr = input("Temperatura representada: ")
valor_temp = float(input("Valor da temperatura: "))

if(temp_repr == "F"):
	c = (5/9) * (valor_temp - 32)
	print(round(c, 2))
else:
	f = (9/5 * valor_temp) + 32
	print(round(f, 2))