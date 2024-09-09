from flask import request


def add_bearer_token():
    auth_header = request.headers.get("Authorization")
    if auth_header and not auth_header.lower().startswith("bearer "):
        # Atualiza o cabeçalho da requisição com o prefixo 'Bearer'
        request.environ["HTTP_AUTHORIZATION"] = "Bearer " + auth_header
