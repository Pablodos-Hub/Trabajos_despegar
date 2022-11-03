from datetime import datetime
from macowins import *
from persistencia import cargar_todos

print (str(datetime.now()) + " : descontinuando productos" )

if __name__ == "__main__":
    for sucursal in cargar_todos().values():
        sucursal.descontinuar_productos()

        
