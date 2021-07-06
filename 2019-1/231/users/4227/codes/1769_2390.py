from numpy import*
p = array(eval(input("")))
f = array(eval(input("")))
k = (p-f)
i = 0 
a = 1
while (i < size(k) and k[i] != max(k)):
		 a = a + 1 
		 i = i + 1
print(a)