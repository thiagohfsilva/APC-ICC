def distancia(x1,y1,x2,y2):
    D = ((x1-x2)**2 +(y1-y2)**2)**(0.5)
    return D
#inicio do programa
x1 =int(input())
y1 =int(input())
x2 =int(input())
y2 =int(input())

d = distancia(x1,y1,x2,y2)
if d <= 100:
    print("É o amor da minha vida!")
elif (100 < d) and (d <= 200):
    print("Talvez dê certo")
else:
    print("Não vale a pena investir")
