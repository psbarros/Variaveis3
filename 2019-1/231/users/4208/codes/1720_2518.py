n=int(input())
soma=0
while(soma!=1 and n!=0):
resto=n%2
if(resto==0):
	soma=n//2
else:
	soma=(n*3)+1
print(soma)