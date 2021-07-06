# Ao testar sua solução, não se limite ao caso de exemplo.
x=float(input('coordenada x: '))
y=float(input('coordenada y: '))

if(x==y==0):
	print('origem')
elif(x<0) or (x>0):
	print('Eixo X')
elif(y<0) or (y>0):
	print('Eixo Y')
