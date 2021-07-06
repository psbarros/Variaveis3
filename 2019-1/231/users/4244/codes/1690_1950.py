#Velocidade em km/h temperatura em celsius para determinar sigma
temperatura = float(input("Temperatura em celsius: "))
velocidade = int(input("Velocidade em km/h: "))

if(temperatura >= -50 and temperatura <= 10 and velocidade > 4.8):
	sigma =  13.12 + (0.6215*temperatura) - ((11.37)*(velocidade**0.16)) + ((0.3965*temperatura)*(velocidade**0.16))
	print(round(sigma, 4))
elif(velocidade < 4.8):
	print("Velocidade invalida")
else:
	print("Temperatura invalida")