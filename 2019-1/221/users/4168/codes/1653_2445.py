escala = input (" C ou F:")
T = float(input("temperatura:"))

if (escala.upper() == "C"):
	F = float((9 * T + 160)/ 5)
	print(F)
else: 
	C = (5/9*(T-32))
	print(C)
	