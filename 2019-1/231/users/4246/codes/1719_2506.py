Qi = int(input()) #qtd incial de tambaquis
Pc = int(input()) #perc. de cresc. anual
Qf = int(input()) #qtd retirados p/ a venda (anual)
x = 12000
anos = 0

while(Qi > 0) and (x > Qi):
	Qi = Qi*(Pc/100) + Qi - Qf
	anos += 1
if(Qi >= x):
	print('LIMITE')
else:
	print('EXTINCAO')
print(anos)	