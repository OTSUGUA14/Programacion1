import random
#Funcion para validar si hizo bingo
def find (cardboard):
    for i in range(5):
        if cardboard[i][0]==cardboard[i][1]==cardboard[i][2]==cardboard[i][3]==cardboard[i][4]:
            
            if cardboard[0][i]==cardboard[1][i]==cardboard[2][i]==cardboard[3][i]==cardboard[4][i]:
                print("Felicidades conseguiste completar la fila: ", (i+1)," Y la columna: ", (i+1))
                return True
            else:
                print("Felicidades conseguiste completar la fila: ", (j+1))

                return True
    for i in range(5):
        if cardboard[0][i]==cardboard[1][i]==cardboard[2][i]==cardboard[3][i]==cardboard[4][i]:
            print("Felicidades conseguiste completar la columna: ", (j+1))

    if cardboard[0][0]==cardboard[1][1]==cardboard[2][2]==cardboard[3][3]==cardboard[4][4]:
        print("Felicidades conseguiste completar la diagonal principal")
        return True
    if cardboard[0][4]==cardboard[1][3]==cardboard[2][2]==cardboard[3][1]==cardboard[4][0]:
        print("Felicidades conseguiste completar la diagonal secundaria")
        return True
        
#Funcion para mostrar el carton
def show(car):
    for i in range(5):
        for j in range(5):
            print("{:<{}}".format(car[i][j],5), end=" ")
        print(" ")

#Funcion donde se muestran los número que salen
def bingo(cardboard, cardboard_comp):
    follow = input("Presione enter o cualquier tecla para empezar a jugar: ")
    while True:

        number_random = num()
        #En caso de que el número ya haya salido el programa vuelve a empezar
        if number_random in last_numbers:
            continue
        else:
            print("El numero de bola que salio fue: ", number_random)
            print("-------------------------------------")
            #Guarda el número que salio en una lista
            last_numbers.append(number_random)
            #Muestra como queda el carton en caso de que el número que salio se encuentre en el carton
            if number_random in cardboard_comp:
                
                for i in range(5):
                    for j in range(5):
                        if number_random == cardboard[i][j]:
                            print("El número: ",cardboard[i][j], " fue encontrado en la posición: ", [i+1],[j+1])
                            print("-------------------------------------")
                            cardboard[i][j] = "X"

                print("El carton queda: ")
                print("-------------------------------------")
                show(cardboard)
                print("-------------------------------------")
                if find(cardboard):
                    print("--------------------------------")
                    last_numbers.clear()
                    break
                else:
                    follow = input("Presione enter o cualquier tecla para seguir: ")
                    print("--------------------------------")
            else:
                print("El número no fue encontrado")
                print("-------------------------------------")
                follow = input("Presione enter o cualquier tecla para seguir: ")
                print("--------------------------------")

#Funcion para sacar el número aleatorio
def num():

    number = random.randint(0, 75)

    return number



#Codigo principal
while True:
    print("Ingrese un valor dentro del rango 1 y 75 ")
    j = 0
    i = 0
    last_numbers = []
    aux = 25
    #Rellenar lista
    cardboard = [[0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0]]
    cardboard_comp = []

    for i in range(5):
        for j in range(5):

            while True:
                number = int(input("Ingrese un número: "))
                if (number < 1 or number > 75):
                    print("Error rango incorecto")
                    continue
                else:
                    if number in cardboard_comp:
                        print("El número ya fue ingresado ingrese otro número")
                        continue
                    #Cambiar valor en caso de que no se haya ingresado antes
                    else:
                        aux -= 1
                        cardboard_comp.append(number)
                        cardboard[i][j] = number
                        break

    bingo(cardboard,cardboard_comp)
    fin=input("Si quiere seguir jugando ingrese Y sino toque cualquier tecla: ").upper()
    if fin !="Y":
        print("Gracias por jugar :)")
        break
    else:
        print("Esa es la actitud")
        cardboard.clear()
        cardboard_comp.clear()
