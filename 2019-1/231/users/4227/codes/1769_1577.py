from numpy import*
a = float(input(""))
v = float(input(""))
n = int(input(""))
t = arange(n, dtype=int)
d = zeros(n)
i = 0 
while (i < size(t)):
	d[i] = ((a*(t[i]**2))/2)+v*t[i]
	i = i + 1
print(d)

	