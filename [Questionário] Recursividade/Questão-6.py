def simples():
    texto = input()
    if texto == "repete":
        print("Olá! Vamos repetir!")
        simples()
simples()
