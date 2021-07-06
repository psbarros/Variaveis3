S = input("coloque uma palavra:")
s = S.upper()
a = s.count("A")
e = s.count("E")
i = s.count("I")
o = s.count("O")
u = s.count("U")
vogais = a + e + i + o + u 
consoantes = len(s) - vogais 
print(vogais)
print(consoantes)