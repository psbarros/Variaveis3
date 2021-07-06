entrada = int(input("metade dos asteriscos iniciais: "))
ast = '*'
vogal= 'o'
p=0
for i in range(entrada):
	print((entrada*ast+p*vogal+entrada*ast))
	entrada = entrada - 1
	p=p+2