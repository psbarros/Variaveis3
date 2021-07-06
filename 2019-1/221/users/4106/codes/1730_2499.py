from math import*
num=int(input("Digite o numero: "))
e=0
a=0
while(a< num):
	e=e+(1/factorial(a))
	a=a+1
print(round(e,8))