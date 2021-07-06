# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.

print("domingo eh 0, segunda eh 1, terca eh 2, ... sabado eh 6")

h = int(input("dia de hoje eh? "))
f = int (input("dia futuro daqui a quantos dias? "))

#dia presente
if (h > 6 or h < 0):
	print ("A entrada ", h, "eh invalida")
elif (h == 0):
	d1 = "domingo"
elif (h == 1):
	d1 = "segunda"
elif (h == 2):
	d1 = "terca"
elif (h == 3):
	d1 = "quarta"
elif (h == 4):
	d1 = "quinta"
elif (h == 5):
	d1 = "sexta"
elif (h == 6):
	d1 = "sabado"
#dia futuro
	d2 = (f%6)
elif (d2 == 0):
	f2 = "domingo"
elif (d2 == 1):
	f2 = "segunda"
elif (d2 == 2):
	f2 = "terca"
elif (d2 == 3):
	f2 = "quarta"
elif (d2 == 4):
	f2 = "quinta"
elif (d2 == 5):
	f2 = "sexta"
elif (d2 == 6):
	f2 = "sabado"
	print ("Hoje eh ", d1, " e o dia futuro eh ", f2)
else:
	print ("A entrada ", h," eh invalida")