from flask import render_template
from flask import session
from flask import redirect
from app.models.material import Material

def educacao():
    if "usuario" not in session:
        return redirect("/login")

    lista = Material.listar()

    return render_template(
        "educacao.html",
        lista=lista
    )