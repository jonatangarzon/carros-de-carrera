import tkinter as tk
import random

def mover_carros():
    global carrera_activa
    if not carrera_activa:
        return

    # Avanzar carro 1
    paso1 = random.randint(2, 8)
    canvas.move(carro1, paso1, 0)
    
    # Avanzar carro 2
    paso2 = random.randint(2, 8)
    canvas.move(carro2, paso2, 0)

    # Obtener coordenadas x2 (borde derecho de cada carro)
    x2_carro1 = canvas.coords(carro1)[2]
    x2_carro2 = canvas.coords(carro2)[2]

    # Verificar si alguno llegó a la meta
    if x2_carro1 >= meta_x or x2_carro2 >= meta_x:
        carrera_activa = False
        if x2_carro1 >= meta_x and x2_carro2 >= meta_x:
            ganador = "¡Empate!"
        elif x2_carro1 >= meta_x:
            ganador = "¡Ganó el Carro Rojo!"
        else:
            ganador = "¡Ganó el Carro Azul!"
        
        canvas.create_text(400, 200, text=ganador, fill="yellow", font=("Arial", 24, "bold"))
    else:
        # Repetir la función cada 30 ms para el movimiento continuo
        ventana.after(30, mover_carros)

def iniciar_carrera():
    global carrera_activa
    if not carrera_activa:
        carrera_activa = True
        mover_carros()

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Competencia de Carritos - Tema B")
ventana.geometry("800x450")

# Creación del Canvas
canvas = tk.Canvas(ventana, width=800, height=350, bg="#2d2d2d")
canvas.pack(pady=10)

# Dibujar la carretera (Líneas y Meta)
canvas.create_line(0, 50, 800, 50, fill="white", width=4)
canvas.create_line(0, 300, 800, 300, fill="white", width=4)

# Línea de Meta
meta_x = 730
canvas.create_line(meta_x, 50, meta_x, 300, fill="red", width=6)
canvas.create_text(meta_x + 35, 175, text="META", fill="white", font=("Arial", 12, "bold"))

# Dibujar los carros cuadrados (Objetos básicos)
# Carro 1 (Rojo - Carril Superior)
carro1 = canvas.create_rectangle(20, 85, 70, 135, fill="red", outline="white")

# Carro 2 (Azul - Carril Inferior)
carro2 = canvas.create_rectangle(20, 210, 70, 260, fill="blue", outline="white")

# Estado de la carrera
carrera_activa = False

# Botón para iniciar
btn_inicio = tk.Button(ventana, text="Iniciar Carrera", font=("Arial", 12, "bold"), command=iniciar_carrera)
btn_inicio.pack()

ventana.mainloop()








from tkinter import * 
import random
from turtle import width