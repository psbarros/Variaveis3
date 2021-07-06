V=int(input("Quantidade inicial de copias do virus no sangue de Micaleteia::"))
L=int(input("Quantidade inicial de leucocitos no sangue::"))
PV=int(input("Percentual de multiplicacao diaria do virus::"))
PL=int(input("Percentual de multiplicacao diaria dos leucocitos::"))
PA1=PV/100
PA2=PL/100
t=0
while(2*V>L):
	a=V*PA1
	b=L*PA2
	V=V+a
	L=L+b
	t=t+1
print(t)