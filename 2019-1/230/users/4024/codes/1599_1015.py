# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
n1 = int(input("numero 1"))
n2= int(input("numero2"))
n3= int(input("numero3"))

print(min(n1,n2,n3), (n1+n2+n3)-min(n1,n2,n3)-max(n1,n2,n3)  ,max(n1,n2,n3))