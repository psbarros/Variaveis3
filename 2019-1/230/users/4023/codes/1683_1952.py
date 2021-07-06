total=float(input("Digite o respectivo valor do salario bruto: R$"))

if(total <= 1659.38):
	rest= 0.92*total
if(total >= 1659.39) and (total <= 2765.66):
	rest=0.91*total
if(total >= 2765.67) and (total <= 5531.31):
	rest=0.89*total
if(total >= 5531.31):
	rest=total - 608.44
	
if(rest >= 1903.99) and (rest <= 2826.65):
	rest=0.925*rest
if(rest >= 2826.66) and (rest <= 3751.05):
	rest=0.85*rest
if(rest >= 3751.06) and (rest <= 4664.68):
	rest=0.775*rest
if(rest >= 4664.68):
	rest=0.725*rest
	
print("Salario liquido = R$", round(rest,2))