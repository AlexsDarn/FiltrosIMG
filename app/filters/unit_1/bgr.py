from global_variables.variables import ruta, ruta_base
from tkinter import NW, Image, PhotoImage
from ui.ui import ventana, canvas

def bgr():
    im=Image.open(ruta)
    [ren,col]=im.size
    out=im
    i=0
    while i<ren:
        j=0
        while j<col:
            niveles=im.getpixel((i,j))
            nivel_r=niveles[0]
            nivel_g=niveles[1]
            nivel_b=niveles[2]
            out.putpixel((i,j),(nivel_b,nivel_g,nivel_r))
            j+=1
        i+=1
    out.save(ruta_base + 'bgr.gif') 
    imagen_l = PhotoImage(file = ruta_base + 'bgr.gif')
    global bgr
    bgr = canvas.create_image(600, 160, anchor=NW, image=imagen_l)
    ventana.mainloop()