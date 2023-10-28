def insertion_sort(arr):
    n = len(arr)
    
    # Recorremos desde el segundo elemento hasta el último
    for i in range(1, n):
        # Guardamos el valor actual para compararlo e insertarlo en la posición correcta
        current_value = arr[i]
        position = i
        
        # Movemos los elementos mayores hacia la derecha
        while position > 0 and len(arr[position - 1]) > len(current_value):
            arr[position] = arr[position - 1]
            position -= 1
        
        # Insertamos el valor actual en la posición correcta
        arr[position] = current_value
    return arr

list_string=["Agua","Fuego","Tierra","Aire","Energia"]
print("Lista original: ", list_string)
print("Lista ordenada: ", insertion_sort(list_string))