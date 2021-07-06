from numpy import*

p = array(eval(input("Digite o vetor peso: ")))
h = array(eval(input("Digite o vetor altura: ")))
t=0
i=0
imc = zeros(size(p), dtype=float)
for n in p:
	t=p[i]/(h[i]**2)
	imc[i]=round(t,2)
	i=i+1
	
maior = max(imc)
sit =0
if (maior<17):
	sit = ("MUITO ABAIXO DO PESO")
elif(maior>=17) and (maior<=18.49):
	sit = ("ABAIXO DO PESO")
elif(maior>=18.5) and (maior<=24.99):
	sit = ("PESO NORMAL")
elif(maior>=25) and (maior<=29.99):
	sit = ("ACIMA DO PESO")
elif(maior>=30) and (maior<=34.99):
	sit = ("OBESIDADE")
elif(maior>=35) and (maior<=39.99):
	sit = ("OBESIDADE SEVERA")
elif(maior>=40):
	sit = ("OBESIDADE MORBIDA")

print(imc)
print("O MAIOR IMC DA TURMA EH: ",round(maior,2))
print(sit)


