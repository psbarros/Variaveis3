s = (float(input("Digite uma senha de 1 a 6 digitos: ")))
d1 = s // 100000
a  = s %  100000
d2 = a // 10000
b  = a %  10000
d3 = b // 1000
c  = b %  1000
d4 = c // 100
d  = c %  100
d5 = d // 10
e  = d %  10
d6 = e // 1
f  = e %  1

w = (d2 + d4 + d6)
x = (d1 + d3 + d5)
y = w // x
z = w % x 

if (z == 0):
	mensagem = " acesso liberado "
	print(mensagem)
else:
	mensagem = " senha invalida "
	print(mensagem)