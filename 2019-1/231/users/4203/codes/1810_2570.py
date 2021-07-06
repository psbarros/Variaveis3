from numpy import*
x = array(eval(input("numeros reais: ")))

m = sum(x)/size(x)
n = size(x)
produto = 1

for i in range(n):
	produto = produto*abs(x[i]-m)

p = produto**(1/n)
print(round(p,3))