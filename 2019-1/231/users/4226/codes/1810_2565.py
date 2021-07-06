from numpy import *

med = array(eval(input("medias da turma: ")))
fqc = array(eval(input("frequencia da turma: ")))
cgh = int(input("carga horaria da disciplina: "))

apv = 0
rpv_n = 0
rpv_f = 0


#for media in med a: freq in fqc:
for media,freq in med,fqc:
	if (media >= 5 and (freq / cgh) <= 0.7499):
		rpv_f = rpv_f + 1
	elif (media <= 4.9999 and freq / cgh >= 0.7500):
		rpv_n = rpv_n + 1
	else:
		apv = apv + 1

res = [apv, rpv_n, rpv_f]

print(res)
