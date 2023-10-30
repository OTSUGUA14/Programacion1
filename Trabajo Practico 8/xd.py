def encontrar_posiciones(a, b, inicio=0):
    # Inicializamos una lista para almacenar las posiciones de coincidencia
    posiciones = []

    # Buscamos la primera ocurrencia de b en a a partir de la posición 'inicio'
    indice = a.find(b, inicio)

    if indice != -1:
        # Si se encontró una coincidencia, la agregamos a la lista de posiciones
        posiciones.append(indice)

        # Llamamos recursivamente a la función para buscar el resto de las coincidencias
        posiciones.extend(encontrar_posiciones(a, b, indice + 1))

    return posiciones

# Ejemplo de uso
a = "abracadabraabracadabra"
b = "abra"
resultados = encontrar_posiciones(a, b)
print(resultados)  # Debería imprimir [0, 11]