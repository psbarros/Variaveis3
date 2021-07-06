# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
x=input()
y=input()

if(x>0 and y>0):
	print("Q1")
elif(x<0 and y>0):
	print("Q2")
elif(x<0 and y<0):
	print("Q3")
elif(x>0 and y<0):
	print("Q4")
elif(x==0 and y!=0):
	print("Eixo Y")
elif(y==0 and x!=0):
	print("Eixo X")
else:
	print("Origem")
