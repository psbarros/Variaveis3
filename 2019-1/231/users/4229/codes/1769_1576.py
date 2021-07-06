from numpy import*
vet1 = array(eval(input("Sequencia de jogadas de Eusapia: ")))
vet2 = array(eval(input("Jogadas de Barsanulfo: ")))

stone = 11
paper = 22
scissours = 33

position = 0
wineusapia = 0
winbarsanulfo = 0

vectorsize = size(vet1)

#verificação de todas as posições
while(position<vectorsize):
	if(vet1[position]==paper) and (vet2[position]==stone):
	   wineusapia = wineusapia + 1
	elif(vet1[position]==stone) and (vet2[position]==scissours):
		wineusapia = wineusapia + 1
	elif(vet1[position]==scissours) and (vet2[position]==paper):
		wineusapia = wineusapia + 1
	elif(vet1[position]) == (vet2[position]):
		wineusapia = wineusapia
		winbarsanulfo = winbarsanulfo
	else:
		winbarsanulfo = winbarsanulfo + 1
	position = position + 1
print(position)
if(wineusapia<winbarsanulfo):
	print("BARSANULFO")
elif(wineusapia>winbarsanulfo):
	print("EUSAPIA")
else:
	print("EMPATE")