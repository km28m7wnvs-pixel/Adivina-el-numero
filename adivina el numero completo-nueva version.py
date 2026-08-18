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


# ==========================================
# PROGRAMA PRINCIPAL
# ==========================================

# Puntuación inicial
puntuacion = 0

# Lista para almacenar el historial
historial = []

# Contador de partidas
numero_partida = 0

# Variable para controlar el programa
salir = False


# ==========================================
# BUCLE PRINCIPAL DEL PROGRAMA
# ==========================================

while salir == False:

    # Mostrar el menú
    mostrar_menu()

    # Pedir una opción al usuario
    opcion = input("Seleccione una opción: ")


    # ======================================
    # OPCIÓN 1: JUGAR
    # ======================================

    if opcion == "1":

        # Aumentar el número de partida
        numero_partida = numero_partida + 1

        # Ejecutar una partida
        resultado, intentos, puntos = jugar_partida()

        # Actualizar la puntuación
        puntuacion = puntuacion + puntos

        # Crear un registro de la partida
        partida = {
            "numero": numero_partida,
            "resultado": resultado,
            "intentos": intentos,
            "puntos": puntos
        }

        # Guardar la partida en el historial
        historial.append(partida)

        print("\nPuntuación acumulada:", puntuacion, "puntos")


    # ======================================
    # OPCIÓN 2: VER PUNTUACIÓN
    # ======================================

    elif opcion == "2":

        mostrar_puntuacion(puntuacion)


    # ======================================
    # OPCIÓN 3: VER HISTORIAL
    # ======================================

    elif opcion == "3":

        mostrar_historial(historial)


    # ======================================
    # OPCIÓN 4: SALIR
    # ======================================

    elif opcion == "4":

        print("\n===================================")
        print("           FIN DEL JUEGO")
        print("===================================")
        print("Puntuación final:", puntuacion, "puntos")
        print("Gracias por jugar.")
        print("¡Hasta luego!")

        # Terminar el programa
        salir = True


    # ======================================
    # OPCIÓN NO VÁLIDA
    # ======================================

    else:

        print("\nOpción no válida.")
        print("Seleccione una opción del 1 al 4.")
        