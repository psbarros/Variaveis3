# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
valor=float(input("Valor original: "))
if(valor>=200.0):
	valor = 0.95*valor
print(round(valor, 2))