from numpy import*

peso = array(eval(input()))
altura = array(eval(input()))
imc = saida = zeros(size(peso),dtype=float) 
i = 0
while(i < size(peso)):
	imc[i] = round(peso[i]/(altura[i]**2),2)
	i += 1
print(imc)
print('O MAIOR IMC DA TURMA EH: {}'.format(max(imc)))
index = where(imc == max(imc))[0][0]
if(imc[index] < 17):
	print('MUITO ABAIXO DO PESO')
elif(imc[index] >= 17 and imc[index] <= 18.49):
	print('ABAIXO DO PESO')
elif(imc[index] >= 18.5 and imc[index] <= 24.99):
	print('PESO NORMAL')
elif(imc[index] >= 25 and imc[index] <= 29.99):
	print('ACIMA DO PESO')
elif(imc[index] >= 30 and imc[index] <= 34.99):
	print('OBESIDADE')
elif(imc[index] >= 35 and imc[index] <= 39.99):
	print('OBESIDADE SEVERA')
elif(imc[index] >= 40):
	print('OBESIDADE MORBIDA')