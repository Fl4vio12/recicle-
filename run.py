from flask import Flask
from app.controllers.auth_controller import auth
from app.controllers.map_controller import mapa
from app.models.db import criar_tabela

app = Flask(
    __name__,
    template_folder="app/templates",
    static_folder="app/static"
)

criar_tabela()

app.register_blueprint(auth)
app.register_blueprint(mapa)

if __name__ == "__main__":
    app.run(debug=True)