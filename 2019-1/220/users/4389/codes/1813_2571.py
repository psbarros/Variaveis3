from numpy import*

nome = input("Informe a string: \n")
aux = ""
print(len(nome))
for i in range(len(nome)):
	if(nome[i] != 'a' or nome[i] != 'A'):
		nome[i] = 
print(aux)
	maior = max(imc)
if(maior<17):
	print("muito abaixo do peso")
elif(maior>17 and maior<18.49):
	print("abaixo do peso")
elif(maior>18.5 and maior<24.99):
	print("peso normal")
elif(maior>25 and maior<29.99):
	print("acima do peso")
elif(maior>30 and maior<34.99):
	print("obesidade")
elif(maior>35 and maior<39.99):
	print("obesidade severa")
elif(maior>40):
	print("obesidade morbida")