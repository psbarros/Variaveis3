preco = float(input("Preco: "))
pagamento = float(input("Pagamento: "))

if(preco > pagamento):
	x = round(preco - pagamento,2)
	msg = "Falta "
	print(msg, x)
else:
	y = round(pagamento - preco, 2)
	msg = "Troco de "
	print(msg, y)