def ehPrimo(n):
    resp = 1
    for i in range(2,n):
        if n%i == 0:
            resp = 0
            break
    return resp
def divisoresPrimos(n):
    cont = 0
    for i in range(2,n):
        if n%i == 0:
           if ehPrimo(i) == 1:
               cont = cont + 1
    return cont
