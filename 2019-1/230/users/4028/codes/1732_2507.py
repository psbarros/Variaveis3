# Entradas inicias

qnp = int(input("quantidade inicial de pirarucus:"))
qmp = float(input("quantidade percentual mensal:"))


# variaveis de laço

n = 0


while ( qnp > 0) and (qnp < 8000):
	qnv = int(input("quantidade inicial retirado para vendas:"))
	qnp = qnp + (qmp/100)*qnp
	qnp = qnp - qnv
	n = n + 1
	
# saidas do codigo

if ( qnp <= 0 ):
	print("ZERO")
	print(n)
if ( qnp >= 8000):
	print("MAXIMO")
	print(n)
	
	