from numpy import*
x = array(eval(input("vetor: ")))
n = size(x)
m = sum(x)/n
d = 0
for i in x:
	d = d + (((i - m)**2)/n - 1)**0.5
print(round(d,3))