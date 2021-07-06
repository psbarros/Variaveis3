from numpy import*

# Leitura do primeiro vetor
vet = array(eval(input("Primeiro vetor: ")))
media = 0

if(size(vet) == 1):
	print(vet)
else:	
# Verifica se o programa vai terminar
	while (size(vet) > 1):
  	 # Zera contador de elementos pares
    
  	 # Conta quantidade de elementos pares
  	 for elemento in vet:
   	   if (elemento % 2 == 0):
    	      npar = npar + 1
				n = n + 1
			else:
				nimpar = nimpar + 1
				n = n + 1
   # No. de elementos pares
print(npar)

   # No. de elementos impares
print(nimpar)

   # No. total de elementos
print(n)

   # Leitura do proximo vetor
   vet = array(eval(input("Proximo vetor: ")))
