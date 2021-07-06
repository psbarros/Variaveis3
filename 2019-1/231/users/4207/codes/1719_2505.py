from math import*

x = eval(input("Digite o angulo em RAD: "))
k = int(input("Digite o numero de termos: "))

soma = 0
i = 0
n = 1

while(i<k):
	soma = soma + (-1)**i*(x**n/factorial(n))
	n = n + 2
	i = i + 1
	
print(round(soma, 10))