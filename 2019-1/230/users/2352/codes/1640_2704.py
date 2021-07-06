nota = float(input("qual eh a nota do aluno? "))
mensagem = input("o aluno vai receber a bonificacao? ")

if(mensagem.upper() == "S"):
	n = nota + (nota * 0.1)
else:
	n = nota
print(n)