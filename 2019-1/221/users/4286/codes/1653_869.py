# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
preco = float(input("valor da compra"))
desconto = float(preco*5/100)
preco_com_desconto = float(preco - desconto)
if(preco>=200):
	print(round(preco_com_desconto, 2))
else:
	print(round(preco, 2))
	