class Triangulo:
    def __init__(self,lado1=0,lado2=0,lado3=0):
        self.__lado1=lado1
        self.__lado2=lado2
        self.__lado3=lado3
    def mostrar(self):
        if (self.__lado1>self.__lado2 and self.__lado1>self.__lado3):
            print(f"El valor del lado de mayor tamaño es de: {self.__lado1}")
        elif(self.__lado2>self.__lado1 and self.__lado2>self.__lado3):
            print(f"El valor del lado de mayor tamaño es de: {self.__lado2}")
        else:
            print(f"El valor del lado de mayor tamaño es de: {self.__lado3}")

        if (self.__lado1==self.__lado2 and self.__lado2==self.__lado3 and self.__lado1==self.__lado3):
            print("El triangulo es equilatero")
        elif(self.__lado1==self.__lado2 or self.__lado2==self.__lado3 or self.__lado1==self.__lado3):
            print("El triangulo es isoceles")
        else:
            print("El triangulo es escaleno")
#Caso de equilatero

triangulo=Triangulo(2,2,2)
triangulo.mostrar()
print("-----------------")
#Caso de isoceles
triangulo=Triangulo(2,5,2)
triangulo.mostrar()
print("-----------------")
#Caso de escaleno
triangulo=Triangulo(2,10,22)
triangulo.mostrar()