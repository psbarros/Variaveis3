vv = float(input())
com = (vv * 0.05)
rest = (vv * 0.15)
 
if (vv <= 1.00000):
	print(round(vv - com, 2))
else:
	print(round(vv - rest, 2))