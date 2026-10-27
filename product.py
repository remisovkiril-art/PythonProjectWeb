import uuid


class Product:
    def __init__(self, title, image, price, rating):
        self.id = str(uuid.uuid4())
        self.title = title
        self.image = image
        self.price = price
        self.rating = rating
