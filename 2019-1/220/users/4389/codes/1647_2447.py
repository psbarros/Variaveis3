preco = float(input("Informe o preco do produto: \n"))
pagamento = float(input("Informe o valor dado ao caixa: \n"))
if (preco>pagamento):
	resultado = preco - pagamento
	print("Falta", round(resultado,2))
else:
	resultado2 = pagamento - preco
	print("Troco de", round(resultado2,2))

	