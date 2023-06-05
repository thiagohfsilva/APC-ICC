frase = input()
for i in range(len(frase)):
    if (i%2== 1) and not(frase[i]== " "):
        print(frase[i],end = "")
        
