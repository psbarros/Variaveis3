qi    = float(input("Quantia inicial: R$ "))
tempo = int(input("Tempo de investimento(mes): "))
juros = 4.0
saldo = qi      

t = 1

while (t <= tempo):
	rend = saldo * (juros/100)
	saldo += rend
	t += 1
	
	print(round(saldo, 2))



	
