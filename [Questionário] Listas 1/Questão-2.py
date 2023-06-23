n = int(input())
lista =[]
for i in range(n):
     texto = input()
     if texto in lista:
         continue
     else:
         lista += [texto]

killer = input().split()

nokiller =[]

for element in lista:
    if element in killer:
        continue
    else:
        nokiller += [element]
        
print(*nokiller)
    
