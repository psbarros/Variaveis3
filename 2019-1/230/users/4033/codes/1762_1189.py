txt=input("frase: ")

txt1=txt.upper()
txt1=txt1.replace("txt1","txt1")
print(txt1)

txt2=""
q=0

while(q<len(txt)):
	txt2=txt2+txt1[-1-q]
	q=q+1
if(txt2==txt1):
	print("1")
else:
	print("0")