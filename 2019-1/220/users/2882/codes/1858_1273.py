from numpy import*
from numpy.linalg import*

vetor1=array([[1,-1,0,0],[0,1,-1,0],[0,0,1,0],[1,0,0,1]])
vetor=array([50,-120,350,870])
vetor=vetor.T

vetor3=solve((vetor1),vetor)


print(array((vetor3.T)))