from flask import Flask
from app.controllers import mapa_controller


def adicionar_rotas(app: Flask):

    app.add_url_rule(
        "/mapa",
        "mapa",
        mapa_controller.mapa,
        methods=["GET"]
    )