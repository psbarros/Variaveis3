from numpy import*
mtr = array(eval(input("Matriz quadrado:")))
l = shape(mtr)[0]
c = shape(mtr)[1]
sm = 0
dnmd = 0
for i in range(l):
	for j in range(c):
		if (i + j) != (l - 1):
			sm = sm + mtr[i,j]
			dnmd = dnmd + 1
rslt = sm/dnmd
print(round(rslt,2))