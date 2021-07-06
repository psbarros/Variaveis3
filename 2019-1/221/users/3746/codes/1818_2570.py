from numpy import *

x = array(eval(input("Digite uma sequencia: ")))

m = sum(x)/size(x)
desvio = 1

for i in arange(size(x)):
	desvio *= abs(x[i] - m)
	
p = ( desvio ) ** (1/len(x))
print(round(p,3))