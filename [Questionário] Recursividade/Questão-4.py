def JaChegou(n, text):
    if n ==0:
        return
    else:
        print(text)
        JaChegou(n-1, text)

