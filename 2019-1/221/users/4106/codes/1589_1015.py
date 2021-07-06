# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
a= int(input("Qual a ordem:"))
b= int(input("Qual a ordem:"))
c= int(input("Qual a ordem:"))
print (min(a,b,c))
print ((a+b+c)-min(a,b,c)-max(a,b,c))
print (max(a,b,c))