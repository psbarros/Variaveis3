# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
produto=float(input("valor:"))
desconto=float(produto*(5/100))
valorpromocional=float(produto-desconto)

if(produto>=200.00):
	print(round(valorpromocional, 2))
else:
	print(round(produto, 2))