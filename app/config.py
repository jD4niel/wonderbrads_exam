from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    USERNAME = os.getenv('DB_USERNAME')
    PASSWORD = os.getenv('DB_PASSWORD')
    DBNAME = os.getenv('DB_NAME')
    HOST = os.getenv('DB_HOST')
    PORT = os.getenv('DB_PORT', 3306)
    SQLALCHEMY_DATABASE_URI = f"mysql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
