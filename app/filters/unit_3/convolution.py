import numpy as np
from global_variables.variables import ruta_base
from tkinter import NW, canvas, Image, PhotoImage, messagebox
from ui.ui import ventana, entrada, canvas

def convolucion():    
    datos = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]
    datos=np.asarray(datos)
    nombre = 'grises.gif'
    im = Image.open(ruta_base + nombre)
    ima = im
    dimension = datos.shape[0]
    datos = np.asarray(datos, dtype = np.float32)
    datos = datos.reshape(dimension, dimension)
    [col,ren] = ima.size
    imagen1 = np.asarray(ima, dtype = np.float32)
    imagen2 = imagen1
    i = 0
    while i < ren-dimension:     
        j = 0
        while j < col-dimension:
            sub = imagen1[i:(dimension + i), j:(dimension + j)]
            suma = 0
            r = 0
            while r < dimension:     
                c=0
                while c < dimension:
                    suma = suma + sub[r,c] * datos[r,c]
                    c+=1
                r+=1
            valor = suma / (dimension * dimension)
            indice1 = ((dimension / 2 + .5) + i)
            indice2 = ((dimension / 2 + .5) + j)
            imagen2[indice1, indice2]=valor
            j+=1
        i+=1
    imagen2=Image.fromarray(imagen2)
    imagen2.save(ruta_base + 'convolucion.gif') 
    imagen_l = PhotoImage(file = ruta_base + 'convolucion.gif')
    global convol    
    convol = canvas.create_image(600, 160, anchor=NW, image=imagen_l)
    ventana.mainloop()