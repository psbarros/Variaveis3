from math import*
x = float(input("Digite um numero: "))
e=1
t=1
while(t<x):
	e = e + (1/factorial(t))
	t=t+1
print(round(e,8))