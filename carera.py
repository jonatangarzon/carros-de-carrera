from tkinter import *
import random
from turtle import width







# -----------------
# ventana principal
# -----------------
ventana_principal = Tk()
ventana_principal.title("carritos")
ventana_principal.resizable(False, False)
ventana_principal.geometry("800x500")
ventana_principal.config(bg="#4cacc8")

# frame de graficacion
frame_graficacion = Frame(ventana_principal)
frame_graficacion.config(bg="#73b159", width=800, height=500)
frame_graficacion.place(x=0,y=250)

frame_graficacion = Frame(ventana_principal)
frame_graficacion.config(bg="black", width=800, height=90)
frame_graficacion.place(x=0,y=200)

frame_graficacion = Frame(ventana_principal)
frame_graficacion.config(bg="black", width=800, height=90)
frame_graficacion.place(x=0,y=410)

#----------------------------
# Círculos
#----------------------------
circulo_1 = Frame(ventana_principal)
circulo_1.config(bg="white", width=100, height=100)
circulo_1.place(x=40, y=50)

circulo_2 = Frame(ventana_principal)
circulo_2.config(bg="white", width=100, height=100)
circulo_2.place(x=200, y=50)

# crear carros 

#---------------------
# carro 1
#-----------------
carro_1 = Frame(ventana_principal)
carro_1.config(bg="red", width=100, height=50)
carro_1.place(x=40, y=180)

#-------------------
# carro 2
#-------------------
carro_2 = Frame(ventana_principal)
carro_2.config(bg="blue", width=100, height=50) 
carro_2.place(x=40, y=400)


#-------------------
# crear meta
#-------------------
meta = Frame(ventana_principal)
meta.config(bg="green", width=20, height=400)
meta.place(x=780, y=0)


# desplegar ventana
ventana_principal.mainloop()
