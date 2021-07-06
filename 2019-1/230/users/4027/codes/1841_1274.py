from numpy import *
from numpy.linalg import *
n = int(input("Numero natural n: "))
z = zeros ((n,n), dtype = int)
for i in range(n):
	for j in range(n):
		if(i>j):
			z[i,j] = j + 1
		else:
			z[i,j] = i + 1
print(z)