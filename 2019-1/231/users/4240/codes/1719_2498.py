a= int(input())
b= int(input())
perca= float(input())
percb=float(input())
ano=0
while(a<b):
	a=a+ (perca/100)*a
	b=b+ (percb/100)*b
	ano=ano+1
	
	
	if(a>=b):
		print(ano)