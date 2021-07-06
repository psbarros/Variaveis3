senha=int(input(""))
n1=(senha%1000000)//100000
n2=(senha%100000)//10000
n3=(senha%10000)//1000
n4=(senha%1000)//100
n5=(senha%100)//10
n6=(senha%10)

x1=n2+n4+n6
x2=n1+n3+n5

if(x1%x2==0):
	print("acesso liberado")
else:
	print("senha invalida") 