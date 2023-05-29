n = int(input())
soma_salario = 0.0
menor_salario = 1000000000.00
menor_pessoa = ""
maior_salario = 0.0
maior_pessoa = ""
for k in range(n):
    nome,salario = input().split(",")
    salario = float(salario)
    soma_salario = soma_salario + salario
    if salario < menor_salario:
        menor_salario = salario
        menor_pessoa = nome
    if salario > maior_salario:
        maior_salario = salario
        maior_pessoa = nome 
if n == 0:
    print("Não tem média\nNão tem\nNão tem")
else:
    media = soma_salario/n
    print(f"{media:.2f}")
    print(f"{maior_pessoa} {maior_salario:.2f}")
    print(f"{menor_pessoa} {menor_salario:.2f}")
