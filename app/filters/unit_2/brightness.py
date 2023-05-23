import numpy as np
from global_variables.variables import ruta_base
from tkinter import NW, Image, messagebox
from ui.ui import ventana

def brillo():
    nombre = 'grises.gif'
    im = Image.open(ruta_base + nombre)
    im9 = im
    arreglo = np.array(im9.size)  
    total = arreglo[0] * arreglo[1]
    i = 0
    suma = 0
    while i < im9.size[0]:
        j = 0
        while j < im9.size[1]:
            suma = suma + im9.getpixel((i, j))
            j+=1
        i+=1
    brillo = suma / total 
    brillo = int(brillo)
    brillo = messagebox.showinfo("BRILLO:", ("El Brillo De La Imagen Es:==> ", brillo))
    ventana.mainloop()