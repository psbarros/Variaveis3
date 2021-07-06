from numpy import*

vet = array(eval(input("notas finais: ")))

while (size(vet) > 1):
   aprov = 0
   for elemento in vet:
      if (elemento >= 5 and elemento < 7):
         aprov = aprov + 1
			
   print(aprov)

   vet = array(eval(input("Proximas notas: ")))