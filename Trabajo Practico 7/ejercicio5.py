def bubble_sort(array):
    size = len(array)
    for i in range(size):
        # El último i elementos ya están en su lugar correcto, así que no es necesario revisarlos nuevamente
        for j in range(0, size-i-1):
            # Intercambia si el elemento encontrado es mayor que el siguiente elemento
            if array[j] < array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array


list_num=[2,0,4,0,5,2,22,14,6,44,1]
print("Lista original: ", list_num)
print("Lista ordenada: ",bubble_sort(list_num))
