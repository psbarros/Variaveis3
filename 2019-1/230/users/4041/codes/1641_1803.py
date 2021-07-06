numero = int(input("insira os digitos mortais: "))

milhar = (numero//1000)
centena = (numero//100)-(10*(numero//1000))
dezena = (numero//10)-(10*(numero//100))
unidade = (numero%10)
a = milhar*5
b = centena*4
c = dezena*3
d = unidade*2
digito_verificador = (a+b+c+d)%11
print(digito_verificador)