num=int(input('digite os quatro digitos da conta: '))
u= num // 1 % 10
d= num // 10 % 10
c= num // 100 % 10
m= num // 1000 % 10

calculo=((u*2)+(d*3)+(c*4)+(m*5)) % 11
print(calculo)

