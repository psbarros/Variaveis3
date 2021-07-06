import math
t1=math.radians(float(input("Qual a latitude 1?")))
g1=math.radians(float(input("Qual a longitude 1?")))
t2=math.radians(float(input("Qual a latitude 2?")))
g2=math.radians(float(input("Qual a longitude 2?")))
R=6371.01
d=R*math.acos((math.sin(t1)*math.sin(t2))+(math.cos(t1)*math.cos(t2)*math.cos(g1-g2)))
print(round(d, 2))