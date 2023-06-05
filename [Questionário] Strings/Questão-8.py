n = int(input())
for k in range(n):
    numstr='0'
    carac = ''
    a = input()
    for letra in a:
        if not(letra.isdigit()):
            print(carac*int(numstr),end ="")
            carac = letra
            numstr=''
        else:
            numstr= numstr + letra
    print(carac*int(numstr))       
    
