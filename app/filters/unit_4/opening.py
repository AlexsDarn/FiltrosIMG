import numpy as np
from scipy import ndimage as ndi
from matplotlib import pyplot as plt
from global_variables.variables import ruta_base
from tkinter import NW, canvas, PhotoImage
from ui.ui import ventana, canvas

def opening():
    square = np.zeros((32, 32))
    square[10:-10, 10:-10] = 1
    np.random.seed(2)
    x, y = (32*np.random.random((2, 20))).astype(np.int)
    square[x, y] = 1
    eroded_square = ndi.binary_erosion(square)
    reconstruction = ndi.binary_propagation(eroded_square, mask=square)
    plt.figure(figsize=(11.14, 8.34))
    plt.subplot(131)
    plt.imshow(square, cmap=plt.cm.gray, interpolation='nearest')
    plt.axis('off')
    plt.subplot(133)
    plt.imshow(reconstruction, cmap=plt.cm.gray, interpolation='nearest')
    plt.axis('off')
    plt.savefig(ruta_base + 'apertura.png')
    imagen_l = PhotoImage(file = ruta_base + 'apertura.png')
    global ape
    ape = canvas.create_image(100, 20, anchor=NW, image=imagen_l)
    ventana.mainloop() 