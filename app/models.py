from app import db


class Product(db.Model):
    __tablename__ = 'product' 

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    qty_available = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)

