a= float(input("a: "))
b= float(input("b: "))
c= float(input("c: "))
d= float(input("d: "))
e= float(input("e: "))
f= float(input("f: "))

if (a*e-b*d==0):
	print("Nao tem solucao")
	
else:
	x=(c*e-b*f)/(a*e-b*d)
	y=(a*f-c*d)/(a*e-b*d)
	print(x)
	print(y)