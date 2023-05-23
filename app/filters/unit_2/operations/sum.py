from global_variables.variables import ruta_base
from tkinter import NW, Canvas, Image, PhotoImage, messagebox
from ui.ui import ventana, entrada

def suma():
    nombre = 'grises.gif'
    im = Image.open(ruta_base + nombre)
    alpha = entrada.get()
    if alpha==0:
        messagebox.showwarning("ADVERTENCIA:", ("Ingrese Un Valor Valido Mayor A 0"))
    else:
        im11 = im
        i = 0
        while i < im11.size[0]:
            j = 0
            while j < im11.size[1]:
                valor = im11.getpixel((i, j))
                valor = valor + alpha
                if valor >= 255:
                    valor = 255
                im11.putpixel((i, j),(valor))
                j+=1
            i+=1
        im11.save(ruta_base + 'suma.gif') 
        imagen_l = PhotoImage(file = ruta_base + 'suma.gif')
        global sum
        sum = Canvas.create_image(600, 160, anchor=NW, image=imagen_l)
        ventana.mainloop()