listfib =[0,0,0,0,0]
listfib += [0,0,0,0,0]
listfib += [0,0,0,0,0]
listfib += [0,0,0,0,0]
listfib += [0,0,0,0,0]
listfib += [0,0,0,0,0]
#print(len(listfib))
def fib(n):
    if n == 0:
        listfib[0] += 1
        return 0
    elif n == 1:
        listfib[1] += 1
        return 1
    else:
        listfib[n] += 1
        return fib(n-1) + fib(n-2)
n = int(input())
print(f"Termo: {fib(n)}")
print("Quantidades:")
for i in range(len(listfib)):
    if not(1 in listfib[i:]):
        break
    else:
        print(f"fibonacci({i}) - {listfib[i]}")

