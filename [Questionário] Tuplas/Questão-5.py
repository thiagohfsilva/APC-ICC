def stockmarket(stock):
    dic_stock ={}
    for operacao in stock:
        if operacao[0] in dic_stock.keys():
            dic_stock[operacao[0]] = dic_stock[operacao[0]]+ float(operacao[1]*operacao[2])
        else:
            dic_stock[operacao[0]] = float(operacao[1]*operacao[2])
    return dic_stock
