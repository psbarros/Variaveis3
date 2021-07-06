from math import *
x = eval(input("O angulo x, medido em radianos:"))
while(x<-pi or x>pi):
	x = eval(input("O Angulo x, medido em radianos:"))
k = int(input("O numero k de termos da serie:"))
t = 1
fe = 3
senx = x
i = -1
#print(round(x,10))
while(t<k):
	senx = x +((x**fe)/factorial(fe))*i
	t = t + 1
	fe = fe + 2
	i = i * (-1)
print(round(senx,10))