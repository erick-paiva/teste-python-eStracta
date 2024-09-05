from flask import Blueprint, request
from app.controllers.company_controller import CompanyController
from app.controllers.auth_controller import AuthController

company_bp = Blueprint("company_bp", __name__)


# Rota de autenticação para obter o token JWT
@company_bp.route("/login", methods=["POST"])
def login():
    return AuthController.login()


# Criar uma nova empresa (protegido por JWT Bearer Token)
@company_bp.route("/", methods=["POST"])
@AuthController.token_required
def create_company(current_user):
    data = request.json
    return CompanyController.create_company(data)


# Atualizar uma empresa existente (protegido por JWT Bearer Token)
@company_bp.route("/<cnpj>", methods=["PUT"])
@AuthController.token_required
def update_company(current_user, cnpj):
    data = request.json
    return CompanyController.update_company(cnpj, data)


# Remover uma empresa (protegido por JWT Bearer Token)
@company_bp.route("/<cnpj>", methods=["DELETE"])
@AuthController.token_required
def delete_company(current_user, cnpj):
    return CompanyController.delete_company(cnpj)


# Listar empresas com paginação e ordenação (protegido por JWT Bearer Token)
@company_bp.route("/", methods=["GET"])
@AuthController.token_required
def list_companies(current_user):
    params = request.args
    return CompanyController.list_companies(params)
