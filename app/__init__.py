from flask import Flask
from app.configs import migration, database, swagger, config
from app import routes
from app.middlewares.auth_middleware import add_bearer_token


app = Flask(__name__)
app.config.from_object(config.Config)

routes.init_app(app)

database.init_app(app)

migration.init_app(app)

swagger.init_app(app)

app.before_request(add_bearer_token)
