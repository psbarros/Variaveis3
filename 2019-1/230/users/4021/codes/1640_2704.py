n=float(input("nota do aluno"))
msg=input("bonificacao (s/n)")
bon=n*10/100
if(msg.upper()=="S"):
	tt=n+bon
	print("nota final",tt)
else:
	print(n)