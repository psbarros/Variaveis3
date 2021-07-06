senha=int(input(":"))
nu1= senha//100000
resto1=senha%100000
nu2=resto1//10000
resto2=resto1%10000
nu3=resto2//1000
resto3=resto2%1000
nu4=resto3//100
resto4=resto3%100
nu5=resto4//10
nu6=resto4%10
if((nu2+nu4+nu6)%(nu1+nu3+nu5)==0):
	me="acesso liberado"
else:
	me="senha invalida"
print(me)