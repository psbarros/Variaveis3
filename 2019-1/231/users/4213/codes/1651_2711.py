a=float(input("Dinheiro disponvel: "))
b=int(input("Tickets desejados: "))
c=float(input("preco dos tickets: "))
d=int(input("quantidade de passes: "))
e=float(input("valor dos passes: "))
if(a >= (b*c+d*e)):
	print("SUFICIENTE")
else:
	print("INSUFICIENTE")