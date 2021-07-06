from math import*
ang=eval(input(":"))
k=int(input(":"))
sen=0
cont=0
while(cont<k):
	sen=sen+((-1)**cont)*(ang**(2*cont+1))/(factorial(2*cont+1))
	cont=cont+1
print(round(sen, 10))