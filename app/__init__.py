from flask import Flask, request
from flask_swagger_ui import get_swaggerui_blueprint
from flask_migrate import Migrate
from app.configs.config import Config
from app.configs.database import init_db, db
from app.routes.company_routes import company_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializar o banco de dados
    init_db(app)

    # Registrar os blueprints
    app.register_blueprint(company_bp, url_prefix="/companies")

    # Configuração do Swagger UI
    SWAGGER_URL = "/swagger"
    API_URL = "/static/swagger.json"  # Apontando para o arquivo JSON
    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL, API_URL, config={"app_name": "Company API"}
    )

    # Registrar o blueprint do Swagger UI
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

    @app.before_request
    def add_bearer_token():
        auth_header = request.headers.get("Authorization")
        if auth_header and not auth_header.lower().startswith("bearer "):
            # Atualiza o cabeçalho da requisição com o prefixo 'Bearer'
            request.environ["HTTP_AUTHORIZATION"] = "Bearer " + auth_header

    return app
