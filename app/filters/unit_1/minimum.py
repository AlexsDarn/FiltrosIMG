import numpy as np
from global_variables.variables import ruta_base
from tkinter import NW, Image, messagebox
from ui.ui import ventana

def minimo():
    nombre = 'grises.gif'
    im = Image.open(ruta_base + nombre)
    arreglo = np.array(im.size)
    menor=255
    reg1=0
    while reg1<arreglo[0]:
        col1=0
        while col1<arreglo[1]:
            nivel=im.getpixel((reg1,col1))
            if nivel<menor:
                menor=nivel
            col1+=1
        reg1+=1
    messagebox.showinfo("MINIMO:", ("El Nivel Minimo De Gris Es:==>", menor))
    ventana.mainloop()