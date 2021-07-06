nota = float(input("digite o valor: "))
boni = input("recebe ou nao: ")
		  
notatual = nota + (10/100)*nota

if(boni == "S"):
	print(notatual)
else:
	print(nota)