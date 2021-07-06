# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

d = min(a,b,c) 
e = max(a,b,c)
meio = (a + b + c) - d - e

print(d)
print(meio)
print(e)