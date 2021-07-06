from numpy.linalg import *
from numpy import *

qua = array(eval(input("Matriz: ")))

bac_ali = array([[2,1,4],[1,2,0],[2,3,2]])

qua = qua.T
r=  dot(inv(bac_ali), qua)


print("estafilococo: ", round(r[0],1))
print("salmonela: ", round(r[1],1))
print("coli: ", round(r[2],1))

if(min(r) == r[0]):
	print("estafilococo")
elif(min(r) == r[1]):
	print("salmonela")
elif(min(r)== r[2]):
	print("coli")