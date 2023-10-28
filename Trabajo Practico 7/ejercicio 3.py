#Funcion para ordenar la lista de libros por un campo específico
def order(list_new):
    #Se puede modicar la clvae para que se ordene de otra forma
    return list_new["Año"]



list=[{"Libro": "El principito", "Autor":"Antoine de Saint-Exupéry","Año":1943},
      {"Libro": "Cien años de soledad", "Autor":"Gabriel García Márquez","Año":1967},
      { "Libro": "El señor de los anillos","Autor":"J. R. R. Tolkien","Año":1954},
      {"Libro":"Don Quijote de la Mancha","Autor": "Miguel de Cervantes","Año":1605}]
print("Lista original")
for i in list:
    print("Título: ", i['Libro']," Autor:" ,i['Autor'], "Año de publicación: ", i['Año'])
# Ordenar la lista de libros en este caso por el campo 'año' (o el campo deseado)
list=sorted(list,key=order)
print("--------------------------------------------")
print("Lista ordenada:")

for i in list:
    print("Título: ", i['Libro']," Autor: ",i['Autor']," Año de publicación: ", i['Año'])