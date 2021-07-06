from math import *

k = int(input())

e = 0

while(k > 0 ):
	k -= 1
	e += 1/factorial(k)
	
	
print(round(e, 8))