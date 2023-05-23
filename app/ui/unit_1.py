from filters.unit_1.open import abrir
from ui.menu import mnuUnidad1
from filters.unit_1.grayscale import grayscale
from filters.unit_1.rbg import rbg
from filters.unit_1.gbr import gbr
from filters.unit_1.grb import grb
from filters.unit_1.brg import brg
from filters.unit_1.bgr import bgr
from filters.unit_1.maximum import maximo
from filters.unit_1.minimum import minimo
from filters.unit_1.binarize import binarizar
from filters.unit_1.negative import negativo

mnuUnidad1.add_command(label = "ABRIR IMAGEN", command = abrir)
mnuUnidad1.add_separator()
mnuUnidad1.add_command(label = "RBG", command = rbg)
mnuUnidad1.add_separator()
mnuUnidad1.add_command(label = "GBR", command = gbr)
mnuUnidad1.add_separator()
mnuUnidad1.add_command(label = "GRB", command = grb)
mnuUnidad1.add_separator()
mnuUnidad1.add_command(label = "BRG", command = brg)
mnuUnidad1.add_separator()
mnuUnidad1.add_command(label = "BGR", command = bgr)
mnuUnidad1.add_separator()
mnuUnidad1.add_command(label = "ESCALA DE GRISES", command = grayscale)
mnuUnidad1.add_separator()
mnuUnidad1.add_command(label = "MAXIMO DE GRISES", command = maximo)
mnuUnidad1.add_separator()
mnuUnidad1.add_command(label = "MINIMO DE GRISES", command = minimo)
mnuUnidad1.add_separator()
mnuUnidad1.add_command(label = "BINARIZACION", command = binarizar)
mnuUnidad1.add_separator()
mnuUnidad1.add_command(label = "NEGATIVO", command = negativo)