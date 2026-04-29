from flask import Flask

from app.routes import auth_router, mapa_router
from app.models.db import criar_tabela
from app.routes import ranking_router

app = Flask(
    __name__,
    template_folder="app/templates",
    static_folder="app/static"
)

app.secret_key = "recicle"

criar_tabela()

auth_router.adicionar_rotas(app)
mapa_router.adicionar_rotas(app)
ranking_router.adicionar_rotas(app)

if __name__ == "__main__":
    app.run(debug=True)