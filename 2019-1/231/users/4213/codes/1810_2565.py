from numpy import *
a=array(eval(input("Medias finais:")))
b=array(eval(input("Presencas:")))
c=float(input("Carga horaria:"))
d=zeros(3,dtype=int)
for i in range (size(a)):
	if((a[i]>=5)and (b[i]/c>=0.75)):
		d[0]=d[0]+1
	elif (a[i]<5):
		d[1]=d[1]+1
	elif (b[i]/c<0.75):
		d[2]=d[2]+1
print(d)