texto = input("numeros: ")
i = 0
saida = ""

while(i<len(texto)):
	if(len(texto)%3==i%3 and i!=0):
		saida = saida + "."
	saida = saida + texto[i]
	i = i + 1
print(saida)
		
#one = texto[:3]
#two = texto[3:6]
#three = texto[-3:]
#final = str(one)+"."+str(two)+"."+str(three)
#print(final)