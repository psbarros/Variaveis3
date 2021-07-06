from math import*
qi = float(input("Ponha o valor inicial: "))
r = float(input("Ponha a taxa anual: "))
qf = 3*qi
y = (1/r)*(log(qf) - log(qi) )

print(int(y)+1)

