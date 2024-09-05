from app.configs.database import db


class Company(db.Model):
    __tablename__ = "companies"

    id = db.Column(db.Integer, primary_key=True)
    cnpj = db.Column(db.String(14), unique=True, nullable=False)
    legal_name = db.Column(db.String(128), nullable=False)
    trade_name = db.Column(db.String(128), nullable=False)
    cnae = db.Column(db.String(10), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "cnpj": self.cnpj,
            "legal_name": self.legal_name,
            "trade_name": self.trade_name,
            "cnae": self.cnae,
        }
