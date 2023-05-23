from matplotlib import pyplot as plt
import numpy as np
from global_variables.variables import ruta_base
from tkinter import NW, Image, PhotoImage
from ui.ui import ventana, canvas

def histograma():
    nombre = 'grises.gif'
    im = Image.open(ruta_base + nombre)
    im16 = im
    [ren, col] = im16.size
    total = ren * col
    a = np.asarray(im16, dtype = np.float32)
    a = a.reshape(1, total)
    a = a.astype(int)
    a = max(a)
    valor = 0
    maxd = max(a)
    grises = maxd
    vec=np.zeros(grises + 1)
    for i in range(total - 1):
        valor = a[i]
        vec[valor] = vec[valor] + 1
    plt.plot(vec)
    plt.savefig(ruta_base + 'histograma.png', dpi=80)
    imagen_l = PhotoImage(file = ruta_base + 'histograma.png')
    global hist
    hist = canvas.create_image(520, 160, anchor=NW, image=imagen_l)
    ventana.mainloop()