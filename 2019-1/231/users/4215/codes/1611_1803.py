x=int(input("Informe um numero de quatro digitos: "))
numero_um=x//1000
x=x%1000
numero_dois=x//100
x=x%100
numero_tres=x//10
x=x%10
numero_quatro=x//1
numero_verificador=(numero_um*5+numero_dois*4+numero_tres*3+numero_quatro*2)%11
print(numero_verificador)