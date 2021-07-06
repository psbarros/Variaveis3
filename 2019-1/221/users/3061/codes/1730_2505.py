from math import*
x = eval(input())
k = int(input())
s = 0
i = 0
while i<k:
	if (-pi<=x<=pi):
		i=i+1
		s = s + ((-1)**(i+1))*((x)**(2*i-1))*(1/factorial(2*i-1))
print(round(s,10))