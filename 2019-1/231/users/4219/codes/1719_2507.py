qi = int(input(""))
pc = float(input(""))
max = 8000
mes = 0
while 0 <qi <= max :
	qv = int(input(""))
	qi = qi + qi*(pc/100) - qv 
	mes = mes + 1
if qi>= max :
	print("MAXIMO")
else :
	print("ZERO")
print(mes)