from numpy import*
alunos=array(eval(input("matriculas:")))

nimpar = 0
i=0
for x in alunos:
	if (x % 2 == 0):
		nimpar=nimpar+0
	else:
		nimpar = nimpar + 1

impar=zeros(nimpar,dtype=int)	
for x in alunos:
	if (x % 2== 0):
		x=x
	else:
		impar[i]=impar[i]+x
		i=i+1
print(impar)