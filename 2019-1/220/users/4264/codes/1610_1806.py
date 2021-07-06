from math import *
x=int(input("numeros de pessoas:"))
a=factorial(365)
b=factorial(365-x)
c=365**x
p=1-(a/b)*(1/c)
por=p*100
print(round(por, 2))
