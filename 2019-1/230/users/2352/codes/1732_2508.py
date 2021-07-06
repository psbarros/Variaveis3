num = int(input("Termo geral: "))

c = 1
a = 3

while(c < num):
	d = (c * 2) * ((c * 2) + 1) * ((c * 2) +2)
	a = a + (-1) ** (c + 1) * (4 / d)
	c = c + 1
	
print(round(a ,8))