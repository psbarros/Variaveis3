from numpy  import*
from numpy.linalg import*

valores = array([[0,2,11,6,15,11,1],[2,0,7,12,4,2,15],[11,7,0,11,8,3,13],[6,12,11,0,10,2,1],[15,4,8,10,0,5,13],[11,2,3,2,5,0,14],[1,15,13,1,13,14,0]])

tempo = 0

var = int(input("Valor: "))
i = (var%10)-1
j = (var%10)-1
while(var!=-1):
	tempo = tempo + valores[i,j]
	
	i = j
	var = int(input("Valor: "))
	j = (var%10-1)

print(tempo)