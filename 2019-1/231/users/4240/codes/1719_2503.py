N=int(input())
i=0
soma=0
sinal=+1
while(i<N):
	soma=soma+sinal*4/(2*i+1)
	sinal=-sinal
	i=i+1
	
print(round(soma,8))