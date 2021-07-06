ha = int(input("Quantidade inicial de habitantes cidade A: "))
hb = int(input("Quantidade inicial de habitantes cidade B: "))
pca = float(input("Percentual de crescimento cidade A: "))
pcb = float(input("Percentual de crescimento cidad B: "))

pca = pca/100
pcb = pcb/100
ano = 0
while(ha < hb):
	ca = ha * pca
	ha = ha + ca
	cb = hb * pcb
	hb = hb + cb
	ano = ano + 1
print(ano)
	

	
	