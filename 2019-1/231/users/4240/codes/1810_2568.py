n = int(input("numero: "))

for i in range(n):
	fig = (n-i)*"*"+i*"o"
	fig2 = i*"o"+(n-i)*"*"
	print(fig+fig2)