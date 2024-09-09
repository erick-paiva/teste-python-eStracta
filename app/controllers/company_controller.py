from validate_docbr import CNPJ
from flask import jsonify
from app.models.company import Company
from app.configs.database import db


class CompanyController:
    @staticmethod
    def create_company(data):
        cnpj_validator = CNPJ()
        cnpj = data.get("cnpj")

        if not cnpj or not cnpj_validator.validate(cnpj):
            return jsonify({"error": "Invalid CNPJ"}), 400

        required_fields = ["cnpj", "legal_name", "trade_name", "cnae"]
        missing_fields = [field for field in required_fields if not data.get(field)]

        if missing_fields:
            return (
                jsonify(
                    {"error": f"Missing required fields: {', '.join(missing_fields)}"}
                ),
                400,
            )

        if Company.query.filter_by(cnpj=cnpj).first():
            return jsonify({"error": "Company already registered"}), 400

        legal_name = data.get("legal_name")
        trade_name = data.get("trade_name")
        cnae = data.get("cnae")

        new_company = Company(
            cnpj=cnpj, legal_name=legal_name, trade_name=trade_name, cnae=cnae
        )
        db.session.add(new_company)
        db.session.commit()

        return (
            jsonify(
                {
                    "message": "Company registered successfully!",
                    "company": new_company.to_dict(),
                }
            ),
            201,
        )

    @staticmethod
    def update_company(cnpj, data):
        company = Company.query.filter_by(cnpj=cnpj).first()
        if not company:
            return jsonify({"error": "Company not found"}), 404

        if not data.get("trade_name") or not data.get("cnae"):
            return jsonify({"error": "Both trade_name and cnae are required"}), 400

        company.trade_name = data.get("trade_name", company.trade_name)
        company.cnae = data.get("cnae", company.cnae)

        db.session.commit()

        return jsonify(
            {"message": "Company updated successfully!", "company": company.to_dict()}
        )

    @staticmethod
    def delete_company(cnpj):
        company = Company.query.filter_by(cnpj=cnpj).first()
        if not company:
            return jsonify({"error": "Company not found"}), 404

        db.session.delete(company)
        db.session.commit()

        return jsonify({"message": "Company deleted successfully!"})

    @staticmethod
    def list_companies(params):
        company_name = params.get("name")
        start = int(params.get("start", 0))
        limit = int(params.get("limit", 10))
        sort = params.get("sort", "legal_name")
        direction = params.get("dir", "asc")

        query = Company.query

        if company_name:
            query = query.filter(
                (Company.legal_name.ilike(f"%{company_name}%"))
                | (Company.trade_name.ilike(f"%{company_name}%"))
            )

        if direction == "asc":
            query = query.order_by(getattr(Company, sort).asc())
        else:
            query = query.order_by(getattr(Company, sort).desc())

        companies = query.offset(start).limit(limit).all()

        total_items = query.count()
        listed_items = len(companies)

        response = {
            "total_items": total_items,
            "listed_items": listed_items,
            "companies": [company.to_dict() for company in companies],
        }

        return jsonify(response), 200
