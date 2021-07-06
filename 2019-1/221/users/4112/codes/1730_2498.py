CA = int(input("Numero de habitantes de uma cidade A:"))
CB = int(input("Numero de habitantes de uma cidade B:"))
PA = float(input("Percentual de crescimento populacional da cidade A:"))
PB = float(input("Percentual de crescimento populacional da cidade B:"))
t=0

while(CA <= CB):
	CA= CA + (CA* (PA/100))
	CB= CB + (CB* (PB/100))
	t=  t+1
print(t)