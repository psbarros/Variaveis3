# Ao testar sua solução, não se limite ao caso de exemplo.
hE = float(input())
hP = float(input())
print(hE, "extras e ", hP, " de falta")

h = hE - 0.25 * hP
if(h <= 400):
 	 print("R$ 100.0")
else:
 	 print("R$ 500.0")