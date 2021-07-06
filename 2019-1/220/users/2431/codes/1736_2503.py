n = int(input("No. de termos: "))
soma = 0
i = 0
c = 1

while (i < n):
	soma = soma + ((-1) ** i) * (4 / c)
	i = i + 1
	c = c + 2
print(round(soma, 8))