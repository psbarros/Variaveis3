from numpy import *
peso = array(eval(input("Informe os pesos: ")))
altura = array(eval(input("Informe as alturas: ")))
imc = zeros(size(peso), dtype = float)

for i in range(size(peso)):
	imc[i] = round(peso[i]/(altura[i]**2),2)

maior = max(imc)
	
for d in range(size(peso)):
	if(maior<17):
		situa = "MUITO ABAIXO DO PESO"
	elif(maior>=17 and maior <=18.49):
		situa = "ABAIXO DO PESO"
	elif(maior>=18.5 and maior <=24.99):
		situa = "PESO NORMAL"
	elif(maior>=25 and maior <=29.99):
		situa = "ACIMA DO PESO"
	elif(maior>=30 and maior <=34.99):
		situa = "OBESIDADE"
	elif(maior>=35 and maior <=39.99):
		situa = "OBESIDADE SEVERA"
	else: 
		situa = "OBESIDADE MORBIDA"

print(imc)
print("O MAIOR IMC DA TURMA EH:",maior)
print(situa)