from numpy import *
from numpy.linalg import *
mat = eval(input("Matriz: "))
x = zeros((shape(mat)[0]),dtype=int)
for i in range(shape(mat)[0]):
	x[i] = sum(mat[i])
print(x)