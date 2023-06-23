numeros = input().split()
for i in range(len(numeros)):
    numeros[i] = int(numeros[i])
    
primeiro,segundo = input().split()
primeiro,segundo = int(primeiro),int(segundo)
print(numeros[primeiro:segundo])
