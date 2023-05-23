import numpy as np
from global_variables.variables import ruta_base
from tkinter import NW, Image, PhotoImage
from ui.ui import ventana, canvas

def transpuesta():
    nombre = 'grises.gif'
    im = Image.open(ruta_base + nombre)
    im7 = im
    ar = np.zeros((im7.size[0], im7.size[1]))
    i = 0 
    while i < im7.size[1]:
        j = 0
        while j < im7.size[0]:
            a = im7.getpixel((j, i))
            ar[j, i] = a
            j+=1
        i+=1
    ar = ar.astype(int)    
    im7 = Image.fromarray(ar)
    im7.save(ruta_base + 'transpuesta.gif') 
    imagen_l = PhotoImage(file = ruta_base + 'transpuesta.gif')
    global trans   
    trans = canvas.create_image(600, 160, anchor=NW, image=imagen_l)
    ventana.mainloop()