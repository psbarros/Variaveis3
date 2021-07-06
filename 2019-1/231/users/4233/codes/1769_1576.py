from numpy import*

v1 = array(eval(input("Digite o numero: ")))
v2 = array(eval(input("Digite o numero: ")))

tamanho = size(v1)

i = 0
e = 0 
b = 0

while(i<tamanho):
	
	if(v1[i]==11 and v2[i]==33):
		e = e + 1
	elif(v1[i]==11 and v2[i]==22):
		b = b + 1
	elif(v1[i]==11 and v2[i]==11) or (v1[i]==22 and v2[i]==22) or (v1[i]==33 and v2[i]==33):
		e = e + 0
		b = b + 0
	elif(v1[i]==22 and v2[i]==11):
		e = e + 1
	elif(v1[i]==22 and v2[i]==33):
		b = b + 1
	elif(v1[i]==33 and v2[i]==22):
		e = e + 1
	elif(v1[i]==33 and v2[i]==11):
		b = b + 1
	i = i + 1
	
if(e>b):
	mensagem = "EUSAPIA"
elif(b>e):
	mensagem = "BARSANULFO"
else:
	mensagem = "EMPATE"
	
print(tamanho)
print(mensagem)
		
	
		