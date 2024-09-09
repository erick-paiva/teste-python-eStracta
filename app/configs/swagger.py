from flask_swagger_ui import get_swaggerui_blueprint
from flask import request


def init_swagger(app):
    @app.before_request
    def adjust_swagger_url():
        SWAGGER_URL = "/swagger"
        API_URL = f"{request.host_url.rstrip('/')}/static/swagger.json"

        swaggerui_blueprint = get_swaggerui_blueprint(
            SWAGGER_URL, API_URL, config={"app_name": "Company API"}
        )
        app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
