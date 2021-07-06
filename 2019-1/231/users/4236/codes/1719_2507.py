Qi = int(input(""))
pc = float(input(""))
max = 8000
mes = 0
while 0 < Qi <= max:
	Qv = int(input(""))
	Qi = Qi + Qi*(pc/100) - Qv
	mes = mes + 1
if Qi >= max:
	print("MAXIMO")
else:
	print("ZERO")
print(mes)