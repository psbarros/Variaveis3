import numpy as np

mat = eval(input())
hor = []
for i in mat:
	hor.append(sum(i))
hor = np.array(hor)
print(hor)