d=int(input("Qual o dia? "))

if((d>=0 and d<=6)):
	j=int(input("Quantos dias? "))
	dl=(d + j) % 7
	if (d==0):
		d = "domingo"
	elif (d==1):
		d = "segunda"
	elif (d==2):
		d = "terca"
	elif (d==3):
		d = "quarta"
	elif (d==4):
		d = "quinta"
	elif (d==5):
		d = "sexta"
	else:
		d="sabado"
	if (dl == 0):
		dl="domingo"
	elif (dl == 1):
		dl="segunda"
	elif (dl == 2):
		dl="terca"
	elif (dl == 3):
		dl="quarta"
	elif (dl == 4):
		dl="quinta"
	elif (dl == 5):
		dl="sexta"
	else:
		dl="sabado"
	print("Hoje eh", d, "e o dia futuro eh", dl)
else:
	print("A entrada", d, "eh invalida")