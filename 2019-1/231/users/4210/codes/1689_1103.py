x = float(input("Insira x:"))
a = float(input("Insira a:"))
b = float(input("Insira b:"))

if (b<=a):
	print("Entradas",a,"e",b,"invalidas")
elif(b>a) and (x<=b) and (a<=x):
	print(x,"pertence ao intervalo",a,",",b)
else:
	print(x,"nao pertence ao intervalo",a,",",b)