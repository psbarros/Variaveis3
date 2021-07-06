from math import*

k= int(input("Digite os termos: "))

i= 1 
soma= 3

while(i < k):
	soma= soma + ((4) / (2*i * (2*i+1) * (2*i+2)))*((-1)**(i+1))
	i= i+1
print(round(soma,8))
