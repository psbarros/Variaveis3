from numpy import *
string = input("palavra: ")
vet = ['a','e','i','o','u']

for i in vet:
			string = string.replace(i, '')
print(string)
			
		