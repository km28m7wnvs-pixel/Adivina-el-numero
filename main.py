# Importar las funciones del archivo funciones.py
from funciones import mostrar_menu, jugar_partida, mostrar_puntuacion, mostrar_historial


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

