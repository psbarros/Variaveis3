num=int(input("digite o numero de termos: "))
i=0
soma = 0

while( i<num ):
	soma += ((1) / ((2*i + 1) * (3**i)))*((-1)**(i))
	i = i + 1
soma = (12**(1/2))*soma
print(round(soma, 8))