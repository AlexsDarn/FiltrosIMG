import numpy as np
from global_variables.variables import ruta_base
from tkinter import NW, canvas, Image, PhotoImage
from ui.ui import ventana, canvas

def ecualizacion_hypercubica():   
    nombre = 'grises.gif'
    im = Image.open(ruta_base + nombre)
    ima = im
    [ren, col] = ima.size 
    ima = np.asarray(ima, dtype = np.float32).reshape(1, ren * col)
    valor = 0 
    maxdata = max(max(ima))
    mindata = min(min(ima))
    niveles = maxdata
    h = np.zeros(niveles)
    ima = ima.reshape(col, ren)
    ac = h
    i = 0
    #cálculo del histograma
    while i < ren:
        j = 0
        while j < col:
            valor = ima[j,i] - 1
            h[valor] = h[valor] + 1
            j+=1
        i+=1
    ac[0] = h[0]
    i = 1
    while i < maxdata:
        ac[i] = ac[i - 1] + h[i]
        i+=1
    ac = ac / (ren * col)
    #funcion de mapeo
    m1 = pow(maxdata, 1/3)
    m2 = pow(mindata, 1/3)
    m3 = m2 * ac
    m4 = m1 - m3
    m5 = m4 + m1
    m6 = pow(m5 , 3)
    mapeo = np.floor(m6)
    #si mindata es cero la imagen sera cero
    newim = np.zeros((col, ren))
    i = 0
    while i < ren:
        j = 0
        while j < col:
            newim[j, i] = mapeo[ima[j, i] - 1]
            j+=1
        i+=1
    newim = Image.fromarray(newim)
    newim.save('G:/TEC/7 SEMESTRE/Procesamiento Digital De Imagenes/Programas (Con Interfaz)/resultados/ecualizacionHypercubica.gif') 
    imagen_l = PhotoImage(file = 'G:/TEC/7 SEMESTRE/Procesamiento Digital De Imagenes/Programas (Con Interfaz)/resultados/ecualizacionHypercubica.gif')
    global ecualizacionHypercubica    
    ecualizacionHypercubica = canvas.create_image(600, 160, anchor=NW, image=imagen_l)
    ventana.mainloop()