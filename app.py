from flask import Flask, render_template

app = Flask(__name__)

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

    products = [
        {
            "name": "Банани",
            "price": 45,
            "image": "https://images.unsplash.com/photo-1571771894821-ce9b6c11b08e?auto=format&fit=crop&w=500&q=80"
        },
        {
            "name": "Яблука",
            "price": 35,
            "image": "https://images.unsplash.com/photo-1560806887-1e4cd0b6cbd6?auto=format&fit=crop&w=500&q=80"
        },
        {
            "name": "Апельсини",
            "price": 55,
            "image": "https://images.unsplash.com/photo-1547514701-42782101795e?auto=format&fit=crop&w=500&q=80"
        },
        {
            "name": "Полуниця",
            "price": 120,
            "image": "https://images.unsplash.com/photo-1464965911861-746a04b4bca6?auto=format&fit=crop&w=500&q=80"
        },
        {
            "name": "Чорниця",
            "price": 150,
            "image": "https://images.unsplash.com/photo-1498557850523-fd3d118b962e?auto=format&fit=crop&w=500&q=80"
        },
        {
            "name": "Виноград",
            "price": 95,
            "image": "https://images.unsplash.com/photo-1537640538966-79f369143f8f?auto=format&fit=crop&w=500&q=80"
        },
        {
            "name": "Ківі",
            "price": 80,
            "image": "https://images.unsplash.com/photo-1618897996318-5a901fa6ca71?auto=format&fit=crop&w=500&q=80"
        },
        {
            "name": "Манго",
            "price": 140,
            "image": "https://images.unsplash.com/photo-1553279768-865429fa0078?auto=format&fit=crop&w=500&q=80"
        }
    ]

    return render_template(
        'index.html',
        title='Фрукти',
        categories=categories,
        products=products
    )


if __name__ == '__main__':
    app.run(debug=True)















