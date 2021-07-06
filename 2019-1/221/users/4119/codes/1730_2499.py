import math 
k = int(input("digite um numero: "))
e = 0
cont = 0
while (cont < k):
	e = e + 1/math.factorial(cont)
	cont = cont + 1
print (round(e,8))