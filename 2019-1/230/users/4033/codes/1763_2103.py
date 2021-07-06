from numpy import*

A=array(eval(input("Digite A: ")))
B=array(eval(input("Digite B: ")))

b=sorted(B,reverse=True)


ta=size(A)
tb=size(B)

i=0
while(i<size(A) and tb==ta):
	if(A[i]>b[i] and A[i]>=0 and b[i]>=0):
		print(A[i])
	else:
		print(b[i])
	i=i+1