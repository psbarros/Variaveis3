n = int(input('Coloque um numero inteiro:'))
v = 2*n*'*'
a = ''
i = n
q = 1
print(v)
while a!=2*n*'o':
		a = '*'*(i-1) + 'oo'*q + '*'*(i-1)
		i = i - 1 
		q = q + 1 
		if a!=2*n*'o':
			print(a)
	
