class Prenda:
    def __init__(self,un_codigo,un_nombre,un_precio,categoria):
        self.codigo = un_codigo
        self.nombre = un_nombre
        self.precio = un_precio
        self.estado = Nueva()
        self.stock = 0
        self.categoria = set()
        self.categoria.add(categoria)       

    def hay_stock(self):
        return self.stock > 0

    def vender_con_stock(self,cantidad_a_vender):
        if self.stock >= cantidad_a_vender:
           self.stock -= cantidad_a_vender
           return True
        else:
           return False

    def codigo_valido(self,codigo):
        return codigo == self.codigo

    def ver_categorias(self):
        categorias = ",".join(self.categoria)
        return categorias
           
    def agregar_categoria(self,nueva_categoria):
        self.categoria.add(nueva_categoria)
    
    def cambiar_estado(self,nuevo_estado):
        self.estado = nuevo_estado

    def precio_final(self):
        return self.estado.precio_final(self.precio)

    def es_de_categoria(self,categoria):
        return categoria in self.categoria

    def es_de_nombre(self,patron):
        return patron == self.nombre    

    def actualizar_precio_segun_porcentaje(self,porcentaje):
        self.precio = self.precio + (self.precio * porcentaje)/100

    def agregar_stock(self,cantidad_agregar):
        self.stock += cantidad_agregar    

# ------ ESTADOS ------
class Nueva:
    def precio_final(self,precio):
        return precio

class Promocion:
    def __init__(self,valor_promo):
        self.valor = valor_promo
    def precio_final(self,precio):
        return precio - self.valor

class Liquidacion:
    def precio_final(self,precio):
        return precio /2

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
        self.precio = precio

    def aplica_a(self,producto):
        return producto.precio < self.precio

class PorStock:
    def aplica_a(self,producto):
        return producto.stock > 0

class PorOposicion:
    def __init__(self,un_criterio):
        self.criterio = un_criterio
        
    def aplica_a(self,producto):
        return not self.criterio.aplica_a(producto)