# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
ce = float(input("insira: "))
x = input("insira: ")
print("Entradas: " ,ce , "kWh e tipo" ,x)

if ((ce<0) or (x!="R") and (x!="") and (x!="I")) :
	print("Dados invalidos")
elif ((x=="R") and (ce==500)) :
	conta = 0.44*ce
	print("Valor total: R$ ", round(conta, 2))
elif ((x=="R") and (ce>500)) :
	conta = 0.65*ce
	print("Valor total: R$ ", round(conta, 2))
elif ((x=="C") and (ce==1000)) :
	conta = 0.55*ce
	print("Valor total: R$ ",round(conta, 2))
elif ((x=="C") and (ce>1000)) :
	conta = 0.60*ce
	print("Valor total: R$ ", round(conta, 2))
elif ((x=="I") and (ce==5000)):
	conta = 0.55*ce
	print("Valor total: R$ ", round(conta, 2))
elif ((x=="I") and (ce>5000)):
	conta = 0.60*ce
	print("Valor total: R$ ", round(conta, 2))
	