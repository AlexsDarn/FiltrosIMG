from scipy import ndimage as ndi
from skimage import feature
from matplotlib import pyplot as plt
from global_variables.variables import ruta_base
from tkinter import NW, canvas, Image, PhotoImage
from ui.ui import ventana, canvas

def bordes_canny():  
    nombre = 'grises.gif'
    im = Image.open(ruta_base + nombre)
    ima = ndi.gaussian_filter(im, 1)
    edges = feature.canny(ima)
    fig, (ax2) = plt.subplots(nrows = 1, ncols = 1, figsize = (8, 6), sharex = True, sharey = True)
    ax2.imshow(edges, cmap = plt.cm.gray)
    ax2.axis('off')
    plt.savefig(ruta_base + 'bordesCanny.png')
    imagen_l = PhotoImage(file = ruta_base + 'bordesCanny.png')
    global bordesCanny    
    bordesCanny = canvas.create_image(450, 100, anchor=NW, image=imagen_l)
    ventana.mainloop()