from global_variables.variables import ruta_base
from tkinter import NW, Image, PhotoImage, messagebox
from ui.ui import ventana, canvas, entrada

def division():
    nombre = 'grises.gif'
    im = Image.open(ruta_base + nombre)
    alpha = entrada.get()
    if alpha==0:
        messagebox.showwarning("ADVERTENCIA:", ("Ingrese Un Valor Valido Mayor A 0"))
    else:    
        im14 = im
        i = 0
        while i < im14.size[0]:
            j = 0
            while j < im14.size[1]:
                valor = im14.getpixel((i, j)) 
                valor = valor / alpha
                valor = int(valor)
                if valor <= 0:
                    valor = abs(valor)
                im14.putpixel((i, j),(valor))
                j+=1
            i+=1
        im14.save(ruta_base + 'division.gif') 
        imagen_l = PhotoImage(file = ruta_base + 'division.gif')
        global div
        div = canvas.create_image(600, 160, anchor=NW, image=imagen_l)
        ventana.mainloop()