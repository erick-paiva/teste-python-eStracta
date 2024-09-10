from flask import Flask, request
from app.configs import migration, database, swagger, config
from app import routes
from app.middlewares.auth_middleware import add_bearer_token
from flask_cors import CORS

app = Flask(__name__)

app.config.from_object(config.Config)

CORS(app)

routes.init_app(app)

database.init_app(app)

migration.init_app(app)

swagger.init_app(app)

app.before_request(add_bearer_token)
