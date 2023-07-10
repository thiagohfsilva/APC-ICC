def controle(n,c):
    if c == 0:
        controle(n-1,c+1)
    elif n == 0:
        print(f"Parabens Julie! Voce tomou todos os {c} comprimidos!")
    else:
        print(f"Voce ja tomou {c} comprimidos, restam {n}.")
        controle(n-1,c+1)

