item = input ("")
quantItem = int (input(""))
refri = int (input(""))

if (item == "L"):
	total = float ((quantItem * 5) + (refri * 4))
	print (round (total, 2))
	
if (item == "S"):
	total = float ((quantItem * 3.50) + (refri * 4))
	print (round (total, 2))