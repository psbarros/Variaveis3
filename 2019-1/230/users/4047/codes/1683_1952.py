sal = float(input("Salario bruto: R$ "))

if (sal <= 1659.38):
	sal -= 0.08*sal
if (sal >= 1659.38) and (sal <= 2765.66):
	sal -= 0.09*sal
if (sal >= 2765.67) and (sal <= 5531.31):
	sal -= 0.11*sal
if (sal > 5531.31):
	sal -= 608.44
	
if (sal >= 1903.99) and (sal <= 2826.65):
	sal -= 0.075*sal
if (sal >= 2826.66) and (sal <= 3751.05):
	sal -= 0.15*sal
if (sal >= 3751.06) and (sal <= 4664.68):
	sal -= 0.225*sal
if (sal > 4664.68):
	sal -= 0.275*sal
	
print("Salario liquido = R$", round(sal,2))
	