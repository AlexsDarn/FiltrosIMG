from tkinter import NW, Canvas, Image, PhotoImage
from global_variables.variables import ruta_base
from main import ventana

def negativo():    
    nombre = 'grises.gif'
    im = Image.open(ruta_base + nombre)
    im15 = im
    i = 0
    while i < im15.size[0]:
        j = 0
        while j < im15.size[1]:
            gris = im15.getpixel((i,j))
            valor = 255 - gris
            im15.putpixel((i, j), valor)
            j+=1
        i+=1
    im15.save(ruta_base + 'negativo.gif') 
    imagen_l = PhotoImage(file = ruta_base + 'negativo.gif')
    global neg
    neg = Canvas.create_image(600, 160, anchor=NW, image=imagen_l)
    ventana.mainloop()