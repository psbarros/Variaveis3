k = int(input("Digite um numero inteiro: "))

div = 0
soma = 0

for n in range(1,k+1):
	if k % n != 0:
		continue
	else:
		div += 1
		soma += n
		
		if n !=k:
			print(n)
			

david = soma - k

if david == k:
	print("PERFEITO")
else:
	print("NAO PERFEITO")