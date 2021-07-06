from numpy import *

vtb = array(eval(input("Digite o tempo de banho: ")))
vmb = array(eval(input("Digite o modo de banho: ")))

if "QUENTE":
	print((90 * 60) * 0.005)
elif "MORNO":
	print((45 * 60) * 0.005)
elif "FRIO":
   print(round(60 * 0.005, 2)