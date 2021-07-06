from numpy import * 

vet = array(eval(input(":")))


i = 1
m = vet[0]
while(i< size(vet)):
	m = m * vet[i]
	
	i = i + 1
d = m**(1/size(vet))
print(round(d,2))