#methdos rest 
#post = crear, get = traer (obtener), put = actualizar, delete = borrar

#codigos de respuestas # exito =200, not found = 404, internal server error = 500
#maquina 127.0.0.1:8000, localhost:8000, 0.0.0.0:8000 son lo mismo

#llamadas por medio de terminal
#linux max
#curl http://127.0.0.1:5000/usuarios -H "Accept: application/json" tipo get
#curl -X "POST" http://127.0.0.1:5000/usuario -d nombre="ramon" -d edad=29
#curl -X "PUT" http://127.0.0.1:5000/usuario -d nombre="ramon" -d edad=30
#usuarios = [{"nombre":"jorge"}, {"nombre":"carlos"}]
#>>> usuarios
#[{'nombre': 'jorge'}, {'nombre': 'carlos'}]
#>>> usuarios.remove({'nombre': 'jorge'})
#>>> usuarios
#[{'nombre': 'carlos'}]
#jorge = list(filter(lambda x: x["nombre"]=="jorge", usuarios))

from flask import Flask, jsonify, request, make_response, render_template
from flask_accept import accept
import json
import csv
import os

template_dir = os.getcwd()

app = Flask(__name__, template_folder=template_dir)

personas = [{'nombre': 'Alice', 'edad': 1986},
          {'nombre': 'Bob', 'edad': 1985}]

@app.route('/')
@accept('text/html')
def hello_world():
    nombre="jorge"
    return render_template("index.html", personas=personas)


@hello_world.support('application/json')
def hello_world_json():
    return jsonify(result="Hello World!")

@app.route('/prueba')
@accept('text/html')
def otro():
    return 'prueba'

@otro.support('application/json')
def otro_json():
    return jsonify(result="prueba")

@app.route("/usuarios")
@accept("application/json")
def usuarios():
    return jsonify(usuarios = personas)

@app.route("/usuario", methods=['POST', "PUT", "DELETE"]) #delete
def create_user():
    if request.method == "POST":
        nombre = request.form.get('nombre')
        edad = request.form.get("edad")
        print("edad ", edad)
        personas.append({'nombre': nombre, 'edad':edad})
        return jsonify(personas)
    if request.method == "PUT":
        persona1 = {}
        nombre = request.form.get('nombre')
        edad = request.form.get("edad")
        for persona in personas:
            if nombre == persona["nombre"]:
                persona["edad"] = edad
                persona1 = persona
        return jsonify(persona1)
    if request.method == "DELETE":
        return jsonify({})

@app.route('/probando')
def projects():
    with open("vinos.csv") as f:
        vinos = list(csv.reader(f, delimiter=';'))
        return jsonify({'vinos': vinos})


if __name__ == '__main__':
    app.run()
