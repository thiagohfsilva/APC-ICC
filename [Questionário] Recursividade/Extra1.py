def laco(n):
    if n==0:
        print(n)
        return
    else:
        print(n)
        laco(n-1)
laco(100)
