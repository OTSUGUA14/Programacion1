def selection_sort(arr):
    n = len(arr)  
    for i in range(n):
        # Encontrar el valor mínimo en el arreglo sin ordenar
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Intercambiar el elemento mínimo encontrado con el primer elemento sin ordenar
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr



list_word=["poder","aprobar", "programacion","uno","con","esfuerzo"]
print("Lista original: ", list_word)
print("Lista ordenada: ",selection_sort(list_word) )