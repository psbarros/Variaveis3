# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
nume1= int(input("n1:"))
nume2=int(input("n2:"))
nume3=int(input("n3:"))
inte=((nume1+nume2+nume3)-max(nume1,nume2,nume3))-min(nume1,nume2,nume3)
print(int(min(nume1,nume2,nume3)))
print(int(inte))
print(int(max(nume1,nume2,nume3)))