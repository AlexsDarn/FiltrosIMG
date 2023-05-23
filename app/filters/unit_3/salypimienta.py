import numpy as np
from global_variables.variables import ruta_base
from tkinter import NW, canvas, Image, PhotoImage, messagebox
from ui.ui import ventana, entrada, canvas

def salypimienta():    
    nombre = 'grises.gif'
    im = Image.open(ruta_base + nombre)
    prob = entrada.get()
    if prob==0:
        messagebox.showwarning("ADVERTENCIA:", ("Ingrese Un Valor Valido Mayor A 0"))
    else:
        [ren, col] = im.size
        sal = im
        n_max_ren = round(ren * prob / 100.0)
        n_max_col = round(col * prob / 100.0)
        i = 1
        for i in range(n_max_ren):
            j = 1
            for j in range(n_max_col):
                cx = round(np.random.rand() * (col - 1)) + 1
                cy = round(np.random.rand() * (ren - 1)) + 1
                aaa = round(np.random.rand() * 255)
            if aaa > 128:
                val = 255
                sal.putpixel((cy, cx),(val))
            else:
                val= 1
                sal.putpixel((cy, cx),(val))
        sal.save(ruta_base + 'sal.gif') 
        imagen_l = PhotoImage(file = ruta_base + 'sal.gif')
        global sal_y_pimienta
        sal_y_pimienta = canvas.create_image(600, 160, anchor=NW, image=imagen_l)
        ventana.mainloop()