from flask import Flask, render_template, request, redirect, url_for
from agenda import Evento, Cita, Reunion, Recordatorio, Agenda
from datetime import datetime

app = Flask(__name__)
agenda = Agenda()

@app.route("/")
def index():
    eventos = [e.to_dict() for e in agenda.get_eventos()]
    return render_template("index.html", eventos=eventos)

@app.route("/agregar", methods=["POST"])
def agregar():
    tipo = request.form["tipo"]
    titulo = request.form["titulo"]
    fecha_raw = request.form["fecha"]
    fecha = datetime.strptime(fecha_raw, "%Y-%m-%dT%H:%M").strftime("%d/%m/%Y %H:%M")
    descripcion = request.form["descripcion"]
    id = agenda.get_siguiente_id()

    if tipo == "Cita":
        evento = Cita(id, titulo, fecha, descripcion,
                      request.form["lugar"],
                      request.form["doctor"])
    elif tipo == "Reunion":
        evento = Reunion(id, titulo, fecha, descripcion,
                         request.form["participantes"])
    else:
        evento = Recordatorio(id, titulo, fecha, descripcion,
                              request.form["persona"])

    agenda.agregar_evento(evento)
    return redirect(url_for("index"))

@app.route("/eliminar/<int:id>")
def eliminar(id):
    agenda.eliminar_evento(id)
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)