Qit=int(input("Quantidade inicial de tambaquis:"))
Pc=float(input("Percentual de crescimento anual dos tambaquis:"))
Qrt=int(input("Quantidade de tambaquis retirados por anos:"))
a=0
while	(Qit>0) and (Qit<12000):
	Qit=Qit+(Qit*(Pc/100))
	Qit=Qit-Qrt
	a=a+1
if	(Qit<=0):
	print("EXTINCAO")
	print(a)
if	(Qit>=12000):
	print("LIMITE")
	print(a)