from tkinter import NW, Canvas, Image, PhotoImage, messagebox
from global_variables.variables import ruta_base
from main import entrada, ventana


def binarizar():
    nombre = 'grises.gif'
    im = Image.open(ruta_base + nombre)
    alpha = entrada.get()
    if alpha==0:
        messagebox.showwarning("ADVERTENCIA:", ("Ingrese Un Valor Valido Mayor A 0"))
    else:
        ima = im
        ren, col = ima.size
        im_actual = ima
        pixeles = im_actual.load()
        im_binaria = Image.new('RGB', (ren, col))
        bin_pix = im_binaria.load()
        for x in range(ren):
            for y in range(col):
                if pixeles[x,y] >= alpha:
                    bin_pix[x,y] = (255,255,255)
                else:
                    bin_pix[x,y] = (0,0,0)
        im_binaria.save(ruta_base + 'binarizar.gif') 
        imagen_l = PhotoImage(file = ruta_base + 'binarizar.gif')
        global binaria
        binaria = Canvas.create_image(600, 160, anchor=NW, image=imagen_l)
        ventana.mainloop()