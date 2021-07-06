from numpy import *
vetor = array(eval(input("Digite os elementos do vetor: ")))
sentinela=0
while(sentinela<size(vetor)):
	if((vetor[sentinela]%2)!=0):
		vetor[sentinela]=0
	sentinela=sentinela+1
print(vetor)