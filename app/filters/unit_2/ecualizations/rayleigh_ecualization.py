import numpy as np
from global_variables.variables import ruta_base
from tkinter import NW, canvas, Image, PhotoImage, messagebox
from ui.ui import ventana, entrada, canvas

def ecualizacion_rayleigh():   
    nombre = 'grises.gif'
    im = Image.open(ruta_base + nombre)
    #alpha = 10
    alpha = entrada.get()
    if alpha==0:
        messagebox.showwarning("ADVERTENCIA:", ("Ingrese Un Valor Valido Mayor A 0"))
    else:
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
        m1 = 1 - ac
        m2 = 1 / m1    
        m3 = alpha * alpha    
        m4 = 2 * m3
        m5 = np.log(m2)
        m6 = m4 * m5
        m7 = pow(m6, 1/2)
        m8 = mindata + m7
        mapeo = np.floor(m8)
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
        newim.save(ruta_base + 'ecualizacionRayleigh.gif') 
        imagen_l = PhotoImage(file = ruta_base + 'ecualizacionRayleigh.gif')
        global ecualizacionRayleigh    
        ecualizacionRayleigh = canvas.create_image(600, 160, anchor=NW, image=imagen_l)
        ventana.mainloop()