import numpy as np
from global_variables.variables import ruta_base
from tkinter import NW, Image, messagebox
from ui.ui import ventana

def contraste():
    nombre = 'grises.gif'
    im = Image.open(ruta_base + nombre)
    im10 = im
    arreglo = np.array(im10.size)  
    total = arreglo[0] * arreglo[1]
    i = 0
    suma = 0
    while i < im10.size[0]:
        j = 0
        while j < im10.size[1]:
            suma = suma + im10.getpixel((i, j))
            j+=1
        i+=1
    brillo = suma / total
    i = 0 
    while i < im10.size[0]:
        j = 0
        while j < im10.size[1]:
            aux = im10.getpixel((i,j)) - brillo 
            suma = suma + aux
            j+=1
        i+=1
    cont = np.sqrt(suma / total)
    contraste = int(cont)
    contraste = messagebox.showinfo("CONTRASTE:", ("El Contraste De La Imagen Es:==> ", contraste))
    ventana.mainloop()