from numpy import*
#Primeiro as entradas
notas=array(eval(input("notas")))
nomes=array(eval(input("nomes")))
#Agora as acumuladoras
t=0    #acumuladora de posicao
p=0    #passou
r=0    #reprovou
f=0    #faltou
n=0    #para somar as notas de quem passou e reprovou
#A quantidade de notas
q=size(notas)
x=max(notas)
#agora o while
while(q!=t):
	if(notas[t]==-1):
		f=f+1
	elif(notas[t]>=6):
		p=p+1
		n=n+notas[t]
	else:
		r=r+1
		n=n+notas[t]
	t=t+1
print(f)
print(p)
print(r)
print(round((n/(p+r)),2))
# Maior nota
i=0
while (notas[i]!=x):
	i = i + 1
print(nomes[i])