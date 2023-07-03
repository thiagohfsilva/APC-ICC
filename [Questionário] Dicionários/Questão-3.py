lista = input().split()
dic ={}
for i in range(1,len(lista),2):
    dic[lista[i-1]] = float(lista[i])
saldo = 0
compras = input().split()

for i in range(1,len(compras),2):
    saldo += float(compras[i])* dic[compras[i-1]]    
print(f"R$ {saldo:.2f}")
