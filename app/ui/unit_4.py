from ui.menu import mnuUnidad4
from filters.unit_4.erosion import erosion
from filters.unit_4.dilatation import dilatacion
from filters.unit_4.opening import opening

mnuUnidad4.add_command(label = "EROSION", command = erosion)
mnuUnidad4.add_separator()
mnuUnidad4.add_command(label = "DILATACION", command = dilatacion)
mnuUnidad4.add_separator()
mnuUnidad4.add_command(label = "APERTURA", command = opening)