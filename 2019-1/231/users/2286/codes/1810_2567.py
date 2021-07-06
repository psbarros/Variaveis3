from numpy import*
n = int(input(""))
p = ""
s = ""
j = 0
for x in range(n):
	j = n - x
	p = (j)* '*'
	print(p)
for i in range(n):
	s = (i + 1)* '*'
	print(s)