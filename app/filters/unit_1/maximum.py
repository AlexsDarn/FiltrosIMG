import numpy as np
from global_variables.variables import ruta_base
from tkinter import NW, Image, messagebox
from ui.ui import ventana

def maximo():
    nombre = 'grises.gif'
    im = Image.open(ruta_base + nombre)
    arreglo = np.array(im.size)
    mayor=255
    reg1=0
    while reg1<arreglo[0]:
        col1=0
        while col1<arreglo[1]:
            nivel=im.getpixel((reg1,col1))
            if nivel>mayor:
                mayor=nivel
            col1+=1
        reg1+=1
    messagebox.showinfo("MAXIMO:", ("El Nivel Maximo De Gris Es:==>", mayor))
    ventana.mainloop()