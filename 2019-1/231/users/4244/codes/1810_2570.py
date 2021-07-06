from numpy import*
from math import*

#Vetor e médias dos elementos
x = array(eval(input("Digite numeros reais: ")))

#Tamanho do vetor
n = size(x)

#Media do vetor
m = sum(x)/n

#Variavel acumuladora
p = 1

#Mod

#Laco de repeticao for
for i in range(n):
	p = p*abs(x[i]-m)**(1/n)
print(round(p, 3))