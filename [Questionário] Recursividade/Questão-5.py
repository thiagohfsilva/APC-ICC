def corrida(n,np,p):
    if n <= 0:
        print("A corrida chegou ao fim.")
        return
    else:
        if n-np > 0:
            print(f"Faltam {n-np} voltas, hora de trocar os pneus.")
        corrida(n-np,p,p)

