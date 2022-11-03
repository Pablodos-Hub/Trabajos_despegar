from time import strftime
from macowins import *
from datetime import datetime

from persistencia import cargar_todos

import subprocess

subprocess.call(["zenity", "--info",  '--title=Hola', "--text=¡Hola mundo!", "--display=:0"])

print ("hola pablo")
print("Descontinuando productos sin stock")

if __name__ == "__main__":
    for sucursal in cargar_todos():
        sucursal.descontinuar_productos()
