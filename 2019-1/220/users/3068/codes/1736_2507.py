qi = int(input("Quantidade inicial de pirarucus:"))
pc = int(input("Percentual de crescimento:"))/100
prc = qi
m = 0
while(prc>0 and prc<8000):
	vm = int(input("Quantidade de venda deste mes:"))
	prc = prc + prc*pc - vm
	m = m + 1
if(prc<=0):
	print("ZERO")
elif(prc>=8000):
	print("MAXIMO")
print(m)