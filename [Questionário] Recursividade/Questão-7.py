def triangulo(x, size):
    if size == 1:
        print(" "*x +"+")
    else:
        triangulo(x+1, size-2)
        print(" "*x +"+"*size)
        
    
