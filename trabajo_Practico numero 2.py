import string
# Ejercicio 1 y 2
usr_inp = int(input("Ingrese la cantidad de años que tiene el computador: "))
#Comprueba el número y segun el número va a mostrar un mensaje
if usr_inp > 2: 
    print("El computador es viejo!")
elif usr_inp < 0:   
    print("Error: El numero debe ser positivo!")
else: 
    print("El computador es nuevo!")

# Ejercicio 3
name_a = input("Ingrese un nombre: ").lower()
name_b = input("Ingrese un segundo nombre: ").lower()
#Comprueba si las dos primeras letras coinciden
if name_a[0]==name_b[0]:  
    print("Coincidencia") 
else:
    print("No coincidencia")

# Ejercicio 4
print("Vote a uno de los siguientes candidatos:")
print("------------")
print("A) Partido Rojo.")
print("B) Partido Verdad.")
print("C) Partido Azul.")
print("------------")
usr_inp = input("Ingrese su voto: ")
#Verifica que partido eligió segun la letra ingresada
if usr_inp.lower() == 'a': 
    print("Usted ha votado por el partido Rojo.")
elif usr_inp.lower() == 'b':
    print("Usted ha votado por el partido Verdad")
elif usr_inp.lower() == 'c':
    print("Usted ha votado por el partido Azul")
else:
    print("Error: Esa no es una opción")

# Ejercicio 5
usr_inp = input("Ingrese una letra: ")
vowels = ["a", "e", "i", 'o', 'u'] #Lista de vocales
if len(usr_inp) == 1:
    if usr_inp in vowels: #verifica que la letra ingresada esta en la lista 
        print("Es una vocal")
    else:
        print("No es una vocal")
else:
    print("No se puede procesar el dato")

# Ejercicio 6  
usr_inp = int(input("Ingrese un año: "))
#Comprueba la entrada y depende del año va a mostrar un mensaje 
if usr_inp % 100 == 0: 
    if usr_inp % 400 == 0:
        print("Año bisiesto")
    else:
        print("No es un año bisiesto")
elif usr_inp % 4 == 0:
    print("Año bisiesto")
else:
    print("Año bisiesto")

# Ejercicio 7
numbers = []
numbers.append(int(input("Ingrese un numero: "))) 
numbers.append(int(input("Ingrese un segundo numero: ")))
numbers.append(int(input("Ingrese un tercer numero: ")))
#Guardamos en la variable menor el primer número ingresado
lesser = numbers[0]
#Recorre la lista y si el número en menor a la variable menor se le asigna ese número a la varibale menor
for number in numbers:
    if number < lesser:
        lesser = number

print("El menor numero es: ", lesser)

# Ejercicio 8
usr_name = input("Ingrese el nombre de usuario: ")
usr_pass = input("Ingrese la contraseña: ")
#Validar si el nombre es Gwenevere y la contraseña excalibur
if usr_name == "Gwenevere" and usr_pass == "excalibur":
    print("Usuario y contraseña correctos. Puede ingresar a Camelot")
else:
    print("Acceso denegado")

# Ejercicio 9
# Obtiene una lista con el alfabeto
alphabet = list(string.ascii_lowercase)

usr_name = input("Ingrese su nomre: ").lower()
usr_gender = input("Ingrese su genero (F/M): ").lower()
# Si el usuario no introduce una f o una m, el código por defecto es una m
if  usr_gender != "f" or not usr_gender != 'm':
    usr_gender = 'm'
print(usr_gender)

# Si la primera letra del nombre es anterior o igual a m y el usuario es mujer, será puesto en el grupo A.
# Si la primera letra del nombre es posterior a la n y el usuario es varón, también se le incluirá en el grupo A.
# Si ninguna de estas condiciones coincide, el usuario será incluido en el grupo B.
if (alphabet.index(usr_name[0]) <= 13 and usr_gender == 'f') or (alphabet.index(usr_name[0]) >= 14 and usr_gender == 'm'):
    print("Estas en el grupo A")
else:
    print("Estas en el grupo B")

