from numpy import *
from numpy.linalg import *

matriz = array(eval(input(":")))

mat = zeros(matriz.shape[0] , dtype = int)

for i in range(matriz.shape[0]):
	mat[i] = sum(matriz[i,:])
print(mat)
	