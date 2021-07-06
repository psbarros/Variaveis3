from math import*
x = int(input())
i = 0
soma = 3

while (i < x):
	soma = soma + i *((-1)**(i-1) * (4 * factorial(2*i + 1) / factorial(2*i + 4)))
	i = i + 1
	
print(round(soma, 8))
	