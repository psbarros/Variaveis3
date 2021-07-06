import math
a=float(input("digite o lado a: "))
b=float(input("digite o lado b: "))
c=float(input("digite o lado c: "))
s=(a+b+c)/2
area=math.sqrt(s*(s-a)*(s-b)*(s-c))
print(round(area,5))