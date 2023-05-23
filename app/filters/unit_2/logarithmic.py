import numpy as np
from global_variables.variables import ruta_base
from tkinter import NW, canvas, Image, PhotoImage, messagebox
from ui.ui import ventana, entrada, canvas

def logaritmica():
    nombre = 'grises.gif'
    im = Image.open(ruta_base + nombre)
    ima = im
    arreglo = np.array(ima.size)
    L = 255
    reg1=0
    while reg1<arreglo[0]:
        col1=0
        while col1<arreglo[1]:
            nivel = ima.getpixel((reg1, col1))
            new_nivel = L * np.log(1 + nivel) / np.log(1 + L)
            new_nivel = int(new_nivel)
            if new_nivel >= 255:
                new_nivel = 255
            ima.putpixel((reg1, col1), (new_nivel))
            col1+=1
        reg1+=1
    ima.save(ruta_base + 'logaritmica.gif') 
    imagen_l = PhotoImage(file = ruta_base + 'logaritmica.gif')
    global loga
    loga = canvas.create_image(600, 160, anchor=NW, image=imagen_l)
    ventana.mainloop()  