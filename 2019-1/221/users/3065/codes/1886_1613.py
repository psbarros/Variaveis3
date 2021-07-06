from numpy import *
from numpy.linalg import *
at = array(eval(input("at: ")))
dm = array(eval(input("dm: ")))
a = 0
for i in at :
	if(i == "ALONGAMENTO"):
		a = a + 3.0
	elif(i == "CORRIDA"):
		a = a + 10.3
	elif(i == "DANCA"):
		a = a + 6.7
	elif(i == "ESCALADA"):
		a = a + 9.7
	elif(i == "HIDROGINASTICA"):
		a = a + 5.0
	i = i + 1
total =  a * sum(dm)
print(around(total,2))