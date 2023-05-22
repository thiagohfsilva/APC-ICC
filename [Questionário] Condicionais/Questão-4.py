def medP(x1,x2,x3,a,b,c):
    return (x1*a+x2*b+x3*c)/(a+b+c)
def medA(x1,x2,x3):
    return medP(x1,x2,x3,1,1,1)
def medH(x1,x2,x3):
    return 3/(1/x1 +1/x2 +1/x3)

x1,x2,x3 = input().split()
x1,x2,x3 = float(x1),float(x2),float(x3)
opcao = input()

if opcao == "A":
    print("Aritmetica")
    print(f"{medA(x1,x2,x3):.2f}")
elif opcao == "P":
    a,b,c = input().split()
    a,b,c = int(a),int(b),int(c)
    print("Ponderada")
    print(f"{medP(x1,x2,x3,a,b,c):.2f}")
elif opcao == "H":
    print("Harmonica")
    print(f"{medH(x1,x2,x3):.2f}")
else:
    print("Operacao inexistente")
