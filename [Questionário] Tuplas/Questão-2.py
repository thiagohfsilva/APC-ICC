def convert(l):
    dic = {}
    for tupla in l:
        if tupla[0] in dic.keys():
            dic[tupla[0]] = dic[tupla[0]] +[tupla[1]]
        else:
            dic[tupla[0]] = [tupla[1]]

    return dic
