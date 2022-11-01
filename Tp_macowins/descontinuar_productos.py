from macowins import *
from datetime import datetime

from persistencia import cargar_todos

# ...
def descontinuar_productos_sin_stock(lista):
    lista = [producto for producto in lista if producto.haystock()]
        
if __name__ == "__main__":
    descontinuar_productos_sin_stock(cargar_todos().values())

        
    print(datetime.now(), "Descontinuando productos sin stock")