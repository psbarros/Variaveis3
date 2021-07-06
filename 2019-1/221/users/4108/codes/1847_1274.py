from numpy import*
from numpy.linalg import*

N = eval(input("Digite N: "))
matriz = zeros((N,N),dtype = int)
n = 0
for i in range (N):
	for j in range (N):
		if (i == j):
			matriz[i,j] = n + 1
			n = n + 1
		elif (i < j):
			matriz [i,j] = i + 1
		else:
			matriz[i,j] = j + 1
print(matriz)
		