# Ejercicio 10
#Pedir que ingrese su edad
usr_age = int(input("Ingrese su edad: "))
#Comprueba la entrada y muestra un mensaje dependiendo de su edad
if usr_age <= 4:
    print("Puede pasar gratis")
elif usr_age > 4 and usr_age < 18:
    print("Debe pagar $500")
elif usr_age>18:
    print("Debe pagar $1000")

# Ejercicio 11
# Lista con los ingredientes por defecto
ingredients = ["Mozzarella", "Tomate"]
# Pregunta al usuario si es vegano o no, el código por defecto será no
usr_inp = input("Es usted vegetariano? y/N: ").lower()
if  usr_inp != "y":
    usr_inp = 'n'
if usr_inp == 'y':
    print("A) Pimiento")
    print("B) Tofu")
    print("-------------------")
    # Pide al usuario que elija un ingrediente
    usr_inp = input("Eliga un ingrediente: ").lower()
    if usr_inp == "a":
        ingredients.append("Pimiento")
    if usr_inp == "b":
        ingredients.append("Tofu")
    print("-------------------")
    print("Ingredientes:")
    # Muestra los ingredientes
    for ingredient in ingredients:
        print(ingredient)
elif usr_inp == 'n':
    print("A) Peperoni")
    print("B) Jamón ")
    print("C) Salmón")
    print("-------------------")
    usr_inp = input("Eliga un ingrediente: " ).lower()
    if usr_inp == "a":
        ingredients.append("Peperoni")
    if usr_inp == "b":
        ingredients.append("Jamón")
    if usr_inp == "c":
        ingredients.append("Salmón")
    print("-------------------")
    print("Ingredientes:")
    for ingredient in ingredients:
        print(ingredient)

# Ejercicio 12
actual_year = int(input("Ingrese el año actual: "))
other_year = int(input("Ingrese otro año: "))
#Comprueba el año actual con el otro año y muestra un mensaje según quien sea mayor o si son iguakes
if actual_year > other_year:
    print("Han pasado "  + str(actual_year-other_year) + " años desde " + str(other_year))
elif actual_year<other_year:
    print("Faltan " + str(other_year-actual_year) + " años para llegar a " + str(other_year))
elif actual_year == other_year:
    print("Ambos años son iguales!!")

# Ejercicio 13
# Atrapa la "excepción ValueError y termina el código".
try:
    numbr_a = int(input("Ingrese un numero: "))
    numbr_b = int(input("Ingrese un segundo numero: "))
except ValueError:
    print("Error: Se ha ingresado un valor erroneo.")
    exit()
# Si uno de los números es negativo, el código se termina
if numbr_a < 0 or numbr_b < 0:
    print("Error: Se han ingresado numeros negativos.")
    exit()

# Comprueba qué número es el mayor y el menor
if numbr_a < numbr_b:
    greater = numbr_b
    lesser = numbr_a
else:
    greater = numbr_a
    lesser = numbr_b

# Permite al usuario saber si el número mayor es múltiplo del menor
if greater % lesser == 0:
    print(str(greater) + " es multiplo de: " + str(lesser))
else:
    print(str(greater) + " no es multiplo de:  " + str(lesser))

# Ejercicio 14
print("ax + b = 0")
print("--------------")
#Pide que ingrese los números de los coeficiente
a = int(input("Ingrese el valor para el coeficiente 'a': "))
b = int(input("Ingrese el valor para el coeficiente 'b': "))
print("--------------")
#Guarda el valor de -b/a en la variable x
x = -b/a
#Imrpime el resultado
print(f"La solucion a la ecuacion {a}x + {b} = 0 es x = {x}")

# Ejercicio 15
print("Para calcular el area de un triangulo, ingrese T")
print("Para calcular el area de un circulo, ingrese C")
print("--------------")
usr_input = input("Ingrese su eleccion: ").lower()
#Comprueba la entrada y muestra al área segunda si eligio triángulo o círculo
if usr_input == 't':
    base = int(input("Ingrese la base del triangulo: "))
    height = int(input("Ingrese la altura del triangulo: "))
    #Muestra el área del triángulo
    print(f"El area del triangulo es de {(base*height)/2}")

