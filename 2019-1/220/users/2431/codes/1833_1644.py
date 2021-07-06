from numpy import *

nf = array(eval(input()))

count = zeros(3, dtype=int)
i = 0
for i in range (size(nf)):
	if (nf[i] >= 5):
		i = i + 0
		count[0] = count[0] + 1
	elif (nf[i] < 5):
		i = i + 0
		count[1] = count[1] + 1
print(count + 1)

# Essa matéria da me deixando perturbadoooooooooooooooooooooooo, ahhhhhhhhhhhhhhhhhhhh!!!!! :-(
	