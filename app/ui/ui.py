from tkinter import Canvas, DoubleVar, Entry, IntVar, Label, Tk

fontT = "Times New Roman"

ventana = Tk()
w = 1000
h = 650
extraW=ventana.winfo_screenwidth() - w
extraH=ventana.winfo_screenheight() - h
ventana.geometry("%dx%d%+d%+d" % (w, h, extraW / 2, extraH / 2))
canvas = Canvas(ventana, width=1000, height=650)
canvas.pack()
ventana.title("PROCESAMIENTO DIGITAL DE IMAGENES")
entrada = IntVar()
entrada2 = DoubleVar()
Entry(ventana, textvariable = entrada, width = 8).place(x=20, y=65)
Label(text = "Ingrese Los Pixeles ", font= (fontT,9)).place(x=0, y=20)
Label(text = "En Enteros ", font= (fontT,9)).place(x=17, y=40)
Label(text = "En Decimales ", font= (fontT,9)).place(x=14, y=87)
Entry(ventana, textvariable = entrada2, width = 8).place(x=20, y=110)
Label(text = "IMAGEN ORIGINAL", font= (fontT,14)).place(x=175, y=120)
Label(text = "IMAGEN PROCESADA", font= (fontT,14)).place(x=650, y=120)
Label(text = "NOTA IMPORTANTE:", fg = 'red', font= (fontT,13)).place(x=5, y=500)
Label(text = "PARA LOS METODOS DE BINARIZAR, SUMA DE PIXELES, RESTA DE PIXELES, MULTIPLICACION DE PIXELES, DIVISION DE PIXELES, ECUALIZACION RAYLEIGH", font= (fontT,10)).place(x=10, y=540)
Label(text = "AND, OR, RUIDO SAL Y PIMIENTA Y BORDES DE CANNY, SE TIENE QUE AGREGAR UN VALOR ENTERO EN EL CAMPO DE" ,font= (fontT,10)).place(x=10, y=560)
Label(text = "(INGRESE LOS PIXELES EN ENTEROS).", fg = 'red', font =(fontT,10)).place(x=690, y=560)
Label(text = "PARA LOS METODOS DE CORRECION GAMMA Y ECUALIZACION EXPONENCIAL", font= (fontT,10)).place(x=10, y=600)
Label(text = "SE TIENE QUE AGREGAR UN VALOR DECIMAL EN EL CAMPO DE" ,font= (fontT,10)).place(x=10, y=620)
Label(text = "(INGRESE LOS PIXELES EN DECIMALES).", fg = 'red', font =(fontT,10)).place(x=385, y=620)