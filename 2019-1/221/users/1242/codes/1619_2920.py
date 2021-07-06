#tres entradas
prato = float(input("Quantas gramas possui o prato: "))
bebidas = int(input("A quantidade de bebidas: "))
sobremesa = int(input("A quantidade de sobremesas: "))
compra = ((prato/1000) * 26.90) + (bebidas * 3.50) + (sobremesa * 3.00)
print(round(compra,2))