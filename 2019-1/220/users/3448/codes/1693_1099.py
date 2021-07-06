a=float(input("lado 1:"))
b=float(input("lado 2:"))
c=float(input("lado 3:"))
if(a>0 and b>0 and c>0):
	if(a==b and b==c):
		x="equilatero"
	elif(a==b and b !=c) or (a==c and c !=b) or (b==c and c !=a):
		x="isosceles"
	elif(a<b+c and b<a+c and c<a+b) and (a !=b and b !=c):
		x="escaleno"
	else:
		x="invalido"
else:
	x="invalido"
print("Entradas:",a,",",b,",",c)
print("Tipo de triangulo:",x)

