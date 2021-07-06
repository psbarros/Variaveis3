# O vírus de Micaleteia.
quantV = int(input("digite a quantidade inicial de virus:"))
quantL = int(input("digite a quantidade inicial de leucocitos:"))
percentV = int(input("digite o percentual diario de virus:"))
percentL = int(input("digite o percentual diario de leucocitos:"))

t = 0
while(quantL<quantV*2):
	quantV=quantV+quantV*(percentV/100)
	quantL=quantL+quantL*(percentL/100)
	t=t+1
print(t)
