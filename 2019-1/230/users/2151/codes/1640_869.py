# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código

r = float(input(":"))

p = (r * 5) / 100

if ( r >= 200):
	m = r - p 
else:
	m = r
	
print(round( m , 2 ))
	