# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
hoje = int(input())
dpf = int(input())
if((hoje<0) or (hoje>6)):
	print("A entrada",hoje, "eh invalida")
else:
	if(hoje==0):
		da = "domingo"
	elif(hoje==1):
		da = "segunda"
	elif(hoje==2):
		da = "terca"
	elif(hoje==3):
		da = "quarta"
	elif(hoje==4):
		da = "quinta"
	elif(hoje==5):
		da= "sexta"
	elif(hoje==6):
		da= "sabado"
		
		futuro=(hoje + dpf)%7
		if(futuro==0):
			df="domingo"
		elif(futuro==1):
			df = "segunda"
		elif(futuro==2):
			df = "terca"
		elif( futuro==3):
			df= "quarta"
		elif( futuro == 4):
			df = "quinta"
		elif( futuro == 5):
			df = "sexta"
		elif( futuro == 6):
			df= "sabado"
		print("Hoje eh",da,"e o dia futuro eh",df)