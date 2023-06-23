numeros = input().split()
rest = int(numeros[0])
for i in range(1,len(numeros)):
    rest = rest*2 + int(numeros[i])*0.5
print(f"{rest:.2f}")
