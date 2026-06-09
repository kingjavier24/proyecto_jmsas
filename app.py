from flask import Flask, request, jsonify, render_template

#instanciar un objeto 
#el nombre __name__ quiere decir que el proyecto flask se llamara igual que el archivo principal en este caso app
app = Flask(__name__)


#@app.route("/") generea una ruta para ver la funcion inicio y su contenido
@app.route("/")
def inicio():
    role="admin"
    notes=["nota 1 ", "nota 2", "nota 3"]
    return render_template("index.html", role=role, notes=notes)

if __name__ == "__main__":
        app.run(debug=True)
