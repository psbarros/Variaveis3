import math

r = float(input("raio: "))
alt = float(input("altura: "))
op = int(input("(1.) Calcular valume de ar ou (2) Calcular valume do combuativel: "))

v_esf = (4*math.pi * r**3) / 3
v_calot = ((math.pi * alt**2) * (3*r - alt)) / 3

if (op == 1):
	print(round(v_calot, 4))
if (op == 2):
	print(round(v_esf - v_calot, 4))
