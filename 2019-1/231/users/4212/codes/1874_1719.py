from numpy import *

notas = array(eval(input("Matriz de notas: ")))
qp = 0
nedia = 0.0

for i in range(shape(notas)[0]):
	nedia = sum(notas[i:])/shape(notas)[1]
	if(nedia > pas):
		qp = qp + 1
	nedia = 0
	
print(qp)
#end ..-. --- ...     - -. -.-.