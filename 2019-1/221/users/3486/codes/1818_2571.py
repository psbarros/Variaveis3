from numpy import*
x = input('Frase: ')
y = "aA"
for i in range(0,len(y)):
	x =x.replace(y[i],"")
print(x)
