n = int(input("Digite o numero de termos: "))
nt = 2
pi = 4
if (n == 1):
	pi = pi
while(nt <= n):
	t = (4 * (-(-1)**(nt))) /(2*nt -1)
	pi = pi + t
	nt = nt + 1
print(round(pi,8))