#EJERCICIO 1 FOR
#letras
letters="abcdefghijklmnñopqrstuvwxyz"
#lugar

place=int(input("ingrese la cantidad de lugares que correrán las letras que quiere realizar: "))
message1=input("ingrese el primer mensaje: ").lower() #transformar lo ingresado a minusculas
long=len(letters)
message1_new=""
message2_new=""
message3_new=""
message4_new=""
message5_new=""
for i in message1:
    
    if i in letters: #fijar si i esta en letters
        
        position=letters.index(i) #sacar la posicón y la guarda en la variable
        message1_new+=letters[(position+place)%27]  #guardar el la nueva letra en la nueva variable
    else:
        message1_new+=i  #en caso de que no este el digito en el string deja tal cual
  #en los otros for se repite lo mismo
message2=input("ingrese el segundo mensaje: ").lower()
for i in message2:
  
    if i in letters:
        position=letters.index(i)
        message2_new+=letters[(position+place)%27]
    else:
        message2_new+=i
message3=input("ingrese el tercer mensaje: ").lower()
for i in message3:
   
    if i in letters:
        position=letters.index(i)
        message3_new+=letters[(position+place)%27]
    else:
        message3_new+=i    
message4=input("ingrese el cuarto mensaje: ").lower()
for i in message4:
    if i in letters:
        position=letters.index(i)
        message4_new+=letters[(position+place)%27]
    else:
        message4_new+=i    
message5=input("ingrese el quinto mensaje: ").lower()
for i in message5:
    if i in letters:
        position=letters.index(i)
        message5_new+=letters[(position+place)%27]
    else:
        message5_new+=i    
print("")
print("El primer mensaje queda asi: ", message1_new)
print("El segundo mensaje queda asi: ", message2_new)
print("El tercer mensaje queda asi: ", message3_new)
print("El cuarto mensaje queda asi: ", message4_new)
print("El quinto mensaje queda asi: ", message5_new)


#EJERICIO 2 WHILE
print("EJERCICIO 2")

total_pairs=0
peers=0
odd=0
total_odd=0
while True:
    number=int(input("ingrese numeros enteros positivos para terminar ingrese el 0: "))
    #en caso de que sea cerro se termine el bucle
    if number ==0:
        break
    else:
        #transformar en string para recorrerlo
        for i in str(number):

            #validar que sea par con el resto del numero
            if int(i)%2==0: 
                peers +=1
                total_pairs +=1
            else:
                odd +=1
                total_odd +=1
        print("El numero tiene: " ,peers," digitos pares y: ", odd, " digitos impares")
        peers=0
        odd=0



print("La cantidad de pares totales son: ",  total_pairs)
print("La cantidad de pares totales son: ",  total_odd)