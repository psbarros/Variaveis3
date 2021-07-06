x=int(input("Valor de PI: "))
a=1
b=3
c=2

while(a < x):
	if(a%2==0):
		b= b-(4/(c*(c+1)*(c+2)))
	elif(a%2==1):
		b= b+(4/(c*(c+1)*(c+2)))
	a=a+1
	c= c+2
print(round(b, 8))