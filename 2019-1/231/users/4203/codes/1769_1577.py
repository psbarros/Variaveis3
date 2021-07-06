from numpy import*
a = float(input("aceleracao: "))
v0 = float(input("velocidade: "))
n = int(input("numero: "))

t = arange(n)
d = zeros(n, dtype=int)
dt = (a*t**2)/2 + v0*t
print(dt+d)