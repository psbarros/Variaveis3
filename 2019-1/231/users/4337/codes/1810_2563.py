from numpy import*

vet = array(eval(input("media: ")))

while (size(vet) > 1):
	alunos = 0
	for i in vet:
		if (i>= 5 and i< 7):
			alunos = alunos + 1
	print(alunos)
	vet = array(eval(input("media: ")))
	