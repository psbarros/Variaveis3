n = int(input("numero: "))
fig = n*"*"
fig2 = "*"
for i in range(len(fig)):
	fig = (n-i)*"*"
	print(fig)

for x in range(n):
	print(fig2)
	fig2 = fig2 + "*"