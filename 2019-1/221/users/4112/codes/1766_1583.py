N = input("N:")
i = 0
novo_N = ""
while( i < len(N)):
	novo_N = novo_N + N[i: i+3] + "."
	i = i + 3
print(novo_N[:-1])