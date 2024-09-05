from flask import Blueprint, request
from app.controllers.company_controller import CompanyController

company_bp = Blueprint("company_bp", __name__)


# Criar uma nova empresa
@company_bp.route("/", methods=["POST"])
def create_company():
    data = request.json
    return CompanyController.create_company(data)


# Atualizar uma empresa existente
@company_bp.route("/<cnpj>", methods=["PUT"])
def update_company(cnpj):
    data = request.json
    return CompanyController.update_company(cnpj, data)


# Remover uma empresa
@company_bp.route("/<cnpj>", methods=["DELETE"])
def delete_company(cnpj):
    return CompanyController.delete_company(cnpj)


# Listar empresas com paginação e ordenação
@company_bp.route("/", methods=["GET"])
def list_companies():
    params = request.args
    return CompanyController.list_companies(params)
