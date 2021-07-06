from numpy import*
from numpy.linalg import*

m = array(eval(input()))
n = shape(m)[0] 
v = zeros(n, dtype=int)

for i in range(n):
	v[i] = sum(m[i,:])
	
print(v)