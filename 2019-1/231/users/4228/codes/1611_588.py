# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Use as mensagens de erro para corrigir seu codigo.
valor = int(input("Valor a ser sacado: "))

n100 = valor // 100
r100 = valor % 100
n50 = r100 // 50
r50 = r100 % 50
n10 = r50 // 10

print (int(n100))
print (int(n50))
print (int(n10))