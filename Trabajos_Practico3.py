#EXERCISE 1

print("EJERCICIO 1")
word=input("ingrese una palabra: ")  #Guardar la palabra en la varieble y luego utilizando for imprimir 10 veces
for i in range(10):
    print(word)


#EXERCISE 2

print("-------------------------------------")

print("EJERCICIO 2")
age=int(input("ingresa tu edad: ")) 
for i in range(age):    #Recorrer desde el cero hasta el rango de la edad y imprimimos los años
    print("Has complido: " ,i, " años") 

#EXERCISE 3

print("-------------------------------------")

print("EJERCICIO 3")
number_imp=[] #Haceme una lista
number=int(input("ingresa un número entero: "))
for i in range(number): 
    if (i%2==0):   #Si es par vuelve a emepzar el bucle 
       continue
    else:
        number_imp.append(i) #Si es impar guarda el valor en la lista con el método append()
print(number_imp)

#EXERCISE 4

print("-------------------------------------")

print("EJERCICIO 4")
number_back=[] #Hacemos una lista 
number=int(input("ingresa un número entero: "))
for i in range(number,0,-1):  #Hacer que en el rango empieze del numero ingresado hasta el 0 restando 1
    number_back.append(i) #Se va guardando en la variable tipo lista
print(number_back)

#EXERCISE 5

print("-------------------------------------")
print("EJERCICIO 5")

number=int(input("Ingrese la cantidad a invertir: "))
interest=int(input("Ingrese el interes : "))
year=int(input("Ingrese el/los años : "))
for i in range(year):
    #Sacar interes multiplicar por año y sumamos a la cantidad invertida 
    print("El capital optenido en el año: ", (i+1) , " es de: $" ,(interest*number)/100*(i+1)+number) 

#EXERCISE 6
print("-------------------------------------")
print("EJERCICIO 6")

number=int(input("Ingrese un número entero: "))
for i in range(number):   #Definir el rango en el for
    for j in range(i+1): # Usar otro for para imprimir seguido y luego hacer espacio
        print(end="*")

    print("")
   

#EXERCISE 7


print("-------------------------------------")
print("EJERCICIO 7")

for i in range(10):  #Definir el rango 10, i muestra el numero multiplicando
    for j in range(10):#Definir el rango de 10, j muestra el numero multiplicador
        print((i+1)," x ",(j+1 )," = ", (i+1)*(j+1) ) #A i y j le suma uno para que no tome el valor 0       

#EXERCISE 8

print("-------------------------------------")
print("EJERCICIO 8")
number=int(input("Ingrese un número entero: "))
for i in range(number+1):  #Dar rango al bucle mas uno para que llegue hasta el número ingresado
       if i%2==0: #Validar que no el número sea par si es parta se salta todo y empieza otra ves el bucle
            continue
       else:
            print("")
            for j in range(i,0,-1): #Dar rango desde i hasta 0 -1 para que sea el orden de menor a mayor
                if j%2==0: #Lo mismo que en el otro if
                    continue
                else:
                    print(j,end=" ") #Imrpime el número


#EXERCISE 9

print("-------------------------------------")
print("EJERCICIO 9")
#Definimos la contraseña
passwords="El salto del papu"
while True:
    #Pedir que ingrese la contraseña
    attempt=input("Ingrese la contraseña: ")
    if attempt==passwords:
        #En caso de que ingrese la contraseña correcta se muestra 
        print("Haz ingresado correctamente ")
        break
    else:
        #En caso de no sea la correcta se muestra
        print("Contrasela incorrecta , intentelo nuevamente ")
        #Este bucle se repite hasta que introduzca la contraseña correcta


#   EXERCISE 10

print("-------------------------------------")
print("EJERCICIO 10")
#Pedir que ingrese un número
number=int(input("ingrese un número entero: "))
aux=0
#Verificar cuanto divisores tiene el número lo sumamos a una varibale auxiliar
for i in range(number):
    if (number % (i+1)==0):
        aux+=1
print("")
#En caso de que tenga dos divisores es primo
if aux==2:
    print("El numero es primo")
else:
#En caso de que tenga menos o mas de dos no es primo
     print("El numero no es primo")


#   EXERCISE 11

print("-------------------------------------")
print("EJERCICIO 11")
word=input("Ingrese una palabra: ")
print("La palabra al revés queda asi: ")
#Hacer que empieze por la ultima letra de la plabra hasta 0 restando 1
for i in range(len(word),0,-1):
    #Mostramos por cada bucle cada letra al revés usando i -1
    print(word[i-1])

#EXERCISE 12

print("-------------------------------------")
print("EJERCICIO 12")
#Pedir las variables
word=input("Ingrese una palabra: ")
letter=input("Ingrese una letra: ")

amount=0
#Recorrer la palabra con for , en caso de que se ecuentre la letra dentro de la palabra le sumamos uno a la variable amount
for i in word:
    if i==letter:
        amount+=1
    else:
        continue
#Validar si amount sigue siendo cero la letra no se encontro
if amount==0:

    print("La letra no se encontró en la palabra")
else:
    #Si es mayor que cero se encontro y muestra cuantas veces se encontró
    print("La letra se encontró: ", amount," veces")

#EXERCISE 13

print("-------------------------------------")
print("EJERCICIO 13")
print("Ingrese fin para finalizar el programa")
while True:
    #Pedir al usuario que ingrese una palabra
    word=input("Ingrese una palabra: ")
    #Validar si esa palabra fue salir para terminar el programa
    if word.lower() =='salir':
        print("Fin del programa")
        break
    else:
    #Si la palabra no es salir imprimimos la palabra que ingreso el usuario
        print(word)

