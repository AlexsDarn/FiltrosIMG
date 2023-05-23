from tkinter import Menu
from ui.ui import canvas, ventana

barraMenu = Menu(ventana)
mnuOpciones = Menu(barraMenu)
mnuUnidad1 = Menu(barraMenu)
mnuUnidad2 = Menu(barraMenu)
mnuUnidad3 = Menu(barraMenu)
mnuUnidad4 = Menu(barraMenu)
mnuUnidad5 = Menu(barraMenu)

barraMenu.add_cascade(label = "UNIDAD I", menu = mnuUnidad1)
barraMenu.add_cascade(label = "UNIDAD II", menu = mnuUnidad2)
barraMenu.add_cascade(label = "UNIDAD III", menu = mnuUnidad3)
barraMenu.add_cascade(label = "UNIDAD IV", menu = mnuUnidad4)
barraMenu.add_cascade(label = "UNIDAD V", menu = mnuUnidad5)
barraMenu.add_cascade(label = "OPCIONES", menu = mnuOpciones)
ventana.config(menu = barraMenu)
ventana.mainloop()

def limpiar():
    canvas.delete("all")
