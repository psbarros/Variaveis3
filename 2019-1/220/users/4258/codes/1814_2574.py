from numpy import *

sen = input("Senha: ")
p = 0
q = 0
	
for i in range(0, len(sen)):
	if(sen[i].islower()):
		p = p + 1
	elif(sen[i].isupper()):
		q = q + 1
		
if (q >= 1 and p >= 1 and (len(sen) >= 8)):
	 print ("SENHA VALIDA")
elif(q < 1 or p < 1 or len(sen) < 8):
	 print ("SENHA INVALIDA")