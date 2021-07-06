from math import *
x = eval(input())
k = eval(input())
cosh = 1
n = 0
for i in range(0,k-1):
	n = n + 2
	cosh = cosh + (x**n)/factorial(n)
	
print(round(cosh,8))