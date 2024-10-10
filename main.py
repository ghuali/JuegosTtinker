import tkinter as tk
from cProfile import label
from codeop import compile_command
from tkinter import ttk, messagebox, Canvas, PhotoImage
from PIL import Image, ImageTk
import random
import os

from PIL.ImageOps import expand


def menu():
    root.title("Juegos varios")
    root.resizable(width=False,height=False)
    root.geometry("600x600")
    canvas = tk.Canvas(root,width=600,height=600,background='white')
    canvas.pack(fill = "both",expand = True)


    image = Image.open("Imagenes/Menu.jpg").resize((600,600))
    photo = ImageTk.PhotoImage(image)
    canvas.create_image(0,0,image = photo,anchor = "nw")
    boton1 = ttk.Button(root,text="piedra papel tijera", command=piedra_papel_tijera)
    boton1.place(x=300,y=240,anchor = "center",width = 150)
    boton2 = ttk.Button(root,text="adivinar numero", command=juego_adivinar_numero )
    boton2.place(x=300, y=290, anchor="center",width = 150)
    boton3 = ttk.Button(root,text="Traducir palabras",command=juego_traducir_palabras)
    boton3.place(x=300, y=340, anchor="center",width = 150)
    boton4 = ttk.Button(root,text="Salir",command=root.destroy)
    boton4.place(x=300, y = 380,anchor="center",width= 150)
    canvas.create_text(300, 100, fill="white", font="Times 100 bold",
                       text="Elige")
    root.mainloop()



def juego_adivinar_numero():
    root.destroy()
    root2 = tk.Tk()
    root2.resizable(width=False,height=False)
    root2.title("Juego Adivinar numero")
    root2.geometry("600x600")
    canvas = tk.Canvas(root2, width=600, height=600, background='white')
    canvas.pack(fill="both", expand=True)
    image = Image.open("Imagenes/HaloPensar.jpg").resize((600, 400))
    photo = ImageTk.PhotoImage(image)
    canvas.create_image(0, 0, image=photo, anchor="nw")

    canvas = tk.Canvas(root2,width=600,height=600)
    canvas.pack(fill = "both",expand = True)

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
    root.destroy()
    root3 = tk.Tk()
    root3.resizable(width=False, height=False)
    root3.title("Juego Traducir palabra")
    root3.geometry("600x600")
    canvas = tk.Canvas(root3, width=600, height=600, background='white')
    canvas.pack(fill="both", expand=True)
    image = Image.open("Imagenes/SolKyTalking.jpg.jpg").resize((600, 400))
    photo = ImageTk.PhotoImage(image)
    canvas.create_image(0, 0, image=photo, anchor="nw")

    canvas = tk.Canvas(root3, width=600, height=600)
    canvas.pack(fill="both", expand=True)

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

    print(f"\nHas obtenido {puntuacion} puntos.")

    root3.mainloop()

def jugar(opcion_jugador, opcion_maquina):
    return tabla_resultados[opcion_jugador][opcion_maquina]

def piedra_papel_tijera():
    root.destroy()
    root4 = tk.Tk()
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

tabla_resultados = {
    "piedra": {"piedra": 2, "papel": 1, "tijera": 0},
    "papel": {"piedra": 0, "papel": 2, "tijera": 1},
    "tijera": {"piedra": 1, "papel": 0, "tijera": 2}
}


menu()