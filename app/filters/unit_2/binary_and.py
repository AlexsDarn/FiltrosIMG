import numpy
from global_variables.variables import ruta_base
from tkinter import NW, canvas, Image, PhotoImage, messagebox
from ui.ui import ventana, entrada, canvas

def binary_and():
    nombre = 'grises.gif'
    im = Image.open(ruta_base + nombre)
    esc = entrada.get()
    if esc==0:
        messagebox.showwarning("ADVERTENCIA:", ("Ingrese Un Valor Valido Mayor A 0"))
    else:  
        [ren, col]=im.size
        m = numpy.asarray(im,dtype = numpy.float32)
        i = 0    
        while i < col:
            j=0
            while j < ren:
                b1 = int(m[i,j])
                np = bin(esc & b1)
                np = int(np,2)
                m[i,j] = np
                j+=1
            i+=1
        out = Image.fromarray(m)
        out.save(ruta_base + 'And.gif')
        imagen_l = PhotoImage(file= ruta_base + 'And.gif')
        global And        
        And = canvas.create_image(600,160,anchor=NW, image=imagen_l)
        ventana.mainloop()