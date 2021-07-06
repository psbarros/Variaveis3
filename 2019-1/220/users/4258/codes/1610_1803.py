numero = int(input("Numero: "))

alg1 = numero//1000
alg2 = numero//100%10
alg3 = numero//10%10
alg4 = numero%10

digito = (alg1*5 + alg2*4 + alg3*3 + alg4*2)%11
print(digito)