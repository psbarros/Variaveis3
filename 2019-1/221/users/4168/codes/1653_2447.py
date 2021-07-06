preco = float(input("preco:"))
pagamento = float(input("pagamento:"))
x = float(preco - pagamento)
y = float(pagamento - preco)

if (preco > pagamento):
	print("Falta", x)
else:
	print("Troco de", y)