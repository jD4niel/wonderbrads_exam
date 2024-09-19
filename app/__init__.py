from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config
import pymysql

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    # Create the database if it doesn't exist
    create_database_if_not_exists(app)

    db.init_app(app)

    # register blueprints
    from app.blueprints.product import product_bp, main_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(product_bp, url_prefix='/products')

    with app.app_context():
        db.create_all()

    return app


def create_database_if_not_exists(app):
    conn = pymysql.connect(user=Config.USERNAME, password=Config.PASSWORD, host=Config.HOST)
    cursor = conn.cursor()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {Config.DBNAME}")
    cursor.close()
    conn.close()