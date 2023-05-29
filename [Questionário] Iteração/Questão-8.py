pa,pb,t1,t2 = input().split()
pa,pb,t1,t2 = int(pa),int(pb),float(t1),float(t2)
if t2 >= t1:
    print("A nunca alcancara B.")
else:
    for i in range(1000):
        if pa>=pb:
            print(f"Vai alcancar em {i} ano(s).")
            break
        if i = 999:
            print("Mais de um milenio.")
        pa = int(pa + pa*t1/100)
        pb = int(pb + pb*t2/100)
