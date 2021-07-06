from numpy import*
from numpy.linalg import*

#Matriz do exemplo de entrada
matriz = array(eval(input()))

#Vai participar montando as colunas
funcao = shape(matriz)[0]

vet = zeros(funcao, dtype = int)

for i in range(funcao):
	vet[i] = vet[i] + sum(matriz[i,:])
print(vet)