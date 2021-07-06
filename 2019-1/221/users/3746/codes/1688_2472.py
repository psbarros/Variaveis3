# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída

resp1 = input("Digite a resposta 1: ")
resp2 = input("Digite a resposta 2: ")
resp3 = input("Digite a resposta 3: ")
gab1 = input("Digite o gabarito 1: ")
gab2 = input("Digite o gabarito 2: ")
gab3 = input("Digite o gabarito 3: ")

certas = 0

if resp1 == gab1 :
	certas += 1
if resp2 == gab2:
	certas += 1
if resp3 == gab3:
	certas += 1
		
print(certas)

	