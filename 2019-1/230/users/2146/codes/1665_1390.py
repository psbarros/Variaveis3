consumo = float(input())

if(consumo <= 100):
	x = consumo * 1.2
	
if(consumo > 100):
	x = 25 + (consumo * 1.4)
	
print(round(x, 2))