from app.routes.company_routes import company_bp


def init_app(app):
    app.register_blueprint(company_bp)
