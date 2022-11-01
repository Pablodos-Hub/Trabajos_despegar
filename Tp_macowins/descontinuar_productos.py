from macowins import *
from datetime import datetime

from persistencia import cargar_todos

# ...
        
if __name__ == "__main__":
    for sucursal in cargar_todos():
        sucursal.descontinuar_productos()

        
    print(datetime.now() + "Descontinuando productos sin stock")