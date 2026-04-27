from flask import Blueprint, request, jsonify, render_template, redirect
from app.models.db import get_connection

auth = Blueprint("auth", __name__)

# PÁGINAS
@auth.route("/")
def home():
    return redirect("/login")

@auth.route("/login")
def login_page():
    return render_template("login.html")

@auth.route("/cadastro")
def cadastro_page():
    return render_template("cadastro.html")


# API LOGIN
@auth.route("/api/login", methods=["POST"])
def api_login():
    data = request.get_json()

    email = data.get("email")
    senha = data.get("senha")

    conn = get_connection()
    user = conn.execute(
        "SELECT * FROM usuarios WHERE email=? AND senha=?",
        (email, senha)
    ).fetchone()
    conn.close()

    if user:
        return jsonify({"status": "ok"})
    else:
        return jsonify({
            "status": "erro",
            "mensagem": "Email ou senha inválidos"
        })


# API CADASTRO
@auth.route("/api/cadastro", methods=["POST"])
def api_cadastro():
    data = request.get_json()

    nome = data.get("nome")
    email = data.get("email")
    senha = data.get("senha")

    conn = get_connection()

    try:
        conn.execute(
            "INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)",
            (nome, email, senha)
        )
        conn.commit()
        conn.close()

        return jsonify({"status": "ok"})

    except:
        conn.close()
        return jsonify({
            "status": "erro",
            "mensagem": "Email já cadastrado"
        })