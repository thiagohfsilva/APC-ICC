listanum = input().split()
divisor = int(input())
divlist =[]
for element in listanum:
    intelement = int(element)
    if intelement%divisor == 0:
        divlist +=[intelement]
print(*divlist)
