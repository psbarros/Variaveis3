from numpy import *
s = input("Digite uma string: ")

n = int((len(s))/3)
vt = zeros(n, dtype=int)
i = 0
p = 0
j = s
 
while(n >= 1):
	vt[i] = j[(p):(p + 3)]
	i = i + 1
	p = p + 3
	n = n - 1

a = 0
b = 0

while(a < size(vt)):
	b = str(b) + "." + str(vt[a])
	a = a + 1
	
c = b[2:]
print(c)