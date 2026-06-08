from flask import Flask, request, jsonify, render_template

#instanciar un objeto 
#el nombre __name__ quiere decir que el proyecto flask se llamara igual que el archivo principal en este caso app
app = Flask(__name__)


#@app.route("/") generea una ruta para ver la funcion inicio y su contenido
@app.route("/")
def inicio():
    return render_template("index.html")

if __name__ == "__main__":
        app.run(debug=True)
