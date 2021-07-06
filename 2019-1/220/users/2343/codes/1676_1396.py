valor = float(input("Digite o valor do consumo: "))
desconto1 = (10/100)
desconto2 = (6/100)

if (valor <= 300):
	garcom = valor * (desconto1)
	total = garcom + valor
	print(round(total,2))
	
else:
	garcom = valor * (desconto2)
	total = garcom + valor
	print(round(total,2))
		
	