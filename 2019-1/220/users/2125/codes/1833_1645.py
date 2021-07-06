from numpy import*
v=array(eval(input("Valores de v: ")))
w=0#Acumuladora de saques que ultrapassou 2 mil
t=0
#ac=zeros(size(v), dtype)
while(size(v)>t):
	if(v[t]>=2000):# Numeros de saques maiores que 2 mil
		w+=1
	t+=1
ac=zeros(w, dtype=int)
print(w)#Primeira parte
#print(ac)
t=0
w=0
while(size(v)>t):
	if(v[t]>=2000):
		ac[w]=ac[w]+t
		w+=1
	t+=1
print(ac)