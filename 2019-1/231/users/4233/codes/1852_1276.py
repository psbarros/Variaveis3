from numpy import*
from numpy.linalg import*

matriz = array(eval(input("Vetor de horas: ")))

vet = zeros(7,dtype=int)

for i in range(7):
	vet[i] = sum(matriz[:,i])
	
for i in range(7):
	if(vet[i]==max(vet)):
		print(i+1)