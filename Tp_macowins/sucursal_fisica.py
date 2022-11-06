from sucursal import *

class SucursalFisica(Sucursal):
    def __init__(self):
        self.productos = set()
        self.ventas = []
        self.gasto_por_dia = 15000
    
    def gastos_del_dia(self):
        return self.gasto_por_dia