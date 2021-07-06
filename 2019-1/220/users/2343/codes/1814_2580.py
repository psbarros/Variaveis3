N = int(input())
lista = []
for i in range(N):
	lista.append(input())
for i in range(N):
	palavra = lista[i]
	saida = ''
	repete =1
	letra_anterior = ''
	letra_diferentes = ''
	for c in palavra:
		if(letra_anterior == c):
			if(letra_diferentes!=''):
				letra_diferentes = letra_diferentes.replace(c,'')
				saida += '1'+letra_diferentes+'1'
				letra_diferentes = ''
			repete += 1
		elif(letra_anterior != ''):
			if(repete > 1):
				saida += '{}{}'.format(repete,letra_anterior)
				repete = 1
			elif(letra_anterior == '1'):
				letra_diferentes += '1'
			letra_diferentes += c
		else:
				letra_diferentes += c
		letra_anterior = c
	if(letra_diferentes!=''):
		saida += '1'+letra_diferentes+'1'
	elif(repete > 1):
		saida += '{}{}'.format(repete,letra_anterior)
	print(saida)
			