def imprimeTermos(n):
    if n == 0:
        print(n)
        return
    elif n==1:
        print(n)
        print(n-1)
        return
    else:
        print(n)
        imprimeTermos(n-2)

