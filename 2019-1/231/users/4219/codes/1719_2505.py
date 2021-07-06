from math import*
x = eval(input("angulo :"))
k = int(input("insira: "))
i = 0
soma = 0 
while i<k :
	conta = x**((2*i) + 1)/factorial (2*i+1)
	x = -1 *x
	soma = soma + conta
	i = i + 1
print (round(soma, 10))

