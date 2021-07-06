a = int(input(""))
n = 0 #acumuladora
soma = 0 #contadora
while( a > n ):
	soma = soma + (4*((-1)**n)/(2*n+1))
	n = n + 1
print(round(soma,8))