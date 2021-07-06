from numpy import*
a = float(input())
vi = float(input())
n = int(input())
t = arange(n)
d = zeros(n)
d = (a*(t**2)/2) + vi*t
print(d)