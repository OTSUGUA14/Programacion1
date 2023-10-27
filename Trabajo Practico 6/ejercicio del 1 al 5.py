#ejericico del 1 al 5
#Funcio para borar número
def delete(list,num):
    aux=0
    if num in list:
        while aux<len(list):
            if aux==0:
            
                position=list.index(num)
                print("la primera ocurrencia del número: ", num, " Fue eliminado")
                del list[position]
                aux+=1
            else:
                aux+=1
    else:
        print("El número no fue encontrado")
    return list
#Funcion para agregar las tuplas a la lista
def tupla(list):
    list_new=[]
    found=[]
    aux=0
    for i in range(len(list)):
        tuppla_add=()
        cant=0
        if list[i] in found:
            continue
        else:
            found.append(list[i])
            cant=0
            for j in range(len(list)):
                if list[i]==list[j]:
                    aux+=i
                    cant+=1
            list_new.insert(aux,(list[i],cant))
    
    return list_new
#Funcion para crear la lista con los números al numero ingresado
def minor(list,num):
    new_list=[]
    for i in range(len(list)):
        if list[i]<num:
            new_list.append(list[i])
    return new_list
#Funcion para sumar los elementos de la lista
def sum(lis):
    total=0
    for i in range(len(lis)):
        total+=lis[i]
    return total
#Ejericio 1
print("Para finalizar el programa ingrese 0")
list_numbers=[]
aux=0
while True:
    number=int(input("ingrese un número: "))
    if number==0:
        break
    else:
        list_numbers.append(number)



print("la lista queda: ", list_numbers)
original_list=[]
original_list=list(list_numbers)
#Fin ejericico 1
#Ejercicio 2
number=int(input("Ahora ingrese un número para borrar de la lista: "))

print("la lista queda: ", delete(list_numbers,number))
#Fin ejercicio 2
print("-------------------------------")
#Ejercicio 3
print("La sumatoria de los números de la lista es: ", sum(list_numbers))
#Fin ejercicio 3
print("----------------------")
#Ejercicio 4
number=int(input("Ingrese un nuevo número: "))
list_new=minor(list_numbers,number)
print("La lista queda asi: ", )
for i in list_new:
    print(i,end=" ")
print(" ")
#Fin ejercicio 4
#Ejercicio 5
list_tupla=tupla(original_list)
print("-------------------------------")
print("Lista original: ", original_list)

print("La nueva lista queda: ", list_tupla)
#Fin ejercicio 5