from numpy import *
from numpy.linalg import *

n = int(input( ))

m = zeros((n,n), dtype=int)

for i in range(0,n):
	for j in range(0,n):
		m[i,j] = min(i,j)+1
print(m)