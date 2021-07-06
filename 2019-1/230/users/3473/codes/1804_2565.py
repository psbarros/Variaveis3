import numpy as np

media = eval(input())
pres = eval(input())
carga = float(input())

apro = 0
repr_n = 0
repr_f = 0

count = 0

while(count < len(media)):
	if(pres[count]/carga < 0.75):
		repr_f = repr_f + 1
	elif(media[count] < 5):
		repr_n = repr_n + 1
	else:
		apro = apro + 1
	count = count + 1

vet = np.array([apro,repr_n,repr_f],dtype = np.int)
print(vet)
	