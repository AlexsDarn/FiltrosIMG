from ui.menu import mnuUnidad3
from filters.unit_3.gaussian import gaussiano
from filters.unit_3.convolution import convolucion
from filters.unit_3.salypimienta import salypimienta
from filters.unit_3.maximum_filter import filtro_maximo
from filters.unit_3.minimum_filter import filtro_minimo
from filters.unit_3.median_filter import filtro_mediana
from filters.unit_3.mode_filter import filtro_moda
from filters.unit_3.borders_sobel import bordes_sobel
from filters.unit_3.borders_canny import bordes_canny

mnuUnidad3.add_command(label = "CONVOLUCION", command = convolucion)
mnuUnidad3.add_separator()
mnuUnidad3.add_command(label = "RUIDO GAUSSIANO", command = gaussiano)
mnuUnidad3.add_separator()
mnuUnidad3.add_command(label = "RUIDO SAL Y PIMIENTA", command = salypimienta)
mnuUnidad3.add_separator()
mnuUnidad3.add_command(label = "FILTRO MAXIMO", command = filtro_maximo)
mnuUnidad3.add_separator()
mnuUnidad3.add_command(label = "FILTRO MINIMO", command = filtro_minimo)
mnuUnidad3.add_separator()
mnuUnidad3.add_command(label = "FILTRO MEDIANA", command = filtro_mediana)
mnuUnidad3.add_separator()
mnuUnidad3.add_command(label = "FILTRO MODA", command = filtro_moda)
mnuUnidad3.add_separator()
mnuUnidad3.add_command(label = "BORDES (SOBEL)", command = bordes_sobel)
mnuUnidad3.add_separator()
mnuUnidad3.add_command(label = "BORDES (CANNY)", command = bordes_canny)