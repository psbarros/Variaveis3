# Ao testar sua solução, não se limite ao caso de exemplo.
x = float(input("coordenada x: "))
y = float(input("coordenada y: "))

if (x == y and x==0 and y==0):
    print("Origem")
elif (x > 0 and y > 0):
    print("Q1")
elif (x < 0 and y > 0):
    print("Q2")
elif (x < 0 and y < 0):
    print("Q3")
elif (x>0 and y<0):
    print("Q4")
elif (y == 0):
    print("Eixo X")
elif (x == 0):
    print("Eixo Y")