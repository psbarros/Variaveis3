from numpy import *
# Vetor contendo o nome dos meses do ano
data = input()
dia = data[0:2]
mes = data[2:4]
ano = data[4:]
vet_mes = array(['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'])
print(dia + ' de ' + vet_mes[int(mes)- 1]+' de ' + ano)