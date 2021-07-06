from numpy import*
a = float(input("Coloque a aceleracao do carro:"))
v0 = float(input("Coloque a velocidade inicial:"))
n = int(input("Coloque um numero inteiro n:"))
t = arange(n)
d = zeros(n,dtype=float)
i = 0
while i!=n:
	d[i]=a*(t[i]**2)/2 + v0*t[i]
	i = i+1
print(d)
	