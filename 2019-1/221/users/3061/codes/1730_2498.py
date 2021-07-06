na = int(input("Numero de habitantes de da cidade A:"))
nb = int(input("Numero de habitantes da cidade B:"))
pa = float(input())/100
pb = float(input())/100
sa = 0 
sb = 0 
anos = 0 
while na < nb :
	na = na + na*pa
	nb = nb + nb*pb 
	anos = anos + 1 
print(anos)
	