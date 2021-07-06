n = int(input())

divisores = 0
denominador = 1

while (n > denominador):
	if(n%denominador == 0):
		divisores = divisores + 1
denominador = denominador + 1	
if(divisores == 1):
	print("1 divisor")
else:
	print(divisores, "divisores")
		