cont = 0
salario_acumulado = 0.0
texto = ""
while texto != "Fim":
    texto,salario = input().split(",")
    salario = float(salario)
    if texto != "Fim":
        salario_acumulado = salario_acumulado + salario
    cont = cont + 1
if cont-1 == 0:
    print("0.00")
else:
    print(f"{salario_acumulado/(cont-1):.2f}")
    
