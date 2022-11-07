from macowins import *

# UTILIDADES
sucursal_retiro = SucursalFisica()
sucursal_madero = SucursalVirtual()
remera_talle_s = Prenda(100,"remera talle s",1500,"remera")
remera_talle_m = Prenda(110,"remera talle m",2000,"remera")
remera_talle_l = Prenda(120,"remera talle l",2500,"remera")
pantalon_talle_38 = Prenda(200,"pantalon talle 38",5000,"pantalon")
pantalon_talle_40 = Prenda(210,"pantalon talle 40",6000,"pantalon")
pantalon_talle_42 = Prenda(220,"pantalon talle 42",7000,"pantalon")

def reiniciar_precios_de_prendas():
    remera_talle_s.precio = 1500
    remera_talle_m.precio = 2000
    remera_talle_l.precio = 2500
    pantalon_talle_38.precio = 5000
    pantalon_talle_40.precio = 6000
    pantalon_talle_42.precio = 7000

def reiniciar_lista_productos_y_ventas():
    sucursal_retiro.productos.clear()
    sucursal_madero.productos.clear()
    sucursal_retiro.ventas.clear()
    sucursal_madero.ventas.clear()

def reiniciar_stock_de_prenda(prenda):
    prenda.stock = 0

def lista_de_2_productos_sin_stock(sucursal):
    sucursal.registrar_producto(remera_talle_s)
    sucursal.registrar_producto(pantalon_talle_38)
    reiniciar_stock_de_prenda(remera_talle_s)
    reiniciar_stock_de_prenda(pantalon_talle_38)

def lista_de_2_productos_con_stock(sucursal):
    sucursal.registrar_producto(remera_talle_s)
    sucursal.registrar_producto(pantalon_talle_38)
    reiniciar_stock_de_prenda(remera_talle_s)
    reiniciar_stock_de_prenda(pantalon_talle_38)
    sucursal.recargar_stock(100,100)
    sucursal.recargar_stock(200,100)

def lista_de_6_productos_con_stock(sucursal):
    sucursal.registrar_producto(remera_talle_s)
    sucursal.registrar_producto(remera_talle_m)
    sucursal.registrar_producto(remera_talle_l)
    sucursal.registrar_producto(pantalon_talle_38)
    sucursal.registrar_producto(pantalon_talle_40)
    sucursal.registrar_producto(pantalon_talle_42)
    reiniciar_stock_de_prenda(remera_talle_s)
    reiniciar_stock_de_prenda(remera_talle_m)
    reiniciar_stock_de_prenda(remera_talle_l)
    reiniciar_stock_de_prenda(pantalon_talle_38)
    reiniciar_stock_de_prenda(pantalon_talle_40)
    reiniciar_stock_de_prenda(pantalon_talle_42)
    sucursal.recargar_stock(100,500)
    sucursal.recargar_stock(110,500)
    sucursal.recargar_stock(120,500)
    sucursal.recargar_stock(200,500)
    sucursal.recargar_stock(210,500)
    sucursal.recargar_stock(220,500)

def realizar_cantidad_de_compras_de_producto(sucursal,codigo_producto,cantidad_compras):
    contador = 0
    while contador < cantidad_compras:
        sucursal.realizar_compra(codigo_producto,1,True)
        contador += 1
