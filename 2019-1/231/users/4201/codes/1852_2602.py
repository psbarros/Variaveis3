from numpy import *
from numpy.linalg import *

alimentos = array([[2 ,1  ,4], 
					  [ 1, 2 ,0  ], 
					  [2, 3  ,2 ]])
vet = array(eval(input(" vetor: ")))
vet = vet.T
total = dot(inv(alimentos), vet.T)

print("estafilococo: ", round(total[0], 1))
print("salmonela: ", round(total[1], 1))
print("coli: ", round(total[2], 1))

if (total[0]==min(total)):
	print("estafilococo")
elif (total[1]==min(total)):
	print("salmonela")
else:
	print("coli")