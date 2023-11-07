class Persona:
    def __init__(self, nombre="", edad=0, dni=""):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni

    # Getter y Setter para el nombre
    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    # Getter y Setter para la edad
    def get_edad(self):
        return self.__edad

    def set_edad(self, edad):
        if edad >= 0:
            self.__edad = edad
        else:
            print("La edad no puede ser negativa")

    # Getter y Setter para el DNI
    def get_dni(self):
        return self.__dni

    def set_dni(self, dni):
        if len(dni) == 8:
            self.__dni = dni
        else:
            print("El DNI debe tener 8 dígitos")
    #Mostrar la informacion dada
    def mostrar(self):
        print(f"Nombre: {self.__nombre}")
        print(f"Edad: {self.__edad}")
        print(f"DNI: {self.__dni}")

    def esMayorDeEdad(self):
        return self.__edad >= 18



# Ejemplo de uso:
persona1 = Persona()
persona1.set_nombre("Augusto Riquelme")
persona1.set_edad(18)
persona1.set_dni("46163488")
persona1.mostrar()