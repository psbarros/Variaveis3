from numpy import*

vec = array(eval(input("Digite numeros inteiros: ")))

i = 0
while (i < size(vec)):
	if (vec[i]%2 != 0):
		vec[i] = 0
	i += 1
print(vec)