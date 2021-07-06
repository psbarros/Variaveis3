A = int(input("num de hab da cidade A:"))
B = int(input("num de hab da cidade B:"))
percA = float(input(""))
percB =float(input(""))


t= 0 #CONTADORa

while(A < B):
	A = A + A * (percA/100)
	B = B + B * (percB/100)
	t = t + 1
	
print(t)