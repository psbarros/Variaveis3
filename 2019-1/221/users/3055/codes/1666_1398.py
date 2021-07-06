t = int(input("Tempo de voo: "))
if(0 < t <= 200):
	custo_total = 5000 + (100 * t)
else: 
	custo_total = 8000 + (100 * 200) + 90 * (t - 200)
print(round(custo_total, 2))