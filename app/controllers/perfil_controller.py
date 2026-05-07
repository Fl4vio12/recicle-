from flask import render_template
from flask import session
from flask import redirect

def perfil():
    if "usuario" not in session:
        return redirect("/login")

    dados = {
        "nome":"Usuário RECICLE+",
        "email":session["usuario"],
        "pontos":150,
        "bio":"Ajudando o planeta ♻️"
    }

    return render_template(
        "perfil.html",
        dados=dados
    )