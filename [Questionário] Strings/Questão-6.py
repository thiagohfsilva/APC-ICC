frase = input()
palavra = input()
if palavra in frase:
    frase = frase.replace(palavra,"*")
    print(frase)
else:
    print("tudo certo :)")
