from numpy import *
from numpy.linalg import *

#QNTD DE ALIMENTO COLOCADA NO TUBO DE ENSAIO
a = array(eval(input( )))
a = a.T #linha transposta em coluna

#MATRIZ DA QNTD DE ALIMENTO CONSUMIDO
c = array([[2,1,4] , [1,2,0] , [2,3,2]])

#RESOLUCAO DO SISTEMA
p = dot(inv(c), a)

#QUANTAS BACTERIAS DE CADA TIPO EXISTEM EM CADA TUBO
print("estafilococo: ", round(p[0], 1))
print("salmonela: ", round(p[1], 1))
print("coli: ", round(p[2], 1))

#BACTERIA COM MENOR POPULACAO
if p[0] == min(p):
	print("estafilococo")
elif p[1] == min(p):
	print("salmonela")
else:
	print("coli")