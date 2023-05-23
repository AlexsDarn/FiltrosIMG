from tkinter import NW, PhotoImage, Canvas, Image
from global_variables.variables import ruta_base, ruta
from ui.ui import ventana

def grayscale():
    im = Image.open(ruta)
    im2 = im
    i = 0
    while i < im2.size[0]:
        j = 0
        while j < im2.size[1]:
            r, g, b = im2.getpixel((i, j))
            g = (r + g + b) / 3
            gris = int(g)
            pixel = tuple([gris, gris, gris])
            im2.putpixel((i, j), pixel)
            j += 1
        i += 1
    g = im2.convert('L')
    g.save(ruta_base + 'grises.gif')
    imagen_l = PhotoImage(file=ruta_base + 'grises.gif')
    global gray
    gray = Canvas.create_image(600, 160, anchor=NW, image=imagen_l)
    ventana.mainloop()
