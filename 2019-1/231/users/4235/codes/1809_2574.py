from numpy import *
s = input("senha: ")
x = 0
for i in s:
	if((i.isupper()==True) and len(i)>=8):
		x = x+1
	elif(i.islower()==True):
		x = x+1
if(x==0):
	print("SENHA INVALIDA")
else:
	print("SENHA VALIDA")
	

