lim =  int(input("Digite um limite: "))

a = ''
i = 0

while i < lim:
	for x in range(0,lim):
		a = (lim - i) * '*' + (2*i) * 'o' + (lim - i) * '*'
		print(a)
		i += 1