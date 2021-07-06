# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
a = float(input())
b = input()
print("Entradas:",a,"kWh e tipo",b.upper())
if (b.upper()=="R" and a<=500 and a>=0):
		print("Valor total: R$",round(a*0.44,2))
elif(b.upper()=="R" and a>500):
		   print("Valor total: R$",round(a*0.65,2))
elif(b.upper()=="C" and a<=1000 and a>=0):
			print("Valor total: R$",round(a*0.55,2))
elif(b.upper()=="C" and a>1000):
			print("Valor total: R$",round(a*0.6,2))
elif(b.upper()=="I" and a<=5000 and a>=0):
			print("Valor total: R$",round(a*0.55,2))
elif(b.upper()=="I" and a>1000):
			print("Valor total: R$",round(a*0.6,2))
else:
		print("Dados invalidos")
			
	
