from numpy import *
from numpy.linalg import *

quant = array(eval(input("Quantidade: ")))
# Matriz do sistema linear (informado no enunciado)
alimento = array([[2 , 1 , 4], [ 1, 2 ,0 ], [ 2, 3 , 2 ]])

# Vetor de constantes (informado no enunciado)

quant = quant.T
q = dot(inv(alimento),quant)

# Imprime o preco de cada fruta
print("estafilococo: ", round(q[0], 1))
print("salmonela: ", round(q[1], 1))
print("coli: ", round(q[2], 1))

# Imprime nome da fruta mais cara
if q[0] == min(q):
    print("estafilococo")
elif q[1] == min(q):
    print("salmonela")
else:
    print("coli")
