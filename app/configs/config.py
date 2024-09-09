import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = "asdasdasd"
    SQLALCHEMY_DATABASE_URI = "postgres://default:wq5fBl0cUekI@ep-young-snow-a4bfflwe-pooler.us-east-1.aws.neon.tech:5432/verceldb?sslmode=require"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = os.getenv("FLASK_ENV") == "development"
