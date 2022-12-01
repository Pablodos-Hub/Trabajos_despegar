from flask import Flask, render_template,request,url_for
from macowins import *

app = Flask(__name__)

@app.get("/")
def index():
    retiro = cargar("retiro")
    return render_template("index.html",productos = retiro.productos)

   
# ------------------------PAGINA2 NOMBRE -----------------------------#                    
@app.get("/nombre")
def pagina2():
    retiro= cargar("retiro")
    productos_nombre = retiro.listar_productos_segun(PorNombre(request.args.get("nombre","remera river s")))
    return render_template("pagina2.html",productos = productos_nombre, busqueda = request.args.get("nombre"))        

    
# ------------------------PAGINA3 CATEGORIA ---------------------------#

@app.get("/categoria")
def pagina3():
    retiro= cargar("retiro")
    productos_categoria = retiro.listar_productos_segun(PorCategoria(request.args.get("categoria","remera")))
    return render_template("pagina3.html",productos = productos_categoria, busqueda = request.args.get("categoria"))  
    
     

# ------------------------PAGINA4 PRECIO MAX---------------------------#

@app.get("/precio")
def pagina4():
    retiro= cargar("retiro")
    productos_precio = retiro.listar_productos_segun(PorPrecio(request.args.get("precio",15000)))
    return render_template("pagina4.html",productos = productos_precio, busqueda = request.args.get("precio"))  