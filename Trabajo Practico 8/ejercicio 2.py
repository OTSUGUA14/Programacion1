def power(n,b):
    aux=2
    while n>=b:
        b=b**aux
    if n==b:
        return True
    else:
        return False
number_1=int(input("Ingrese el primer número: "))
number_2=int(input("Ingrese el segundo número: "))
if power(number_1,number_2):
    print("El: ",number_1," es potencia de: ", number_2)
else:
    print("El: ",number_1," NO es potencia de: ", number_2)