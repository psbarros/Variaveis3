from numpy import*
v = array(eval(input()))
i = 0
c = 0			 
while i<size(v):
	if v[i]>99:
		c = c+1
		print(i)
		
	i = i+1
print(c)			 
	
	