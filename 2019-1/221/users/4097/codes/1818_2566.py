from numpy import*
v = array(eval(input("v: ")))
t = size(v)
s = zeros(6, dtype = float)
for x in v:
	s[x - 2] = s[x - 2] + 1
s = (s*100)/t
print(around(s, 1))