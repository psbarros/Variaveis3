from numpy import *
from numpy.linalg import *

m = array(eval(input()))
y = array([[10,20,30],[50,40,10],[30,10,40]])
n = m.T 
x = dot(inv(y),n)

a = round(x[0],0)
b = round(x[1],0)
c = round(x[2],0)

print("abacate:", a)
print("manga:", b)
print("pera:", c) 

ok = around(x,0)

if ok[0] == min(ok):
	print("abacate")
elif ok[1] == min(ok):
	print("manga")
else:
	print("pera")