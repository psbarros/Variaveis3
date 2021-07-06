x=int(input("um numereo n:"))
pi=0
k=1
s=1
while(k<=x):
	pi=pi+(4*s/(k*2-1))
	s=s*(-1)
	k=k+1
print(round(pi,8))