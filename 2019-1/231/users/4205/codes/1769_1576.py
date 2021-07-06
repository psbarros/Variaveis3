from numpy import*
eusapia = array(eval(input("Eusapia:")))
barsanulfo = array(eval(input("Barsanulfo:")))

tamanho = size(eusapia)
print(tamanho)		

contador = 0 
v_eusa = 0
v_bars = 0

while( contador < tamanho ):
	if(eusapia[contador] == 11 and barsanulfo[contador] == 22):
		v_bars = v_bars + 1
	elif(eusapia[contador] == 11 and barsanulfo[contador] == 33):
		v_eusa = v_eusa + 1
	elif(eusapia[contador] == 22 and barsanulfo[contador] == 11):	
		v_eusa = v_eusa + 1
	elif(eusapia[contador] == 22 and barsanulfo[contador] == 33):
		v_bars = v_bars + 1	
	elif(eusapia[contador] == 33 and barsanulfo[contador] == 11):
		v_bars = v_bars + 1	
	elif(eusapia[contador] == 33 and barsanulfo[contador] == 22):
		v_eusa = v_eusa + 1
	contador = contador + 1
if(v_eusa > v_bars):
	print("EUSAPIA")
elif(v_eusa < v_bars):
	print("BARSANULFO")
else:
	print("EMPATE")


	
