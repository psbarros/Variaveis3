#O tanque de tambaquis
# Quantidade inicial de peixes
quant=int(input("Quantidade de peixes inicial: "))
# Percentual de crescimento da população de peixes
pq=float(input("Aumento de: "))
#Quantidade de peixes retirados
menos=int(input("Peixes retirados: "))
# Variável contadora
t=0
# Variável acumuladora
w=0
while(quant>0 and quant<12000):
	t+=1
	w=quant*(pq/100)
	quant=(quant+w)-menos
if(quant>=12000):
	print("LIMITE")
else:
	print("EXTINCAO")
print(t)