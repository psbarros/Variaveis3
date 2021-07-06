from numpy import *
notas = array(eval(input("Notas dos alunos: ")))
pre = array(eval(input("Presenca dos alunos: ")))
carga = int(input("Carga horaria: "))
freq = carga*0.75

saida = zeros(3, dtype=int)

for i in range(size(notas)):
	if (pre[i] < freq):
		saida[2] = saida[2] + 1
	elif (notas[i] < 5):
		saida[1] = saida[1] + 1
	else:
		saida[0] = saida[0] + 1
print(saida)