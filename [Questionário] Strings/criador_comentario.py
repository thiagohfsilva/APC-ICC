meuArquivo = open('QuestionárioCompleto.txt',encoding='utf-8',errors = "ignore")
questoes = meuArquivo.read().split("")
nova_questoes = []
for questao in questoes:
    if "Questão" in questao:
        nova_questoes += [questao.split("For example:")[0].replace("<","menor que").replace(">","maior que")]
print(nova_questoes[1])

for i in range(len(nova_questoes)):
    with open('Q' +str(i+1)+'.txt', 'w') as f:
        f.write(nova_questoes[i])
