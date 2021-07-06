# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
con=float(input(":"))
tipo=input("R/I/C").upper()
print("Entradas:", con, "kWh", "e tipo", tipo)
if(tipo=="R"):
	if(con<0):
		print("Dados invalidos")
	elif(con<=500):
		t=round((con*0.44), 2)
		print("Valor total: R$", t)
	else:
		t=round((con*0.65), 2)
		print("Valor total: R$", t)
elif(tipo=="I" ):
	if(con<0):
		print("Dados invalidos")
	elif(con<=5000):
		t=round((con*0.55), 2)
		print("Valor total: R$", t)
	else:
		t=round((con*0.60), 2)
		print("Valor total: R$", t)
elif(tipo=="C"):
	if(con<0):
		print("Dados invalidos")
	elif(con<=1000):
		t=round((con*0.55), 2)
		print("Valor total: R$", t)
	else:
		t=round((con*0.60), 2)
		print("Valor total: R$", t)
else:
	print("Dados invalidos")