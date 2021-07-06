# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
a=float(input("numero"))
b=float(input("outro numero"))
c=float(input("mais um numero"))
from math import*
s=((a+b+c)/2)
print(round(sqrt(s*(s-a)*(s-b)*(s-c)),5))