senha=int(input("senha:"))
d1=senha//100
d2=senha//10%10
d3=senha%10
if((d1+d3)%d2!=0):
	print("senha  invalida")
else:
	print("acesso liberado")
	