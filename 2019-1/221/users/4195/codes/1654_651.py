A = float(input("Digite a Altura: "))
S = input("Para sexo masculino digite M e para o sexo feminino digite F: ")

if (S == "M"):
	pi = (72.7 * A) - 58
else:
	pi = (62.1 * A) - 44.7

print(round(pi, 2))