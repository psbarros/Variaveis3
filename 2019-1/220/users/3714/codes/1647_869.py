# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.

compra = float(input("valor? "))

if(compra >= 200.00):
	pagar = compra - compra*(5/100)
else:
	pagar = compra

print(round(pagar,2))