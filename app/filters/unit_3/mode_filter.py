from collections import Counter
import numpy as np
from global_variables.variables import ruta_base
from tkinter import NW, canvas, Image, PhotoImage
from ui.ui import ventana, canvas

def filtro_moda():    
    nombre = 'grises.gif'
    im = Image.open(ruta_base + nombre)
    out = im
    [ren, col] = out.size
    matriz = np.asarray(out, dtype = np.float32)
    i = 0
    while i < ren - 3:
        j = 0
        while j < col - 3:
            submatriz = matriz[j:j+3,i:i+3]
            submatriz = submatriz.reshape(1, 9)
            nuevo = (max(submatriz))
            data = Counter(nuevo)
            nuevo = data.most_common(1)
            nuevo = max(nuevo)
            nuevo = int(nuevo[0])
            out.putpixel((i + 1, j + 1),(nuevo))
            j+=1
        i+=1
    out.save(ruta_base + 'filtroModa.gif') 
    imagen_l = PhotoImage(file = ruta_base + 'filtroModa.gif')
    global filtroModa    
    filtroModa = canvas.create_image(600, 160, anchor=NW, image=imagen_l)
    ventana.mainloop()