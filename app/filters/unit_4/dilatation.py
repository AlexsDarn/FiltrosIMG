import numpy as np
from scipy import ndimage as ndi
from matplotlib import pyplot as plt
from global_variables.variables import ruta_base
from tkinter import NW, canvas, PhotoImage
from ui.ui import ventana, canvas

def dilatacion():
    datos = np.zeros((16, 16))
    datos[4:-4, 4:-4] = 1
    dist = ndi.distance_transform_bf(datos)
    dilate_dist = ndi.grey_dilation(dist, size=(3, 3), structure=np.ones((3, 3)))
    plt.figure(figsize=(11.14, 8.34))
    plt.subplot(131)
    plt.imshow(dist, interpolation='nearest', cmap=plt.cm.spectral)
    plt.axis('off')
    plt.subplot(133)
    plt.imshow(dilate_dist, interpolation='nearest', cmap=plt.cm.spectral)
    plt.axis('off')
    plt.savefig(ruta_base + 'dilatacion.png')
    imagen_l = PhotoImage(file = ruta_base + 'dilatacion.png')
    global dil    
    dil = canvas.create_image(100, 20, anchor=NW, image=imagen_l)
    ventana.mainloop() 