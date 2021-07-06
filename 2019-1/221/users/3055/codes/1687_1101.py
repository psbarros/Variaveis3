# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
consumo = float(input("Consumo de energia: "))
instalacao = input("Tipo de instalcao: ").upper()

print("Entradas:",consumo,"kWh e tipo",instalacao)

if(consumo >= 0 and (instalacao == "R" or instalacao == "C" or instalacao == "I")):
	if(consumo <= 500 and instalacao == "R"):
		total = consumo * 0.44
		print("Valor total: R$",total)
	elif(consumo > 500 and instalacao == "R"):
		total = consumo * 0.65
		print("Valor total: R$",total)
	elif(consumo <=1000 and instalacao == "C"):
		total = consumo * 0.55
		print("Valor total: R$",total)
	elif(consumo > 1000 and instalacao == "C"):
		total = consumo * 0.60
		print("Valor total: R$",total)
	elif(consumo <= 5000 and instalacao == "I"):
		total = consumo * 0.55
		print("Valor total: R$",total)
	elif(consumo > 5000 and instalacao == "I"):
		total = consumo * 0.60		
		print("Valor total: R$",total)
else:
	print("Dasos invalidos")


	

			
	
	