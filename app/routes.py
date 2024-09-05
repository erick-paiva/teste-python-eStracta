from flask import Blueprint, request, jsonify
from models import Company

company_bp = Blueprint('company_bp', __name__)

# Store companies in memory
companies = {}

# Endpoint to register a new company
@company_bp.route('/', methods=['POST'])
def create_company():
    data = request.json
    cnpj = data.get('cnpj')
    if cnpj in companies:
        return jsonify({"error": "Company already registered"}), 400
    
    legal_name = data.get('legal_name')
    trade_name = data.get('trade_name')
    cnae = data.get('cnae')
    
    new_company = Company(cnpj, legal_name, trade_name, cnae)
    companies[cnpj] = new_company
    
    return jsonify({"message": "Company registered successfully!"}), 201

# Endpoint to edit an existing company
@company_bp.route('/<cnpj>', methods=['PUT'])
def update_company(cnpj):
    if cnpj not in companies:
        return jsonify({"error": "Company not found"}), 404
    
    data = request.json
    trade_name = data.get('trade_name')
    cnae = data.get('cnae')
    
    company = companies[cnpj]
    company.trade_name = trade_name if trade_name else company.trade_name
    company.cnae = cnae if cnae else company.cnae
    
    return jsonify({"message": "Company updated successfully!"})

# Endpoint to delete a company
@company_bp.route('/<cnpj>', methods=['DELETE'])
def delete_company(cnpj):
    if cnpj not in companies:
        return jsonify({"error": "Company not found"}), 404
    
    del companies[cnpj]
    
    return jsonify({"message": "Company deleted successfully!"})

# Endpoint to list companies with pagination, sorting, and limits
@company_bp.route('/', methods=['GET'])
def list_companies():
    start = int(request.args.get('start', 0))
    limit = int(request.args.get('limit', 10))
    sort = request.args
