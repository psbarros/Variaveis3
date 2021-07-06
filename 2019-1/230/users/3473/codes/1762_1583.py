ent = input()

count = 0
saida = ""
while(count < len(ent)):
	if(count > 0):
		if(count%3 == 0 and count<len(ent)-1):
			saida = saida + "."
	saida = saida+ent[count]
	print(saida)
	count = count + 1
print(saida)