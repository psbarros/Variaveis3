from numpy import*
gli = array(eval(input("")))
i = 0
k = 0
while (i < size(gli)):
	if (gli[i] > 99):
		k = k + 1
		print(i)
	i = i + 1 
print(k)