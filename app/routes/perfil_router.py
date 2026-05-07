from flask import Flask
from app.controllers import perfil_controller

def adicionar_rotas(app: Flask):
    app.add_url_rule(
        "/perfil",
        "perfil",
        perfil_controller.perfil,
        methods=["GET"]
    )