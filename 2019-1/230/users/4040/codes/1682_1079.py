from math import *

a = float(input ("Lado 1: "))
b = float(input ("Lado 2: "))
c = float(input ("Lado 3: "))

print("Entradas:", a, ",", b, ",", c)

if((a > 0) and (b > 0) and (c > 0)):
	if((a + b > c) and (a + c > b) and (b + c > a)):
		s = (a + b + c) / 2.0
		area = sqrt(s * (s-a) * (s-b) * (s-c))
		area = round(area, 3)
		print("Area: ", area)
	else:
		print("Area: invalida")
else:
	print("Area: invalida")
