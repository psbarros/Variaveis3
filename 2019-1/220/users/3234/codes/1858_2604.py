from numpy import *
from numpy.linalg import *
mat = array(eval(input("Ficha de pagamento: ")))
fun = shape(mat)[0]
total = zeros(fun, dtype = int)

for i in range(fun):
	m = max(mat[i,:])
	print(m)
