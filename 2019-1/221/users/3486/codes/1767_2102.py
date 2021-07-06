from numpy import*
n = array(eval(input('digite qnt de pos do vetor:')))
i = 0
a = 0
while(size(n) > i):
	if(n[i]%2==0):
		n[i] = n[i]
	else:
		n[i] = n[i] - n[i]
	i = i + 1
print(n)