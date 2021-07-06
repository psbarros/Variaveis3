# Tanque de combustivel.

from math import*

raio = float(input("digite o raio:"))
altura = float(input("digite a altura:"))
opcao = float(input("digite 1 para volume do ar ou 2 para do combustivel:"))

calota_esferica = ((pi*(altura**2)*(3*raio-altura)))/3
volume_esfera = 4*pi*(raio**3)/3
if (opcao==1):
	v = calota_esferica	
else:
	v = volume_esfera - calota_esferica
	
print(round(v,4))


