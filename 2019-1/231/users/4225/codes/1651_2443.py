from math import*

r = float(input( ))
x = float(input( ))
n = int(input( ))

ve = ((4*pi*(r**3))/3) - (((pi*x**2)*(3*r-x))/3)

vc = ((pi*x**2)*(3*r-x))/3

if (n == 1):
	print(round(vc, 4))
else:
	print(round(ve, 4))