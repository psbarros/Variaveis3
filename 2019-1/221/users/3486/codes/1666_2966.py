x = input('escreva S para mulheres e N para homens:')
p = float(input('preco do ingresso:'))
q = int(input('quantidade de ingressos:'))

if(x == 'S'):
	a = (p*0.80)*q
	print(round(a,2))
else:
	a = p*q
	print(round(a, 2))
