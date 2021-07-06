import math
t1= math.radians(float(input("-3.130601")))
g1= math.radians(float(input("-60.02306")))
t2= math.radians(float(input("-3.083550")))
g2= math.radians(float(input("-60.027781")))
R=6371.01
d= R*math.acos((math.sin(t1)*math.sin(t2))+(math.cos(t1)*math.cos(t2)*math.cos(g1-g2)))
print(round(d, 2))

