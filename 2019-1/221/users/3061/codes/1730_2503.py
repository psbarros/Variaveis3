n = int(input())
s = 0 
i = 0 
while i<=n-1:
	s = s + ((-1)**i)*4*(1/(2*i+1))
	i = i+1
print(round(s,8))	