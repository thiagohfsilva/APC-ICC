#bubble sort
def soma(lista):
    soma = 0
    for num in lista:
        soma += int(num)
    return soma

def comparador(num_a,num_b,t):
    if int(num_a[t]) > int(num_b[t]) :
        return True
    elif int(num_a[t]) < int(num_b[t]):
        return False   
    else:
        if soma(num_a) > soma(num_b):
            return True
        else:
            return False
        
def order(lista,t): #O(n) = n^2
    for i in range(len(lista)):
        for j in range(len(lista)-1):
            if comparador(lista[j],lista[j+1],t):
                lista[j],lista[j+1] = lista[j+1],lista[j]
    return lista
def printmat(mat):
    for k in range(len(mat)):
        print(*mat[k])
    
n = int(input())
t = int(input())
mat =[]
for i in range(n):
    mat += [input().split()]

printmat(order(mat,t))
