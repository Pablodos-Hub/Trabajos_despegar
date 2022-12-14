import pytest
from macowins import *
from utilidades_pytest import * 

#TEST 1. REGISTRAR PRODUCTOS

def test_registrar_un_producto_en_lista_de_productos():
    reiniciar_lista_productos_y_ventas()
    sucursal_retiro.registrar_producto(remera_talle_s)
    assert len(sucursal_retiro.productos) == 1
    
def test_registrat_seis_productos_en_lista_de_productos():
    reiniciar_lista_productos_y_ventas()
    lista_de_6_productos_con_stock(sucursal_retiro)
    assert len(sucursal_retiro.productos) == 6
    

#TEST 2. RECARGAR STOCK
        
def test_recargar_stock_a_remera_talle_s(): 
    reiniciar_lista_productos_y_ventas()
    sucursal_retiro.registrar_producto(remera_talle_s)  
    sucursal_retiro.recargar_stock(100,50)
    assert sucursal_retiro.hay_stock(100) 
    
    
def test_recargar_100_de_stock_a_remera_talle_s():
    reiniciar_lista_productos_y_ventas()
    reiniciar_stock_de_prenda(remera_talle_s)
    sucursal_retiro.registrar_producto(remera_talle_s)  
    sucursal_retiro.recargar_stock(100,100)
    assert remera_talle_s.stock == 100

#TEST 3. HAY STOCK 

def test_hay_stock_con_0_de_stock_del_producto_remera_talle_s():
     reiniciar_lista_productos_y_ventas()
     sucursal_retiro.registrar_producto(remera_talle_s)
     reiniciar_stock_de_prenda(remera_talle_s)
     assert sucursal_retiro.hay_stock(100) == False
     
def test_hay_stock_con_1_de_stock_del_producto_remera_talle_s():
    reiniciar_lista_productos_y_ventas()
    sucursal_retiro.registrar_producto(remera_talle_s)
    sucursal_retiro.recargar_stock(100,1)
    assert sucursal_retiro.hay_stock(100) == True 
    
#TEST 4. CALCULAR PRECIO FINAL    

def test_calcular_precio_final_de_remera_talle_s_con_vendedor_extranjero():
    reiniciar_lista_productos_y_ventas()
    sucursal_retiro.registrar_producto(remera_talle_s)
    assert sucursal_retiro.calcular_precio_final(100,True) == 1500
    
def test_calcular_precio_final_de_remera_talle_s_con_vendedor_local():
    reiniciar_lista_productos_y_ventas()
    sucursal_retiro.registrar_producto(remera_talle_s)
    assert sucursal_retiro.calcular_precio_final(100,False) == 1815
    
#TEST 5. CUANTAS CATEGORIAS UNICAS HAY

def test_cuantas_categorias_tengo_con_1_producto():
    reiniciar_lista_productos_y_ventas()
    sucursal_retiro.registrar_producto(remera_talle_s)
    assert sucursal_retiro.contar_categorias() == 1

def test_cuantas_categorias_tengo_con_2_productos_de_misma_categoria():
    reiniciar_lista_productos_y_ventas()
    sucursal_retiro.registrar_producto(remera_talle_s)
    sucursal_retiro.registrar_producto(remera_talle_m)
    assert sucursal_retiro.contar_categorias() == 1
    
def test_cuantas_categorias_tengo_con_2_productos_de_distinta_categoria():
    reiniciar_lista_productos_y_ventas()
    lista_de_2_productos_sin_stock(sucursal_retiro)
    assert sucursal_retiro.contar_categorias() == 2
          
#TEST 6. REALIZAR COMPRA  
def test_realizar_compra_con_1_producto():    
    reiniciar_lista_productos_y_ventas()
    reiniciar_stock_de_prenda(remera_talle_s)
    sucursal_retiro.registrar_producto(remera_talle_s)
    sucursal_retiro.recargar_stock(100,100)
    sucursal_retiro.realizar_compra(100,50,True)
    assert len(sucursal_retiro.ventas) == 1
    
