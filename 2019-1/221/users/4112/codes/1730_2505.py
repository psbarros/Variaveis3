from math import*
x=eval(input("O angulo  x,medido em raianos:"))
k=int(input("O numero k de termos da serie:"))
soma=0
t=0
i=1
sinal=1
while(t<k):
	soma=soma+(((x)**i/factorial(i))*sinal)
	sinal=sinal*(-1)
	i=i+2
	t=t+1
print(round(soma,10))