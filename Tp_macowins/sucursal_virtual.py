from sucursal import *

class SucursalVirtual(Sucursal):
    def __init__(self):
        self.productos = set()
        self.ventas = []
        self.gasto_por_dia = 15000
        self.gasto_variable = 1

    def gastos_del_dia(self):
        if len(self.ventas) > 100:
            return len(self.ventas)*self.gasto_variable
        else:
            return self.gasto_por_dia

    def modificar_gasto_variable(self,nuevo_valor):
        self.gasto_variable = nuevo_valor