# Importar la librería para generar números aleatorios
import random


# ==========================================
# FUNCIÓN PARA MOSTRAR EL MENÚ
# ==========================================

def mostrar_menu():

    print("\n===================================")
    print("       ADIVINA EL NÚMERO")
    print("===================================")
    print("1. Jugar")
    print("2. Ver puntuación")
    print("3. Ver historial")
    print("4. Salir")
    print("===================================")


# ==========================================
# FUNCIÓN PARA JUGAR UNA PARTIDA
# ==========================================

def jugar_partida():

    # Generar un número secreto entre 1 y 100
    numero_secreto = random.randint(1, 100)

    # Contador de intentos
    intentos = 0

    # Máximo de intentos permitidos
    max_intentos = 7

    # Variable para saber si el jugador ganó
    gano = False

    print("\n===================================")
    print("          NUEVA PARTIDA")
    print("===================================")
    print("He generado un número entre 1 y 100.")
    print("Tienes máximo 7 intentos para adivinarlo.")

    # Repetir mientras tenga intentos disponibles
    while intentos < max_intentos and gano == False:

        # Pedir un número al usuario
        numero = int(input("\nIngrese un número entre 1 y 100: "))

        # Aumentar el contador de intentos
        intentos = intentos + 1

        # Comparar el número ingresado con el número secreto
        if numero < numero_secreto:

            print("El número secreto es mayor.")

        elif numero > numero_secreto:

            print("El número secreto es menor.")

        else:

            print("\n¡Felicidades!")
            print("Adivinaste el número secreto.")
            print("Número de intentos:", intentos)

            # El jugador ganó
            gano = True

    # Comprobar si ganó
    if gano == True:

        resultado = "Ganó"
        puntos = 10

        print("¡Ganaste 10 puntos!")

    # Si no ganó después de 7 intentos, pierde
    else:

        resultado = "Perdió"
        puntos = 0

        print("\nSe acabaron tus 7 intentos.")
        print("¡Perdiste la partida!")
        print("El número secreto era:", numero_secreto)

    # Devolver los datos de la partida
    return resultado, intentos, puntos


# ==========================================
# FUNCIÓN PARA MOSTRAR LA PUNTUACIÓN
# ==========================================

def mostrar_puntuacion(puntuacion):

    print("\n===================================")
    print("           PUNTUACIÓN")
    print("===================================")
    print("Puntuación actual:", puntuacion, "puntos")


# ==========================================
# FUNCIÓN PARA MOSTRAR EL HISTORIAL
# ==========================================

def mostrar_historial(historial):

    print("\n===================================")
    print("       HISTORIAL DE PARTIDAS")
    print("===================================")

    # Comprobar si existen partidas
    if len(historial) == 0:

        print("Todavía no has jugado ninguna partida.")

    else:

        # Recorrer el historial
        for partida in historial:

            print(
                "Partida", partida["numero"],
                "| Resultado:", partida["resultado"],
                "| Intentos:", partida["intentos"],
                "| Puntos:", partida["puntos"]
            )