from flask import Flask
from app.routes import auth_router
from app.routes import mapa_router
from app.routes import ranking_router
from app.routes import perfil_router
from app.routes import educacao_router

app = Flask(__name__)

app.secret_key = "recicle123"

auth_router.adicionar_rotas(app)
mapa_router.adicionar_rotas(app)
ranking_router.adicionar_rotas(app)
perfil_router.adicionar_rotas(app)
educacao_router.adicionar_rotas(app)

app.run(debug=True)