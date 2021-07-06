# Ao testar sua solução, não se limite ao caso de exemplo.

from math import *

# Leitura dos lados do triangulo a, b, and c
a = float(input ("Lado 1: "))
b = float(input ("Lado 2: "))
c = float(input ("Lado 3: "))

print("Entradas:", a, ",", b, ",", c)

# Testa se pelo menos uma das entradas eh negativa 
if (a <= 0 or b <= 0 or c <= 0):
	Area = "invalida"
	print ("Area: ", Area)
elif (a <= c+b or b <= a+c or c <= a+b ):
		s = (a + b + c) / 2.0
		area = sqrt(s * (s-a) * (s-b) * (s-c))
		Area = round(area, 3)
elif (Area >= 0):
		print("Area: ", Area)
else:
		Area = "invalida"
		print ("Area: ", Area)
