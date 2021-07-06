# codeCheck = 'CodeCheckTeste.txt'
# ArquivoListaAlunos = 'ListaAlunosTeste.txt'
# ConcatenacaoAlunoExercicio = 'ListaAlunosExercicios.txt'

codeCheck = 'CodeCheck.txt'
ArquivoListaAlunos = 'ListaAlunos.txt'
ConcatenacaoAlunoExercicio = 'ListaAlunosExerciciosTotal.txt'

manipulador = open(ArquivoListaAlunos,'r')
alunos_list = manipulador.readlines()

manipulador2 = open(codeCheck, 'r')
exercicio_list =  manipulador2.readlines()

print(alunos_list)
print(exercicio_list)

concat_list = []

for i in range(len(alunos_list)):
    aluno = alunos_list[i].rstrip()
    exercicio = exercicio_list[i].rstrip()

    concat = "{}_{}\n".format(aluno,exercicio)

    concat_list.append(concat)

print(concat_list)

manipulador3 = open(ConcatenacaoAlunoExercicio,'w')
manipulador3.writelines(concat_list)
