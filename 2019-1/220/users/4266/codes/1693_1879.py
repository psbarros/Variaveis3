# Ao testar sua solução, não se limite ao caso de exemplo.
extras = float(input("Digite o numero de horas extras: "))
faltou = float(input("Digite o numero de horas que faltou: "))
h = extras - ((1/4)*faltou)
if (h>400):
	g = 500.0
else:
	g = 100.0
print(extras, " extras e ", faltou, " de falta")
print("R$ ",g)



