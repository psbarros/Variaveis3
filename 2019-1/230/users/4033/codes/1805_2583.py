from numpy import*

inf=array(eval(input("Digite um limite inferior: ")))
sub=array(eval(input("Digite um limite superior: ")))

for i in range(inf,sub+1):
	if(i%6==0):
		print(i)