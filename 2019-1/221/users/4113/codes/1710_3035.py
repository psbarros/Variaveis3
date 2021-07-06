from math import *
x=input()
if(x<=0 and x>90) or (x<=180 and x<270):
	print(sin(x))
elif(x<=90 and x<180) or (x<=270 and x<360):
	print(cos(x))
else:
	print("entrada invalida")