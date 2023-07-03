n = int(input())
dic ={}
for i in range(n):
    dados = input().split()
    email = dados[1]
    media = (float(dados[2])+
             float(dados[3])+
             float(dados[4])+
             float(dados[5]))/4
    
    dic[dados[0]] = email,media
Nome = input()
if Nome not in dic.keys():
    print(f"O aluno {Nome} não está na turma.")
else:
    print(f"Destinatário: {dic[Nome][0]}")
    if dic[Nome][1] < 5:
        print(f"O aluno {Nome} foi reprovado com média {dic[Nome][1]:.2f}.")
    else:
        print(f"O aluno {Nome} foi aprovado com média {dic[Nome][1]:.2f}.")
        
