peso = float(input("peso: "))

if(peso <= 4999.9):
	frete = peso * 0.05
else:
	frete = (peso * 0.04) + 60

print(round(frete, 2))