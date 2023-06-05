palavra = input()
cont = 0
for i in range(len(palavra)):
    if palavra[i] != palavra[-1-i]:
        cont = cont+1
falha = cont//2
if (falha == 1) or ((falha == 0)and (len(palavra)%2==1)):
    print("ON")
else:
    print("OFF")

