from flask import Flask
from app.configs.config import Config
from app.configs.database import init_db
from app.routes.company_routes import company_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializar o banco de dados
    init_db(app)

    # Registrar os blueprints das rotas
    app.register_blueprint(company_bp, url_prefix="/companies")

    return app
