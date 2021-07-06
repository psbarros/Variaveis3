from numpy import *
cst = array(eval(input("Custos:")))
ctc = 0
five = 5/100
i = 0
while(i<size(cst)):
	if(cst[i]>80):
		ctc = cst[i] - cst[i]*five + ctc
	else:
		ctc = cst[i] + ctc
	i = i + 1
print(round(ctc,2))