def test_realizar_2_compras_con_1_producto():
    reiniciar_lista_productos_y_ventas()
    sucursal_retiro.registrar_producto(remera_talle_s)
    reiniciar_stock_de_prenda(remera_talle_s)
    sucursal_retiro.recargar_stock(100,10)
    sucursal_retiro.realizar_compra(100,1,True)
    sucursal_retiro.realizar_compra(100,2,True)
    assert len(sucursal_retiro.ventas) == 2 
    
def test_realizar_compra_sin_stock():
    reiniciar_lista_productos_y_ventas()
    sucursal_retiro.registrar_producto(pantalon_talle_38)
    reiniciar_stock_de_prenda(pantalon_talle_38)
    with pytest.raises(ValueError) as auxiliar:
        sucursal_retiro.realizar_compra(200,1,True)
    assert str(auxiliar.value) ==  "No hay suficiente stock para realizar la venta"
    
    
#TEST 7. ELIMINAR LOS PRODUCTOS SIN STOCK

def test_eliminar_pantalon_talle_38_y_remera_talle_s_sin_stock():
    reiniciar_lista_productos_y_ventas()
    lista_de_2_productos_sin_stock(sucursal_retiro)
    sucursal_retiro.descontinuar_productos()
    assert len(sucursal_retiro.productos) == 0

# ADICIONAL!!!! POR LAS DUDAS 

def test_probar_multiples_asserts():
    lista_de_2_productos_con_stock(sucursal_retiro)
    lista_nombres_inicial = [producto.nombre for producto in sucursal_retiro.productos]
    errores = []
    if "pantalon talle 38" not in lista_nombres_inicial:
        errores.append("no existe pantalon talle 38 en la lista inicial")
    reiniciar_stock_de_prenda(pantalon_talle_38)
    
    sucursal_retiro.descontinuar_productos()
    
    lista_nombres_final= [producto.nombre for producto in sucursal_retiro.productos]
    if "pantalon talle 38" in lista_nombres_final:
        errores.append("si existe pantalon talle 38 en lista final(no se borro)")
    assert not errores, "errores encontrados: {}".format("".join(errores)) 
    
#TEST 8. DEVOLVER EL VALOR DE LAS VENTAS DEL DIA

def test_ventas_del_dia_con_1_venta_de_pantalon_talle_38_y_una_remera_talle_s_da_12500():
    reiniciar_lista_productos_y_ventas()
    lista_de_2_productos_con_stock(sucursal_retiro)
    sucursal_retiro.realizar_compra(100,1,True)
    sucursal_retiro.realizar_compra(200,1,True)
    assert sucursal_retiro.valor_ventas_del_dia() ==  6500
    
#TEST 9. DEVOLVER LAS VENTAS DEL ANIO

def test_ventas_del_anio_me_devuelve_el_valor_total_con_2_ventas_del_mismo_anio():
    reiniciar_lista_productos_y_ventas()
    lista_de_2_productos_con_stock(sucursal_retiro)
    sucursal_retiro.realizar_compra(200,1,True)
    sucursal_retiro.realizar_compra(100,1,True)
    assert sucursal_retiro.ventas_del_anio() == 6500
    
def test_ventas_anio_me_devuele_valor_total_con_2_ventas_de_distinto_anio_remera_talle_s_valor_1500():
    reiniciar_lista_productos_y_ventas()
    lista_de_2_productos_sin_stock(sucursal_retiro)
    sucursal_retiro.recargar_stock(100,10)
    sucursal_retiro.realizar_compra(100,1,True)
    sucursal_retiro.ventas.append({"producto":"pelota","monto":500,"anio":2023})
    assert sucursal_retiro.ventas_del_anio() == 1500
        
#TEST 10. DEVUELVE UNA LISTA CON LOS PRODUCTOS QUE MAS APARECIERON EN VENTAS
    
def test_remera_talle_s_aparece_3_veces_y_pantalon_talle_38_aparece_1_vez():
    reiniciar_lista_productos_y_ventas()
    lista_de_2_productos_con_stock(sucursal_retiro)
    sucursal_retiro.realizar_compra(100,1,True)
    sucursal_retiro.realizar_compra(100,1,True)
    sucursal_retiro.realizar_compra(100,1,True)
    sucursal_retiro.realizar_compra(200,1,True)
    assert len(sucursal_retiro.productos_mas_vendidos(2)) == 2

