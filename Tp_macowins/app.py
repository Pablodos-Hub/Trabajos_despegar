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
                 
        
    
           

@app.get("/pagina2")
def pagina2():
    return render_template("pagina2.html",nombre =nombre())  


def nombre():
    return request.args.get("nombre","")      
       
@app.get("/pagina3")
def pagina3():
    return render_template("pagina3.html",categoria =categoria())  


def categoria():
    return request.args.get("categoria","")

@app.get("/pagina4")
def pagina4():
    return render_template("pagina4.html",precio =precio())  


def precio():
    return request.args.get("precio","")    