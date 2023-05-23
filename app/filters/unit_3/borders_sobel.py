from global_variables.variables import ruta_base
from tkinter import NW, canvas, Image, PhotoImage
from ui.ui import ventana, canvas

def bordes_sobel():
    nombre = 'grises.gif'
    im = Image.open(ruta_base + nombre)
    ima = im
    [ren, col] = ima.size
    pix = ima.load()
    out_im = Image.new("L", (ren, col))
    mask = ([1,3,3],[-3,-2,3],[-3,-3,1])   
    out = out_im.load()
    for i in range(ren):
        for j in range(col):
            suma = 0
            for n in range(i-1, i+2):
                for m in range(j-1, j+2):
                    if n >= 0 and m >= 0 and n < ren and m < col:
                        suma += mask[n - (i - 1)][ m - (j - 1)] * pix[n, m]
            out[i, j] = suma
    out_im.save(ruta_base + 'bordesSobel.gif') 
    imagen_l = PhotoImage(file = ruta_base + 'bordesSobel.gif')
    global bordesSobel    
    bordesSobel = canvas.create_image(600, 160, anchor=NW, image=imagen_l)
    ventana.mainloop()