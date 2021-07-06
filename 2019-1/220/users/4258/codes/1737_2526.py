n1 = int(input("Numero inteiro 1: "))
n2 = int(input("Numero inteiro 2: "))

i1 = 1
soma1 = 0
i2 = 1
soma2 = 0

while (i1 <= n1):
	if(n1%i1 == 0 and n1 != i1):
		soma1 = soma1 + i1
	i1 = i1 + 1

while (i2 <= n2):
	if(n2%i2 == 0 and n2 != i2):
		soma2 = soma2 + i2
	i2 = i2 + 1
	
print(soma1)
print(soma2)
	
if((soma1 == n2) and (soma2 == n1)):
	print("AMIGOS")
	
else:
	print("NAO AMIGOS")
