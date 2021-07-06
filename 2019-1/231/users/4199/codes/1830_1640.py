from numpy import*
vett = array(eval(input(" quantidade alunos matriculados: ")))
i = 0
imp = 0
for i in range(size(vett)):
	if(vett[i] %2 != 0):
		imp = imp + 1

veti = zeros(1,dtype=int)

for v in range(size(vett)):
	if(v %2 !=0):
		v = veti

print(imp)
print(veti)