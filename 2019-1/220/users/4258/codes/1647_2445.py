escala = input("Escolha C para Celsius, ou F para Fahrenheit: ")
temp = float(input("Temperatura: "))

c = (5/9)*(temp - 32)
f = ((9/5)*temp) + 32

if(escala == "C"):
	print(f)
	
if(escala == "F"):
	print(c)