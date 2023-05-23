from ui.menu import mnuUnidad2
from filters.unit_2.brightness import brillo
from filters.unit_2.contrast import contraste
from filters.unit_2.operations.sum import suma
from filters.unit_2.operations.subtraction import resta
from filters.unit_2.operations.multiplication import multiplicacion
from filters.unit_2.operations.division import division
from filters.unit_2.binary_and import binary_and
from filters.unit_2.binary_or import binary_or
from filters.unit_2.logarithmic import logaritmica
from filters.unit_2.gamma import gamma
from filters.unit_2.histogram import histograma
from filters.unit_2.transposed import transpuesta
from filters.unit_2.ecualizations.uniform_equalization import ecualizacion_uniforme
from filters.unit_2.ecualizations.exponential_ecualization import ecualizacion_exponencial
from filters.unit_2.ecualizations.hyperbolic_equalization import ecualizacion_hyperbolica
from filters.unit_2.ecualizations.hypercubic_ecualization import ecualizacion_hypercubica
from filters.unit_2.ecualizations.rayleigh_ecualization import ecualizacion_rayleigh

mnuUnidad2.add_command(label = "BRILLO", command = brillo)
mnuUnidad2.add_separator()
mnuUnidad2.add_command(label = "CONTRASTE", command = contraste)
mnuUnidad2.add_separator()
mnuUnidad2.add_command(label = "SUMA DE PIXELES", command = suma)
mnuUnidad2.add_separator()
mnuUnidad2.add_command(label = "RESTA DE PIXELES", command = resta)
mnuUnidad2.add_separator()
mnuUnidad2.add_command(label = "MULTIPLICACION DE PIXELES", command = multiplicacion)
mnuUnidad2.add_separator()
mnuUnidad2.add_command(label = "DIVISION DE PIXALES", command = division)
mnuUnidad2.add_separator()
mnuUnidad2.add_command(label = "AND", command = binary_and)
mnuUnidad2.add_separator()
mnuUnidad2.add_command(label = "OR", command = binary_or)
mnuUnidad2.add_separator()
mnuUnidad2.add_command(label = "CORRECION LOGARITMICA", command = logaritmica)
mnuUnidad2.add_separator()
mnuUnidad2.add_command(label = "CORRECION GAMMA", command = gamma)
mnuUnidad2.add_separator()
mnuUnidad2.add_command(label = "HISTOGRAMA", command = histograma)
mnuUnidad2.add_separator()
mnuUnidad2.add_command(label = "ECUALIZACION UNIFORME", command = ecualizacion_uniforme)
mnuUnidad2.add_separator()
mnuUnidad2.add_command(label = "ECUALIZACION EXPONENCIAL", command = ecualizacion_exponencial)
mnuUnidad2.add_separator()
mnuUnidad2.add_command(label = "ECUALIZACION RAYLEIGH", command = ecualizacion_rayleigh)
mnuUnidad2.add_separator()
mnuUnidad2.add_command(label = "ECUALIZACION HIPERCUBICA", command = ecualizacion_hypercubica)
mnuUnidad2.add_separator()
mnuUnidad2.add_command(label = "ECUALIZACION HYPERBOLICA", command = ecualizacion_hyperbolica)
mnuUnidad2.add_separator()
mnuUnidad2.add_command(label = "TRANSPUESTA", command = transpuesta)