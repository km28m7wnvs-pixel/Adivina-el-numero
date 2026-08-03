# Juego: Adivina el número

import random

# Generar el número secreto del juego
numero_secreto = random.randint(1, 100)

print("--------------------------------")
print("      JUEGO: ADIVINA EL NÚMERO")
print("--------------------------------")
print("Adivina un número entre 1 y 100")
print("¡Buena suerte!")

# Mantener el juego activo hasta acertar
while True:

    # Pedir la respuesta del jugador
    numero = int(input("Ingresa tu número: "))

    # Comparar la respuesta con el número secreto
    if numero == numero_secreto:
        print("--------------------------------")
        print("¡Felicidades! Ganaste.")
        print("Adivinaste el número correcto.")
        print("--------------------------------")
        break

    # Si la respuesta es incorrecta, seguir intentando
    else:
        if numero < numero_secreto:
            print("El número secreto es mayor.")
            print("Intenta nuevamente.")

        else:
            print("El número secreto es menor.")
            print("Intenta nuevamente.")

# Finalizar el juego
print("Gracias por jugar. ¡Hasta la próxima!")
