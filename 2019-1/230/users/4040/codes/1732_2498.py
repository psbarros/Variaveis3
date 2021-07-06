# Data

Pa = int(input("Number of Citzens of city A: "))
Pb = int(input("Number of Citzens of city B: "))
RoGa = float(input("Rate of Gownth per year of city A: "))/100
RoGb = float(input("Rate of Gownth per year of city B: "))/100
t = 0

# Data working

while(Pa < Pb):
	t = t + 1
	Pa = Pa*(1 + RoGa)
	Pb = Pb*(1 + RoGb)

print(t)