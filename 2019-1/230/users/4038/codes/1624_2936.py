pressao = int(input("pressao: ")
numero_de_mols = int(input("mols: "))
temperatura = float(input("teperatura: "))
constante = float(input("constante: "))

volume = (numero_de_mols*constante*temperatura)//pressao

print(volume)