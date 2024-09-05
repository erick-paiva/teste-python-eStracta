from flask import Flask
from routes import company_bp
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

# Register routes
app.register_blueprint(company_bp, url_prefix='/companies')

if __name__ == '__main__':
    app.run(debug=True)




SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL, config={'app_name': "CRUD Company"})

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)
