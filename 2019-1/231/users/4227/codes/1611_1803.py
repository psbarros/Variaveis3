k= int(input("a"))
a= (k//1000)
b= ((k%1000)//100)
c=((k%100)//10)
d=(k%10)
t= (((d*2)+(c*3)+(b*4)+(a*5))%11) 
print(t)