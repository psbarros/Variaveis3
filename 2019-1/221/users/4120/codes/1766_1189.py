from numpy import *

p = input("Escreva uma palavra: ")

print(p.upper().replace(" ", ""))

if(p.replace(p[0],p[-1]) == p):
	print(1)
else:
	print(0)