n,val_ing = input().split()
n,val_ing = int(n),int(val_ing)
soma_valor = 0
for k in range(n):
    dinheiro = int(input())
    soma_valor = soma_valor + dinheiro
print(f"media: {soma_valor//n}")
if soma_valor//n >= val_ing:
    print(f"o rock reinara mais uma vez")
else:
    print(f"rockeiros trabalhando ja")
