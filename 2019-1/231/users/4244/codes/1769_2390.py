from numpy import*
p = array(eval(input()))
f = array(eval(input()))

F = p - f
i = 0

while(F[i] != max(F)):
	i = i + 1
print(i + 1)
			 
