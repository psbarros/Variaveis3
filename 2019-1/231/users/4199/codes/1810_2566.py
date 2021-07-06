from numpy import*
faltas = array(eval(input()))

cont = zeros(6, dtype = float)
p = zeros(6, dtype = float)

for i in range(size(faltas)):
	if(faltas[i] == 2):
		cont[0] = cont[0] + 1
	elif(faltas[i] == 3):
		cont[1] = cont[1] + 1
	elif(faltas[i] == 4):
		cont[2] = cont[2] + 1
	elif(faltas[i] == 5):
		cont[3] = cont[3] + 1
	elif(faltas[i] == 6):
		cont[4] = cont[4] + 1
	elif(faltas[i] == 7):
		cont[5] = cont[5] + 1
for i in range(size(p)):
	p[i] = round(cont[i]/size(faltas)*100,1)
print(p)