#TEST 11. ACTUALIZAR LOS PRECIOS POR CATEGORIA

def test_actualizar_todos_los_precios_50_porciento_de_una_categoria_remera():
    reiniciar_lista_productos_y_ventas()
    sucursal_retiro.registrar_producto(remera_talle_s)
    reiniciar_stock_de_prenda(remera_talle_s)
    sucursal_retiro.registrar_producto(remera_talle_m)
    reiniciar_stock_de_prenda(remera_talle_m)
    sucursal_retiro.registrar_producto(remera_talle_l)
    reiniciar_stock_de_prenda(remera_talle_l)
    sucursal_retiro.actualizar_precios_segun(PorCategoria("remera"),50)
    assert remera_talle_s.precio == 2250
    assert remera_talle_m.precio == 3000
    assert remera_talle_l.precio == 3750

#TEST GANANCIA DIARIA SUCURSAL FISICA Y SUCURSAL VIRTUAL

def test_ganancia_diara_sucursal_fisica_igual_a_total_ventas_20000_menos_15000():
    reiniciar_lista_productos_y_ventas()
    reiniciar_precios_de_prendas()
    lista_de_6_productos_con_stock(sucursal_retiro)
    sucursal_retiro.realizar_compra(100,4,True) # total venta $6000
    sucursal_retiro.realizar_compra(200,2,True) # total venta $10000
    sucursal_retiro.realizar_compra(120,1,True) # total venta $2500
    sucursal_retiro.realizar_compra(100,1,True) # total venta $1500
    assert sucursal_retiro.ganancia_diaria() == 5000

def test_ganancia_diara_sucursal_virtual_con_101_ventas_151500_menos_50500_con_gasto_variable_igual_500():
    reiniciar_lista_productos_y_ventas()
    lista_de_6_productos_con_stock(sucursal_madero)
    sucursal_madero.modificar_gasto_variable(500)
    realizar_cantidad_de_compras_de_producto(sucursal_madero,100,100)
    sucursal_madero.realizar_compra(100,1,True)
    assert sucursal_madero.ganancia_diaria() == 101000 
    
# TEST DE ACTUALIZAR PRECIO SEGUN CRITERIOS

def test_actualizar_precio_un_50_porciento_segun_stock_igual_0():
    reiniciar_lista_productos_y_ventas()
    reiniciar_precios_de_prendas()
    lista_de_2_productos_con_stock(sucursal_retiro)
    sucursal_retiro.actualizar_precios_segun(PorStock(),50)
    assert remera_talle_s.precio == 2250
    assert pantalon_talle_38.precio == 7500

def test_actualizar_precio_un_100_porciento_segun_precio_10000():
    reiniciar_lista_productos_y_ventas()
    reiniciar_precios_de_prendas()
    lista_de_2_productos_con_stock(sucursal_retiro)
    sucursal_retiro.actualizar_precios_segun(PorPrecio(10000),100)
    assert remera_talle_s.precio == 3000
    assert pantalon_talle_38.precio == 10000  

def test_actualizar_precio_un_75_porciento_segun_nombre():
    reiniciar_lista_productos_y_ventas()
    reiniciar_precios_de_prendas()
    lista_de_2_productos_con_stock(sucursal_retiro)
    sucursal_retiro.actualizar_precios_segun(PorNombre("remera talle s"),75)
    assert remera_talle_s.precio == 2625

def test_actualizar_precio_un_100_porciento_segun_oposicion():
    reiniciar_lista_productos_y_ventas()
    reiniciar_precios_de_prendas()
    lista_de_2_productos_con_stock(sucursal_retiro)
    sucursal_retiro.actualizar_precios_segun(PorOposicion(PorNombre("pelota")),100)
    assert remera_talle_s.precio == 3000
    assert pantalon_talle_38.precio == 10000        
    