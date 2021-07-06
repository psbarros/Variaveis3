x = int(input("senha"))
a = (x//100000)
b = (x//10000)%10
c = (x//1000)%10
d = (x//100)%10
e = (x//10)%10
f = (x%10)
if ((b+d+f)%(a+c+e) == 0):
	print("acesso liberado")
else:
	print("senha invalida")