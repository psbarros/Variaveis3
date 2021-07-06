from numpy import*
vet = array(eval(input("insira as medias: ")))

while (size(vet) > 1):
	aprov = 0
	for i in vet:
		if(i>=5 and i<7):
			aprov = aprov + 1
	print(aprov)
	vet = array(eval(input("Proximo vetor: ")))
		