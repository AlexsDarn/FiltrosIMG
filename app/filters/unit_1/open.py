from tkinter import filedialog, PhotoImage, NW
from app.global_variables.variables import ruta_base
from ui.ui import canvas, ventana

def abrir():
    ventana.filename = filedialog.askopenfilename(initialdir = ruta_base,title = "Elige Tu Archivo De Imagen:", filetypes = (("Imagenes PNG", "*.png"),("Imagenes GIF ", "*.gif")))    
    ruta = ventana.filename
    imagen_l = PhotoImage(file = ruta)
    global abrirImagen
    abrirImagen = canvas.create_image(110, 160, anchor=NW, image=imagen_l)
    ventana.mainloop()
