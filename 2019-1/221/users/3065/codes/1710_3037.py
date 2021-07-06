x = float(input("x: "))
if(x < -1)or(x > 1):
	x = x**2
elif(((x > -1) and (x < 0))or((0 < x)and(x < 1))):
	x = x
elif(x == 0):
	x = 1
print(x)	