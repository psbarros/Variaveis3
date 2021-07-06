from numpy import*
from numpy.linalg import*

un = int(input('quantidade de unidades: '))
f = int(input('quantidade de funcionarios: '))
m = zeros([un,f], dtype=int)
i = 0
for i in range(un):
	l = array(eval(input('')))
	m[i] = l
print(m)
print(size(m))
	
	
