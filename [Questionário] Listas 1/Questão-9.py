def menordist(texto,n):
    lista = texto.split()
    distancia = len(lista)
    for k in range(1,len(lista)):
        if n+k < len(lista):
            if lista[n+k] =='1':
                return k
        if n-k >= 0:
            if lista[n-k] =='1':
                return k

def Maislong(texto):
    lista = texto.split()
    maiordistancia = 0
    for i in range(len(lista)):
        if lista[i] == "0":
            if menordist(texto,i) > maiordistancia:
                maiordistancia = menordist(texto,i)
    return maiordistancia
            
n,m = input().split()
n,m = int(n),int(m)
maiordistancia2 = 0
for i in range(n):
    texto = input()
    if Maislong(texto)> maiordistancia2:
        maiordistancia2 = Maislong(texto)
print(maiordistancia2)



