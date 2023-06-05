frase = input()
cont = 0
for letra in frase:
    if letra.isdigit():
        cont = cont + 1
print(cont)
