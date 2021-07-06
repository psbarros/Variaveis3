from numpy import *
from numpy.linalg import *
A = array([[1, -1, 0, 0], 
			  [0, 1, -1, 0],
			  [0, 0, 1, 0], 
			  [1, 0, 0, 1]])
B = array([50,-120,350,870])
B = B.T
pinga = dot(inv(A),B)
print(pinga)