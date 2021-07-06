# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import*

consumo=float(input("Consumo: "))
tipo=input("Tipo: ").upper()

print("Entradas:",consumo,"kWh e tipo",tipo)
if((consumo>0) and ((tipo=='R') or (tipo=='C') or (tipo=='I'))):
	if(tipo=='R'):
		if(consumo<=500):
			m=float(round((0.44*consumo),2))
			print("Valor total: R$",m)
		elif(consumo>500):
			m=float(round((0.65*consumo),2))
			print("Valor total: R$",m)
	if(tipo=='C'):
		if(consumo<=1000):
			m=float(round((0.55*consumo),2))
			print("Valor total: R$",m)
		elif(consumo>1000):
			m=float(round((0.60*consumo),2))
			print("Valor total: R$",m)
	if(tipo=='I'):
		if(consumo<=5000):
			m=float(round((0.55*consumo),2))
			print("Valor total: R$",m)
		elif(consumo>5000):
			m=float(round((0.60*consumo),2))
			print("Valor total: R$",m)
else:
	print("Dados invalidos")