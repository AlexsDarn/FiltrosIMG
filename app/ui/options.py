from main import limpiar
from ui.menu import mnuOpciones, ventana


mnuOpciones.add_command(label = "LIMPIAR", command = limpiar)
mnuOpciones.add_separator()
mnuOpciones.add_command(label = "SALIR", command = ventana.destroy)