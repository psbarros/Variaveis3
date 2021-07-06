from numpy import*
from numpy.linalg import *
mat = array([[0,2,11,6,15,11,1],
				 [2,0,7,12,4,2,15],
				 [11,7,0,11,8,3,13],
				 [6,12,11,0,10,2,1],
				 [15,4,8,10,0,5,13],
				 [11,2,3,2,5,0,14],
				 [1,15,13,1,13,14,0]])
A = eval(input("Cidade A: "))
j= 0
if(A == 111):
	j= 0
elif(A == 222):
	j= 1
elif(A == 333):
	j= 2 
elif(A == 444):
	j= 3
elif(A == 555):
	j= 4
elif(A == 666):
	j= 5
elif(A == 777):
	j= 6
x= 0
while(A != -1):
	i =0
	if(A == 111):
		i =0
	elif(A == 222):
		i =1 
	elif(A == 333):
		i =2 
	elif(A == 444):
		i =3 
	elif(A == 555):
		i =4 
	elif(A == 666):
		i =5
	elif(A == 777):
		i =6
	x = x + mat[i][j]
	j= i
	A = eval(input("Cidade A: "))

print(x)

