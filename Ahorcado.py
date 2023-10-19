import random

# Lista de palabras predefinidas
palabras = ["python", "programacion", "tecnologia", "desarrollo", "computadora", "inteligencia"]

# Función para seleccionar una palabra al azar
def seleccionar_palabra():
    return random.choice(palabras)

# Función para inicializar el tablero con guiones bajos
def inicializar_tablero(palabra):
    return ['_'] * len(palabra)

# Función para mostrar el tablero actual
def mostrar_tablero(tablero):
    return ' '.join(tablero)

# Función para jugar el juego
def jugar():
    palabra_secreta = seleccionar_palabra()
    intentos = 6
    tablero = inicializar_tablero(palabra_secreta)
    letras_adivinadas = []

    print("¡Bienvenido al Juego del Ahorcado!")
    
    while True:
        print(mostrar_tablero(tablero))
        letra = input("Ingresa una letra: ").lower()

        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, ingresa una letra válida.")
            continue

        if letra in letras_adivinadas:
            print("Ya has adivinado esta letra. Intenta con otra.")
            continue

        if letra in palabra_secreta:
            letras_adivinadas.append(letra)
            for i in range(len(palabra_secreta)):
                if palabra_secreta[i] == letra:
                    tablero [i] = letra
            print("Adivinaste una letra correctamente!")
        else:
            intentos -= 1
            print(f"Letra incorrecta. Te quedan {intentos} intentos.")

        if ''.join(tablero) == palabra_secreta:
            print("¡Felicidades! Has adivinado la palabra: " + palabra_secreta)
            break

        if intentos == 0:
            print("¡Oh no! Te quedaste sin intentos. La palabra era: " + palabra_secreta)
            break

if __name__ == "__main__":
    jugar()