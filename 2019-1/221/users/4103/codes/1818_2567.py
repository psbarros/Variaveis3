from numpy import *
x = int(input("Valor a ser inserido: "))

a = "*"*x

for i in range(x):
	print(a)
	a = a[:-1]
	
a = "*"
for i in range(x):
	print(a)
	a = a + "*"