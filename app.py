from flask import Flask, render_template
from models.product_model import ProductModel

app = Flask(__name__)

product_model = ProductModel()


@app.route('/index')
@app.route('/')
def home():
    categories = [
        "Всі фрукти",
        "Ягоди",
        "Цитрусові",
        "Кісточкові",
        "Тропічні",
        "Яблука та груші"
    ]

    products = product_model.get_all_products()

    return render_template(
        'index.html',
        title='Фрукти',
        categories=categories,
        products=products
    )


@app.route('/product/<product_id>')
def product_by_id(product_id):
    product = product_model.get_product_by_id(product_id)

    if product is None:
        return "Product not found", 404

    return render_template(
        'product.html',
        product=product
    )


if __name__ == '__main__':
    app.run(debug=True)
















