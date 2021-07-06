from numpy import*
v=array(eval(input("v:")))
tamanho=size(v)
i=0
cont=0
num=99
while(i<tamanho):
	if(v[i]>num):
		cont=cont+1
		print(i)
	i=i+1	
print(cont)