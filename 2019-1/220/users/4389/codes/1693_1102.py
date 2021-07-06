# Teste todas as possibilidades de entradas 'H', 'h' e 'x'
# Se seu programa funciona para apenas um caso de tese, isso não quer dizer que ele vai funcionar para todos os outros
# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
from math import*
tanque = float(input("informe o valor da altura do tanque:\n "))
combustivel = float(input("informe o nivel de combustivel no tanque:\n "))
r = float(input("informe o valor do raio dos bojos:\n "))
mil = 1000
if(tanque == 0) or (combustivel==0) or (r==0) or (tanque<=2*r):
	print("Entradas:", tanque,",",combustivel,",",r)
	print("Entradas invalidas")
	
elif(combustivel<=r):
	volume = (pi/3) * (combustivel**2) * (3*r - combustivel)
	
	print("Entradas:", tanque,",",combustivel,",",r)
	print("Volume:", round(volume*1000,3), "litros")

elif(combustivel>r) and (combustivel<=tanque-r):
	volume = (((4/3)*pi*(r**3))/2) +(pi*(r**2)*(combustivel-r))
 
	print("Entradas:", tanque,",",combustivel,",",r)
	print("Volume:", round(volume*1000,3), "litros")
								 
elif(combustivel>tanque-r):
	volume = ((4/3)*pi*(r**3))/2 + pi*(r**2)*(combustivel-r)	- ((pi/3)*((tanque - combustivel)**2)*(3*r - (tanque  -  combustivel)))				
	
	print("Entradas:", tanque,",",combustivel,",",r)
	print("Volume:", round(volume*1000,3), "litros")							 
					