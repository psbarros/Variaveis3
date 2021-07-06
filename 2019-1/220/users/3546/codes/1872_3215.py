from numpy import *

matriculas = array(eval(input()), dtype=int)

aux = zeros( (size(matriculas), 2) ,dtype=int)
for i in range(size(matriculas)):
	faltas = int(input())
	aux[i,0] = matriculas[i]
	aux[i,1] = faltas

max_faltas = max(aux[:,1])
print(aux)
for i in range(size(matriculas)):
	if aux[i,1] == max_faltas:
		print("O aluno que possui o maior numero de faltas e o", aux[i,0])