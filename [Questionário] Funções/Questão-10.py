def troco(x):
    div50 = x//50
    resto50 = x%(50)
    print(f"{div50} moedas de 50 centavos")
    div25 = resto50//25
    resto25 = resto50%(25)
    print(f"{div25} moedas de 25 centavos")
    div10 = resto25//10
    resto10 = resto25%(10)
    print(f"{div10} moedas de 10 centavos")
    div5 = resto10//5
    resto5 = resto10%(5)
    print(f"{div5} moedas de cinco centavos")
    div1 = resto5//1
    print(f"{div1} moedas de 1 centavo")
