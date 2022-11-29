from flask import Flask, render_template,request,url_for
from macowins import *

app = Flask(__name__)

@app.get("/")
def index():
    return render_template("index.html",productos = articulos())

def articulos():
    for producto in retiro.productos:
        if producto.codigo == 100:
            articulo1 = producto
        
        if producto.codigo == 110:
            articulo2 = producto
                
        if producto.codigo == 120:
            articulo3 = producto
                
        if producto.codigo == 130:
            articulo4 = producto
                
        if producto.codigo == 140:
            articulo5 = producto
                
        if producto.codigo == 150:
            articulo6 = producto
                
        if producto.codigo == 200:
            articulo7 = producto
                
        if producto.codigo == 210:
            articulo8 = producto
                
        if producto.codigo == 220:
            articulo9 = producto
                
        if producto.codigo == 230:
            articulo10 = producto
                
        if producto.codigo == 240:
            articulo11 = producto
                
        if producto.codigo == 250:
            articulo12 = producto
    productos  = [articulo1,articulo2,articulo3,articulo4,articulo5,articulo6,articulo7,articulo8,articulo9,articulo10,articulo11,articulo12]        
    return productos
# ------------------------PAGINA2 NOMBRE -----------------------------#                    
@app.get("/nombre")
def pagina2():
    return render_template("pagina2.html",productos = productos_nombre())        

def productos_nombre():
    lista = retiro.listar_productos_segun(PorNombre(request.args.get("nombre","")))
    for producto in lista:
        articulo1 = producto
        productos_new = [articulo1]
    return productos_new    
# ------------------------PAGINA3 CATEGORIA ---------------------------#

@app.get("/categoria")
def pagina3():
    return render_template("pagina3.html",productos = productos_categoria())  

def productos_categoria():
    retiro2 = cargar ("retiro")
    lista = retiro2.listar_productos_segun(PorCategoria(request.args.get("categoria","")))
    productos_new1= []
    for producto in lista:
        productos_new1.append(producto)
    return productos_new1    
     

# ------------------------PAGINA4 PRECIO MAX---------------------------#

@app.get("/pagina4")
def pagina4():
    return render_template("pagina4.html",productos = productos())  

def productos():
    retiro = cargar("retiro")
    productos_new = []
    for producto in retiro.productos:
        productos_new.append(producto)
    return productos_new