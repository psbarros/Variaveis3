from numpy import*
from numpy.linalg import*

u = int(input("unidades:"))
f = int(input("funcionarios:"))
#funL = array(eval(input("lista funcionarios:")))

mat = zeros((u,f),dtype=int)

for i in range(u):
	funL = array(eval(input()))
	mat[i,:] = funL
	
	
	
	#for j in range(u):
		#funL = array(eval(input("lista funcionarisos:")))
	#	mat[i,:] = funL[i]
	#	mat[j,:] = funL[j]
		
print(mat)
print(u*f)
