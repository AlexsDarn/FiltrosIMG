from global_variables.variables import ruta_base
from tkinter import NW, Image, PhotoImage, messagebox
from ui.ui import ventana, canvas, entrada

def multiplicacion():
    nombre = 'grises.gif'
    im = Image.open(ruta_base + nombre)
    alpha = entrada.get()
    if alpha==0:
        messagebox.showwarning("ADVERTENCIA:", ("Ingrese Un Valor Valido Mayor A 0"))
    else:
        im13 = im
        i = 0
        while i < im13.size[0]:
            j = 0
            while j < im13.size[1]:
                valor = im13.getpixel((i, j))
                valor = valor * alpha
                if valor >= 255:
                    valor = 255
                im13.putpixel((i, j),(valor))
                j+=1
            i+=1
        im13.save(ruta_base + 'multiplication.gif') 
        imagen_l = PhotoImage(file = ruta_base + 'multiplication.gif')
        global multiplication
        multiplication = canvas.create_image(600, 160, anchor=NW, image=imagen_l)
        ventana.mainloop()