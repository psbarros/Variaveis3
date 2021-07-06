from numpy import *
from numpy.linalg import *

# Entries

mi = array(eval(input("Insert desired matrix:")))

# Definitions

i,j = shape(mi)
base = zeros((i,j), dtype=int)

# Processing

for j in range(j):
	for i in range(i):
		base[i,j] += mi[i,j]
	base[:,j] = sorted(mi[:,j], reverse=True)				 
print(base)
	