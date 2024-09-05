import jwt
import datetime
from flask import jsonify, request, current_app


class AuthController:

    @staticmethod
    def login():
        auth = request.json
        username = auth.get("username")
        password = auth.get("password")

        # Validar usuário e senha (no mundo real, seria feito via banco de dados)
        if username == "admin" and password == "password":
            token = jwt.encode(
                {
                    "user": username,
                    "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30),
                },
                current_app.config["SECRET_KEY"],
                algorithm="HS256",
            )

            return jsonify({"token": token}), 200

        return jsonify({"error": "Invalid credentials"}), 401

    @staticmethod
    def token_required(f):
        def wrapper(*args, **kwargs):
            auth_header = request.headers.get("Authorization")
            if not auth_header or not auth_header.startswith("Bearer "):
                return jsonify({"error": "Token is missing or invalid"}), 403

            token = auth_header.split(" ")[1]

            try:
                data = jwt.decode(
                    token, current_app.config["SECRET_KEY"], algorithms=["HS256"]
                )
                current_user = data["user"]
            except jwt.ExpiredSignatureError:
                return jsonify({"error": "Token has expired"}), 403
            except jwt.InvalidTokenError:
                return jsonify({"error": "Token is invalid"}), 403

            return f(current_user, *args, **kwargs)

        wrapper.__name__ = (
            f.__name__
        )  # Isso é necessário para evitar problemas ao empacotar a função
        return wrapper
