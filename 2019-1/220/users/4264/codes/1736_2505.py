from math import *
x=eval(input())
k=int(input())
if(x >= -pi and x <= pi):
	senx=0
	i=1
	sinal=-1
while(i<=k):
	senx=senx*sinal+x**(2**i+1)/factorial(2**i+1)
	#sinal=-sinal
	i=i+1
print(round(senx, 10))
	