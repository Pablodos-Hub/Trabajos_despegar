# ------ CRITERIOS ------

class PorCategoria:
    def __init__(self, categoria):
        self.categoria = categoria

    def aplica_a(self, producto):
        return producto.es_de_categoria(self.categoria)

class PorNombre:
    def __init__(self, nombre):
        self.nombre = nombre

    def aplica_a(self, producto):
        return producto.es_de_nombre(self.nombre)

class PorPrecio:
    def __init__(self,precio):
        if type(precio) == int:
            self.precio = precio
        else:
            self.precio = int(precio)   

    def aplica_a(self,producto):
        return self.precio > producto.precio 

class PorStock:
    def aplica_a(self,producto):
        return producto.stock > 0

class PorOposicion:
    def __init__(self,un_criterio):
        self.criterio = un_criterio
        
    def aplica_a(self,producto):
        return not self.criterio.aplica_a(producto)