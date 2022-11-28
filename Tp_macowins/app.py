from flask import Flask, render_template,request,url_for
from macowins import *

app = Flask(__name__)

@app.get("/")
def main():
    return render_template("main.html")

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