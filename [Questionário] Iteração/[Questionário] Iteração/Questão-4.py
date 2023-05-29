texto = ""
menor_salario = 1000000000.0
nome_menor_salario = "Não tem"
while texto != "Fim":
    texto,salario = input().split(",")
    salario = float(salario)
    if salario < menor_salario:
        if texto != "Fim":
            menor_salario = salario
            nome_menor_salario = texto
print(nome_menor_salario)

        

    
