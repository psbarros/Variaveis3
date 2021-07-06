v0 = int(input())
l0 = int(input())
pv = float(input())/100
pl = float(input())/100

cont = 0

while(l0 < 2*v0):
	v0 += v0*pv
	l0 += l0*pl
	cont += 1
print(cont)