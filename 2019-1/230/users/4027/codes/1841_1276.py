from numpy import *
from numpy.linalg import *
tabel = array(eval(input("Insira a tabela de horarios: ")))
n = shape(tabel)[1]
z = zeros(n, dtype = int)
for i in range(n):
	z[i] = sum(tabel[:,i])

for i in range(n):
	if(max(z) == z[i]):
		print(i + 1)

		