n = int(input())
lista_de_pessoas =[]
for i in range(n):
    texto = input()
    lista_de_pessoas += [texto]

lista_de_pessoas.sort(reverse = True)

for elemento in lista_de_pessoas:
    print(elemento)
