class Cuenta:
    def __init__(self,titular, cantidad=0):
        self.__titular=titular
        self.__cantidad=cantidad
    # Getter para el titular
    def get_tiular(self):
        return self.__titular

    def get_cantidad(self):
        return self.__cantidad
    
      # Getter y Setter para la cantidad
    def mostrar(self):
        print(f"Titular: {self.__titular}")
        print(f"Cantidad: {self.__cantidad}")

    #Funcion para ingresar dinero
    def ingresar(self,cantidad):
        if cantidad>0:
            self.__cantidad+=cantidad
    
    #Funcion para retirar dinero
    def retirar(self,cantidad):
        self.__cantidad-=cantidad

#Ejemplo de uso
cuenta1 = Cuenta("Augusto", 1000.0)

cuenta1.mostrar()
print("-------------------")
cuenta1.ingresar(500.0)
cuenta1.mostrar()
print("-------------------")
cuenta1.retirar(200.0)
cuenta1.mostrar()