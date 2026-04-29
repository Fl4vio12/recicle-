from flask import Flask

from app.controllers import auth_controller


def adicionar_rotas(app: Flask):

    app.add_url_rule(
        "/",
        "home",
        auth_controller.home,
        methods=["GET"]
    )

    app.add_url_rule(
        "/login",
        "login",
        auth_controller.exibir_login,
        methods=["GET"]
    )

    app.add_url_rule(
        "/login",
        "logar",
        auth_controller.logar_usuario,
        methods=["POST"]
    )

    app.add_url_rule(
        "/cadastro",
        "cadastro",
        auth_controller.exibir_cadastro,
        methods=["GET"]
    )

    app.add_url_rule(
        "/cadastro",
        "salvar",
        auth_controller.salvar_usuario,
        methods=["POST"]
    )

    app.add_url_rule(
        "/logout",
        "logout",
        auth_controller.sair,
        methods=["GET"]
    )