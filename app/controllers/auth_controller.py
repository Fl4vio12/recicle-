from flask import render_template
from flask import request
from flask import redirect
from flask import session

from app.models.usuario import Usuario


def home():

    return redirect("/login")


def exibir_login():

    return render_template("login.html")


def exibir_cadastro():

    return render_template("cadastro.html")


def salvar_usuario():

    nome = request.form["nome"]
    email = request.form["email"]
    senha = request.form["senha"]

    usuario = Usuario(nome, email, senha)

    usuario.salvar()

    return redirect("/login")


def logar_usuario():

    email = request.form["email"]
    senha = request.form["senha"]

    usuario = Usuario("", email, senha)

    if usuario.entrar():

        session["usuario"] = email

        return redirect("/mapa")

    return redirect("/login")


def sair():

    session.clear()

    return redirect("/login")