from numpy import *
a = float(input("Digite a aceleracao do carro: "))
v0 = float(input("Digite a velocidade inicial do carro: "))
n = int(input("Digite um numero inteiro: "))
i = 0
t = arange(n)
d = zeros(n)
while(i<size(d)):
	d[i] = (a*(t[i]**2)/2) + v0*t[i]
	i = i + 1
print(d)