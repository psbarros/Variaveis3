from numpy import*
vp = array(eval(input()))
vc = array(eval(input()))
v = zeros(3, dtype=int)
i = 0
while(i<size(vp)):
	if(vp[i]>vc[i]):
		v[0]=v[0]+1
		
	elif(vp[i]==vc[i]):
		v[1]=v[1]+1
			
	else:
		v[2]=v[2]+1
	i = i + 1
print(v)
			