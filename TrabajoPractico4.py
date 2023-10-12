
#EXERCISE 1
print("Ejercicio 1")

x = 0   # Initialize the variable 'x' to 0.

while(x < 30):  # Start a while loop that runs as long as 'x' is less than 30.
    x += 1      # Increment 'x' by 1 in each iteration.
    if (x == 4 or x == 6 or x == 10):   # Check if 'x' is equal to 4, 6, or 10
        print('Se saltó el valor ',  x, ' de x')    # Print a message indicating that the value was skipped.
        continue    # Skip the rest of the loop for this iteration and move to the next one.
    if (x == 15):   # Check if 'x' is equal to 15.
        print('La ejecución del bucle se interrumpe cuando x valía ', x)    # Print a message indicating that the loop was interrupted when 'x' was 15.
        break
    print('El valor del bucle es: ', x)   # Print the current value of 'x' for all other cases.


#EXERCISE 2
print("Ejercicio 2")

# Prompt the user to input 5 sentences and convert them to uppercase.
str1 = input("Ingrese una oracion 1 para convertir a mayusculas: ").upper()
str2 = input("Ingrese una oracion 2 para convertir a mayusculas: ").upper()
str3 = input("Ingrese una oracion 3 para convertir a mayusculas: ").upper()
str4 = input("Ingrese una oracion 4 para convertir a mayusculas: ").upper()
str5 = input("Ingrese una oracion 5 para convertir a mayusculas: ").upper()

# Print an empty line for formatting.
print("")

# Print the sentences that were entered in uppercase.
print("Las oraciones ingresadas convertidas a mayusculas quedan: ")
print(str1)
print(str2)
print(str3)
print(str4)
print(str5)


#EXERCISE 3
print("Ejercicio 3")

option = ""  # Variable to store user's menu choice
balance = 0 # Variable to store the account balance
balance_input = 0    # Variable to store the user's input for deposit/withdrawal amounts


print("Bienvenido")
while(option != "d" or option != "r" or  option != "s" or option != "x"):   # Create a loop to interact with the user
    print("Por favor pulse: \n 'D' para hacer un deposito \n 'R' para hacer un retiro \n 'S' para ver su saldo \n 'X' para salir")   # Display options to the user
    option = input("").lower()  # Get user input and convert it to lowercase for easier comparison
    
    if option == "d": # User chose to make a deposit
        balance_input = int(input("Ingrese la cantidad a Depositar: \n"))  # Get the amount to deposit from the user
        if (balance_input >= 1):
            balance += balance_input
        else:
            print("No se puede ingresar esa cantidad de dinero")
        print("Su saldo Actual es: ", balance)
        print("")
        continue

    if option == "r": # User chose to make a withdrawal
        print("Su saldo es: ", balance)
        balance_input = int(input("Ingrese la cantidad a Retirar: \n"))      # Display the current balance and get the withdrawal amount from the user
        if (balance_input > 0 and (balance - balance_input) > 0 and balance >= balance_input):
            balance -= balance_input
        else: 
            print("No se puede retirar esa cantidad")
        print("Su saldo Actual es: ", balance)
        print("")
        continue

    if option == "s":   # User chose to check their balance
        print("Su saldo Actual es: ", balance)   # Display the current balance to the user
        print("")
        continue

    if option == "x": # Exit the loop if the user selects 'x'
        break
    
print("")
print("Su saldo Actual es: ", balance)
print("Muchas gracias por usar nuestros Servicios")

#EXERCISE 4
print("Ejercicio 4")

num = 1  # Initialize a variable for user input
prime_number = 0    # Initialize a variable to count prime numbers
divisors=0  # Initialize a variable to count divisors
div = 0      # Initialize a variable for divisor calculation


while (num > 0):
    num= int(input("Ingrese un numero positivo mayor que 0: ")) # Prompt the user for a positive number
    div = num   # Initialize the divisor with the user's input
    for i in range(num):    # Iterate through numbers from 1 to 'num'
        if(num % div == 0): 
            divisors +=1    # If 'num' is divisible by 'div', increment the divisors count
        div -= 1
    if divisors == 2:
        prime_number += 1    # If there are exactly 2 divisors, 'num' is prime, so increment the prime count
    divisors = 0# Reset the divisors count for the next input

print("La cantidad de primos ingresada fueron: ", prime_number) # Print the count of prime numbers

#EXERCISE 5
print("Ejercicio 5")

year = int(input("Ingrese un año: "))    # Input for the starting year
year_1 = int(input("Ingrese otro año: "))   # Input for the ending year
leap_year =0    # Initialize a variable to count leap years

# Ensure the starting year is smaller than the ending year
if (year_1 < year):
    aux = year
    year = year_1
    year_1=aux

for i in range(year, year_1+1):     # Iterate through the range of years from 'year' to 'year_1'
    if (i % 4 == 0) and ((i % 100 != 0) or (i % 400 == 0)) and (i % 10 == 0):   # Check if the year is a leap year:
        print(i)# Print the leap year
        leap_year +=1# Increment the leap year count
        print(leap_year)
print("La cantidad de años bisiestos en el rango ", year, " y ", year_1, " es : ", leap_year)   # Print the count of leap years within the specified range

#EXERCISE 6
print("Ejercicio 6")

for i in range(1, 21):  # Iterate through numbers from 1 to 20 using a for loop
    if i % 2 != 0:  # Check if the current number 'i' is not divisible by 2 
        continue    # If 'i' is odd, continue to the next iteration without executing the next lines
    print(i)    # If 'i' is even, print it

#EXERCISE 7
print("Ejercicio 7")

list_1 = [1, 45, 32, 0, 21, 100, 3, 5, 79, 69, 39]      # Define a list of numbers
number_to_search = int(input("Ingrese un numero  para buscar "))    # Prompt the user to enter a number to search for

for i in range(len(list_1)):    # Use a for loop to iterate through the elements of the list
    if list_1[i] == number_to_search:   # Check if the current element at index 'i' in the list matches the number to search for
        print("El numero fue encontrado dentro de la lista ")    
        break   # Exit the loop as soon as the number is found
else:
    print("El numero no fue encontrado")     # If the loop completes without finding the number, print a message indicating that it was not found


#EXERCISE 8
print("Ejercicio 8")

option = 0  # Initialize the 'option' variable

while (option != 1 and option != 2 and option != 3):    # Create a loop that continues until the user selects option 1, 2, or 3
    option = int(input("Seleccione una opcion: \n 1 \n 2 \n 3 \n")) # Prompt the user to select an option
    
    # Check the user's choice and print a corresponding message
    if option == 1:
        print("Seleciciono la opcion 1")
    elif option == 2:
        print("Seleciciono la opcion 2")
    elif option == 3:
        print("Seleciciono la opcion 3")
    elif ( option == 0):
        break# Exit the loop if the user selects option 0