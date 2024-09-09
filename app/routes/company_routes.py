from flask import Blueprint, request
from app.controllers.company_controller import CompanyController
from app.controllers.auth_controller import AuthController

company_bp = Blueprint("company_bp", __name__)


@company_bp.route("/login", methods=["POST"])
def login():
    return AuthController.login()


@company_bp.route("/", methods=["POST"])
@AuthController.token_required
def create_company():
    data = request.json
    return CompanyController.create_company(data)


@company_bp.route("/<cnpj>", methods=["PUT"])
@AuthController.token_required
def update_company(cnpj):
    data = request.json
    return CompanyController.update_company(cnpj, data)


@company_bp.route("/<cnpj>", methods=["DELETE"])
@AuthController.token_required
def delete_company(cnpj):
    return CompanyController.delete_company(cnpj)


@company_bp.route("/", methods=["GET"])
@AuthController.token_required
def list_companies():
    params = request.args
    return CompanyController.list_companies(params)
