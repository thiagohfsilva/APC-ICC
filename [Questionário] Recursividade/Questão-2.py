def bomb(time,explodir):
    if time == 1:
        if explodir:
            print("Seja rápido. Falta 1 segundo")
            bomb(time -1,explodir)
        else:
            print("Bomba desativada automaticamente!")
    elif time == 0:
        print("Cabum!!!! Explodiu")
    elif time == 5:
        print("Seu tempo está acabando!")
        bomb(time -1,explodir)
    else:
        print(f"Atenção faltam {time} segundos...")
        bomb(time -1,explodir)


N = int(input())
rec = int(input())
explodir = True if rec < N else False
bomb(N,explodir)
