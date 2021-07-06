from numpy import *
from numpy.linalg import *
tab=array(eval(input("Tab:")))
ali=array([[2,1,2],[1,2,3],[4,0,2]])
bac=dot(tab,inv(ali))
print("estafilococo:",round(bac[0],1))
print("salmonela:",round(bac[1],1))
print("coli:",round(bac[2],1))
if bac[0]==min(bac):
	print("estafilococo")
elif bac[1]==min(bac):
	print("salmonela")
elif bac[2]==min(bac):
	print("coli")