ent=input()
ent=ent.replace(" ","").upper()
ent2=""
for i in ent:
	ent2=i+ent2
cont=0

print(ent)
saida=1
while(cont<len(ent)):
	if(ent[cont]!= ent2[cont]):
		saida=0
	cont=cont+1
print(saida)