elif usr_input == 'c':
    radius = int(input("Ingrese el radio del circulo: "))
    
    print(f"El area del circulo es de {radius**2 * 3.14159265359}")

else:
    print("Esa no es una opcion.")
    exit()

# Ejercicio 16
#Pide los números 
numbr_a = int(input("Ingrese el primer numero: "))
numbr_b = int(input("Ingrese el segundo numero: "))
#Muestra las opciones
print("---------------")
print("1) Suma")
print("2) Resta")
print("3) Multiplicacion")
print("4) Division")
usr_input = int(input("Ingrese el numero de operacion que quiera realizar: "))
#Comprueba si la opción y muestra segun la opcón ingresada
if usr_input < 0 or usr_input > 4:
    print("Error: Numero no valido")
    exit()
elif usr_input == 1:
    print(numbr_a + numbr_b)
elif usr_input == 2:
    print(numbr_a - numbr_b)
elif usr_input == 3:
    print(numbr_a * numbr_b)
elif usr_input == 4:
    print(numbr_a / numbr_b)

# Ejercicio 17
# Lista con todos los días posibles
week_days = ['domingo', 'lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado']

usr_inp = input("Ingrese un dia de la semana: ").lower()
# Si la entrada no está en la lista de días posibles, salir del programa
if usr_inp not in week_days:
    print("Error: Ese no es un dia de la semana")
    exit()
# Comprueba la entrada y da un mensaje según el día
elif usr_inp == week_days[1]:
    print("A comenzar la semana!!")
elif usr_inp == week_days[5]:
    print("Ultimo dia de la semana!!")
elif usr_inp == week_days[6] or usr_inp == week_days[0]:
    print("Hoy es fin de semana, a descansar!!")
else:
    print("Dia de semana, a trabajar!!")

# Ejercicio 18
# Atrapa la excepción de ValueError
try:
    usr_hr = int(input("Cuantas horas has trabajado este mes? "))
    usr_pay = int(input("Cuanto cobras por hora? "))
except ValueError:
    print("Error: Valor no valido")
    exit()
print("----------------------")
if usr_hr < 48:
    print("Error: La jornada laboral minima es de 48 horas")
    exit()
else:
    # Comprueba si el usuario tiene más de 48 horas
    print(f"Pago por jornada laboral 48 horas: {usr_hr*usr_pay}")
    if usr_hr>48:
        print(f"Pago por {(usr_hr-48)} hora/s extra: {(usr_hr-48)*(usr_pay+usr_pay*0.10)}")

# Ejercicio 19
print("Cuantos lapices se compraran?\nCada lapiz cuesta $60, con un descuento por comprar 1000 o mas")
# Atrapa la excepción de ValueError
try:
    usr_inp = int(input("Lapices a comprar: "))
except ValueError:
    print("Error: Valor no valido")
    exit()
print("----------------------")
#Comprueba la entrada y si es mayor a 1000 muestra un mensaje y si es menor otro mensaje 
if usr_inp<1000:
    print(f"El precio a pagar por {usr_inp} lapices es de: {usr_inp*60}")
else:
    print(f"Tienes un descuento del 7%!!")
    print(f"El precio a pagar por {usr_inp} lapices es de: {(usr_inp*(60*0.93))}")

# Ejercicio 20
usr_score = []
#Recorre del 0 al 3
for i in range(0,4):
    try:
        usr_score.append(int(input(f"Ingrese la nota para el trabajo numero {i+1}: ")))
    except ValueError:
        print("Error: Valor invalido")
        exit()
    if usr_score[i]<1:
        print("Error: Valor invalido")
        exit()

usr_average = 0
#Optiene el promedio
for score in usr_score:
    usr_average += score

usr_average = usr_average / len(usr_score)
print(f"Su promedio es de {usr_average}")
#Valida el promedio y depende de cuanto saco es el mensaje que muestra 
if usr_average>=6:
    print("Usted ha aprobado")
else:
    print("Usted no ha aprobado")
