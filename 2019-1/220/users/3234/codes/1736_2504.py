qV = int(input("Qt inicial - Virus: "))
qL = int(input("Qt inicial - Leucocitos: "))
cpV = float(input("Percentual de Crescimento - Virus: "))
cpL = float(input("Percentual de Crescimento - Leucocitos: "))
pcpV = cpV / 100
pcpL = cpL / 100

tV = 0
tL = 0
d = 0

while (qL < (2 * qV)):
	qV = qV + (qV * pcpV)
	qL = qL + (qL * pcpL)
	tV = qV
	tL = qL
	d = d + 1
print(d)