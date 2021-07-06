from numpy import*
x = array(eval(input('Numeros: ')))
i = 0 # Indice
o = 0 # Ocorrencias

while(len(x)>i):	#tamanho dos valores de ver sao maiores que o indice
	if(x[i] > 99): #comparação para ver se os valores de x sao maiores que 99
		o += 1
		print(i)
	i += 1
print(o)