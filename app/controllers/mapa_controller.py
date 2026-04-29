from flask import render_template, request, session, redirect
from app.models.ponto import Ponto


def exibir_mapa():

    if "usuario" not in session:
        return redirect("/login")

    tipo = request.args.get("tipo")

    if tipo:
        pontos = Ponto.filtrar(tipo)
    else:
        pontos = Ponto.listar()

    return render_template(
        "mapa.html",
        pontos=pontos
    )