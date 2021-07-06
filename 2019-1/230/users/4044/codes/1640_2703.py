#--------------------------------------------
# Universidade Federal do Amazonas
# Instituto de Ciências Exatas
# Departamento de Física
#
# Micael Davi Lima de Oliveira - 21851626
# Data: 12/04/2019
#
# Questão 2: Descobrir via programação e pelo
#            uso de estruturas condicionais se
#            conforme a idade digitada, a
#            pessoa é tida como eleitor obriga-
#            tório ou não.         
#---------------------------------------------

# Nesta parte, tem-se como dado de entrada a idade
# da pessoa, onde o valor é do tipo inteiro.

idade = int(input("1. Digite a sua idade: "))

# Aqui, entra a estrutura condicional. Caso a pessoa
# tenha uma idade igual ou superior a 18 anos, uma
# variável auxiliar(sit_eleitoral) receberá um dado
# correspondente à condição verdadeira.

# Se a pessoa tiver 18 anos ou mais, a varíavel 
# auxiliar recebe como dado: (eleitor)

# Caso contrário, isto é, se a pessoa tiver menos
# que 18 anos, a variável auxiliar recebe como
# dado: (nao_eleitor)

if (idade >= 18):
	sit_eleitoral = "eleitor"
else:
	sit_eleitoral = "nao_eleitor"

# Por último, é impresso ao usuário o valor da
# variável (sit_eleitoral)

print(sit_eleitoral)