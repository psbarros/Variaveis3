from numpy import *
v = eval(input("Numero: "))
i=0
x=0
a=0
while(i != v):
	a = '*' * v
	print(a+'o'*x + a) 
	v=v-1
	x=x+2