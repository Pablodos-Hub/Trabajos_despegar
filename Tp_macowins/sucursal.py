from datetime import datetime
from collections import *
from prendas import *
from criterios import *

class Sucursal:
    #######################-ADICIONAL VER PRODUCTOS CARGADOS EN LA LISTA-###########################################################################################################
    def ver_productos(self):
        if not len(self.productos) == 0:
           for producto in self.productos:
            print("codigo:"+str(producto.codigo)+" nombre:"+producto.nombre+" precio:"+str(producto.precio)+" stock:"+str(producto.stock)+" categoria/s:"+producto.ver_categorias())
        else:
            raise ValueError ("No hay productos registrados")
    ################################################################################################################################################################################        

    def registrar_producto(self,nuevo_producto):
        largo_inicial = len(self.productos)
        self.productos.add(nuevo_producto)
        if len(self.productos) == largo_inicial:
            raise ValueError ("El producto ya se encuentra registrado")

    def recargar_stock(self,codigo_producto,cantidad_a_agregar):
        codigo_valido = False
        for producto in self.productos:
            if producto.codigo_valido(codigo_producto):
               codigo_valido = True
               producto.agregar_stock(cantidad_a_agregar)
        if not codigo_valido:
            raise ValueError ("El codigo no corresponde a un producto registrado")

    def hay_stock(self,codigo_producto):
        for producto in self.productos:
            if producto.codigo_valido(codigo_producto):
               return producto.hay_stock()
        return False

    def calcular_precio_final(self,codigo_producto,es_extranjero):
        for producto in self.productos:
            if producto.codigo_valido(codigo_producto) and producto.precio_final() > 70 and es_extranjero:
               return producto.precio_final()
            if producto.codigo_valido(codigo_producto) and not es_extranjero:
               return producto.precio_final() + (producto.precio_final()*21)/100 

    def contar_categorias(self):
        lista_total_categorias = set()
        for producto in self.productos:
            for categoria in producto.categoria:
                lista_total_categorias.add(categoria)
        return len(lista_total_categorias)

    def realizar_compra(self,codigo_producto,cantidad_a_vender,es_extranjero):
        codigo_valido = False
        for producto in self.productos:
            if producto.codigo_valido(codigo_producto):
               codigo_valido = True
               if producto.vender_con_stock(cantidad_a_vender):
                  monto_total = self.calcular_precio_final(codigo_producto,es_extranjero)*cantidad_a_vender
                  self.ventas.append({"producto":producto.nombre,"cantidad_vendida":cantidad_a_vender,"monto":monto_total,"fecha":datetime.strftime(datetime.now(),"%d/%m"),"anio":datetime.strftime(datetime.now(),"%Y")})
               else:
                  raise ValueError ("No hay suficiente stock para realizar la venta")      
        if not codigo_valido:
           raise ValueError ("El codigo no corresponde a un producto registrado")       

    def descontinuar_productos(self):
        self.productos = {producto for producto in self.productos if producto.hay_stock()}

    def valor_ventas_del_dia(self):
        venta_dia = 0
        if self.hay_ventas():
           for venta in self.ventas:
            if datetime.strftime(datetime.now(),"%d/%m") == venta["fecha"]:
               venta_dia += venta["monto"]
        else:
            raise ValueError ("No hay ventas registradas") 
        return venta_dia          

    def ventas_del_anio(self):
        venta_anio = 0
        if self.hay_ventas(): 
           for venta in self.ventas:
               if datetime.strftime(datetime.now(),"%Y") == venta["anio"]:
                  venta_anio += venta["monto"]
        else:
            raise ValueError ("No hay ventas registradas")
        return venta_anio              

    def productos_mas_vendidos(self,cantidad_de_productos):
        productos_vendidos = []
        mas_vendidos = []
        for venta in self.ventas:
            productos_vendidos.append(venta["producto"])
        
        mas_vendidos = Counter(productos_vendidos)
        return mas_vendidos.most_common(cantidad_de_productos)

    def actualizar_precios_segun(self, criterio, porcentaje):
        for producto in self.productos:
            if criterio.aplica_a(producto):
               producto.actualizar_precio_segun_porcentaje(porcentaje)

    def ganancia_diaria(self):
        if self.hay_ventas():
           return self.valor_ventas_del_dia() - self.gastos_del_dia()
        else:
            return self.gastos_del_dia()
    
    def hay_ventas(self):
        return len(self.ventas) > 0

    def listar_productos_segun(self,criterio):
        return {producto for producto in self.productos if criterio.aplica_a(producto)}