vet = input(":")

d = len(vet)/ 3-1

i = 0
saida = ""
while(i <= d):
		saida = saida + vet[i*3:i*3+3]
		if (i < d):
			saida = saida + "."
		
		i = i + 1
print(saida)
		