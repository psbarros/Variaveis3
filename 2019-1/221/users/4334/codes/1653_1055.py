# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import*
Vo=float(input("velocidade inicial em m/s: "))
ang=float(input("angulo em graus: "))
D=float(input("distancia em metros: "))
#g=gravidade em m/(s*2)
g=9.8
R=(Vo**2)*sin(radians(2*ang))/g
abs(D-R)
if(abs(D-R)<= 0.1):
	mensagem="sim"
else:
	mensagem="nao"
print(mensagem)