#EXERCISE 14

print("-------------------------------------")
print("EJERCICIO 14")
#Pedir los números
number1=int(input("Ingrese el primer número: "))
number2=int(input("Ingrese el segundo número: "))
#Dar rango desde el número 1 hasta el número 2 mas 1 (asi toma todo el valor )
for i in range(number1,(number2+1)):
    #Validar si es par
    if i%2==0:
        #Si es par imprime
        print("El número: ", i, " es par")
    else:
        #Si no es par imprime
        print("El número: ", i, " es impar")

#EXERCISE 15

print("-------------------------------------")
print("EJERCICIO 15")
#Pedir el ingreso del número
number=int(input("Ingrese un número mayor a cero: "))
#Recorrer el número con range , sumarle luego a la i para que tome todos los valores
#Y luego usando el %(resto)verifica si es igual a 0 es divisor del número ingresado
for i in range(number):
    if (number%(i+1)==0):
        print(i+1 ," es divisor de: ", number)
    

#EXERCISE 16

print("-------------------------------------")
print("EJERCICIO 16")
negative=0

quantity=int(input("Ingrese la cantidad de números que va ingresar: "))
for i in range(quantity):
    print("Ingrese el",i+1,"° número: ",end=(""))
    number=int((input()))
    if (number<0):
        negative+=1
print("La cantidad de números negativo que ingreso fueron: ", negative)

#EXERCISE 17

print("-------------------------------------")
print("EJERCICIO 17")
new_Vowls=[] #Crear una lista
word=input("ingrese una frase: ").lower()
vowels=["a","e","i","o","u"] #crear lista de vocales
for i in word:
    if i in new_Vowls: #En caso de que la letra ya esta en la lista de nueva vocales vulve el bucle
        continue
    else:
        if i in vowels: #Si no se encuentra en la lista vocales nueva se agrega a la lista
            new_Vowls.append(i)
print("Las vocáles encontradas son: ", new_Vowls)   

#EXERCISE 18

print("-------------------------------------")
print("EJERCICIO 18")
numbers=[0,1] #Crear una lista
for i in range(8):
    numbers.append(numbers[i+1]+numbers[i]) #Agregar a la lista la suma de la posicion i+ y i

print(numbers)

#EXERCISE 19

print("-------------------------------------")
print("EJERCICIO 19")
total=0
save=int(input("Ingrese la cantidad de dinero que quiere ahorrar: "))
while True:
    enter=int(input("¿Cuanto dinero va a ingresar ahora? "))
    while True:
        if enter<0: #Si es menor a cero pedira que ingrese un nuevo número hasta que sea mayor a 0
            enter=int(input("El número no puede ser uno negativo , ingrese otro monto: "))
        else:
            break
    
    total+=enter #Sumar el monto ingresado a la variable total
    if total>=save:  #Si la variable total es mayor o igual al ahorro ingresado se termina el bucle
        break
    
print("El dinero ahorrado fue de:$ ", total)    

#EXERCISE 20

print("-------------------------------------")
print("EJERCICIO 20")
print("Ingrese 0 para terminar el programa")
total=0
while True:
    number=int(input("Ingrese un número: "))
    if number==0: #Cuando el usuario ingrese 0 se termina el bucle
        break
    else:
        total+=number #Sumar el número ingresado a la varibale total
print("La sumatoria de los números ingresados es de: ", total)

#EXERCISE 21

print("-------------------------------------")
print("EJERCICIO 21")
older=0
print("Ingrese 0 para terminar el programa")
while True:
    number=int(input("Ingrese un número: "))
    if number==0: #Cuando el usuario ingrese 0 se termina el bucle
        break
    else:
        if number>older: #En caso de que el número ingresado sea mayor al número mayor ingresado anteriormente se guarda en la variable mayor
            older=number
       
print("El mayor número fue el: ", older)

 #EXERCISE 22

print("-------------------------------------")
print("EJERCICIO 22")   
par=0
print("Ingrese -1 para terminar el programa")
while True:
    sum=0
    number=int(input("Ingrese un número: "))
    if number==-1: #Cuando el usuario ingrese -1 se termina el bucle
        break
    else:
        if number%2==0: #En caso de ser número par se le suma 1 a la variable par
            par+=1
        for i in str(number):#Pasar a string el número para recorrerlo y luego pasarlo a int para sumar cada dígito del mismo
            sum+=int(i)
    
    print("La suma de los dígitos de: ", number," es: ",sum )
        
print("La cantidad de números ingresados fueron : ", par)

#EXERCISE 23

print("-------------------------------------")
print("EJERCICIO 23")   
print("Ingrese 0 para terminar el programa")
pay=0
while True:
    number=int(input("Ingrese los montos de las compras del cliente: "))
    if number==0: #Cuando el usuario ingrese 0 se termina el bucle
        break
    else:
       while True:
            if number<0:
               number=int(input("No se puede ingresar un monto negativo ingrese otro monto: "))
            else:
               pay+=number
               break
        
if pay>1000:
    print("El monto a pagar es de: ", (10*pay)/100 +pay)
else:
    print("El monto a pagar es de: ",pay)

#EXERCISE 24

print("-------------------------------------")
print("EJERCICIO 24")   
factorial=1
number=int(input("ingrese un número entero: "))
for i in range(number):
    factorial*=i+1

if number==0:
    print("El factorial de: ", number," es 1")
else:
    print("El factorial de: ", number," es :", factorial)
