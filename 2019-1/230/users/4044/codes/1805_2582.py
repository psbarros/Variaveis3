from math import*

x = float(input("Angulo em graus: "))
k = int(input("Quantidade de termos na serie: "))

soma = 0
for i in range(k):
	soma += ((x)**(2*i)) / (factorial(2*i))
print(round(soma, 8))