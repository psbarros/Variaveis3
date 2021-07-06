
n = int(input("numero natural: "))
ct = 3
nt = 1
np = 3
while(nt < n):
	if(nt%2==0):
		np = np - (4/((ct-1)*(ct)*(ct+1)))
	else:
		np = np + (4/((ct-1)*(ct)*(ct+1)))
	ct = ct + 2
	nt = nt + 1
	
print(round(np, 8))