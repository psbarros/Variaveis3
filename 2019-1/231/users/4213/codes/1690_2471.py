a=float(input("Idade:"))
b=float(input("IMC:"))
if(a<0 or b<0):
	print("Dados ivalidos")
elif (a<45 and b<22):
	print(a,"anos")
	print(b)
	print("baixo")
elif (a<45 and b>=22):
	print(a+"anos")
	print(b)
	print("medio")
elif (a>=45 and b<22):
	print(a+"anos")
	print(b)
	print("medio")
else:
	print(a+"anos")
	print(b)
	print("alto")