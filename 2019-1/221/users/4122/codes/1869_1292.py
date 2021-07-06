from numpy import*
from numpy.linalg import*
mina=array([[8,3,1],[5,12,10],[1,3,2]])
peso=array(eval(input("Quanto de peso: ")))
T=mina.T
resultado=dot(inv(mina),peso)
a=round(resultado[0],0)
e=round(resultado[1],0)
s=round(resultado[2],0)
print("ametista:",a)
print("esmeralda:",e)
print("safira:",s)

resul_tado=around(resultado,0)

if(a==max(resul_tado)):
	print("ametista")
elif(e==max(resul_tado)):
	print("esmeralda")
else:
	print("safira")