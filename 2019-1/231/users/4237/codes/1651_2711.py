valor = float(input())
r1 = int(input())
r2 = float(input())
p1 = int(input())
p2 = float(input())

x = (r1*r2) + (p1*p2)
if ( x < valor): 
	print("SUFICIENTE".upper())
else: 
	print("INSUFICIENTE".upper())