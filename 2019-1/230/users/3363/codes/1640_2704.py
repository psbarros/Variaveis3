nota = float(input("Digite a respectiva nota do aluno: "))
bonus = input("Voce deseja que o aluno receba a bonificacao(S/N): ")

if (bonus == "S"):
	nota = nota + 0.1*nota
	
print(round(nota, 1))