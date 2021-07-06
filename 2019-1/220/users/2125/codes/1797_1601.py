from numpy import*
v=array(eval(input("Valor de v: ")))#Vetor
#v=array([45.2,30.25,90.2,150.3,65.5])
t=0
while(size(v)>t):
	if(v[t]==min(v)):#Condição para ser vencedor
		ven=t
	t+=1
print(ven)