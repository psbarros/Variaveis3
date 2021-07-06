# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
brasao = str(input("Digite o brasao: "))

print("Entrada:",brasao.lower())

if(brasao.lower() == "lobo"):
	print("Casa: Stark")
elif(brasao.lower() == "leao"):
	print("Casa: Lannister")
elif(brasao.lower() == "veado"):
	print("Casa: Baratheon")
elif(brasao.lower() == "dragao"):
	print("Casa: Targaryen")
elif(brasao.lower() == "rosa"):
	print("Casa: Tyrell")
elif(brasao.lower() == "sol"):
	print("Casa: Martell")
elif(brasao.lower() == "lula"):
	print("Casa: Greyjoy")
elif(brasao.lower() == "esfolado"):
	print("Casa: Bolton")
elif(brasao.lower() == "turta"):
	print("Casa: Tully")
else:
	print("Brasao invalido")