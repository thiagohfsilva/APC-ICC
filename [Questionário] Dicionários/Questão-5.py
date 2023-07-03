n = int(input())
dic_cor = {}
for i in range(n):
    valor = 0
    nomes = ""
    dados = input().split()
    for j in range(len(dados)):
        if j%2 ==0:
            nomes += dados[j] +", "
        else:
            valor += float(dados[j])
    dic_cor[i+1] = nomes[:-2],valor/(len(dados)//2)
v =int(input())
if v not in dic_cor.keys():
    print("Esse corredor não existe no mercado.")
else:
    print(f'No corredor {v} encontramos:\n{dic_cor[v][0]}\nE o preço médio é {dic_cor[v][1]:.2f}.')
            
    
