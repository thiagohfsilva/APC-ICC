dic ={}
texto = input()
for letra in texto:
    if letra in ["d","t","v"]:
        if letra in dic.keys():
            dic[letra] += 1
        else:
            dic[letra] = 1
if "d" in dic.keys():
    print("d",dic["d"])
if "t" in dic.keys():
    print("t",dic["t"])
if "v" in dic.keys():
    print("v",dic["v"])
