from flask import Flask

#instanciar un objeto 
#el nombre __name__ quiere decir que el proyecto flask se llamara igual que el archivo principal en este caso app
app = Flask(__name__)


#@app.route("/") generea una ruta para ver la funcion inicio y su contenido
@app.route("/")
def inicio():
    return "Pagina principal jmsas"

@app.route("/acercade_jmsas")
def about():
    return "informacion principal de informacion jmasas"