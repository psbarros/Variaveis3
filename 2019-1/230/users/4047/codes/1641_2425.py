dist = float(input("Distancia total percorrida(km): "))
combustivel = float(input("Combustivel gasto(litros): "))

media = dist/combustivel
print(round(media, 3), "km/l")