# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
x = float(input("coordenada x do ponto p: "))
y = float(input("coordenada u do ponto p: "))
reta = (2*x + y)
if (reta ==3) :
	mensagem = "ponto pertence a reta"
	print(mensagem.lower())
else:
	mensagem = "ponto nao pertence a reta"
	print(mensagem.lower())