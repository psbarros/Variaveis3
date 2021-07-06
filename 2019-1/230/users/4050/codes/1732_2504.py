A = int(input("Digite a quantidades de habitantes de A: "))
B = int(input("Digite a quantidades de habitantes de B: "))
pA = float(input("Taxa de crescimento a "))
pB = float(input("Taxa de crescimento de b "))

anos = 0 
while (B < A*2 ):
	A = A + (pA/100)*A
	B = B + (pB/100)*B
	
	anos = anos + 1
print(anos)