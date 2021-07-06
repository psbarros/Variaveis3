valor_disponivel=float(input("Digite o seu valor disponivel: "))
qtd_de_tickets_do_ru=int(input("Digite a quantidades de tickets RU desejada: "))
valor_dos_tickets=float(input("Digite o valor dos tickets: "))
qtds_de_passes_de_onibus=int(input("Digite a quantidade de passes de onibus: "))
valor_dos_passes=float(input("Digite o valor dos passes: "))
valor_gasto=(qtd_de_tickets_do_ru*valor_dos_tickets)+(qtds_de_passes_de_onibus*valor_dos_passes)
if (valor_gasto<=valor_disponivel):
	mensagem="SUFICIENTE"
else:
	mensagem="INSUFICIENTE"
print(mensagem)