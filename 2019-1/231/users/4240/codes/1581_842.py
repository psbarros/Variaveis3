# Teste seu codigo aos poucos.
# Nao teste tudo no final, pois fica mais dificil de identificar erros.
# Nao se intimide com as mensagens de erro. Elas ajudam a corrigir seu codigo.
numero =  int(input("Digite um numero: "))
u= numero%10
d= numero//10%10
c= numero//100%10
m= numero//1000%10
soma= u+d+c+m
print(soma)