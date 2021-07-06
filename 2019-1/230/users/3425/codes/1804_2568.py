base = int(input("valor: "))
x = "*"

print(2*(x*base))

o = "oo"
g = 1
i = 1
t = base
while((i <= base) and (g < base)):
	t = t - 1
	print(x*t + o*g + x*t)
	i = i +1
	g = g +1

