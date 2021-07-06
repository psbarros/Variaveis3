# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.

compra = float(input())
desconto = compra - (compra * 0.05)

if(compra >= 200):
	print(round(desconto, 2))