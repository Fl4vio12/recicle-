from flask import Flask
from app.controllers import ranking_controller

def adicionar_rotas(app: Flask):
    app.add_url_rule(
        "/ranking",
        "ranking",
        ranking_controller.ranking,
        methods=["GET"]
    )