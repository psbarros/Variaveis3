idade = int(input("insira sua idade: "))
imc = float(input("insira sua imc: "))

if(idade<45 and imc<22.0):
	print("Entradas:", idade, "anos e IMC", imc)
	risco = "Baixo"
	print("Risco:", risco)
elif(idade<45 and imc>=22.0):
	print("Entradas:", idade, "anos e IMC", imc)
	risco = "Medio"
	print("Risco:", risco)
elif(idade>=45 and imc<22.0):
	print("Entradas:", idade, "anos e IMC", imc)
	risco = "Medio"
	print("Risco:", risco)
elif(idade>=45 and imc>=22.0):
	print("Entradas:", idade, "anos e IMC", imc)
	risco =  "Alto"
	print("Risco:", risco)
elif(idade<=0 and idade>130 and imc<=0):
	print("Entradas:", idade, "anos e IMC", imc)
	print("Dados invalidos")