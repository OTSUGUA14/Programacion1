
def digit_sum(num):
    result=0
    #Pasar a string el número para recorrerlo y luego pasarlo a int para sumar cada dígito del mismo
    for i in str(num):
     
        result+=int(i)
    
    return result    

print("para finalizar el programa ingrese 0")
number_total=0
number=int(input("ingrese un número: "))
while True:
     #Cuando el usuario ingrese 0 se termina el bucle , muestra la suma de todos los números y la suma de sus dígitos
    if number==0:

        print("La suma de todos los número ingresado es: ", number_total, "Y la suma de sus dígitos es: " ,digit_sum(number_total))
        break
    else:
        #Sumar número a la varibale numbero total y luego muestra la suma de los dígitos
        number_total += number
        print("La suma de los dígitos de: ",number, "es : ", digit_sum(number))
        number=int(input("ingrese otro número "))
        



