from flask import render_template
from flask import session
from flask import redirect


def mapa():

    if "usuario" not in session:
        return redirect("/login")

    return render_template("mapa.html")