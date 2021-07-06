from numpy import*
matr = array(eval(input("Coloque as matriculas dos alunos:")))
g1 = array([z for z in matr if z%2==0]) 
g2 = array([h for h in matr if h%2!=0])
print(g2)