num=int(input("num:"))
from math import*
#valor aproximado dessa série para a soma dos seus k primeiros termos
e=1
cont=1
while ( cont!= num ) :
	e=e+(1/factorial(cont))
	cont=cont+1
print(round(e,8))