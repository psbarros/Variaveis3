from numpy import*
from numpy.linalg import*
m1 = array([[1, -1, 0, 0], [0, 1, -1, 0], [0, 0, 1, 0], [1, 0, 0, 1]])

m2 = array([50, -120, 350, 870])
res = dot(inv(m1), m2.T)

print(res)