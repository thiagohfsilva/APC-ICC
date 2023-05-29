def fibonacci(n):
    anteanterior = 0
    anterior = 1
    for k in range(n):
        print(anteanterior,end = ' ')
        anteanterior,anterior = anterior, anterior + anteanterior
        
