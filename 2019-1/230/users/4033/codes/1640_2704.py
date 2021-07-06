nota_aluno = float(input(" nota do aluno: "))
bonus = input("aluno tem nota extra: ")
bonus_aluno = nota_aluno + (10*nota_aluno/100)
if (bonus == "S"):
	print (bonus_aluno)
else:
	print (nota_aluno)
