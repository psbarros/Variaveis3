t = int(input("Quantidade inicial de tambaquis: "))
p = float(input("Percentual de crescimento anual: "))
q = int(input("Quantidade de tambaquis retirados:"))

at = 0
c = 0

while(12000>=t>=0):
	t = (t + ((p/100)*t) - q)
	at = at + 1
	
	if (t >= 12000):
		print("LIMITE")
	if (t <= 0):
		print("EXTINCAO")
print(at)