from numpy import*
from numpy.linalg import*

N=array(eval(input("Digite as horas semanais de cada funcionario: ")))
linha=shape(N)[0]
coluna=shape(N)[1]

horas=zeros(linha,dtype=int)


for i in range(linha):
	if(coluna==7):
		soma=sum(N[i,:])
		horas[i]=soma
print(horas)