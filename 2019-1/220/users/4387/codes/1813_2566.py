from numpy import*
vetor = array(eval(input("Historico de faltas: ")))
pf = zeros(6,float)
faltas=zeros(6,int)
for i in range(size(vetor)):
   if(vetor[i]==2):
      faltas[0] = faltas[0] + 1
   elif(vetor[i]==3):
      faltas[1] = faltas[1] + 1
   elif(vetor[i]==4):
      faltas[2] = faltas[2] + 1
   elif(vetor[i]==5):
      faltas[3] = faltas[3] + 1
   elif(vetor[i]==6):
      faltas[4] = faltas[4] + 1
   elif(vetor[i]==7):
      faltas[5] = faltas[5] + 1
for n in range (size(faltas)):
   pf[n] = round(faltas[n]*100/size(vetor) ,1) 
print(pf)