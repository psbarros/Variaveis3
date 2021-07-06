from numpy import*

x = array(eval(input('Matricula dos alunos: ')))

y = array([i for i in x if i%2!=0])
print(y)
