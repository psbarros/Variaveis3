from math import*

# Informações iniciais
x = eval(input("Valor do angulo:"))
k = int(input("Quantidade de termos da série:"))

# variavel acumuladora
soma = 0

# variavel contadora
n = 0
# condições finais
while (n < k):
	soma = soma + ((-1)**n)*((x**(2*n+1))/factorial(2*n+1))
	n = n + 1
print(round(soma,10))
