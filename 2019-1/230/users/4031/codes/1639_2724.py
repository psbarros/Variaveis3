a = int(input("numero a: "))
b = int(input("numero b: "))
c = int(input("numero c: "))
if (a < b):
	if (a < c):
		menor = a
if (b < a):
	if (b < c):
		menor = b
if (c < a):
	if (c < b):
		menor = c
if (a > b):
	if (a > c):
		maior = a
if (b > a):
	if (b > c):
		maior = b
if (c > a):
	if (c > b):
		maior = c
print((a + b + c) - (menor + maior))