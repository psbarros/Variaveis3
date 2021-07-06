dia=int(input(" qual dia eh numero do dia de hoje: "))
futuro=int(input(" qual dia sera o numero do dia na segunda: "))		 

if (dia >= 0) and ( dia <= 6):
	if (dia == 0):
	   k = "Hoje eh domingo"
	elif (dia == 1):
		k = "Hoje eh segunda"
	elif (dia == 2):
		k = "Hoje eh terca"
	elif (dia == 3):
		k = "Hoje eh quarta"
	elif (dia == 4):
		k = "Hoje eh quinta"
	elif (dia == 5):
		k = "Hoje eh sexta"
	elif (dia == 6):
		k = "Hoje eh sabado"
else:
	print("A entrada",dia, "eh invalida")
	
if (futuro>=0)and(dia>=0 and dia<=6):
   
   estimativa = ((futuro%7)+dia)%7
	
   if(estimativa==0):
	   print(k,"e o dia futuro eh domingo")
   elif(estimativa==1):
    	print(k,"e o dia futuro eh segunda")
   elif(estimativa==2):
   	print(k,"e o dia futuro eh terca")
   elif(estimativa==3):
   	print(k,"e o dia futuro eh quarta")
   elif(estimativa==4):
   	print(k,"e o dia futuro eh quinta")
   elif(estimativa==5):
   	print(k,"e o dia futuro eh sexta")
   elif(estimativa==6):
   	print(k,"e o dia futuro eh sabado")	