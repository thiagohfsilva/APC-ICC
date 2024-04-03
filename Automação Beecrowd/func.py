def Entrada():
    texto =""
    while True:
        linha = input()
        if linha == "FIM":
            break
        else:
            texto = texto +linha +"\n"
    return texto

def Porcess(texto):
    numero = ""
    titulo = ""
    testcase =""
    testlist =[]
    for i in range(len(texto.split("\n"))):
        linha = texto.split("\n")[i]
        if "beecrowd | " in linha:
            numero = linha.replace("beecrowd | ","")
            titulo = texto.split("\n")[i+1]
        if "Exemplos de Entrada" in linha:
            testlist = texto.split("\n")[i+1:]
    for linha in testlist:
        testcase = testcase + linha +"\n"
    return numero,titulo,testcase

