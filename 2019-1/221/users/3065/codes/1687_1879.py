# Ao testar sua solução, não se limite ao caso de exemplo.
e = float(input("e: "))
f =  float(input("f: "))
H = e - (1/4*f)
print(e ,"extras e", f ,"de falta")
if(H>400):
	valor = 500.0
	valor = round(valor,2)
elif(H<=400):
	valor = 100.0
	valor = round(valor,2)
print("R$", valor)