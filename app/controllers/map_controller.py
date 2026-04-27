from flask import Blueprint, jsonify, render_template
from app.models.db import get_connection

mapa = Blueprint("mapa", __name__)

@mapa.route("/mapa")
def pagina_mapa():
    return render_template("mapa.html")

@mapa.route("/api/pontos")
def listar_pontos():
    conn = get_connection()
    dados = conn.execute("SELECT * FROM pontos_coleta").fetchall()
    conn.close()

    pontos = []
    for p in dados:
        pontos.append({
            "nome": p["nome"],
            "lat": p["latitude"],
            "lng": p["longitude"],
            "tipo": p["tipo"]
        })

    return jsonify(pontos)