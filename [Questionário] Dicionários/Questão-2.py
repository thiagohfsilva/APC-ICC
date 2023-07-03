n = int(input())
dic_alunos ={}
for i in range(n):
    nome,nota = input().split(", ")
    nota = float(nota)
    dic_alunos[nome] = nota

my_nota =float(input())
retorno = ""
for nome in sorted(dic_alunos.keys()):
    if dic_alunos[nome] == my_nota:
        retorno += nome+"/"
if retorno =="":
    print("Você foi o único aluno com essa nota.")
else:
    print(retorno[:-1])
    
