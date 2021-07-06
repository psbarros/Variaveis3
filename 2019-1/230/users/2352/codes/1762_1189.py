string = input("Digite uma string: ")

print(string.replace("","").upper())

s1 = string[:-1]

if string[0] == string[(len(string) - 1)] and string[1 : (len(string) -2)] == s1[1 : (len(string) - 2)]:
	print(1)
else:
	print(0)