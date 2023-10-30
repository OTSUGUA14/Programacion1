def size(n):
    aux=0
    for i in str(n):
        aux+=1
    return aux


number=int(input("ingrese un número positivo: "))
print("La cantidad de dígitos que tiene el número es: ", size(number))