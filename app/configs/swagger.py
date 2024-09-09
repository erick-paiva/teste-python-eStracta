from flask import request
from flask_swagger_ui import get_swaggerui_blueprint


def init_app(app):
    SWAGGER_URL = "/swagger"

    @app.context_processor
    def override_url():
        API_URL = request.host_url.rstrip("/") + "/static/swagger.json"
        swaggerui_blueprint = get_swaggerui_blueprint(
            SWAGGER_URL, API_URL, config={"app_name": "Company API"}
        )
        return dict(swagger_ui_blueprint=swaggerui_blueprint)

    swaggerui_blueprint = get_swaggerui_blueprint(
        SWAGGER_URL, "/static/swagger.json", config={"app_name": "Company API"}
    )
    app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
