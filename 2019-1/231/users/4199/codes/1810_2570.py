from numpy import*
from math import*
x = array(eval(input()))
m =  sum(x)/size(x)
v = 1
for i in range(size(x)):
	v = v * abs(x[i]-m)**(1/size(x))
print(round(v,3))