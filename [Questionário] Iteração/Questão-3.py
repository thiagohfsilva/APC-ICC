cont = 0
texto = ""
maior_salario = 0.0
while texto != "Fim":
    texto,salario = input().split(",")
    salario = float(salario)
    if salario > maior_salario:
        if texto != "Fim":
            maior_salario = salario
    cont = cont + 1
if cont-1 == 0:
    print("Não tem")
else:
    print(f"{maior_salario:.2f}")
    
