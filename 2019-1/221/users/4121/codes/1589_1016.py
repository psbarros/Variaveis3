# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
a = float(input("lado triangulo"))
b = float(input("lado triangulo"))
c = float(input("lado triangulo"))
s =((a+b+c)/2)
from math import*
A = (sqrt(s*(s-a)*(s-b)*(s-c)))
print(round(A,5))
