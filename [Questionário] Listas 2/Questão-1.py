def checkimput(n):
    for k in range(n):
        linha = input().split()
        primeiro = k
        segundo = n-1 -k
        for m in range(n):
            if m in [primeiro,segundo]:
                if linha[m] == "X":
                    continue
                else:
                    return False
            else:
                if linha[m] != "X":
                    continue
                else:
                    return False
    return True

n = int(input())
if checkimput(n):
    print("O one piece eh real!")
else:
    print("Talvez o tesouro seja os amigos que fizemos no caminho")
