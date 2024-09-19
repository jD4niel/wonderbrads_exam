from flask import Blueprint, jsonify, render_template, redirect, url_for
from app.models import Product
from sqlalchemy.exc import OperationalError

product_bp = Blueprint('product', __name__, template_folder='templates')
main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    return redirect(url_for('product.index'))

@main_bp.route('/<path:anything>')
def catch_all(anything):
    return redirect(url_for('product.index'))

@product_bp.route('/')
def index():
    try:
        products = Product.query.all()

        if not products:
            return render_template('product_list.html', error="No products available.")

        # Identifying products
        product_max_quantity = max(products, key=lambda p: p.qty_available)
        product_min_quantity = min(products, key=lambda p: p.qty_available)
        
        products_with_max_quantity = [p for p in products if p.qty_available == product_max_quantity.qty_available]
        product_max_price = max(products_with_max_quantity, key=lambda p: p.price)
        
        prices = [p.price for p in products]
        average_price = sum(prices) / len(prices)
        product_closest_to_avg = min(products, key=lambda p: abs(p.price - average_price))

        return render_template(
            'product_list.html',
            products=products,
            product_max_quantity=product_max_quantity,
            product_min_quantity=product_min_quantity,
            product_max_price=product_max_price,
            product_closest_to_avg=product_closest_to_avg
        )

    except OperationalError:
        return render_template('error.html', message='Database not available or does not exist'), 500

@product_bp.route('/<int:product_id>')
def get_product(product_id):
    try:
        product = Product.query.get(product_id)
        if product is None:
            # Render an error template if the product is not found
            return render_template('error.html', message="Product not found"), 404
        
        return render_template('product_detail.html', product=product)
    
    except OperationalError:
        return render_template('error.html', message="Database error occurred"), 500