from numpy import*
v = array(eval(input("v: ")))
vs = array([y for y in v if(y > 0)])
print(vs)