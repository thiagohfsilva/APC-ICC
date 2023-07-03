lista1 =[]
lista2 =[]
for i in range(10):
    if i > 4:
        lista2 +=[int(input())]
    else:
        lista1 +=[int(input())]
list_tuple = zip(lista1,lista2)
print(list_tuple)
list_media =[]
for i in range(5):
    list_media += [(list_tuple[i][0]+list_tuple[i][1])/2]
print(list_media)
