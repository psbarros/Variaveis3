# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
preco = float(input("preco: "))

if(preco >= 200):
	desconto = preco - (preco * 0.05)
else:
	desconto = preco
	
print(round(desconto, 2))