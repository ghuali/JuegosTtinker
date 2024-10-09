import tkinter as tk
from cProfile import label
from tkinter import ttk, messagebox, Canvas, PhotoImage
from PIL import Image, ImageTk
import random
import os

from PIL.ImageOps import expand


def menu():
    canvas = tk.Canvas(root,width=600,height=600,background='white')
    canvas.pack(fill = "both",expand = True)

    canvas.create_text(100,10,fill="white",font="Times 20 italic bold",
                        text="Click the bubbles that are multiples of two.")
    image = Image.open("Imagenes/Menu.jpg").resize((800,800))
    photo = ImageTk.PhotoImage(image)
    canvas.create_image(0,0,image = photo,anchor = "nw")
    boton1 = ttk.Button(root,text="piedra papel tijera", command=piedra_papel_tijera)
    boton1.place(x=300,y=240,anchor = "center",width = 150)
    boton2 = ttk.Button(root,text="adivinar numero", command=juego_adivinar_numero)
    boton2.place(x=300, y=290, anchor="center",width = 150)
    boton3 = ttk.Button(root,text="Traducir palabras",command=juego_traducir_palabras)
    boton3.place(x=300, y=340, anchor="center",width = 150)
    root.mainloop()



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

root = tk.Tk()
root.title("Juegos varios")
tabla_resultados = {
    "piedra": {"piedra": 2, "papel": 1, "tijera": 0},
    "papel": {"piedra": 0, "papel": 2, "tijera": 1},
    "tijera": {"piedra": 1, "papel": 0, "tijera": 2}
}


menu()