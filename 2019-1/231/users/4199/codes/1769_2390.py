from numpy import*
presente = array(eval(input("presentes no curso:")))
faltantes = array(eval(input("faltantes no curso:")))
f = presente - faltantes
i=0
while(f[i] != max(f)):
	i=i+1
print(i+1)