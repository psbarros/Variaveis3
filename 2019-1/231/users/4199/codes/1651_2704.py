nota= float(input("nota"))
opcao=input("bonificacao? (S/N)")
if(opcao.upper()=="S"):
	print(float(nota+nota*0.1))
if(opcao.upper()=="N"):
	print(float(nota))