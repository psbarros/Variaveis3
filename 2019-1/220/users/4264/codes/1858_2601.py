from numpy import *
from numpy.linalg import *
qtd=array([[3, 12, 1], [12, 0, 2], [0, 2, 3]])
preco=array([23.60, 52.60, 27.70])
preco=preco.T
solucao=solve(qtd, preco)
print(solucao)