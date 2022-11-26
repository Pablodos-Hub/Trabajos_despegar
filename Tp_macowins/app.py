from flask import Flask, render_template,request,url_for
from macowins import *

app = Flask(__name__)

@app.get("/")
def main():
    return render_template("main.html")

@app.get("/pagina2")
def pagina2():
    return render_template("pagina2.html")    
       
