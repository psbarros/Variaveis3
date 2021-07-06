from math import*
# Entradas inicias
k = int(input("valor do numero aproximado de pi:"))

# variaveis intermediarias

soma = 0

# Saida do programa
while (k > 0):
	soma = soma + (1/k**2)
	k = k - 1
soma = sqrt(6*soma)
print(round(soma, 6))