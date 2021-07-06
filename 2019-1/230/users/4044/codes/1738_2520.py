from math import*

k = int(input("Digite a quantidade de termos da Formula de Euler: "))

soma = 0
i = 0

while (i < k):
	soma += ((1)/((i+1)**2))
	i += 1
	
soma = sqrt(soma*6)
print("%.6f" %soma)