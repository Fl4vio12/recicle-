from flask import render_template, session, redirect
from app.models.ranking import Ranking


def ranking():

    if "usuario" not in session:
        return redirect("/login")

    lista = Ranking.listar()

    return render_template(
        "ranking.html",
        lista=lista
    )