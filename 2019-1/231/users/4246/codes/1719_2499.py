from math import *
k = int(input()) #1
i = 0    #contador
e = 1   #acumulador (soma)

while(i < k):
	e = e + 1/factorial(i)
	i = i + 1
print(round(e, 8))