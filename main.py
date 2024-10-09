import tkinter as tk
from cProfile import label
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import random
import os


root = tk.Tk()
root.resizable(False, False)
root.title("Juegos varios")

def piedra():

    es_valido = False

    while not es_valido:
        try:
            seleccion_juego = int(input("Elige un juego (1-3): "))
            if seleccion_juego == 1:
                piedra_papel_tijera()
                es_valido = True
            elif seleccion_juego == 2:
                juego_traducir_palabras()
                es_valido = True
            elif seleccion_juego == 3:
                juego_adivinar_numero()
                es_valido = True
            else:
                print("Opción no reconocida. Por favor, elige una opción válida.")
        except ValueError:
            print("Por favor, introduce un número válido.")

def juego_adivinar_numero():
    intentos_restantes = 3
    numero_aleatorio = random.randint(0, 200)
    print("\nAdivina el número del 0 al 200")

    while intentos_restantes > 0:
        try:
            numero_usuario = int(input("Escoge un número: "))
            if numero_usuario == numero_aleatorio:
                print(f"¡Has ganado! El número era {numero_aleatorio}.")
                break
            else:
                intentos_restantes -= 1
                pista = "menor" if numero_usuario > numero_aleatorio else "mayor"
                if intentos_restantes > 0:
                    print(f"Pista: El número es {pista}. Te quedan {intentos_restantes} intentos.")
                else:
                    print(f"Has perdido. El número era {numero_aleatorio}.")
        except ValueError:
            print("Por favor, introduce un número válido.")

    print("Volviendo al menú principal...\n")


def juego_traducir_palabras():
    palabras_a_traducir = {
        "House": "Casa", "Tree": "Árbol", "Phone": "Teléfono", "Table": "Mesa",
        "Sky": "Cielo", "Sun": "Sol", "Moon": "Luna", "Book": "Libro",
        "Pen": "Pluma", "Computer": "Computadora", "Water": "Agua", "Fire": "Fuego",
        "Food": "Comida", "Air": "Aire", "Road": "Carretera", "Bridge": "Puente",
        "Chair": "Silla", "Door": "Puerta", "Window": "Ventana", "Star": "Estrella"
    }

    print("\nTraduce las siguientes palabras:")
    puntuacion = 0

    for _ in range(5):
        palabra_aleatoria = random.choice(list(palabras_a_traducir.keys()))
        respuesta = input(f"Traduce la palabra '{palabra_aleatoria}': ").strip().capitalize()

        if respuesta == palabras_a_traducir[palabra_aleatoria]:
            print("¡Correcto!")
            puntuacion += 1
        else:
            print(f"Incorrecto. La respuesta correcta era: {palabras_a_traducir[palabra_aleatoria]}")

    print(f"\nHas obtenido {puntuacion} puntos.\nVolviendo al menú principal...\n")


tabla_resultados = {
    "piedra": {"piedra": 2, "papel": 1, "tijera": 0},
    "papel": {"piedra": 0, "papel": 2, "tijera": 1},
    "tijera": {"piedra": 1, "papel": 0, "tijera": 2}
}

def jugar(opcion_jugador, opcion_maquina):
    return tabla_resultados[opcion_jugador][opcion_maquina]

def piedra_papel_tijera():
    print("\n--- Piedra, Papel o Tijera ---")
    while True:
        print("Opciones: Piedra, Papel, Tijera")
        opcion_jugador = input("Elige una opción: ").lower()

        if opcion_jugador in tabla_resultados:
            opcion_maquina = random.choice(list(tabla_resultados.keys()))
            resultado_juego = jugar(opcion_jugador, opcion_maquina)

            print(f"\nEl jugador ha elegido {opcion_jugador}, la máquina ha elegido {opcion_maquina}\n")
            if resultado_juego == 0:
                print("¡Ha ganado el jugador!")
            elif resultado_juego == 1:
                print("¡Ha perdido el jugador!")
            else:
                print("Hubo un empate.")
            break
        else:
            print("Opción no reconocida. Por favor, elige nuevamente.")

    print("Volviendo al menú principal...\n")


# Iniciar el programa
if __name__ == "__main__":

