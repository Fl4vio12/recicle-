from flask import  Flask
from app.controllers import educacao_controller

def adicionar_rotas(app: Flask):
    app.add_url_rule(
        "/educacao",
        "educacao",
        educacao_controller.educacao,
        methods=["GET"]
    )