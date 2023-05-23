from matplotlib import pyplot as plt
import numpy as np
import scipy
from global_variables.variables import ruta_base
from tkinter import NW, canvas, PhotoImage
from ui.ui import ventana, canvas

def gaussiano():
    nombre = 'grises.gif'
    l = scipy.misc.imread(ruta_base + nombre)
    noisy = l + 0.4 * l.std() * np.random.random(l.shape)
    plt.imshow(noisy, cmap=plt.cm.gray, vmin=40, vmax=220)
    plt.axis('off')
    plt.savefig(ruta_base + 'gaussiano.png', dpi=90)
    imagen_l = PhotoImage(file = ruta_base + 'gaussiano.png')
    global gauss
    gauss = canvas.create_image(450, 130, anchor=NW, image=imagen_l)
    ventana.mainloop()