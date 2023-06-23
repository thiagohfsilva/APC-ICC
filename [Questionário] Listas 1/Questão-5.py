vogais = ["a","á","à","â","ã",
          "e","é","è","ê",
          "i","í","ì","î",
          "o","ó","ò","ô","õ",
          "u","ú","ù","û",]
def checkword(palavra):
    i = 0
    for letra in palavra:
        if letra.lower() in vogais:
            i += 1
    if i%2 == 0:
        return True
    else:
        return False
        
def paron(palavras):
    newpalavras =[]
    for palavra in palavras:
        if checkword(palavra):
            newpalavras += [palavra]
        else:
            continue
    return newpalavras
    
