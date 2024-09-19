from app import create_app, db
from app.models import Product  

def seed_products():
    app = create_app()
    with app.app_context():
        db.drop_all()
        db.create_all()

        products = [
            {'name': 'Tortillas', 'qty_available': 150, 'price': 20.00},
            {'name': 'Salsa Verde', 'qty_available': 100, 'price': 35.00},
            {'name': 'Chocolate Abuelita', 'qty_available': 80, 'price': 25.00},
            {'name': 'Café de Olla', 'qty_available': 60, 'price': 45.00},
            {'name': 'Frijoles Negros', 'qty_available': 120, 'price': 30.00},
            {'name': 'Tamarindos', 'qty_available': 90, 'price': 40.00},
            {'name': 'Churros', 'qty_available': 75, 'price': 50.00},
            {'name': 'Queso Fresco', 'qty_available': 110, 'price': 55.00},
            {'name': 'Maizena', 'qty_available': 70, 'price': 35.00},
            {'name': 'Valentina', 'qty_available': 200, 'price': 60.00},
        ]

        for product_data in products:
            product = Product(**product_data)
            db.session.add(product)

        db.session.commit()

        print("Created data correctly ROWS:",len(products))

if __name__ == '__main__':
    seed_products()
