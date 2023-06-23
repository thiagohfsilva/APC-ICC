lista = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
def mediana_e_mais_proximo_media_e_pos(lista):
    lista2 = lista[:]
    lista = sorted(lista)
    tam = len(lista)
    #print("lista:",lista)
    if tam > 0:
        if tam % 2 == 0:
            mediana = (lista[int(tam/2)] + lista[int(tam/2-1)])/2
        else:
            mediana = (lista[int(tam/2)])
        somador = 0
        for i in lista:
            somador += i
        media = somador/tam
        delta = lista[tam-1] - lista[0]
        prox_media = lista[0]
        index=0
        for i in range(len(lista2)):
            if abs(media-lista2[i]) < delta:
                prox_media = lista2[i]
                index = i
                delta = abs(media - lista2[i])
                print("-"*70)
                print("prox_media:",prox_media)
                print("index:",index)
                print("delta:",delta)
    else:
        prox_media = None
        mediana = None
        index = None
    return [mediana, prox_media, index]
print(mediana_e_mais_proximo_media_e_pos(lista))
