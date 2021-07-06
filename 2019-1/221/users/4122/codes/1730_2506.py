Q=int(input("Qual a quantidade de tambaquis::"))
Pc=float(input("Porcentagem de crescimento::"))
R=int(input("Quantos sao retirados por ano"))
P=Pc/100
t=0
c=0
while(Q>0)and(Q<12000):
	c=Q*P
	Q=Q+c-R
	t=t+1
if(Q<0):
	print("EXTINCAO")
	print(t)
else:
	print("LIMITE")
	print(t)